import streamlit as st
import pandas as pd

st.title("Placement Data Analytics")

# Read CSV
df = pd.read_csv("data.csv")

# --- Summary Cards ---
total_students = len(df)
total_branches = df['Branch'].nunique()
total_recruiters = df['Name of the Employer'].nunique()

col1, col2, col3 = st.columns(3)
col1.metric("Total Students", total_students)
col2.metric("Unique Branches", total_branches)
col3.metric("Recruiters", total_recruiters)

# Display full table
st.subheader("Full Placement Data")
st.dataframe(df)
