from urllib.request import urlopen
from bs4 import BeautifulSoup
import re, datetime, random, sys, io

# backslashreplace = replace with backslashed escape sequences (escape unsuported chars)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,'cp437','backslashreplace')

pages = set()
random.seed(datetime.datetime.now())

# Retrieves a list of all internal links found on a page
def getInternalLinks(bsObj, includeUrl):
	internalLinks = []
	# Finds all links that begin with "/" or have the website's url
	for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in internalLinks:
				internalLinks.append(link.attrs['href'])
	return internalLinks

# Retrieves a list of external links found on a page
def getExternalLinks(bsObj, excludeUrl):
	externalLinks = []
	# Finds all links that start with "http" or "www" that
	# do not contain the current URL
	for link in bsObj.findAll("a",
						href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in externalLinks:
				externalLinks.append(link.attrs['href'])
	return externalLinks

def splitAddress(address):
	return address.replace("http://", "").replace("https://", "").split("/")

def getRandomExternalLink(startingPage):
	html = urlopen(startingPage)
	bsObj = BeautifulSoup(html, "html.parser")
	externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
	if len(externalLinks) == 0:
		internalLinks = getInternalLinks(bsObj, startingPage)
		return getRandomExternalLink(internalLinks[random.randint(0, 
													len(internalLinks)-1)])
	else:
		return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingSite):
	externalLink = getRandomExternalLink(startingSite)
	print("Random external link is: " + externalLink)
	followExternalOnly(externalLink)

followExternalOnly("https://en.wikipedia.org/wiki/Main_Page")