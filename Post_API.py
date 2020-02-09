'''
Created on 30-Jan-2020

@author: HP
'''
import requests
from speedtest import json
from jsonpath import jsonpath


#POSITIVE TEST CASE
url= "https://api.postalpincode.in/pincode/523286"

response= requests.get(url)
json_response= json.loads(response.text)

print(json_response) 
name= jsonpath(json_response,'Name')
print(name)


#NEGATIVE TEST CASE
url1= "https://api.postalpincode.in/pincode/56662773"
response= requests.get(url1)
json_response= json.loads(response.text)
print(json_response) 
