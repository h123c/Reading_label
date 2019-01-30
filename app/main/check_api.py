#encoding:utf-8
import time
import json
import requests

def language_check(text):
    HOST_check_api = 'http://localhost:8081/v2/check'
    data = {
            "language": "en-US",
            "text": text
        }
    r = requests.get(HOST_check_api, data)
    return r

def analysis_check_res(check_res):
    DICT_res = json.loads(check_res.text)
    res = DICT_res["matches"]
    return res
if __name__ == "__main__":
    text = "I am do homework now. No, I'm not. "
    #text = "my last name, and Chen is my first name. I am a good student. My favourite food is fish. It's very delicious. Do you like this? Some chicken! Chicken is my mothers favourite food. She think chicken is healthy and delicious food. Her name is Liu Mel. Her job is at a hospital. She is a nurse. What about my father? He is a manager of a company. His name is Li Wei. He likes noodles. It is his favourite food. He usually eats noodles for his breakfast in weekdays. This is my family, I love my family very much. And they love me too. "
    TIME_start = time.time()
    res = language_check(text)
    analysis_check_res(res)
    print "time is:", time.time() - TIME_start
    print res.text
    with open("language_res.json", "w") as f:
        json.dump(json.loads(res.text), f)