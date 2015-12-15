from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")
# Find all "img" tags whose "src" attribute matches the regex
images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
for image in images:
	print(image["src"]) # same as print(image.attrs["src"])

#Find all tags which have exactly 2 attributes
two_attrs = bsObj.findAll(lambda tag: len(tag.attrs) == 2)
for tag in two_attrs:
	print(tag)