import requests
import json
"""
# survey_list = response_json["data"]["surveys"]
# Will print to file to json api connect
# https://developer.surveymonkey.com/api/v3/: 
 curl -i -X GET -H "Authorization:bearer YOUR_ACCESS_TOKEN" -H "Content-Type""application/json" https://api.surveymonkey.net/v3/surveys
"""

client = requests.session()
Acctkn = 'vh3yCNiDUqVnfioIVDTZDVePjwGeBIUlr..U-zubCTFvdUl4vWiUUUWgZVgoycoJ474NvFW-qSTD-s2XQ5KNt1GwH1gjjkFFkp2MGSbkHdi3fW0Vdmcfq5CpaGukTzM3'

client = requests.session()

headers = {
    "Authorization": "bearer %s" % Acctkn,
    "Content-Type": "application/json"
}

HOST = "https://api.surveymonkey.net"
SURVEY_DETAIL_ENDPOINT = "/v3/surveys/SURVEYID/details"
uri = "%s%s" % (HOST, SURVEY_DETAIL_ENDPOINT)

response = client.get(uri, headers=headers)

survey_data = response.json()

response_json = response.json()
answer_dict = {}
for page in survey_data['pages']:
    for question in page['questions']:

        # Rows, choices, other, and cols all make up the possible answers
        answers = question['answers'].get('rows', [])\
            + question['answers'].get('choices', [])\
            + question['answers'].get('other', [])\
            + question['answers'].get('cols', [])

        for answer in answers:
            answer_dict[answer['id']] = answer

print(response_json['data'])