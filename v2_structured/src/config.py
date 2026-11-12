PDF_PATH = "docs/time_book.pdf"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
SEPERATORS = ["/n/n" , "/n" , "." , " "]

EMPEDDING_MODEL = "intfloat/multilingual-e5-small"
TOP_K = 5

LLM_MODEL = "qwen/qwen3.8-27b"
TEMPERATURE = 0

SYSTEM_PROMPT = """
You are a helpful AI assistant.

Answer the user's question using ONLY the context provided below.
If the context does not contain enough information,
say clearly that you do not know.

context:
{context}
"""

