from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO, open

def readPDF(pdfFile):
    resman = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(resman, retstr, laparams=laparams)

    process_pdf(resman, device, pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content

pdfFile = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf");
outString = readPDF(pdfFile)

print(outString)
pdfFile.close()