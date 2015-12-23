from bs4 import BeautifulSoup
from urllib.request import urlopen
import re, pymysql, connectvars

conn = pymysql.connect(host = connectvars.DB_HOST, user = connectvars.DB_USER, 
                        passwd = connectvars.DB_PWD, db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute("USE wikipedia")

def insertPageIfNotExists(url):
    cur.execute("SELECT * FROM pages WHERE url = %s", (url))
    if cur.rowcount == 0:
        cur.execute("INSERT INTO pages (url) VALUES (%s)", (url))
        conn.commit
        return cur.lastrowid
    else:
        fetch_res = cur.fetchone()
        print("Already exists: " + str(fetch_res))
        return fetch_res[0]

def insertLink(fromPageId, toPageId):
    cur.execute("SELECT * FROM links WHERE fromPageId = %s AND toPageId = %s",
                        (int(fromPageId), int(toPageId)))
    if cur.rowcount == 0:
        cur.execute("INSERT INTO links(fromPageId, toPageId) VALUES(%s, %s)", (int(fromPageId), int(toPageId)))
        conn.commit()

pages = set()

def getLinks(pageUrl, recursionLevel):
    global pages
    if recursionLevel > 5:
        return
    pageId = insertPageIfNotExists(pageUrl)
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
        insertLink(pageId, insertPageIfNotExists(link.attrs['href']))

        if link.attrs['href'] not in pages:
            # New page found! Add it and search for links
            newPage = link.attrs['href']
            pages.add(newPage)
            getLinks(newPage, recursionLevel + 1)

getLinks("/wiki/Kevin_Bacon", 0)
cur.close()
conn.close()