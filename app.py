import streamlit as st
import pandas as pd
import duckdb
import io

st.write(
    """
# SQL SRS
Spaced Repetition System SQL practice 
"""
)

with st.sidebar:
    option = st.selectbox(
        "What would you like to review ?",
        ["Joins", "GoupBy", "Windows Functions"],
        index=None,
        placeholder="Select a theme",
    )
    st.write("You selected: ", option)

csv = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""
beverages = pd.read_csv(io.StringIO(csv))

csv2 = """
food_item,food_price
cookie ,2.5
chocolatine,2
muffin,3
"""
food_items = pd.read_csv(io.StringIO(csv2))

answer = """
SELECT * FROM beverages
CROSS JOIN food_items
"""
solution = duckdb.sql(answer).df()

st.header("Entre votre code:")

sql_query = st.text_area(label="Entrez votre input", key="user_input")
if sql_query:
    result = duckdb.sql(sql_query).df()
    st.dataframe(result)
    st.write(f"Vous avez entrez la requête suivante: {sql_query}")

tab1, tab2 = st.tabs(["Tables", "Solution"])

with tab1:
    st.write("Table: beverages")
    st.dataframe(beverages)
    st.write("Table: food_items")
    st.dataframe(food_items)
    st.write("Table attendue:")
    st.dataframe(solution)

with tab2:
    st.write(answer)
