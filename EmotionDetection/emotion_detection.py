import requests


def emotion_detector(text_to_analyze):
    """
    Analyze emotions in text using the Watson NLP emotion prediction API.
    Returns a formatted dictionary with the dominant emotion.
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, json=input_json, headers=headers, timeout=30)
    formatted_response = response.json()["emotionPredictions"][0]["emotion"]

    anger = formatted_response["anger"]
    disgust = formatted_response["disgust"]
    fear = formatted_response["fear"]
    joy = formatted_response["joy"]
    sadness = formatted_response["sadness"]

    emotions = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness
    }

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion
    }