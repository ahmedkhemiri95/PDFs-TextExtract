from extract_text import PDFToText

if __name__ == '__main__':

    userInputPDF = input("[+] Path to PDF file... >> ")
    userOutPDF = input("[+] Path to the outfile location... >> ")
    extractText = PDFToText(userInputPDF)
    writeText = extractText.run()

    if '\\' in userOutPDF:
        userOutPDF = userOutPDF.replace('\\', '\\')
        with open(userOutPDF, 'w') as outPath:
            for line in writeText:
                outPath.write(line)
