import streamlit as st
import pandas as pd


# Load dataset
data = pd.read_csv("sales_data.csv")

# Convert date column
data["Date"] = pd.to_datetime(data["Date"])

# Dashboard title
st.title("Sales Data Analysis Dashboard")

st.sidebar.header("Filter Data")

region = st.sidebar.selectbox("Select Region", data["Region"].unique())

filtered_data = data[data["Region"] == region]

st.write(filtered_data)

# Region filter
region = st.selectbox("Select Region", data["Region"].unique())
filtered_data = data[data["Region"] == region]

# Show data
st.write(filtered_data)

# Sales Overview
st.header("Sales Overview")

col1, col2 = st.columns(2)

with col1:
    total_sales = filtered_data["Sales"].sum()
    st.metric("Total Sales", total_sales)

with col2:
    total_profit = filtered_data["Profit"].sum()
    st.metric("Total Profit", total_profit)

# Product Analysis
# Product Analysis
st.header("Product Analysis")

product_sales = filtered_data.groupby("Product")["Sales"].sum()

st.subheader("Product Sales")
st.bar_chart(product_sales)

import matplotlib.pyplot as plt

st.subheader("Product Sales Distribution")

fig, ax = plt.subplots()

product_sales.plot(kind="pie", autopct='%1.1f%%', ax=ax)

ax.set_ylabel("")

st.pyplot(fig)

product_sales = filtered_data.groupby("Product")["Sales"].sum()
profit_data = filtered_data.groupby("Product")["Profit"].sum()

col3, col4 = st.columns(2)

with col3:
    st.subheader("Product Sales")
    st.bar_chart(product_sales)

with col4:
    st.subheader("Profit by Product")
    st.bar_chart(profit_data)

# Sales Trend
st.header("Sales Trend")

sales_trend = filtered_data.groupby("Date")["Sales"].sum()
st.line_chart(sales_trend)