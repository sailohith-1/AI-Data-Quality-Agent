from pathlib import Path
import pickle

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


rules_folder = Path("rules")
vector_store_folder = Path("vector_store")

vector_store_folder.mkdir(exist_ok=True)

model = SentenceTransformer("all-MiniLM-L6-v2")


def load_documents():
    documents = []

    for file in rules_folder.glob("*.md"):
        text = file.read_text(encoding="utf-8")

        documents.append({
            "source": file.name,
            "text": text
        })

    return documents


def chunk_by_section(text):
    sections = text.split("\n## ")

    chunks = []

    for i, section in enumerate(sections):
        section = section.strip()

        if not section:
            continue

        if i == 0:
            chunks.append(section)
        else:
            chunks.append("## " + section)

    return chunks


# Load documents
documents = load_documents()

# Create chunks
all_chunks = []

for document in documents:

    chunks = chunk_by_section(document["text"])

    for chunk in chunks:
        all_chunks.append({
            "source": document["source"],
            "text": chunk
        })


# Extract text
texts = [chunk["text"] for chunk in all_chunks]

# Create embeddings
embeddings = model.encode(texts)

embeddings = np.array(embeddings).astype("float32")

# Normalize embeddings
faiss.normalize_L2(embeddings)

# Create FAISS index
dimension = embeddings.shape[1]

index = faiss.IndexFlatIP(dimension)

# Add embeddings to index
index.add(embeddings)


# Save FAISS index
faiss.write_index(
    index,
    str(vector_store_folder / "rules.index")
)


# Save chunk information
with open(vector_store_folder / "chunks.pkl", "wb") as file:
    pickle.dump(all_chunks, file)


print("Vector store created successfully!")
print("Total vectors:", index.ntotal)
print("Vector dimension:", dimension)
print("Saved FAISS index: vector_store/rules.index")
print("Saved chunks: vector_store/chunks.pkl")