from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src import config

def split_pages (pages):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = config.CHUNK_SIZE,
        chunk_overlap = config.CHUNK_OVERLAP,
        separators= config.SEPERATORS,
    )
    return splitter.split_documents(pages)


def build_vector_store(chunks):
    embeddings = HuggingFaceEmbeddings(model_name = config.EMBEDDING_MODEL)
    return Chroma.from_documents(chunks, embeddings)


def get_retriever(vector_store):
    return vector_store.as_retriever(search_kwargs={"k": config.TOP_K})
