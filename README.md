# ☕ Afficionado Coffee Roasters — Sales Trend & Time-Based Performance Analysis



## 📌 Project Overview

This project delivers a comprehensive **Sales Trend and Time-Based Performance Analysis** for Afficionado Coffee Roasters — a specialty coffee retail chain operating across three New York City locations.

Using **149,116 transaction records** from 2025, this analysis uncovers temporal demand patterns to help management make **data-driven decisions** on staffing, promotions, and operational planning.

---

## 🏪 Store Locations

| Store | Revenue | Share |
|-------|---------|-------|
| Hell's Kitchen | $236,511.17 | 33.8% |
| Astoria | $232,243.91 | 33.2% |
| Lower Manhattan | $230,057.25 | 32.9% |

---

## 📊 Key Findings

- ⏰ **Morning (6–11 AM) drives 55.6%** of total annual revenue
- 🔝 **Peak hour is 10:00 AM – 11:00 AM** across all 3 store locations
- 🏪 **All 3 stores perform within 1%** of each other in revenue share
- ☕ **Coffee is the #1 product category** by revenue
- 🥇 **Top product:** Sustainably Grown Organic Lg
- 📉 **Afternoon revenue drops 47%** from peak — a key growth opportunity

---

## 🗂️ Project Structure

```
afficionado-coffee-analysis/
│
├── app.py                          # ☁️ Streamlit Interactive Dashboard
├── eda.py                          # 🔍 Data Cleaning & Exploratory Analysis
├── research_paper.py               # 📄 Research Paper Generator
├── executive_summary.py            # 📋 Executive Summary Generator
│
├── research_paper.txt              # 📝 Full Research Paper (8 sections)
├── executive_summary.txt           # 📋 Executive Summary for Stakeholders
├── requirements.txt                # 📦 Python Dependencies
│
├── charts/
│   ├── transactions_by_hour.png    # 📈 Hourly Transaction Chart
│   ├── revenue_by_time_bucket.png  # 🥧 Time Bucket Revenue Chart
│   ├── revenue_by_store.png        # 🏪 Store Revenue Chart
│   └── revenue_by_category.png     # 🛍️ Category Revenue Chart
│
└── README.md                       # 📖 This file
```

---

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/ThakorJaydeep8208/afficionado-coffee-analysis.git
cd afficionado-coffee-analysis
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Add the Dataset
Place the file `Afficionado Coffee Roasters.xlsx - Transactions.csv` in the project root folder.

### 4. Run the Streamlit Dashboard
```bash
streamlit run app.py
```

### 5. Run EDA Script
```bash
python eda.py
```

---

## 📦 Requirements

```
pandas==2.2.2
plotly==5.22.0
streamlit==1.35.0
seaborn==0.13.2
matplotlib==3.9.0
openpyxl==3.1.2
```

---

## 📈 Dashboard Features

| Feature | Description |
|---------|-------------|
| 🔢 KPI Cards | Total Revenue, Transactions, Avg Value, Store Count |
| 🕐 Hourly Demand Curve | Bar chart of revenue/transactions by hour |
| ⏰ Time Bucket Pie Chart | Morning / Afternoon / Evening breakdown |
| 🏪 Store Comparison | Revenue comparison across 3 locations |
| 🛍️ Category Breakdown | Revenue by product category |
| 🔥 Heatmap | Hourly demand heatmap per store |
| 🏆 Top 10 Products | Best performing products by revenue |
| 🎛️ Filters | Store selector, hour range slider, metric toggle |

---

## 🧪 Dataset Description

| Column | Description |
|--------|-------------|
| `transaction_id` | Unique transaction identifier |
| `year` | Transaction year (2025) |
| `transaction_time` | Time of sale (HH:MM:SS) |
| `transaction_qty` | Units purchased |
| `unit_price` | Price per unit (USD) |
| `store_id` | Store identifier |
| `store_location` | Physical store name |
| `product_id` | Product identifier |
| `product_category` | Broad product group |
| `product_type` | Product variant |
| `product_detail` | Specific product name |

**Derived Features:**
- `revenue` = `transaction_qty` × `unit_price`
- `hour` = extracted from `transaction_time`
- `time_bucket` = Morning / Afternoon / Evening / Late

---

## 💡 Recommendations

1. **Staff Scheduling** — Maximum staff 8–11 AM, reduce post 1 PM
2. **Afternoon Promotions** — Happy Hour deals 2–4 PM to fill revenue gap
3. **Evening Expansion** — New evening products and community events
4. **Protect Morning Peak** — Ensure inventory and equipment ready by 6 AM
5. **Deploy Dashboard** — Use Streamlit app for real-time store decisions

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| Python 3.14 | Core programming language |
| pandas | Data cleaning & transformation |
| matplotlib & seaborn | Static EDA visualizations |
| plotly | Interactive dashboard charts |
| Streamlit | Web dashboard deployment |
| Git & GitHub | Version control & hosting |

---

## 👤 Author

**Jaydeep Thakor**
- GitHub: [@ThakorJaydeep8208](https://github.com/ThakorJaydeep8208)
- Project Type: Data Analyst  Project
- Year: 2026

