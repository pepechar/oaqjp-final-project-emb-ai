import requests
import json 

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    inputJson = { "raw_document": { "text": text_to_analyse } }

    resp = requests.post(url, 
                        headers = headers, 
                        json = inputJson)

    jsonResp = json.loads(resp.text)

    emotionDict = jsonResp["emotionPredictions"][0]["emotion"]
    emotionDict["dominant_response"] = max(emotionDict, key= emotionDict.get)

    
    return emotionDict

