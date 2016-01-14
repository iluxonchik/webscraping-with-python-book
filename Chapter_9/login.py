import requests

params = {'username':'user', 'password':'password'}
r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
print("Cookie is set to: " + str(r.cookies.get_dict()))
print("----------------")
print("Profile page:")
r = requests.get("http://pythonscraping.com/pages/cookies/profile.php", cookies=r.cookies)
print(r.text)

# Session object keeps track of session infomation, sucha as cookies, headers and info about protocol
session = requests.Session()
s = session.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
print("Cookie is set to:")
print(s.cookies.get_dict())
print("----------------")
print("Profile page:")
s = session.get("http://pythonscraping.com/pages/cookies/profile.php")
print(s.text)