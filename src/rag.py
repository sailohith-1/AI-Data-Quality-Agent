from pathlib import Path
from sentence_transformers import SentenceTransformer


rules_folder = Path("rules")

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


documents = load_documents()

all_chunks = []

for document in documents:

    chunks = chunk_by_section(document["text"])

    for chunk in chunks:
        all_chunks.append({
            "source": document["source"],
            "text": chunk
        })


print("Total chunks:", len(all_chunks))


for i, chunk in enumerate(all_chunks):

    embedding = model.encode(chunk["text"])

    print("\nChunk:", i)
    print("Source:", chunk["source"])
    print("Text:", chunk["text"])
    print("Embedding dimensions:", len(embedding))