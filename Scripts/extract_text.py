import os
import re
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import BytesIO


def clear_text():
    open("../output/Output.txt", "w").close()

# writelines function


def writelines(self, lines):
    self._checkClosed()
    for line in lines:
        self.write(line)

# PDF to text Function.


def pdf_to_text(path):
    manager = PDFResourceManager()
    retstr = BytesIO()
    layout = LAParams(all_texts=True)
    device = TextConverter(manager, retstr, laparams=layout)
    filepath = open(path, 'rb')
    interpreter = PDFPageInterpreter(manager, device)

    for page in PDFPage.get_pages(filepath, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()
    filepath.close()
    device.close()
    retstr.close()
    return text


if __name__ == "__main__":

    clear_text()
    # fname : List contain pdf documents names.
    fname = os.listdir('../split/')
    # fname: must be sorted.
    fname.sort(key=lambda f: int(re.sub('\D', '', f)))
    length = len(fname)

    for i in range(length):  # Repeat each operation for each document.

        # Extract text with PDF_to_text Function call
        text_output = pdf_to_text(('../split/{}').format(fname[i]))
        # Decode result from bytes to text
        text1_output = text_output.decode("utf-8")
        print(text1_output)

        # Save extracted text to TEXT_FILE
        with open("../output/Output.txt", "a", encoding="utf-8") as text_file:
            text_file.writelines(text1_output)
