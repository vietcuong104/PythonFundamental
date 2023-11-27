import PyPDF2

pdf = open("eBook-How-to-Build-a-Career-in-AI.pdf", "rb")
reader = PyPDF2.PdfReader(pdf)
page = reader.pages[2]
print(page.extract_text())