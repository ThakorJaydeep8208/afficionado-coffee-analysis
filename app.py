# ================================================
# Afficionado Coffee Roasters - Streamlit Dashboard
# Sales Trend & Time-Based Performance Analysis
# ================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------
st.set_page_config(
    page_title="Afficionado Coffee Roasters",
    page_icon="☕",
    layout="wide"
)

# ------------------------------------------------
# LOAD DATA
# ------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("Afficionado Coffee Roasters.xlsx - Transactions.csv")
    df['transaction_time'] = pd.to_datetime(df['transaction_time'], format='%H:%M:%S', errors='coerce')
    df['hour'] = df['transaction_time'].dt.hour
    df['revenue'] = df['transaction_qty'] * df['unit_price']

    def time_bucket(hour):
        if 6 <= hour <= 11:
            return 'Morning (6-11)'
        elif 12 <= hour <= 16:
            return 'Afternoon (12-16)'
        elif 17 <= hour <= 21:
            return 'Evening (17-21)'
        else:
            return 'Late/Early (22-5)'

    df['time_bucket'] = df['hour'].apply(time_bucket)
    return df

df = load_data()

# ------------------------------------------------
# SIDEBAR FILTERS
# ------------------------------------------------
st.sidebar.image("https://img.icons8.com/emoji/96/coffee-emoji.png", width=80)
st.sidebar.title("☕ Filters")

# Store filter
all_stores = ['All Stores'] + list(df['store_location'].unique())
selected_store = st.sidebar.selectbox("📍 Store Location", all_stores)

# Hour range slider
hour_range = st.sidebar.slider("🕐 Hour Range", 0, 23, (6, 21))

# Metric toggle
metric = st.sidebar.radio("📊 Show Metric", ["Revenue ($)", "Transaction Count"])

# Apply filters
filtered = df.copy()
if selected_store != 'All Stores':
    filtered = filtered[filtered['store_location'] == selected_store]
filtered = filtered[(filtered['hour'] >= hour_range[0]) & (filtered['hour'] <= hour_range[1])]

metric_col = 'revenue' if metric == "Revenue ($)" else 'transaction_id'
agg_func = 'sum' if metric == "Revenue ($)" else 'count'

# ------------------------------------------------
# HEADER
# ------------------------------------------------
st.title("☕ Afficionado Coffee Roasters")
st.subheader("Sales Trend & Time-Based Performance Dashboard")
st.markdown("---")

# ------------------------------------------------
# KPI CARDS
# ------------------------------------------------
k1, k2, k3, k4 = st.columns(4)
k1.metric("💰 Total Revenue", f"${filtered['revenue'].sum():,.0f}")
k2.metric("🧾 Total Transactions", f"{len(filtered):,}")
k3.metric("📦 Avg Transaction Value", f"${filtered['revenue'].mean():,.2f}")
k4.metric("🏪 Stores", filtered['store_location'].nunique())

st.markdown("---")

# ------------------------------------------------
# ROW 1: Hourly Demand + Time Bucket
# ------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("🕐 Hourly Demand Curve")
    hourly = filtered.groupby('hour').agg(
        value=(metric_col, agg_func)
    ).reset_index()
    fig = px.bar(hourly, x='hour', y='value',
                 labels={'hour': 'Hour of Day', 'value': metric},
                 color='value', color_continuous_scale='Blues',
                 title=f"{metric} by Hour of Day")
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("⏰ Revenue by Time Bucket")
    bucket = filtered.groupby('time_bucket').agg(
        value=(metric_col, agg_func)
    ).reset_index()
    fig2 = px.pie(bucket, names='time_bucket', values='value',
                  title=f"{metric} by Time Bucket",
                  color_discrete_sequence=px.colors.sequential.Oranges_r)
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# ------------------------------------------------
# ROW 2: Store Comparison + Category Breakdown
# ------------------------------------------------
col3, col4 = st.columns(2)

with col3:
    st.subheader("🏪 Store Location Comparison")
    store_data = filtered.groupby('store_location').agg(
        value=(metric_col, agg_func)
    ).reset_index()
    fig3 = px.bar(store_data, x='store_location', y='value',
                  color='store_location',
                  labels={'store_location': 'Store', 'value': metric},
                  title=f"{metric} by Store Location")
    fig3.update_layout(showlegend=False)
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    st.subheader("🛍️ Product Category Breakdown")
    cat_data = filtered.groupby('product_category').agg(
        value=(metric_col, agg_func)
    ).reset_index().sort_values('value', ascending=True)
    fig4 = px.bar(cat_data, x='value', y='product_category',
                  orientation='h',
                  color='value', color_continuous_scale='Purples',
                  labels={'product_category': 'Category', 'value': metric},
                  title=f"{metric} by Product Category")
    st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")

# ------------------------------------------------
# ROW 3: Hourly Heatmap by Store
# ------------------------------------------------
st.subheader("🔥 Hourly Demand Heatmap by Store Location")
heatmap_data = df.groupby(['store_location', 'hour']).agg(
    value=(metric_col, agg_func)
).reset_index()
heatmap_pivot = heatmap_data.pivot(index='store_location', columns='hour', values='value').fillna(0)

fig5 = go.Figure(data=go.Heatmap(
    z=heatmap_pivot.values,
    x=heatmap_pivot.columns.tolist(),
    y=heatmap_pivot.index.tolist(),
    colorscale='YlOrRd',
    colorbar=dict(title=metric)
))
fig5.update_layout(
    title=f"Hourly {metric} Heatmap Across Store Locations",
    xaxis_title="Hour of Day",
    yaxis_title="Store Location",
    height=300
)
st.plotly_chart(fig5, use_container_width=True)

st.markdown("---")

# ------------------------------------------------
# ROW 4: Top Products
# ------------------------------------------------
st.subheader("🏆 Top 10 Products by Revenue")
top_products = filtered.groupby('product_detail')['revenue'].sum().sort_values(ascending=False).head(10).reset_index()
fig6 = px.bar(top_products, x='revenue', y='product_detail',
              orientation='h',
              color='revenue', color_continuous_scale='Teal',
              labels={'product_detail': 'Product', 'revenue': 'Revenue ($)'},
              title="Top 10 Products by Revenue")
fig6.update_layout(yaxis={'categoryorder': 'total ascending'})
st.plotly_chart(fig6, use_container_width=True)

st.markdown("---")
st.caption("📊 Dashboard built for Afficionado Coffee Roasters | Data Analyst Project 2025")