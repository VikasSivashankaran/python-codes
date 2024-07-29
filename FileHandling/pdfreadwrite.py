from pypdf import PdfReader

reader = PdfReader("Resume.pdf")
number_of_pages = len(reader.pages)
get_fields = (reader.get_fields())
page = reader.pages[0]
text = page.extract_text()
print(number_of_pages)
print(get_fields)
print(page)
print(text)