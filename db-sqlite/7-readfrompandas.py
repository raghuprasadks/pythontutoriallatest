import pandas as pd
import sqlite3

# Read sqlite query results into a pandas DataFrame
con = sqlite3.connect("demosql.db")
df = pd.read_sql_query("SELECT * from COMPANY", con)
print(df)