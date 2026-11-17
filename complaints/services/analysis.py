
from .urgency import detect_urgency
from .classifier import predict_category

REVIEW_CONFIDENCE_THRESHOLD = 0.60


def analyze_complaint(text: str) -> dict:
    """Combine ML category prediction and rule-based urgency detection."""

    priority, urgency_reasons = detect_urgency(text)

    try:
        prediction = predict_category(text)
    except (FileNotFoundError, OSError, ValueError) as error:
        prediction = {
            "category": "Unclassified",
            "confidence": None,
            "model_loaded": False,
        }

    confidence = prediction.get("confidence")
    category = prediction.get("category", "Unclassified")

    needs_review = (
        category == "Unclassified"
        or confidence is None
        or confidence < REVIEW_CONFIDENCE_THRESHOLD
    )

    return {
        "category": category,
        "confidence": confidence,
        "priority": priority,
        "requires_human_review": needs_review,
        "urgency_reasons": urgency_reasons,
    }
