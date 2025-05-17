import streamlit as st
import pandas as pd
import duckdb

data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)
sql_query = st.text_area(label="Entrez votre input")
result = duckdb.query(sql_query).df()


st.write(
    """
#SQL SRS
Spaced Repetition System SQL practice 
"""
)

option = st.selectbox(
    "What would you like to review ?",
    ["Joins", "GoupBy", "Windows Functions"],
    index=None,
    placeholder="Select a theme",
)
st.write("You selected: ", option)

st.write(f"Vous avez entrez la requête suivante: {sql_query}")
st.dataframe(result)
