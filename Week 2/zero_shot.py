from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# Initialize Gemini model (Google Generative AI)
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
# Define some example tools
tools = [
    Tool(
        name="Calculator",
        func=lambda x: str(eval(x)),
        description="Useful for simple math calculations. Input should be a valid Python expression."
    ),
    Tool(
        name="CountryInfo",
        func=lambda country: {
            "France": "Paris",
            "Germany": "Berlin",
            "Italy": "Rome"
        }.get(country, "Unknown"),
        description="Returns the capital of a given country. Input should be the country name."
    )
]

# Initialize zero-shot agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

if __name__ == "__main__":
    query = input("Enter your query: ")
    result = agent.run(query)
    print(result)
