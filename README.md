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
| Furniture | 742K | 18K | 2.49% |

### Insight:

- Technology is the most profitable category.
- Furniture generates high revenue but very low profit margin.
- Furniture is highly sensitive to discounting.

---

## 🎯 Discount Impact Analysis

- Discounts above 40% consistently result in losses.
- Profit turns negative significantly after 0.3 discount level.
- Heavy discounting strategy destroys profitability in Furniture category.

### Insight:

A controlled discount strategy is critical.  
High discount ≠ high profit.

---

## 🔥 Most Profitable Products

- Canon imageCLASS 2200 Advanced Copier
- Fellowes PB500 Electric Binding Machine
- HP LaserJet Series
- Canon Personal Laser Copier
- HP Designjet T520

These premium printers contribute disproportionately to overall profit.

---

## ❌ Most Loss-Making Products

- Cubify CubeX 3D Printer (Double Head)
- Lexmark MX611dhe Laser Printer
- Cubify CubeX 3D Printer (Triple Head)
- Chromcraft Conference Tables
- Bush Advantage Collection Tables

### Insight:

Some high-value products generate significant losses due to heavy discounting.

---

## 📊 Monthly Trends

- Revenue peaked during 2016–2017.
- Profit fluctuations closely follow discount patterns.
- Average shipping time is approximately 4 days.

---

# 🎯 Business Recommendations

1. Reduce aggressive discounting in Furniture category.
2. Focus marketing on high-margin Technology products.
3. Re-evaluate pricing strategy for 3D printers.
4. Introduce margin-based discount policies.
5. Monitor products with recurring negative profit contribution.

---

# 🚀 How To Run Dashboard

```bash
streamlit run dashboard/app.py


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
| Furniture | 742K | 18K | 2.49% |

### Insight:

- Technology is the most profitable category.
- Furniture generates high revenue but very low profit margin.
- Furniture is highly sensitive to discounting.

---

## 🎯 Discount Impact Analysis

- Discounts above 40% consistently result in losses.
- Profit turns negative significantly after 0.3 discount level.
- Heavy discounting strategy destroys profitability in Furniture category.

### Insight:

A controlled discount strategy is critical.  
High discount ≠ high profit.

---

## 🔥 Most Profitable Products

- Canon imageCLASS 2200 Advanced Copier
- Fellowes PB500 Electric Binding Machine
- HP LaserJet Series
- Canon Personal Laser Copier
- HP Designjet T520

These premium printers contribute disproportionately to overall profit.

---

## ❌ Most Loss-Making Products

- Cubify CubeX 3D Printer (Double Head)
- Lexmark MX611dhe Laser Printer
- Cubify CubeX 3D Printer (Triple Head)
- Chromcraft Conference Tables
- Bush Advantage Collection Tables

### Insight:

Some high-value products generate significant losses due to heavy discounting.

---

## 📊 Monthly Trends

- Revenue peaked during 2016–2017.
- Profit fluctuations closely follow discount patterns.
- Average shipping time is approximately 4 days.

---

# 🎯 Business Recommendations

1. Reduce aggressive discounting in Furniture category.
2. Focus marketing on high-margin Technology products.
3. Re-evaluate pricing strategy for 3D printers.
4. Introduce margin-based discount policies.
5. Monitor products with recurring negative profit contribution.

---

# 🚀 How To Run Dashboard

```bash
streamlit run dashboard/app.py

Conclusion
This project demonstrates an end-to-end retail analytics workflow:
Data cleaning
SQL modeling
Business intelligence
Interactive dashboard development
