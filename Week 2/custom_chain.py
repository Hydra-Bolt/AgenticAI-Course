from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain, llm
from dotenv import load_dotenv

load_dotenv()

gemini_llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Step 1: Rephrase for clarity
clarity_prompt = PromptTemplate(
    input_variables=["question"],
    template="Rephrase the following question to make it clearer:\n{question}"
)
clarity_chain = llm.LLMChain(
    llm=gemini_llm,
    prompt=clarity_prompt,
    output_key="clear_question"
)

# Step 2: Rephrase for conciseness
answer_prompt = PromptTemplate(
    input_variables=["clear_question"],
    template="Answer the following question:\n{clear_question}"
)
answer_chain = llm.LLMChain(
    llm=gemini_llm,
    prompt=answer_prompt,
    output_key="answer"
)

# Combine into a SequentialChain
rephrase_chain = SequentialChain(
    chains=[clarity_chain, answer_chain],
    input_variables=["question"],
    output_variables=["clear_question", "answer"],
    verbose=True
)

# Example usage
if __name__ == "__main__":
    question = "What are the possible effects of artificial intelligence on the healthcare industry in terms of patient outcomes and operational efficiency?"
    rephrased = rephrase_chain({"question": question})
    print("Clear Question:\n", rephrased["clear_question"])
    print("\nConcise Question:\n", rephrased["concise_question"])
