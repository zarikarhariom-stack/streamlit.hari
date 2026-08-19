from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser

#creating my prompts
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant, please respond to the question"),
        ("user", "Question: {question}")
    ]
)
#frontend using streamlit
st.title("Chat gpt")
input_text = st.text_input("Ask your questions ")

#Ollama and llm model integration
llm = Ollama(model="gemma2:2b")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser


if input_text:
    st.write(chain.invoke({"question": input_text}))