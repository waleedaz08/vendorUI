import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect(r"practice.db")

df = pd.read_sql_query("SELECT * FROM vendor", conn)

st.title("Vendor Transactions")

st.dataframe(df)

