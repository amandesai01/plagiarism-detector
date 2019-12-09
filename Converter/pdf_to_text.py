import PyPDF2
import textract

from ntlk.tokenize import word_tokenize
from ntlk.corpus import stopwords

def grab(file_path):
    pdf_file = open(file_path,'rb')
    pdf_reader = PyPDF2.PDF
