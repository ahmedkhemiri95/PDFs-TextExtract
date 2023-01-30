import os
from PyPDF2 import PdfReader, PdfWriter
# Solution based in two functions:
# 1.pdf remove : Remove existed pdf documents(result for your last split operation)
# 2.pdf splitter : Split your main pdf document into group of documents.


def pdf_remove(length):
    for i in range(length):
        # Remove existed pdf documents in folder.
        os.remove("../PDFs-TextExtract/split/{}".format(fname[i]))
        print("Deleted: ../PDFs-TextExtract/split/{}".format(fname[i]))


def pdf_splitter(path):
    fname = os.path.splitext(os.path.basename(path))[0]
    pdf_reader = PdfReader(path)
    for page in range(len(pdf_reader.pages)):
        pdf_writer = PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[page])

        output_filename = '../PDFs-TextExtract/split/{}.pdf'.format(page+1)

        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)

        print('Created: {}'.format(output_filename))


if __name__ == '__main__':

    # specifiy your main pdf document path.
    path = '../PDFs-TextExtract/pdf_merged.pdf'
    # fname: List contain pdf documents names in folder
    fname = os.listdir('../PDFs-TextExtract/split/')
    length = len(fname)  # Retrieve List fname Length.

    # call pdf remove function
    pdf_remove(length)
    # call pdf splitter function
    pdf_splitter(path)
