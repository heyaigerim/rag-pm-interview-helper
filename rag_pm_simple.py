from pdfminer.high_level import extract_text
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

PDF_PATH = "data/cracking_pm_interview.pdf"
CHUNK_SIZE = 800  # characters
CHUNK_OVERLAP = 200

# 1. Load PDF
def load_pdf_text(path):
    print("Extracting text from PDF...")
    return extract_text(path)

# 2. Chunk the text
def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        start += chunk_size - overlap
    print(f"Total chunks created: {len(chunks)}")
    return chunks

# 3. Embed and search
def find_best_chunk(query, chunks, model):
    print("Embedding query and chunks...")
    chunk_embeddings = model.encode(chunks)
    query_embedding = model.encode([query])
    scores = cosine_similarity(query_embedding, chunk_embeddings)[0]
    best_idx = np.argmax(scores)
    return chunks[best_idx], scores[best_idx]

def main():
    text = load_pdf_text(PDF_PATH)
    chunks = chunk_text(text)

    model = SentenceTransformer('all-MiniLM-L6-v2')

    while True:
        query = input("\nEnter your Product Management interview query (or type 'exit'):\n> ")
        if query.lower() == 'exit':
            break

        best_chunk, score = find_best_chunk(query, chunks, model)

        print(f"\n🔍 Top Matching Chunk (Score: {score:.4f}):\n")
        print(best_chunk)
        print("\n You can now copy this chunk into ChatGPT with your query for an enhanced answer.\n")

if __name__ == "__main__":
    main()
