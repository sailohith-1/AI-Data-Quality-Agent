import pickle

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# Load FAISS index
index = faiss.read_index("vector_store/rules.index")


# Load original rule chunks
with open("vector_store/chunks.pkl", "rb") as file:
    all_chunks = pickle.load(file)


def retrieve_rule(question, k=1, threshold=0.50):

    # Convert the question into an embedding
    query_embedding = model.encode([question])

    query_embedding = np.array(query_embedding).astype("float32")

    # Normalize the query embedding
    faiss.normalize_L2(query_embedding)

    # Search FAISS
    scores, indices = index.search(query_embedding, k)

    best_score = scores[0][0]
    best_index = indices[0][0]

    # Reject unrelated results
    if best_score < threshold:
        return None

    # Retrieve the original rule text
    result = all_chunks[best_index]

    return {
        "source": result["source"],
        "text": result["text"],
        "score": float(best_score)
    }