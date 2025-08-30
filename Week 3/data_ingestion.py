import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

# Load environment variables
load_dotenv()

def ingest_pdf_to_chroma(pdf_path, persist_directory="./chroma_db"):
    """Ingest PDF data into ChromaDB"""
    
    # Load PDF
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    
    # Split text
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = text_splitter.split_documents(documents)
    
    # Create embeddings
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )
    
    # Create and persist ChromaDB
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_directory
    )
    
    print(f"Ingested {len(chunks)} chunks into ChromaDB")
    return vectorstore

if __name__ == "__main__":
    pdf_path = "./data/MARCOMS-PROSPECTUS-2025-V.5.0-04032025_compressed.pdf"
    ingest_pdf_to_chroma(pdf_path)