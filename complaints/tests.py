from django.test import TestCase
from .services.urgency import detect_urgency

class UrgencyRuleTests(TestCase):
    def test_high_urgency_phrase(self):
        priority, reasons = detect_urgency("There was an unauthorized transaction.")
        self.assertEqual(priority, "high")
        self.assertIn("unauthorized transaction", reasons)

    def test_default_is_low(self):
        priority, reasons = detect_urgency("I have a question about my statement.")
        self.assertEqual(priority, "low")
        self.assertEqual(reasons, [])
