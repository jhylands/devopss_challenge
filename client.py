from getpass import getpass
import requests
import json

if __name__=="__main__":
    session = requests.Session()
    email = input("email:")
    password = getpass()
    session.post("http://chat.timep.co.uk/login", data={"email": email, "password":password})
    headers = {'Content-type': 'application/json'}
    while True:
        message = input(">")
        if message:
            response = session.post("http://chat.timep.co.uk/store_message", headers=headers, data=json.dumps({"message": message}))
            if response.status_code==200:
                print(response.text)
            else:
                print(response.text)
                print("Some kind of issue has occurred")
