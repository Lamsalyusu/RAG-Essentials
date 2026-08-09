import os
from langchain_community.document_loaders import (
    TextLoader,
    WebBaseLoader,
    DirectoryLoader,
    PyPDFLoader,)
import tempfile
# import beautifulsoup4 as bs4
from pathlib import Path
# form langchain_community.document_loaders import PyPDFLoader, TextLoader
from dotenv import load_dotenv
load_dotenv()


def load_text_file():
    with tempfile.NamedTemporaryFile(delete=False,suffix='.txt') as temp_file:
        temp_file.write (b"Hello, this is a sample text file for testing.")
        temp_file_path = temp_file.name


    try:
        loader = TextLoader(temp_file_path)
        # function that returns a list of Document objects
        documents =loader.load()
        print(f'loaded {len(documents)} documents from {temp_file_path}')
        print(f'content preview: {documents[0].page_content[:100]}')
        print(f'metadata: {documents[0].metadata}')

        for doc in documents:
            print("Document Content")
            print(doc)
            print(doc.page_content)
            # print(doc.metadata)
    finally:
        os.remove(temp_file_path)


def pdf_loader(pdf_path:str):
    try:
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()

        print(f'Loaded {len(documents)} document(s) from PDFs')
        for i ,doc in enumerate(documents):
            print(f"Document {i+1} Content:")
            print(doc.page_content)
            print(f"Metadata: {doc.metadata}")
    except Exception as e:
        print(f"Error loading PDF: {e}")


if __name__ == "__main__":
#     load_text_file()
    pdf_loader('docs/hello.pdf')