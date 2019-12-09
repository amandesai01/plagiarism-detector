import PyPDF2
import textract
import cleaner

def grab(file_path):
    pdf_file = open(file_path,'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    num_of_pages = pdf_reader.numPages

    count = 0
    text =""

    while count<num_of_pages:
        page = pdf_reader.getPage(count)
        count+=1
        text+= page.extractText()

    if text != "":
        text = text
    else:
        text = textract.process(file_path,method='tesseract',language='eng')

    # text = cleaner.clean(text)


    return(text)


file1 = input()
grab(file1)
