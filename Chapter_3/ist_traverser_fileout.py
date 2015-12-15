from urllib.request import urlopen
from urllib import error
from bs4 import BeautifulSoup
import re, datetime, random

pages = set()

def getLinks(pageUrl):
	f = open("out.txt", "a", encoding="utf-8")
	try:
		html = urlopen("http://tecnico.ulisboa.pt/" + pageUrl)
		bsObj = BeautifulSoup(html, "html.parser")
		for link in bsObj.findAll("a", href=re.compile("^/")):
			if 'href' in link.attrs:
				if link.attrs["href"] not in pages:
					# New page found
					newPage = link.attrs["href"]
					f.write(newPage + "\n")
					pages.add(newPage)
					getLinks(newPage)
	except IOError as err:
		print("I/O ERROR number {}: {}".format(err.errno, err.strerror))
	except error.HTTPError as err:
		print("HTTPError: {}".format(err.code))
	except Exception:
		print("Exception: something went wrong...")
	finally:
		f.close()

getLinks("")
