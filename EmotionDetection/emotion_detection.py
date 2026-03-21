import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj =  { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj , headers = headers)
    response = json.loads(response.text)
    emotions_map = response['emotionPredictions'][0]
    emotions_map = emotions_map['emotion']
    anger_score = emotions_map['anger']
    disgust_score = emotions_map['disgust']
    fear_score = emotions_map['fear']
    joy_score = emotions_map['joy']
    sadness_score = emotions_map['sadness']
    gathered_emotions = {'anger': anger_score,'disgust': disgust_score,'fear': fear_score,'joy': joy_score,'sadness': sadness_score,}
    dominant_emotion_score = 0
    for emotion,score in gathered_emotions.items():
        if(score > dominant_emotion_score):
            dominant_emotion = emotion
            dominant_emotion_score = score
    gathered_emotions['dominant_emotion'] = dominant_emotion
    return gathered_emotions