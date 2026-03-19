"""Unit tests for emotion detector."""

import unittest
from unittest.mock import patch, Mock
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test suite for emotion detector."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_emotion_detector(self, mock_post):
        """Test dominant emotion detection."""
        test_cases = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear"
        }

        mock_responses = {
            "I am glad this happened": {
                "emotionPredictions": [{
                    "emotion": {
                        "anger": 0.01,
                        "disgust": 0.02,
                        "fear": 0.03,
                        "joy": 0.90,
                        "sadness": 0.04
                    }
                }]
            },
            "I am really mad about this": {
                "emotionPredictions": [{
                    "emotion": {
                        "anger": 0.88,
                        "disgust": 0.03,
                        "fear": 0.02,
                        "joy": 0.01,
                        "sadness": 0.06
                    }
                }]
            },
            "I feel disgusted just hearing about this": {
                "emotionPredictions": [{
                    "emotion": {
                        "anger": 0.04,
                        "disgust": 0.87,
                        "fear": 0.03,
                        "joy": 0.01,
                        "sadness": 0.05
                    }
                }]
            },
            "I am so sad about this": {
                "emotionPredictions": [{
                    "emotion": {
                        "anger": 0.03,
                        "disgust": 0.02,
                        "fear": 0.04,
                        "joy": 0.01,
                        "sadness": 0.90
                    }
                }]
            },
            "I am really afraid that this will happen": {
                "emotionPredictions": [{
                    "emotion": {
                        "anger": 0.02,
                        "disgust": 0.01,
                        "fear": 0.91,
                        "joy": 0.01,
                        "sadness": 0.05
                    }
                }]
            }
        }

        for text, expected_emotion in test_cases.items():
            mock_post.return_value = Mock(
                status_code=200,
                json=lambda response=mock_responses[text]: response
            )
            response = emotion_detector(text)
            self.assertEqual(response["dominant_emotion"], expected_emotion)


if __name__ == "__main__":
    unittest.main()
