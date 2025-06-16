# pylint: disable=(missing-module-docstring)
import io

import duckdb
import pandas as pd


con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=False)

# ------------------------------------------------------------------------------------------------
# EXERCICE LIST
# ------------------------------------------------------------------------------------------------

data = {
    "theme": ["cross_join", "cross_join"],
    "exercice_name": ["beverages_and_food", "sizes_and_trademarks"],
    "tables": [["beverages", "food_items"], ["sizes", "trademarks"]],
    "last_reviewed": ["1970-01-01", "1970-01-01"],
}

memory_state_df = pd.DataFrame(data)
con.execute("CREATE TABLE IF NOT EXISTS memory_state AS SELECT * FROM memory_state_df")

# ------------------------------------------------------------------------------------------------
# CROSS JOIN EXERCICES 1
# ------------------------------------------------------------------------------------------------

CSV = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""
beverages = pd.read_csv(io.StringIO(CSV))
con.execute(
    "CREATE TABLE IF NOT EXISTS beverages AS SELECT * FROM beverages"
)


CSV2 = """
food_item,food_price
cookie ,2.5
chocolatine,2
muffin,3
"""
food_items = pd.read_csv(io.StringIO(CSV2))
con.execute("CREATE TABLE IF NOT EXISTS food_items AS SELECT * FROM food_items")

# ------------------------------------------------------------------------------------------------
# CROSS JOIN EXERCICES 2
# ------------------------------------------------------------------------------------------------

SIZE = """
size
XS
M
L
XL
"""
sizes = pd.read_csv(io.StringIO(SIZE))
con.execute("CREATE TABLE IF NOT EXISTS size AS SELECT * FROM sizes")

TRADEMARK = """
trademark
Nike
Asphalte
Abercrombie
Lewis
"""
trademarks = pd.read_csv(io.StringIO(TRADEMARK))
con.execute("CREATE TABLE IF NOT EXISTS trademark AS SELECT * FROM trademarks")
