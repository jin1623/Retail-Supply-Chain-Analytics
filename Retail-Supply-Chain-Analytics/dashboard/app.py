import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

# --- Database Connection ---
engine = create_engine(
    "mysql+mysqlconnector://retail_user@127.0.0.1:3306/retail_analytics",
    connect_args={"password": "Retail@123"}
)

# --- Load Data ---
df = pd.read_sql("SELECT * FROM orders", engine)

# --- KPIs ---
total_revenue = df['sales'].sum()
total_profit = df['profit'].sum()
profit_margin = (total_profit / total_revenue) * 100

st.title("Retail Sales & Supply Chain Dashboard")

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"${total_revenue:,.0f}")
col2.metric("Total Profit", f"${total_profit:,.0f}")
col3.metric("Profit Margin", f"{profit_margin:.2f}%")

# --- Revenue by Category ---
st.subheader("Revenue by Category")
cat = df.groupby("category")["sales"].sum().reset_index()
fig1 = px.bar(cat, x="category", y="sales")
st.plotly_chart(fig1)

# --- Monthly Trend ---
st.subheader("Monthly Revenue Trend")
monthly = df.groupby(["order_year", "order_month"])["sales"].sum().reset_index()
monthly["date"] = monthly["order_year"].astype(str) + "-" + monthly["order_month"].astype(str)
fig2 = px.line(monthly, x="date", y="sales")
st.plotly_chart(fig2)

# --- Discount Impact ---
st.subheader("Discount vs Profit")
disc = df.groupby("discount")["profit"].sum().reset_index()
fig3 = px.bar(disc, x="discount", y="profit")
st.plotly_chart(fig3)

# --- Top 10 Profitable Products ---
st.subheader("Top 10 Profitable Products")
top = df.groupby("product_name")["profit"].sum().reset_index()
top = top.sort_values(by="profit", ascending=False).head(10)
fig4 = px.bar(top, x="profit", y="product_name", orientation="h")
st.plotly_chart(fig4)
