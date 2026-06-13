import streamlit as st

# Website ka Title aur Heading
st.title("Government Employee Pension Forecast Dashboard")
st.write("Welcome! This AI-driven web application calculates and predicts retirement benefits.")

# User se input lene ke liye website par boxes aur sliders
basic_pay = st.number_input("Enter Last Basic Pay (PKR):", min_value=10000, value=85000, step=5000)
service_years = st.slider("Select Total Service Years:", min_value=10, max_value=40, value=32)
bps_scale = st.selectbox("Select BPS Scale:", list(range(1, 23)), index=16)

# Button jis par click kar k website calculate karegi
if st.button("Generate AI Forecast Dashboard"):
    
    # 1. Service years cap logic
    calculated_years = 30 if service_years > 30 else service_years
    
    # 2. Formulas
    gross_pension = (basic_pay * calculated_years * 7) / 300
    net_monthly_base = gross_pension * 0.65
    medical_allowance = 1500 if bps_scale <= 15 else 2500
    adhoc_relief = net_monthly_base * 0.15
    current_total_payout = net_monthly_base + medical_allowance + adhoc_relief
    
    # Website par Results display karna
    st.subheader("📊 Current Payout Summary")
    st.write(f"**Calculated Gross Pension:** PKR {gross_pension:,.2f}")
    st.write(f"**Net Monthly Base Pension:** PKR {net_monthly_base:,.2f}")
    st.write(f"**Medical Allowance:** PKR {medical_allowance:,.2f}")
    st.write(f"**Adhoc Relief Increase:** PKR {adhoc_relief:,.2f}")
    st.success(f"**TOTAL CURRENT MONTHLY PAYOUT:** PKR {current_total_payout:,.2f}")
    
    # Future 5-Year Forecast Table
    st.subheader("📈 AI Future 5-Year Pension Forecasting Matrix")
    year_data = []
    future_payout = current_total_payout
    
    for year in range(1, 6):
        increment_amount = future_payout * 0.10
        future_payout += increment_amount
        year_data.append({
            "Year": f"Year {year}",
            "Estimated Increment (10%)": f"PKR {increment_amount:,.2f}",
            "Predicted Monthly Payout": f"PKR {future_payout:,.2f}"
        })
    
    # Website par poora table show karna
    st.table(year_data)
  
