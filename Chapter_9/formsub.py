import requests
params = {'firstname':'hello', 'lastname':'there'}
r = requests.post("http://pythonscraping.com/files/processing.php", data=params)
print(r.text)

files = {'uploadFile': open('1.png', 'rb')}
r = requests.post("http://pythonscraping.com/files/processing2.php", files=files)
print(r.text)