from langchain_community.document_loaders import PyPDFLoader,TextLoader

pdf_loader = PyPDFLoader("hello.pdf")
pdf_pages = pdf_loader.load()

print(pdf_pages[0].page_content)  # Text of page 1
print(pdf_pages[0].metadata)
print("doc loaded")
