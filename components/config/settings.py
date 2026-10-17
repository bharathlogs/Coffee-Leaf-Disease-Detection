from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
IMAGE = "Image"
SOURCES_LIST = [IMAGE]
IMAGES_DIR = ROOT / "static" / "images"
DEFAULT_IMAGE = IMAGES_DIR / "DB2.jpg"
DEFAULT_DETECT_IMAGE = IMAGES_DIR / "DB.jpg"
MODEL_DIR = ROOT / "weights"
DISEASE_MODELS = {
    "YOLO11m - 5 classes": MODEL_DIR / "yolo11m96.pt",
    "YOLO11s - 6 classes": MODEL_DIR / "cdisease.pt",
    "YOLO12n - Spots": MODEL_DIR / "spots.pt",
    "YOLO12n - 5 classes": MODEL_DIR / "yolo12n.pt",
}

LEAF_MODEL = MODEL_DIR / "cleaf.pt"
