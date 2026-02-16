# 📦 Retail Supply Chain & Sales Intelligence System

## 📌 Project Overview

This project analyzes retail sales data to uncover revenue trends, profitability drivers, and the impact of discount strategies using **Python, MySQL, and Streamlit**.

The system simulates a real-world retail analytics workflow:

- Data cleaning & feature engineering (Python)
- Data storage & querying (MySQL)
- Analytical views & insights (SQL)
- Interactive dashboard (Streamlit + Plotly)

---

## 🛠 Tech Stack

- Python (Pandas, SQLAlchemy)
- MySQL
- SQL (Views, Aggregations)
- Streamlit
- Plotly
- Jupyter Lab

---

## ⚙️ Data Engineering Process

### 1️⃣ Data Cleaning & Feature Engineering (Python)

- Converted date columns to datetime
- Created `shipping_days`
- Calculated `profit_margin`
- Extracted `order_year` and `order_month`
- Removed null values

---

### 2️⃣ Database Design (MySQL)

- Created `retail_analytics` database
- Designed structured `orders` table
- Loaded 9,994 records using SQLAlchemy
- Created analytical views for reporting

---

### 3️⃣ Analytical SQL Views

- Monthly revenue & profit trends
- Category performance
- Discount vs Profit impact
- Top & Worst performing products

---

# 📈 Key Business Insights

## 💰 Revenue & Profit Overview

- Total Revenue: **$2.29M**
- Total Profit: **$286K**
- Overall Profit Margin: **12.47%**

The business is profitable but margins are heavily impacted by discounting strategies.

---

## 🏷 Category Performance

| Category | Revenue | Profit | Profit Margin |
|----------|---------|--------|---------------|
| Technology | 836K | 145K | 17.4% |
| Office Supplies | 719K | 122K | 17.04% |
|

