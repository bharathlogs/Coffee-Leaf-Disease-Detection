from pathlib import Path
from PIL import ImageOps
from PIL.Image import DecompressionBombError, open as pillow_open

import streamlit as st
from ultralytics import YOLO
from ultralytics.utils import ThreadingLocked


@st.cache_resource(max_entries=2, show_spinner="Loading detection model...")
def load_model(model_path):
    path = Path(model_path)
    if not path.is_file():
        raise FileNotFoundError(f"Trained model is missing: {path.name}")
    return YOLO(path)


@ThreadingLocked()
def predict(model, image, confidence):
    # Cached YOLO predictors share mutable state across browser sessions.
    return model.predict(image, conf=confidence, device="cpu", verbose=False)


def open_image(source):
    source.seek(0)
    try:
        image = pillow_open(source)
    except DecompressionBombError:
        raise ValueError("Photos must be 16 megapixels or smaller.") from None
    with image:
        if image.width * image.height > 16_000_000:
            raise ValueError("Photos must be 16 megapixels or smaller.")
        image = ImageOps.exif_transpose(image)
        image.thumbnail((1600, 1600))
        return image.convert("RGB")
