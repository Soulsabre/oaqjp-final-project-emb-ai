import requests,json

def emotion_detector(text_to_analyze):
    '''This function analyzes the given text using the IBM NLP AI Emotion Prediction engine.
        It returns a dictionary with the scores of the 5 emotions - anger, digust, fear, joy and sadness
        as well as the dominnat_emotion (emotion with the highest score)
    '''
    url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url,json=myobj, headers=headers)

    if response.status_code == 400:
        anger_score = 'None'
        disgust_score = 'None'
        fear_score = 'None'
        joy_score = 'None'
        sadness_score = 'None'
        dominant_emotion = 'None'
        
    else:
        formatted_response = json.loads(response.text)
        emotions = formatted_response["emotionPredictions"][0]["emotion"]
   
        anger_score = emotions["anger"]
        disgust_score = emotions["disgust"]
        fear_score = emotions["fear"]
        joy_score = emotions["joy"]
        sadness_score = emotions["sadness"]

        dominant_emotion = ""
        dominant_score = 0
        for emotion, score in emotions.items():
            if score > dominant_score:
                dominant_score = score
                dominant_emotion = emotion

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
