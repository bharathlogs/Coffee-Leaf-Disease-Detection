import io
import unittest
from pathlib import Path
from unittest.mock import patch

import streamlit as st
from streamlit.testing.v1 import AppTest


class DemoTests(unittest.TestCase):
    def test_home_starts_without_google_credentials(self):
        with patch.object(st, 'secrets', {}):
            app = AppTest.from_file(str(Path(__file__).resolve().parents[1] / 'app.py')).run(timeout=60)
        self.assertEqual([e.message for e in app.exception], [])
        self.assertIn('YOLO11m - 5 classes', app.sidebar.selectbox[1].options)
        self.assertIn('YOLO11s - 6 classes', app.sidebar.selectbox[1].options)

    def test_drive_is_optional_without_credentials(self):
        from modules.image_uploader import authenticate_drive
        with patch.object(st, 'secrets', {}):
            self.assertIsNone(authenticate_drive())

    def test_map_starts_without_google_credentials(self):
        def render_map():
            from components.disease_tracking import main
            main()
        with patch.object(st, 'secrets', {}):
            app = AppTest.from_function(render_map).run(timeout=60)
        self.assertEqual([e.message for e in app.exception], [])
        self.assertTrue(app.info)

    def test_models_produce_annotated_results(self):
        from modules.detection_utils import run_detection
        for mode in ('YOLO11m - 5 classes', 'YOLO11s - 6 classes'):
            with self.subTest(model=mode):
                image = io.BytesIO(Path('static/images/diseases/leaf-rust.jpg').read_bytes())
                with patch.object(st, 'secrets', {}):
                    result = run_detection(image, {
                        'detection_model_choice': 'Disease',
                        'disease_model_mode': mode,
                        'confidence': 0.25,
                        'overlap_threshold': 0.3,
                    })
                self.assertIsNotNone(result['result_image'])
                self.assertGreater(len(result['all_disease_instances']), 0)
                for label, confidence in result['all_disease_instances']:
                    self.assertIsInstance(label, str)
                    self.assertTrue(0 <= confidence <= 100)

    def test_restored_checkpoints_work_in_combined_mode(self):
        from PIL import Image
        from modules.detection_utils import load_models
        from modules.detection_runner import generate_preview_image, detect_with_confidence
        image = Image.open('static/images/diseases/leaf-rust.jpg')
        for mode in ('YOLO12n - Spots', 'YOLO12n - 5 classes'):
            with self.subTest(model=mode):
                model, leaf, disease = load_models('Both Models', mode)
                self.assertIsNone(model)
                self.assertEqual(set(leaf.names.values()), {'arabica', 'liberica', 'robusta'})
                self.assertEqual(set(disease.names.values()),
                                 {'abiotic disorder', 'cercospora', 'healthy', 'rust', 'sooty mold'})
                preview = generate_preview_image(image, 'Both Models', model, leaf, disease,
                                                 0.25, 0.3, {}, {})
                self.assertEqual(preview.shape[:2], (image.height, image.width))
                detections = detect_with_confidence(image, 'Both Models', model, leaf,
                                                    disease, 0.25, 0.3)
                self.assertIsInstance(detections, list)

    def test_uploaded_images_are_bounded_before_inference(self):
        from PIL import Image, UnidentifiedImageError
        from components.config.helper import open_image
        data = io.BytesIO()
        Image.new('RGB', (3200, 2000)).save(data, format='PNG')
        data.seek(0)
        image = open_image(data)
        self.assertEqual(image.size, (1600, 1000))
        self.assertEqual(image.mode, 'RGB')
        data = io.BytesIO()
        Image.new('RGB', (5000, 4000)).save(data, format='PNG')
        data.seek(0)
        with self.assertRaises(ValueError):
            open_image(data)
        with self.assertRaises(UnidentifiedImageError):
            open_image(io.BytesIO(b'not an image'))

    def test_huge_dimension_header_is_recoverable(self):
        import struct
        import zlib
        from PIL import Image
        from components.config.helper import open_image
        data = io.BytesIO()
        Image.new('RGB', (1, 1)).save(data, format='PNG')
        payload = bytearray(data.getvalue())
        payload[16:24] = struct.pack('>II', 20000, 20000)
        payload[29:33] = struct.pack('>I', zlib.crc32(payload[12:29]))
        with self.assertRaises(ValueError):
            open_image(io.BytesIO(payload))

    def test_sample_flow_works_without_storage(self):
        with patch.object(st, 'secrets', {}):
            app = AppTest.from_file(str(Path(__file__).resolve().parents[1] / 'app.py')).run(timeout=60)
            button = next(b for b in app.button if b.label == 'Try a sample leaf')
            button.click().run(timeout=60)
        self.assertEqual([e.message for e in app.exception], [])
        self.assertTrue(app.session_state['detection_run'])
        save_buttons = [b for b in app.button if 'Save to' in b.label]
        self.assertEqual(len(save_buttons), 2)
        self.assertTrue(all(b.disabled for b in save_buttons))

    def test_legacy_model_labels_map_to_disease_information(self):
        from modules.detection_runner import normalize_label
        self.assertEqual(normalize_label('leaf_rust'), 'rust')
        self.assertEqual(normalize_label('sooty-mold'), 'sooty mold')
        self.assertEqual(normalize_label('leaf_miner'), 'leaf miner')


if __name__ == '__main__':
    unittest.main()
