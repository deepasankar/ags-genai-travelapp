import os

from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
import streamlit as st

llm = ChatOllama(model="llama3.2:latest")

prompt_template = PromptTemplate(
    input_variables=[ "city", "month", "language", "budget" ],
    template="""
    Welcome to the {city} travel guide! 
    If you are visiting in {month}, here's what you can do:
    1. Must visit attractions
    2. Local cuisines you can try
    3. Useful phrases in {language}
    4. Tips for travelling on a budget of {budget}
    """
)

st.title("Travel recommendations application")

city = st.text_input("Enter the city you are visiting: ")
month = st.text_input("Enter the month in which you plan to travel to the city: ")
language = st.text_input("Enter the local language spoken in the city : ")
budget = st.text_input("Enter your travel budget: ")

if city:
    response = llm.invoke(prompt_template.format(city=city, month=month, language=language, budget=budget))
    st.write(response.content)
    print(response)
