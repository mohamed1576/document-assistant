# Make Time RAG Assistant: v1 vs v2

A Retrieval-Augmented Generation (RAG) project that answers questions about the book *Make Time* using only text retrieved from its PDF.

This repo keeps **two versions of the same project side by side**: [v1_basic](v1_basic/) is the original single script, and [v2_structured](v2_structured/) is the same logic reorganized into modules and functions.

## What it does

```
PDF -> load & clean -> split into chunks -> embed -> store in Chroma
                                                          |
question -> retrieve top 5 chunks -> prompt -> LLM -> answer
```

The prompt forces the model to answer **only** from the retrieved context and to say it does not know when the context is not enough.

## Tech stack

- **Language:** Python (version pinned in `.python-version`), managed with `uv`
- **Framework:** LangChain
- **PDF loading:** PyMuPDF
- **Embeddings:** Hugging Face `intfloat/multilingual-e5-small` (runs locally)
- **Vector store:** Chroma
- **LLM:** `qwen/qwen3.8-27b` served by Groq

## Project structure

```
ai-document-assistant/
├── v1_basic/
│   ├── RAG_training.py        # the original single script
│   ├── structured_output.py
│   └── README.md
├── v2_structured/
│   ├── main.py                # CLI entry point
│   └── src/
│       ├── config.py          # all settings in one place
│       ├── loader.py          # load and clean the PDF
│       ├── indexer.py         # split, embed, store, retriever
│       └── rag.py             # prompt + LLM chain + ask()
├── docs/                      # put time_book.pdf here (not committed)
├── pyproject.toml
└── uv.lock
```

## Getting started

1. Install [uv](https://docs.astral.sh/uv/) and clone this repo.
2. Install dependencies:
   ```bash
   uv sync
   ```
3. Create a `.env` file in the repo root:
   ```
   GROQ_API_KEY=your_groq_api_key
   ```
4. Put your own copy of the book at `docs/time_book.pdf` (the PDF is not included because it is copyrighted).
5. Run a version **from the repo root**:
   ```bash
   uv run python v1_basic/RAG_training.py
   uv run python v2_structured/main.py
   ```
   The first run downloads the embedding model and builds the index, which takes a little while. Then type a question at the `you:` prompt.

## v1 vs v2: what changed

| Aspect | v1 | v2 |
|---|---|---|
| Structure | Everything in one file, top to bottom | `loader`, `indexer` and `rag` modules, each with one job |
| Settings | Hardcoded inside the logic | All in `config.py` |
| Reuse | Runs once and exits | `build_assistant()` builds the chain once, and `ask(chain, question)` can be called as many times as needed |
| Entry point | Code runs as soon as the file is executed or imported | `main.py` with an `if __name__ == "__main__"` guard |
| Debug output | Test prints and a hardcoded test query left in | None |
| Behavior | Baseline | Identical on purpose: same models, chunking and prompt |

### A bug found along the way

`clean_text` returned `text.split()`, which is a **list**, not a string. The text splitter then crashed with `TypeError: expected string or bytes-like object, got 'list'`. It is fixed in both versions (in v1 with the smallest possible change).