"""Flask server for emotion detection application."""

from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the main application page."""
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Emotion Detector</title>
    </head>
    <body>
        <h1>Emotion Detection Application</h1>
        <form action="/emotionDetector" method="get">
            <input type="text" name="textToAnalyze" placeholder="Enter text here">
            <input type="submit" value="Analyze">
        </form>
    </body>
    </html>
    """


@app.route("/emotionDetector")
def sent_analyzer():
    """Analyze the provided text and return formatted emotion output."""
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is <b>{response['dominant_emotion']}</b>."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
