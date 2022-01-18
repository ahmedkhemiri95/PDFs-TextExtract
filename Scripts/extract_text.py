from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser


class PDFToText:

    def __init__(self, filePath):
        self.outString = StringIO()  # instantiate object
        self.pdfPath = filePath

    def openFile(self):
        with open(self.pdfPath, 'rb') as pdfFile:
            # instantiate objects for imported classes
            parser = PDFParser(pdfFile)
            doc = PDFDocument(parser)
            rsrcmgr = PDFResourceManager()
            device = TextConverter(rsrcmgr, self.outString, laparams=LAParams())
            interpreter = PDFPageInterpreter(rsrcmgr, device)

            # iterate over pages
            for page in PDFPage.create_pages(doc):
                interpreter.process_page(page)

    def run(self):
        self.openFile()
        return self.outString.getvalue()
