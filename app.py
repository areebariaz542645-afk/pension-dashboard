import streamlit as st
import pandas as pd  # Data ko table aur graph me badalne k liye

# Website ka Title aur Heading
st.set_page_config(page_title="AI Pension Dashboard", page_icon="📊", layout="centered")
st.title("📊 Government Employee Pension Forecast & AI Dashboard")
st.write("Welcome! This AI-driven web application calculates and visualizes retirement benefits with future growth trends.")

# User se input lene ke liye website par boxes aur sliders
st.sidebar.header("User Profile Input")
basic_pay = st.sidebar.number_input("Enter Last Basic Pay (PKR):", min_value=10000, value=85000, step=5000)
service_years = st.sidebar.slider("Select Total Service Years:", min_value=10, max_value=40, value=32)
bps_scale = st.sidebar.selectbox("Select BPS Scale:", list(range(1, 23)), index=16)

# 1. Service years cap logic
calculated_years = 30 if service_years > 30 else service_years

# 2. Formulas
gross_pension = (basic_pay * calculated_years * 7) / 300
net_monthly_base = gross_pension * 0.65
medical_allowance = 1500 if bps_scale <= 15 else 2500
adhoc_relief = net_monthly_base * 0.15
current_total_payout = net_monthly_base + medical_allowance + adhoc_relief

# --- VISUAL FEATURE 1: Highlighted KPI Cards ---
st.subheader("📋 Current Payout Summary")
col1, col2, col3 = st.columns(3)
col1.metric(label="Gross Pension", value=f"PKR {gross_pension:,.0f}")
col2.metric(label="Net Base Pension", value=f"PKR {net_monthly_base:,.0f}")
col3.metric(label="Medical & Adhoc", value=f"PKR {(medical_allowance + adhoc_relief):,.0f}")

st.success(f"### 💰 TOTAL CURRENT MONTHLY PAYOUT: PKR {current_total_payout:,.2f}")

# Data generation for future 5 years
years_list = ["Current Year"]
payouts_list = [current_total_payout]
future_payout = current_total_payout

for year in range(1, 6):
    increment_amount = future_payout * 0.10
    future_payout += increment_amount
    years_list.append(f"Year {year}")
    payouts_list.append(future_payout)

# Creating a DataFrame for charts
chart_data = pd.DataFrame({
    "Timeline": years_list,
    "Predicted Monthly Payout (PKR)": payouts_list
})

# --- VISUAL FEATURE 2: Interactive AI Growth Chart ---
st.subheader("📈 AI Future 5-Year Pension Growth Trend")
st.write("This interactive chart visualizes the compounding effect of the estimated 10% annual increment.")
# Streamlit line chart widget
st.line_chart(chart_data.set_index("Timeline"))

# --- VISUAL FEATURE 3: Detailed Data Matrix Table ---
st.subheader("📊 Detailed Forecasting Matrix")
formatted_data = []
future_payout = current_total_payout
for year in range(1, 6):
    increment_amount = future_payout * 0.10
    future_payout += increment_amount
    formatted_data.append({
        "Timeline": f"Year {year}",
        "Estimated Increment (10%)": f"PKR {increment_amount:,.2f}",
        "Predicted Monthly Payout": f"PKR {future_payout:,.2f}"
    })
st.table(formatted_data)

