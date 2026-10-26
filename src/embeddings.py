from pathlib import Path
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

rules_folder = Path("rules")

for file in rules_folder.glob("*.md"):
    text = file.read_text(encoding="utf-8")

    embedding = model.encode(text)

    print("\nFile:", file.name)
    print("Embedding dimensions:", len(embedding))