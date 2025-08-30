# Simple RAG Application

A minimal RAG (Retrieval Augmented Generation) application using ChromaDB, Gemini API, and Streamlit.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your Google API key in `.env`:
```
GOOGLE_API_KEY=your_google_api_key_here
```

## Usage

1. **Ingest Data**: Run the data ingestion script to load PDF into ChromaDB
```bash
python data_ingestion.py
```

2. **Run Streamlit App**: Start the web interface
```bash
streamlit run streamlit_app.py
```

## Files

- `data_ingestion.py` - Loads PDF data into ChromaDB
- `rag_pipeline.py` - RAG system using Gemini and ChromaDB
- `streamlit_app.py` - Web interface for chatting with documents
