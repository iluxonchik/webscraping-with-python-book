from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode("ascii", "ignore")
dataFile = StringIO(data) # treat sring as a file
csvReader = csv.reader(dataFile)

for row in csvReader:
    print("The album is: " + row[0] + " and the year is: " + row[1])