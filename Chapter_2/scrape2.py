from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)

# Only print the children (i.e. direct descendants) of table with id giftList
for child in bsObj.find("table", {"id":"giftList"}).children:
	print(child)

# Print all descendants of table with id giftList
for child in bsObj.find("table", {"id":"giftList"}).descendants:
	print(child)

# Print all rows from table, except the fitst one
for sibling in bsObj.find("table", {"id":"giftList"}).tr.next_siblings:
	print(sibling)

# Print the previous sibling of the parent of "img" tag with the specified "src" attribute value
print(bsObj.find("img", {"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())