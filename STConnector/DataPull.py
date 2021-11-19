'''
Created on Nov 18, 2021

@author: nifty
'''

import requests
import json


def pull_jobs(p, auth_key):
    pageSize = 25
    pageNumber = p
    url = "https://ws.synchroteam.com/api/v3/job/list?page="+str(pageNumber)+"&pageSize="+str(pageSize)
    print(str(auth_key)[2:-1])
    payload={}
    headers = {
      'Content-Type': 'application/json',
      'Cache-Control': 'no-cache',
      'Accept': 'text/json',
      'Authorization': 'Basic '+str(auth_key)[2:-1],
      'Cookie': 'incap_ses_470_1982613=AqB3Dz4tyAB+v7CRCceFBlXClmEAAAAAqarg7LsDmWKfRHEhL9OWvQ==; visid_incap_1731256=LTiMQFjLRrGroWf4T1ehdeoOlGEAAAAAQUIPAAAAAADJqxM56s9FV6wfQGkMopqy; visid_incap_1982613=rM/3NEO5TE+h6vpvSybZHYMPlGEAAAAAQUIPAAAAAAAP80bL+chwIrzEz5CXDLgP; ASP.NET_SessionId=b01cgsbo2m1ege1gb5cecjg5'
    }
    
    response = requests.request("GET", url, headers=headers, data=payload)
    
    return response.json()
def pull_customs(auth_key):
    url = "https://ws.synchroteam.com/api/v3/customfield/list?type=job"

    payload = ""
    headers = {
        'authorization': "Basic "+str(auth_key)[2:-1],
        'accept': "text/json",
        'content-type': "application/json",
        'cache-control': "no-cache"
        }
    
    response = requests.request("GET", url, data=payload, headers=headers)
    return response.json()
leo = """"id": "160453_2111190756181",
            "myId": "",
            "num": 1,
            "description": "Description",
            "priority": "low",
            "customer": {
                "id": 5409780,
                "myId": null,
                "name": "ACME Corp"
            },
            "site": null,
            "equipment": null,
            "type": {
                "id": 108866,
                "name": "Standard Job"
            },
            "reportTemplate": {
                "id": 93689,
                "name": "Standard Job Report template"
            },
            "createdBy": {
                "id": 160453,
                "login": "tech1",
                "name": "Tech TEST"
            },
            "addressStreet": "279 Water Street",
            "addressProvince": null,
            "addressCity": "New York",
            "addressZIP": "10038",
            "addressCountry": "USA",
            "address": "279 Water Street, New York, USA",
            "addressComplement": null,
            "contactFirstName": null,
            "contactLastName": null,
            "contactMobile": null,
            "contactPhone": null,
            "contactEmail": null,
            "status": "created",
            "publicLink": "",
            "technician": {
                "id": 160453,
                "name": "Tech TEST",
                "login": "tech1"
            },
            "scheduledStart": "2021-11-19 07:56",
            "scheduledEnd": "2021-11-19 09:56",
            "actualStart": null,
            "actualEnd": null,
            "position": {
                "latitude": "40.7087252",
                "longitude": "-74.0008762"
            },
            "customFieldValues": null,
            "dateCreated": "2021-11-19 07:56",
            "dateModified": "2021-11-19 07:56"
rir = leo.split("\n")

tn = ""
for l in rir:
    if "{" in l:
        tn = l[l.index('"')+1:l.index('":')]+"_"
        continue
    if "}" in l:
        tn = ""
        continue
    #print(l)
    print(tn+l[l.index('"')+1:l.index(':')].replace('"','')+"|+|")
"""


    