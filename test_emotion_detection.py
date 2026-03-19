"""Unit tests for emotion detector."""

import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test suite for emotion detector."""

    def test_emotion_detector(self):
        """Test dominant emotion detection."""
        test_cases = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear"
        }

        for text, expected_emotion in test_cases.items():
            response = emotion_detector(text)
            self.assertEqual(response["dominant_emotion"], expected_emotion)


if name == "__main__":
    unittest.main()
