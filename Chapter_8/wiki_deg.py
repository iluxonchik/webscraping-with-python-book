from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql, connectvars

conn = pymysql.connect(host=connectvars.DB_HOST, user=connectvars.DB_USER, passwd=connectvars.DB_PWD, charset='utf8')

cur = conn.cursor()
cur.execute("USE wikipedia")

# BAD solution, exceptions should not be used for that!
class SolutionFound(RuntimeError):
    def __init__(self, message):
        self.message = message

def getLinks(fromPageId):
    cur.execute("SELECT toPageId FROM links WHERE fromPageId = %s", (fromPageId))
    return None if cur.rowcount == 0 else [x[0] for x in cur.fetchall()]

def constructDict(currentPageId):
    links = getLinks(currentPageId)
    if links:
        return dict(zip(links, [{}]*len(links))) # form a 
    return {}

def searchDepth(targetPageId, currentPageId, linkTree, depth):
    if depth == 0:
        return linkTree
    if not linkTree:
        linkTree = constructDict(currentPageId)
        if not linkTree:
            # no links found, cannot continue at this node
            return {}
    if targetPageId in linkTree.keys():
        print("TARGET " + str(targetPageId) + " FOUND!")
        raise SolutionFound("PAGE: " + str(currentPageId))

    for branchKey, branchValue in linkTree.items():
        try:
            linkTree[branchKey] == searchDepth(targetPageId, branchKey, branchValue, depth-1)

        except SolutionFound as e:
            print(e.message)
            raise SolutionFound("PAGE: " + str(currentPageId))
    return linkTree

try:
    searchDepth(10, 2, {}, 4)
    print("No solution found!")
except SolutionFound as e:
    print(e.message)