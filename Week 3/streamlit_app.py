import streamlit as st
from rag_pipeline import query 

st.title("Simple RAG ChatBot")
st.write("Ask questions about your document!")

# Chat input section
user_input = st.text_input("Ask a question about your document:")
send_button = st.button("Send")

if user_input and send_button:

    with st.spinner("Processing your question, please wait..."):

        response = query(user_input)

        st.write("Here is the answer to your question:")
        st.write(response)
