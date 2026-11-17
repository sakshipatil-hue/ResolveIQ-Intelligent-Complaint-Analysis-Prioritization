import re

HIGH_URGENCY_PHRASES = (
    "fraud", "unauthorized transaction", "money stolen", "account hacked",
    "identity theft", "threatened", "legal notice", "locked out of account",
    "urgent", "immediately", "emergency",
)
MEDIUM_URGENCY_PHRASES = (
    "unable to access", "incorrect charge", "charged twice",
    "payment failed", "refund delayed", "not received",
)

def detect_urgency(text: str) -> tuple[str, list[str]]:
    normalized = re.sub(r"\s+", " ", (text or "").lower()).strip()
    high = [p for p in HIGH_URGENCY_PHRASES if p in normalized]
    if high:
        return "high", high
    medium = [p for p in MEDIUM_URGENCY_PHRASES if p in normalized]
    if medium:
        return "medium", medium
    return "low", []
