from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from langserve import add_routes

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")    
# Initialize model
model = ChatGroq(model="llama-3.1-8b-instant", groq_api_key=groq_api_key)

system_message = "Translate the following from English to {language}."
promt_template = ChatPromptTemplate.from_messages(  
    [
        ("system",system_message),
        ( "user","{text}")
    ])
parser = StrOutputParser()
#create chain
chain = promt_template | model | parser

#app definition
app = FastAPI(title="LCEL with Groq API",version="1.2",description="A simple example of using LCEL with Groq API to create a translation service.")
add_routes(app,
            chain,
            path="/translate")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)



