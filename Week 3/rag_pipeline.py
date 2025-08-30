import asyncio
import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

# Load environment variables
load_dotenv()

try:
    asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
# Initialize LLM
llm = GoogleGenerativeAI(
    model="models/gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Initialize embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Load existing ChromaDB
persist_directory = "./chroma_db"
vectorstore = Chroma(
    persist_directory=persist_directory,
    embedding_function=embeddings
)

# Create RAG chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
    verbose=True
)

# Query the RAG system
def query(question):
    """Query the RAG system"""
    return qa_chain.run(question)

if __name__ == "__main__":
    response = query("What is this document about?")
    print(response)
