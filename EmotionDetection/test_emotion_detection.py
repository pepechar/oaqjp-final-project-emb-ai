import EmotionDetection
import unittest

class TestEmotionDetection(unittest.TestCase):

    def test_joy(self):
        text = "I am glad this happened"
        result = EmotionDetection.emotion_detector(text)
        dominant = result['dominant_response']
        self.assertEqual(dominant, "joy")

    def test_anger(self):
        text = "I am really mad about this"
        result = EmotionDetection.emotion_detector(text)
        dominant = result['dominant_response']
        self.assertEqual(dominant, "anger")

    def test_disgut(self):
        text = "I feel disgusted just hearing about this"
        result = EmotionDetection.emotion_detector(text)
        dominant = result['dominant_response']
        self.assertEqual(dominant, "disgust")

    def test_sadness(self):
        text = "I am so sad about this"
        result = EmotionDetection.emotion_detector(text)
        dominant = result['dominant_response']
        self.assertEqual(dominant, "sadness")

    def test_fear(self):
        text = "I am really afraid that this will happen"
        result = EmotionDetection.emotion_detector(text)
        dominant = result['dominant_response']
        self.assertEqual(dominant, "fear")


if __name__ == "__main__":
    unittests.main()
