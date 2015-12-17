import json
from urllib.request import urlopen

def getCountry(ipAddress):
	response = urlopen("http://freegeoip.net/json/" + ipAddress).read().decode('utf-8')
	response_json = json.loads(response)
	return response_json.get("country_code")

print(getCountry("50.78.253.58"))