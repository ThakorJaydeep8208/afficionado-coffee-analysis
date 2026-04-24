# ================================================
# Phase 2: Data Cleaning & EDA
# Afficionado Coffee Roasters - Sales Analysis
# ================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ------------------------------------------------
# 1. LOAD DATA
# ------------------------------------------------
df = pd.read_csv(r"D:\time base sales poject\afficionado_coffee_project\Afficionado Coffee Roasters.xlsx - Transactions.csv")

print("=" * 50)
print("STEP 1: DATA LOADED SUCCESSFULLY")
print("=" * 50)
print(f"Total Rows    : {df.shape[0]}")
print(f"Total Columns : {df.shape[1]}")
print(f"\nColumn Names:\n{list(df.columns)}")

# ------------------------------------------------
# 2. DATA VALIDATION
# ------------------------------------------------
print("\n" + "=" * 50)
print("STEP 2: DATA VALIDATION")
print("=" * 50)

# Missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# Duplicate transaction IDs
duplicates = df.duplicated(subset='transaction_id').sum()
print(f"\n--- Duplicate Transaction IDs: {duplicates} ---")

# Negative values check
neg_qty = (df['transaction_qty'] <= 0).sum()
neg_price = (df['unit_price'] <= 0).sum()
print(f"\n--- Negative/Zero Quantities: {neg_qty} ---")
print(f"--- Negative/Zero Prices   : {neg_price} ---")

# ------------------------------------------------
# 3. FEATURE ENGINEERING
# ------------------------------------------------
print("\n" + "=" * 50)
print("STEP 3: FEATURE ENGINEERING")
print("=" * 50)

# Parse transaction_time as datetime (date part doesn't matter)
df['transaction_time'] = pd.to_datetime(df['transaction_time'], format='%H:%M:%S', errors='coerce')

# Extract hour
df['hour'] = df['transaction_time'].dt.hour

# Day of week (need a date column — use transaction_id as proxy row index for now)
# Since the dataset has a 'year' column = 2025, we'll reconstruct dates
# The dataset likely spans Jan-Jun 2025 based on ~149k rows
# We'll derive day_of_week from transaction order using a running date
# But since no date column exists, we create hour & time bucket from time only

# Time buckets
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

# Revenue per transaction
df['revenue'] = df['transaction_qty'] * df['unit_price']

print("New columns added: hour, time_bucket, revenue")
print(df[['transaction_id', 'transaction_time', 'hour', 'time_bucket', 'revenue']].head(10))

# ------------------------------------------------
# 4. BASIC STATS
# ------------------------------------------------
print("\n" + "=" * 50)
print("STEP 4: BASIC STATISTICS")
print("=" * 50)

print(f"\nTotal Revenue       : ${df['revenue'].sum():,.2f}")
print(f"Average Transaction : ${df['revenue'].mean():,.2f}")
print(f"Total Transactions  : {len(df):,}")
print(f"\nStore Locations     : {df['store_location'].unique()}")
print(f"Product Categories  : {df['product_category'].unique()}")

# ------------------------------------------------
# 5. SAVE CLEANED DATA
# ------------------------------------------------
df.to_csv("cleaned_transactions.csv", index=False)
print("\n✅ Cleaned data saved as: cleaned_transactions.csv")

# ------------------------------------------------
# 6. QUICK VISUALIZATIONS
# ------------------------------------------------
os.makedirs("charts", exist_ok=True)

# Chart 1: Transactions by Hour
plt.figure(figsize=(12, 5))
hourly = df.groupby('hour')['transaction_id'].count()
sns.barplot(x=hourly.index, y=hourly.values, palette='Blues_d')
plt.title('Number of Transactions by Hour of Day')
plt.xlabel('Hour (0-23)')
plt.ylabel('Number of Transactions')
plt.tight_layout()
plt.savefig("charts/transactions_by_hour.png")
plt.show()
print("✅ Chart saved: charts/transactions_by_hour.png")

# Chart 2: Revenue by Time Bucket
plt.figure(figsize=(8, 5))
bucket_rev = df.groupby('time_bucket')['revenue'].sum().sort_values(ascending=False)
sns.barplot(x=bucket_rev.index, y=bucket_rev.values, palette='Oranges_d')
plt.title('Total Revenue by Time Bucket')
plt.xlabel('Time Bucket')
plt.ylabel('Total Revenue ($)')
plt.tight_layout()
plt.savefig("charts/revenue_by_time_bucket.png")
plt.show()
print("✅ Chart saved: charts/revenue_by_time_bucket.png")

# Chart 3: Revenue by Store Location
plt.figure(figsize=(8, 5))
store_rev = df.groupby('store_location')['revenue'].sum().sort_values(ascending=False)
sns.barplot(x=store_rev.index, y=store_rev.values, palette='Greens_d')
plt.title('Total Revenue by Store Location')
plt.xlabel('Store Location')
plt.ylabel('Total Revenue ($)')
plt.tight_layout()
plt.savefig("charts/revenue_by_store.png")
plt.show()
print("✅ Chart saved: charts/revenue_by_store.png")

# Chart 4: Revenue by Product Category
plt.figure(figsize=(10, 5))
cat_rev = df.groupby('product_category')['revenue'].sum().sort_values(ascending=False)
sns.barplot(x=cat_rev.index, y=cat_rev.values, palette='Purples_d')
plt.title('Total Revenue by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Revenue ($)')
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("charts/revenue_by_category.png")
plt.show()
print("✅ Chart saved: charts/revenue_by_category.png")

print("\n🎉 Phase 2 Complete! All charts saved in the 'charts' folder.")