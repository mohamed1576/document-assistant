import re

from langchain_community.document_loaders import PyMuPDFLoader

def text_clean(text: str) -> str:
    return re.sub(r"\t+", " " , text)


def pdf_loader(pdf_path: str):
    loader = PyMuPDFLoader(pdf_path)
    pages = loader.load()

    for page in pages: 
        page.page_content = text_clean(page.page_content)

    return pages

