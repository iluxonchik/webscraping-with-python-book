from urllib.request import urlopen
from bs4 import BeautifulSoup
import re, datetime, random

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
	html = urlopen("https://en.wikipedia.org/" + articleUrl)
	bsObj = BeautifulSoup(html, "html.parser")
	return bsObj.find("div", id="bodyContent").findAll("a", 
						{"href":re.compile("^(/wiki/)((?!:).)*$")})

def getHistoryIPs(pageUrl):
	pageUrl = pageUrl.replace("/wiki/", "")
	historyUrl = "http://en.wikipedia.org/w/index.php?title=" + pageUrl + "&action=history"
	print("history is: " + historyUrl)
	html = urlopen(historyUrl)
	bsObj = BeautifulSoup(html, "html.parser")

	ipAddresses = bsObj.findAll("a", {"class":"mw-anonuserlink"})
	addressList = set()
	for ipAddress in ipAddresses:
		addressList.add(ipAddress.get_text())
	return addressList

links = getLinks("/wiki/Python_(programming_language)")

while len(links) > 0:
	for link in links:
		print("-----------------------")
		historyIPs = getHistoryIPs(link.attrs['href'])
		for historyIP in historyIPs:
			print(historyIP)

	newLink = links[random.randint(0, len(links) - 1)].attrs["href"]
	links = getLinks(newLink)