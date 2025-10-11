import os

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import streamlit as st


api_key = st.text_input("Enter your OpenAI API key", type="password")
if not api_key:
    st.warning("Please enter your OpenAI API key to continue")
    st.stop()
    
llm = ChatOpenAI(model="gpt-4o-mini", api_key=api_key)

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
