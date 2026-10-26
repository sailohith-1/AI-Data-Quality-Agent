# RAG-Based Data Quality Assistant

An AI-powered assistant that retrieves organization-specific data quality rules using **Retrieval-Augmented Generation (RAG)** and uses a Large Language Model (LLM) to generate contextual answers to user queries.

The project combines semantic search, vector embeddings, and a rule-based knowledge base to help users understand data quality constraints and investigate potential data issues.

## Overview

Data quality rules are often documented in separate files, making it difficult to locate the right rule when investigating a data issue. This project addresses that challenge by building a retrieval pipeline that searches relevant rules and uses them as context for an AI-generated response.

For example, a user can ask:

> Can a purchase amount be negative?

The system searches the rule knowledge base for relevant revenue and validation rules, retrieves the most relevant information, and uses Gemini to formulate an answer based on the retrieved context.

## Key Features

- **Semantic Search:** Finds relevant data quality rules based on the meaning of a query rather than exact keyword matches.
- **RAG Pipeline:** Retrieves relevant knowledge before generating an LLM response.
- **Embedding Generation:** Converts rule documents and user queries into numerical vector representations using Sentence Transformers.
- **Vector Similarity Search:** Uses FAISS to efficiently retrieve relevant rule vectors.
- **Domain-Specific Knowledge Base:** Organizes data quality documentation into Markdown files covering general rules, revenue constraints, and schema requirements.
- **LLM Integration:** Uses Google Gemini to generate contextual responses using retrieved rules.
- **Data Quality Validation:** Includes Python-based checks for missing values, duplicate records, negative purchase amounts, and invalid session durations.

## Architecture

```text
              User Query
                   |
                   v
       Query Embedding Generation
       (Sentence Transformers)
                   |
                   v
          FAISS Similarity Search
                   |
                   v
       Retrieve Relevant Rule Chunks
                   |
                   v
       Retrieved Rules + User Query
                   |
                   v
          Google Gemini LLM
                   |
                   v
       Contextual Answer to User
```

### Knowledge Base and Indexing Pipeline

```text
Markdown Rule Documents
    general.md
    revenue.md
    schema.md
          |
          v
    Document Processing
          |
          v
    Text Embeddings
          |
          v
    FAISS Vector Index
          |
          v
    Saved Index and Rule Chunks
    rules.index + chunks.pkl
```

The indexing pipeline prepares the rule documents for retrieval. The query pipeline uses the saved index to find relevant rules and passes the retrieved context to the LLM.

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Data Processing | Pandas |
| Embedding Model | Sentence Transformers |
| Vector Search | FAISS |
| Generative AI | Google Gemini |
| Knowledge Base | Markdown |
| Serialized Rule Chunks | Pickle |

## Project Structure

```text
AI-Data-Quality-Agent/
│
├── data/
│   └── games.csv
│
├── rules/
│   ├── general.md
│   ├── revenue.md
│   └── schema.md
│
├── src/
│   ├── data_quality.py
│   ├── embeddings.py
│   ├── llm.py
│   ├── rag.py
│   ├── search.py
│   └── vector_store.py
│
├── vector_store/
│   ├── chunks.pkl
│   └── rules.index
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

*Note: `.env.example` and `requirements.txt` should be added if they do not already exist.*

## How the RAG Pipeline Works

1. **Knowledge preparation:** Data quality rules are maintained in Markdown documents.
2. **Embedding generation:** Sentence Transformers converts rule text into 384-dimensional embeddings.
3. **Index creation:** FAISS stores the vectors for efficient similarity search. The corresponding rule chunks are serialized for retrieval.
4. **Query processing:** A user's question is converted into an embedding using the same embedding model.
5. **Rule retrieval:** FAISS searches for semantically similar rules and returns relevant chunks.
6. **Response generation:** The retrieved rules and user query are provided to Google Gemini to generate a contextual answer.

## Getting Started

### Prerequisites

- Python 3.10 or a compatible Python environment
- pip
- A Google Gemini API key

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Data-Quality-Agent.git
cd AI-Data-Quality-Agent
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root and configure your Gemini API key using the variable name expected by `src/llm.py`.

For example:

```env
GEMINI_API_KEY=your_api_key_here
```

Ensure `.env` is excluded from version control. Never commit your actual API key.

### 5. Run the Project

Start with the existing indexing and search scripts in `src/`, following their execution order and configuration.

The vector index must be available before performing retrieval. If you regenerate the index, ensure that the corresponding rule chunks are saved as well.

*Refer to the source files for the exact execution commands and required configuration.*

## Example Query

**Question:**

Can a purchase amount be negative?

**Processing:**

1. The question is converted into an embedding.
2. FAISS retrieves relevant rules from the knowledge base.
3. The retrieved context is supplied to Gemini.
4. Gemini generates a response based on the available rules.

## Future Improvements

- Integrate data quality validation results directly into the RAG workflow.
- Add a FastAPI backend for exposing the assistant through REST endpoints.
- Build a web interface for submitting queries and viewing retrieved evidence.
- Display source rule references alongside generated answers.
- Add automated tests and evaluation metrics for retrieval quality.
- Support larger rule repositories and additional data domains.

## Learning Outcomes

This project demonstrates practical experience with Retrieval-Augmented Generation, vector embeddings, semantic retrieval, FAISS indexing, LLM integration, and data quality validation.
