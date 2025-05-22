import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        response.raise_for_status()
        response_json = json.loads(response.text)

        emotion_scores = response_json['emotionPredictions'][0]['emotion']
        anger = emotion_scores.get('anger', 0)
        disgust = emotion_scores.get('disgust', 0)
        fear = emotion_scores.get('fear', 0)
        joy = emotion_scores.get('joy', 0)
        sadness = emotion_scores.get('sadness', 0)

        dominant_emotion = max(
            {
                'anger': anger,
                'disgust': disgust,
                'fear': fear,
                'joy': joy,
                'sadness': sadness
            },
            key=lambda k: emotion_scores[k]
        )

        return {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
