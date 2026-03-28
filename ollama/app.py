import os
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

prompt  = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant please respond to the question."),
    ("user", "Question {question}"),
])

#Streamlit vramework
st.title("Langchain Demo With Llama2")
input_text = st.text_input("Enter your question here")

##Ollama llama 2 model
if input_text:
    llm = OllamaLLM(model="gemma:2b")
    document_chain = prompt | llm | StrOutputParser()
    response = document_chain.invoke({"question": input_text})
    st.write(response)









