from langchain.agents import Tool, initialize_agent, AgentType
from langchain_google_genai import GoogleGenerativeAI
from rag_pipeline import query

from dotenv import load_dotenv
import os

load_dotenv()

llm = GoogleGenerativeAI(
    model="models/gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

tools = [
    Tool(
        name="Retrieval Augmented Generation",
        func=query,
        description="Useful for when you need to answer questions about a NUST. Input should be a search query, and the output will be a relevant documents fetched from the database",
    )
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

if __name__ == "__main__":
    while True:
        user_query = input("Enter your query: ")
        if user_query.lower() == "exit":
            break
        result = agent.run(user_query)
        print(result)