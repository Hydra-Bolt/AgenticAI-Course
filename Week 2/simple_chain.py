from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import llm
from dotenv import load_dotenv

load_dotenv()

gemini_llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Define a prompt template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Write a short summary about {topic}."
)

llm_chain = llm.LLMChain(
    llm=gemini_llm,
    prompt=prompt
)

if __name__ == "__main__":
    topic = "the importance of artificial intelligence"
    summary = llm_chain.run(topic)
    print(summary)

