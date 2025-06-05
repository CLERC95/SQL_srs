# pylint: disable=(missing-module-docstring)
import duckdb
import streamlit as st


con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=False)

with st.sidebar:
    theme = st.selectbox(
        "What would you like to review ?",
        ["cross_join", "GoupBy", "Windows Functions"],
        index=None,
        placeholder="Select a theme",
    )
    st.write("You selected: ", theme)

    exercice = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'").df()
    st.write(exercice)

st.header("Entre votre code:")

sql_query = st.text_area(label="Entrez votre input", key="user_input")
# if sql_query:
#     result = duckdb.sql(sql_query).df()
#     st.dataframe(result)
#     # st.write(f"Vous avez entrez la requête suivante: {sql_query}")

# try:
#     result = result[solution_df.columns]
#     st.dataframe(result.compare(solution_df))
# except KeyError as e:
#     st.write("Some columns are missing")

# n_lignes_diff = abs(result.shape[0] - solution_df.shape[0])
# if n_lignes_diff != 0:
#     st.write(f"Result has a {n_lignes_diff} lines difference with the solution")


# tab1, tab2 = st.tabs(["Tables", "solution"])

# with tab1:
#     st.write("Table: beverages")
#     st.dataframe(beverages)
#     st.write("Table: food_items")
#     st.dataframe(food_items)
#     st.write("Table attendue:")
#     st.dataframe(solution_df)

# with tab2:
#     st.write(ANSWER)
