from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq

from src import config

def fromat_docs(documents):
    return "\n\n".join(doc.page_content for doc in documents)

def build_prompt():
    return ChatPromptTemplate.from_messages([
        ("system", config.SYSTEM_PROMPT),
        ("human", "{question}"),
    ])

def build_model():
    return ChatGroq(model=config.LLM_MODEL, temperature=config.TEMPERATURE)


def ask (chain, question: str)-> str:
    return chain.invoke(question)

