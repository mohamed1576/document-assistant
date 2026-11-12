from src import config
from src.indexer import split_pages , build_vector_store , get_retriever
from src.loader import pdf_loader
from src.rag import ask , build_chain
from dotenv import load_dotenv

def build_assistant ():
    pages = pdf_loader(config.PDF_PATH)
    chunks = split_pages(pages)
    vector_store = build_vector_store(chunks)
    retriever = get_retriever(vector_store)
    return build_chain(retriever)

def main():
    load_dotenv()
    chain = build_assistant()

    question = input("you: ")
    print(ask(chain , question))

if __name__ == "__main__":
    main()
