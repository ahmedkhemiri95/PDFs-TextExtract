"""
This script consist of:
* Collect Pdf Files from uploads folder
* Split Pdf Files page by page.
* Save Splitted pdf pages to output Folder.
"""

import os
from PyPDF2 import PdfFileReader, PdfFileWriter


def splitting(upload_folder, split_folder):
    '''Do collect PDF files, split pages and save them
    '''

    entries = os.listdir(upload_folder)
    path = os.path.abspath(split_folder)

    for entry in entries:

        uploaded_file = os.path.join(upload_folder, entry)
        output_file_folder = os.path.join(path, entry)

        if not os.path.isdir(output_file_folder):
            os.mkdir(output_file_folder)

            pdf = PdfFileReader(uploaded_file, strict=False)
            for page in range(pdf.getNumPages()):
                pdf_writer = PdfFileWriter()
                pdf_writer.addPage(pdf.getPage(page))
                output_filename = \
                    os.path.join(output_file_folder, f'{page+1}.pdf')
                with open(output_filename, 'wb') as out:
                    pdf_writer.write(out)
