import streamlit as st
import pandas as pd

st.title("Placement Data Analytics")
df = pd.read_csv("data.csv")
st.dataframe(df) 