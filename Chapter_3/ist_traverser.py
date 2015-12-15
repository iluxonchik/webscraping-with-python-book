from urllib.request import urlopen
from bs4 import BeautifulSoup
import re, datetime, random

pages = set()

def getLinks(pageUrl):
	html = urlopen("http://tecnico.ulisboa.pt/" + pageUrl)
	bsObj = BeautifulSoup(html)
	for link in bsObj.findAll("a", href=re.compile("^/")):
		if 'href' in link.attrs:
			if link.attrs["href"] not in pages:
				# New page found
				newPage = link.attrs["href"]
				print(newPage)
				pages.add(newPage)
				getLinks(newPage)

getLinks("")
