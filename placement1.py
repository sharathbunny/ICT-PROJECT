import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")  # Full-width layout
st.title("Placement Data Analytics Dashboard")

# Read CSV
df = pd.read_csv("data.csv")

# --- Summary Cards ---
total_students = len(df)
total_branches = df['Branch'].nunique()
total_recruiters = df['Name of the Employer'].nunique()

col1, col2, col3 = st.columns(3)
col1.metric("Total Students", total_students)
col2.metric("Unique Branches", total_branches)
col3.metric("Total Recruiters", total_recruiters)

st.markdown("---")  # Horizontal line

# --- Side-by-side graphs ---
col1, col2 = st.columns(2)

# 1️⃣ Bar chart: Year-wise student count
year_counts = df['Year'].value_counts().sort_index()
fig_bar = px.bar(
    x=year_counts.index,
    y=year_counts.values,
    color = year_counts.index,
    labels={'x': 'Year', 'y': 'Number of Students'},
    title="Year-wise Placement Count"
)
col1.plotly_chart(fig_bar, use_container_width=True)

# 2️⃣ Pie chart: Branch-wise distribution
year_counts = df['Year'].value_counts()
fig_pie = px.pie(
    names=year_counts.index,
    values=year_counts.values,
    title="year-wise Distribution"
)
col2.plotly_chart(fig_pie, use_container_width=True)

st.markdown("---")

# --- Full data table ---
st.subheader("Full Placement Data")
st.dataframe(df, use_container_width=True)
