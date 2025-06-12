# 🤖 RAG-PM Interview Helper

A lightweight Retrieval-Augmented Generation (RAG) chatbot that answers **Product Management interview questions** using context from **Cracking the PM Interview** by Gayle Laakmann McDowell and Jackie Bavaro.

Built as a hands-on experiment in applying **LLMs + vector search** to a focused real-world use case: helping candidates prepare for PM interviews by generating contextual, source-backed answers from a trusted prep guide.

---

## Why This Project?

Traditional GPT-based interview prep tools are useful, but often lack accuracy or depth when it comes to niche domains like product management. This project explores how **context injection through retrieval** can significantly improve the quality and relevance of answers.

Instead of fine-tuning a model, I use OpenAI’s embeddings and FAISS to search relevant content from a trusted guidebook, then pass that into GPT-4 for grounded, reliable responses.

---

## Features

- **PDF-based document retrieval** using OpenAI Embeddings
- **FAISS vector database** for fast and efficient semantic search
- **Prompt injection** with retrieved context to guide GPT responses
- Simple Python script — no frameworks, just code you can build on

---

## Files Included

- `rag_pm_simple.py` – Main script for indexing the PDF and answering questions
- `cracking_pm_interview.pdf` – Source knowledge base (replaceable)
- `.env` – Your API key config (not committed to GitHub)

---

## How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/heyaigerim/rag-pm-interview-helper.git
   cd rag-pm-interview-helper

2. Add your .env file with your OpenAI API key:
   ```bash
   OPENAI_API_KEY=your-api-key-here

3. Install required packages:
   ```bash
   pip install openai faiss-cpu python-dotenv PyPDF2

4. Run it:
   ```bash
   python rag_pm_simple.py

**You’ll be prompted to ask a PM-style question. The script will:**
- Embed the source PDF (if it hasn’t already)
- Retrieve the most relevant chunks using vector search
- Pass your query and the retrieved context to GPT-4
- Return a clean, focused answer

## Example Use Cases
- PM Interview Prep – Ask questions like “What’s the STAR method?” or “How do I explain a product failure?”
- Domain-specific retrieval – Swap in other PDFs (e.g., UX design, system design, consulting)
- RAG learning sandbox – A clean starting point to build your own RAG prototype

## What You’ll Learn
- How to use OpenAI Embeddings to encode long-form text
- How to use FAISS to build a searchable vector index
- How to structure prompts using retrieved context to improve LLM responses
- How simple tools can meaningfully improve AI accuracy in narrow domains


## Credits
Inspired by Cracking the PM Interview

**Built by Aigerim Kurmanbekova**

UC Berkeley MIMS | Product Manager | AI & Data Enthusiast

Want to use your own material? Just replace the PDF file and rerun the script.







