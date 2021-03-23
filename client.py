import requests
import json

if __name__=="__main__":
    headers = {'Content-type': 'application/json'}
    while True:
        message = input(">")
        if message:
            response = requests.post("http://localhost:8008/store", headers=headers, data=json.dumps({"message": message}))
            if response.status_code==200:
                print(response.text)
            else:
                print("Some kind of issue has occurred")
