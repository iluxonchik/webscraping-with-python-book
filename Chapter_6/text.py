from urllib.request import urlopen

text = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1.txt").read()
print(text)

text = str(urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt").read(), "utf-8")
print(text)  