from extract_text import PDFToText

if __name__ == '__main__':

    userInput = input("[+] Path to PDF file... >> ")
    extractText = PDFToText(userInput)
    writeText = extractText.run()

    with open('C:\\Users\\tutko\\Desktop\\output.txt', 'w') as outPath:
        for line in writeText:
            outPath.write(line)
