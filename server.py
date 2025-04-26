
"""Server to detect emotions from text using Flask and EmotionDetection module."""

from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_endpoint():
    """
    API endpoint that receives text and returns the dominant emotion detected.
    Returns:
        dict: JSON response containing the detected emotion or an error message.
    """
    text = request.args.get("textToAnalyze")
    result= emotion_detector(text)

    if result["dominant_response"] is None:
        return {"Error": "Invalid text! Please try again!."}

    return {"emotion": result}

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
