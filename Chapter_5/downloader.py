import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory = "downloaded"
baseUrl = "http://pythonscraping.com"

def getAbsoluteURL(baseUrl, source):
	if source.startswith("http://www."):
		url = "http://" + source[11:]
	elif source.startswith("http://"):
		url = source
	elif source.startswith("www."):
		url = "http://" + source[4:]
	else:
		url = baseUrl + "/" + source
	if baseUrl not in url:
		return None
	return url

def getDownloadPath(baseUrl, absoluteUrl, dowonloadDirectory):
	path = absoluteUrl.replace("www.", "")
	path = path.replace(baseUrl, "")
	path = dowonloadDirectory + path

	directory = os.path.dirname(path)
	if not os.path.exists(directory):
		os.makedirs(directory)

	return removeGet(path)

def removeGet(fileName):
	"""
	Removes any characters after "?" in string
	"""
	pos = fileName.find("?")
	if pos != -1:
		return fileName[:pos]
	return fileName

html = urlopen(baseUrl)
bsObj = BeautifulSoup(html, "html.parser")
downloadList = bsObj.findAll(src=True)

for download in downloadList:
	fileUrl = getAbsoluteURL(baseUrl, download["src"])
	if fileUrl is not None:
		print(fileUrl)
		urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))
