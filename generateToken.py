import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def generateToken():
    url = "https://cloud.appscan.com/api/V2/Account/ApiKeyLogin"
    payload = json.dumps({
        "KeyId": os.environ['keyId'],
        "KeySecret": os.environ['secretKey']
    })
    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.json()['Token'])
    return response.json()['Token']