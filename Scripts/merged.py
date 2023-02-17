import glob
from PyPDF2 import PdfWriter, PdfReader


def merger(output_path, input_paths):
    pdf_writer = PdfWriter()
    for path in input_paths:
        pdf_reader = PdfReader(path)
        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])
    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)


if __name__ == '__main__':
    paths = glob.glob('../PDFs-TextExtract/samples/*.pdf')
    paths.sort()
    merger('../PDFs-TextExtract/pdf_merged.pdf', paths)
    print("Done, PDF Merged successfully..")
