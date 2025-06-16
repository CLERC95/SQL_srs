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
    st.dataframe(exercice)

    exercice_name = exercice.loc[0, "exercice_name"]
    with open(f"answers/{exercice_name}.sql", "r", encoding="UTF-8") as f:
        answer = f.read()

    solution_df = con.execute(answer).df()

st.header("Entre votre code:")

sql_query = st.text_area(label="Entrez votre input", key="user_input")
if sql_query:
    result = con.execute(sql_query).df()
    st.dataframe(result)
    st.write(f"Vous avez entrez la requête suivante: {sql_query}")

    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write("Some columns are missing")

    n_lignes_diff = abs(result.shape[0] - solution_df.shape[0])
    if n_lignes_diff != 0:
        st.write(f"Result has a {n_lignes_diff} lines difference with the solution")


tab1, tab2 = st.tabs(["Tables", "Solution"])

try:
    with tab1:
        exercice_tables = exercice.loc[0, "tables"]
        for table in exercice_tables:
            st.write(f"Table: {table}")
            df_table = con.execute(f"SELECT * FROM {table}").df()
            st.dataframe(df_table)

    with tab2:
        st.write(answer)
except KeyError:
    st.write("No exercices seleced")
