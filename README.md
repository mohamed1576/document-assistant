# 📚 Make Time Book RAG Assistant

A Retrieval-Augmented Generation (RAG) project that answers questions about the *Make Time* book using information retrieved from its PDF.

The application uses LangChain to process the book, Chroma to retrieve relevant text, and a Large Language Model (LLM) to generate answers based on the retrieved context.

---

## 📌 Project Overview

This project demonstrates how RAG can be used to build a question-answering system based on a specific document, helping users find information from a book without relying solely on the model's general knowledge.

### Key Features:
- **PDF Processing:** Loads and processes the book's content.
- **Text Chunking:** Splits the extracted text into smaller, overlapping chunks.
- **Semantic Search:** Uses Hugging Face embeddings and Chroma to retrieve relevant information.
- **Context-Based Answers:** Uses a Groq-hosted LLM to answer questions based on the retrieved text.
- **Interactive CLI:** Allows users to ask questions directly from the terminal.

---

## 📁 Project Structure

- `main.py` - Main script containing the RAG pipeline.
- `time_book.pdf` - Source book used for question answering.
- `.env` - Stores the Groq API key.
- `requirements.txt` - Project dependencies.

---

## 🛠️ Tech Stack

- **Language:** Python
- **Framework:** LangChain
- **PDF Processing:** PyMuPDF
- **Embeddings:** Hugging Face (`multilingual-e5-small`)
- **Vector Database:** Chroma
- **LLM Provider:** Groq
- **Language Model:** Qwen

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd <YOUR_PROJECT_FOLDER>
```

### 2. Install dependencies

```bash
pip install langchain-community langchain-text-splitters langchain-huggingface langchain-chroma langchain-groq langchain-core pymupdf sentence-transformers python-dotenv
```

### 3. Configure environment variables

Create a `.env` file and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key
```

### 4. Add the PDF

Place `time_book.pdf` in the project directory.

### 5. Run the application

```bash
python main.py
```

Enter your question in the terminal to receive an answer based on the retrieved book content.

---

## 🧠 RAG Pipeline

1. **Document Loading:** Extracts text from the PDF.
2. **Text Splitting:** Divides the text into chunks with overlapping content.
3. **Embedding Generation:** Converts text chunks into vector representations.
4. **Vector Storage & Retrieval:** Stores embeddings in Chroma and retrieves the most relevant chunks for each question.
5. **Answer Generation:** Passes the retrieved context and user question to the LLM to generate an answer.

---

## 🎯 Project Goal

The goal of this project is to gain practical experience building a document-based question-answering system using Retrieval-Augmented Generation and modern AI tools.

---
