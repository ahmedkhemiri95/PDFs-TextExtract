import os
from PyPDF2 import PdfFileReader, PdfFileWriter
#Solution based in two functions:
#1.pdf remove : Remove existed pdf documents(result for your last split operation)
#2.pdf splitter : Split your main pdf document into group of documents.



def pdf_remove (length):
 for i in range(length): 
        os.remove("../PDFs-TextExtract/split/{}".format(fname[i])) #Remove existed pdf documents in folder.
        print("Deleted: ../PDFs-TextExtract/split/{}".format(fname[i]))

def pdf_splitter(path):
    fname = os.path.splitext(os.path.basename(path))[0]
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
 
        output_filename = '../PDFs-TextExtract/split/{}.pdf'.format(page+1)
 
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)
 
        print('Created: {}'.format(output_filename))
        
 
if __name__ == '__main__':

  path = '../PDFs-TextExtract/pdf_merged.pdf' #specifiy your main pdf document path.
  fname = os.listdir('../PDFs-TextExtract/split/') #fname: List contain pdf documents names in folder
  length = len(fname) #Retrieve List fname Length.
  
  #call pdf remove function
  pdf_remove(length) 
  #call pdf splitter function
  pdf_splitter(path) 

