from flask import Flask, render_template, request
import requests
import json
import generateToken

app = Flask(__name__)
token=generateToken.generateToken()

# For getting tenant details
@app.route('/')
def index():
    response = requests.request(
         "GET", "https://cloud.appscan.com/api/V2/Account/TenantInfo", headers={
              'Authorization':'Bearer ' + token
            })
    print(response.json())
    return render_template('index.html', data=response.json())

# For getting scan details based on id
@app.route('/scan',)
def scanReport():
    scanID = request.args.get('scanid')
    url = f'https://cloud.appscan.com/api/v2/Scans/{scanID}'
    response = requests.request("GET", url, headers={
        'Authorization': 'Bearer ' + token,
    })
    print(response.json())
    return render_template('result.html', data=response.json())


if __name__ == '__main__':
    app.run()
