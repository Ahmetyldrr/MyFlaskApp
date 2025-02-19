import unittest
from emotion_app.emotion_predictor import emotion_predictor

class TestEmotionPredictor(unittest.TestCase):
    def test_emotion_predictor(self):
        text = "I am very happy today!"
        result = emotion_predictor(text)
        self.assertIn("emotions", result)
        self.assertIn("text", result)
        self.assertEqual(result["text"], text)

if __name__ == '__main__':
    unittest.main()