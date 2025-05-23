import json
import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        emotion_dict = formatted_response['emotionPredictions'][0]['emotion']
        end_response = {
                    'anger': emotion_dict['anger'],
                    'disgust': emotion_dict['disgust'],
                    'fear': emotion_dict['fear'],
                    'joy': emotion_dict['joy'],
                    'sadness': emotion_dict['sadness'],
                    'dominant_emotion': max(emotion_dict, key = emotion_dict.get)
        }
    elif response.status_code == 400:
        end_response = {
                    'anger': None,
                    'disgust': None,
                    'fear': None,
                    'joy': None,
                    'sadness': None,
                    'dominant_emotion': None
        }
    return end_response