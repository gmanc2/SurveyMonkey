import requests
import json
"""
# survey_list = response_json["data"]["surveys"]
# Will print to file to json api connect
# https://developer.surveymonkey.com/api/v3/: 
 curl -i -X GET -H "Authorization:bearer YOUR_ACCESS_TOKEN" -H "Content-Type""application/json" https://api.surveymonkey.net/v3/surveys
"""

client = requests.session()
Acctkn = 'Redacted'

client = requests.session()

headers = {
    "Authorization": "bearer %s" % Acctkn,
    "Content-Type": "application/json"
}

HOST = "https://api.surveymonkey.net"
SURVEY_DETAIL_ENDPOINT = "/v3/surveys/277817842/details"
uri = "%s%s" % (HOST, SURVEY_DETAIL_ENDPOINT)

response = client.get(uri, headers=headers)

survey_data = response.json()

response_json = response.json()
answer_dict = {}

with open('data.json', 'w') as df:
    json.dump(response_json, df)

print(answer_dict)
