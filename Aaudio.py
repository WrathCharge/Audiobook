import pyttsx3
import PyPDF2
book = open('The Hidden Oracle.pdf', 'rb')# Write the book name you want it to read. But make sure it is in the same folder as the python file 
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
for num in range(212, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()