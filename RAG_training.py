import os
from langchain_community.document_loaders import PyMuPDFLoader
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
import re
load_dotenv()

pdf_path = "time_book.pdf"
loader = PyMuPDFLoader(pdf_path)

pages = loader.load()

print(len(pages))

print("##################################################")
## print(pages[3].page_content[:500])
print("\n\n")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def clean_text(text):
    text = re.sub(r"\s+" , " " , text)
    return text.split()

for doc in pages: 
    doc.page_content = clean_text(doc.page_content)


print("\n\n")
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap= 100, 
    separators=["\n\n", "\n" , "." , " "]
)

chunks = splitter.split_documents(pages)

print(len(chunks))

#print(chunks[0].page_content)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

embeddings = HuggingFaceEmbeddings(model_name = "intfloat/multilingual-e5-small")
vector_store = Chroma.from_documents(chunks, embeddings)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

retriver = vector_store.as_retriever(search_kwargs={"k":5})
test_query= "What are the four main steps of the Make Time framework?"
retrived = retriver.invoke(test_query)

for i , doc in enumerate(retrived): 
    print(f"====== chunk {i+1} ========")
    print(doc.page_content)
    print("\n")  

def format_docs(documents):
    texts=[]

    for doc in documents:
        texts.append(doc.page_content)
    return "\n\n".join(texts)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

SYSTEM_PROMPT = """
              You are a helpful AI assistant.

Answer the user's question using ONLY the context provided below.

If the context does not contain enough information,
say clearly that you do not know.

context:
{context}
"""

prompt = ChatPromptTemplate.from_messages([
    ("system",SYSTEM_PROMPT),
    ("human","{question}"),
])

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

llm = ChatGroq(
    model="qwen/qwen3.8-27b",
    temperature=0
)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

chain = ({
    "context": retriver | format_docs,
    "question": RunnablePassthrough(),
}
|prompt
|llm
|StrOutputParser()

)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

question = input ("you: ")
answar = chain.invoke(question)
print(answar)