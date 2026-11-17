
import re
import joblib
from pathlib import Path

# Project root / artifacts / model file
MODEL_PATH = (
    Path(__file__).resolve().parents[2]
    / "ml_artifacts"
    / "complaint_pipeline.joblib"
)

_pipeline = None


def clean_text(text: str) -> str:
    """Apply the same preprocessing used during model training."""
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", " ", text)
    text = re.sub(r"\b[\w.-]+@[\w.-]+\.\w+\b", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def load_model():
    """Load the trained pipeline once."""
    global _pipeline

    if _pipeline is None:
        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                f"Trained model not found at: {MODEL_PATH}"
            )

        _pipeline = joblib.load(MODEL_PATH)

    return _pipeline


def predict_category(text: str) -> dict:
    """Predict the category of a consumer complaint."""

    pipeline = load_model()
    cleaned_text = clean_text(text)

    probabilities = pipeline.predict_proba([cleaned_text])[0]
    classes = pipeline.classes_

    best_index = probabilities.argmax()

    return {
        "category": str(classes[best_index]),
        "confidence": float(probabilities[best_index]),
        "model_loaded": True,
    }

