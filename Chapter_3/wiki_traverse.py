from urllib.request import urlopen
from bs4 import BeautifulSoup
import re, datetime, random, io, sys

# backslashreplace = replace with backslashed escape sequences (escape unsuported chars)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,'cp437','backslashreplace')

pages = set()

def getLinks(pageUrl):
	html = urlopen("https://en.wikipedia.org" + pageUrl)
	bsObj = BeautifulSoup(html)

	try:
		print(bsObj.h1.get_text()) # title
		print(bsObj.find(id = "mw-content-text").findAll("p")[0]) # first paragraph
		print(bsObj.find(id = "ca-edit").find("span").find("a").attrs["href"]) # edit link
	except AttributeError:
		print("This page is missing something, but it's all good.")

	for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
		if 'href' in link.attrs:
			if link.attrs["href"] not in pages:
				# New page found
				newPage = link.attrs['href']
				print("------------------------\n" + newPage)
				pages.add(newPage)
				getLinks(newPage)

getLinks("")
