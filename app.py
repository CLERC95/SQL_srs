import streamlit as st
import pandas as pd
import duckdb
import io

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
solution_df = duckdb.sql(answer).df()

st.header("Entre votre code:")

st.write(
    """
# SQL SRS
## Spaced Repetition System SQL practice 
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


sql_query = st.text_area(label="Entrez votre input", key="user_input")
if sql_query:
    result = duckdb.sql(sql_query).df()
    st.dataframe(result)
    # st.write(f"Vous avez entrez la requête suivante: {sql_query}")

try:
    result = result[solution_df.columns]
    st.dataframe(result.compare(solution_df))
except KeyError as e:
    st.write("Some columns are missing")

n_lignes_diff = abs(result.shape[0] - solution_df.shape[0])
if n_lignes_diff != 0:
    st.write(f"Result has a {n_lignes_diff} lines difference with the solution")


tab1, tab2 = st.tabs(["Tables", "solution"])

with tab1:
    st.write("Table: beverages")
    st.dataframe(beverages)
    st.write("Table: food_items")
    st.dataframe(food_items)
    st.write("Table attendue:")
    st.dataframe(solution_df)

with tab2:
    st.write(answer)
