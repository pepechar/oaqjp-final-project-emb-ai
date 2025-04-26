import requests
import json 

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    inputJson = { "raw_document": { "text": text_to_analyse } }

    resp = requests.post(url, 
                        headers = headers, 
                        json = inputJson)

    print(f"THIS IS THE STATUS CODE FORM THE API: {resp.status_code}")


    if resp.status_code == 200: 
        jsonResp = json.loads(resp.text)
        emotionDict = jsonResp["emotionPredictions"][0]["emotion"]
        emotionDict["dominant_response"] = max(emotionDict, key= emotionDict.get)

    elif resp.status_code == 400: 
        emotionDict = {
            "dominant_response": None, 
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None
        }
    
    else: 
        emotionDict = {
            "dominant_response": None, 
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None
        }

    return emotionDict

