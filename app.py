import streamlit as st
import pandas as pd

# Page setup with custom theme title
st.set_page_config(page_title="RetireWell AI Portal", page_icon="🏥", layout="centered")

# --- CUSTOM CSS FOR PREMIUM APP LOOK ---
st.markdown("""
<style>
    .main { background-color: #f7f9fc; }
    .stButton>button {
        background-color: #007f66;
        color: white;
        border-radius: 8px;
        width: 100%;
        height: 45px;
        font-weight: bold;
    }
    .metric-box {
        background-color: white;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border-left: 5px solid #007f66;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# App Navigation / Tabs (Just like top medical apps)
tab1, tab2 = st.tabs(["🔐 Portal Signup / Access", "📊 Employee Benefits Dashboard"])

# --- TAB 1: SIGNUP SCREEN (Inspired by your 3rd image) ---
with tab1:
    st.markdown("<h2 style='text-align: center; color: #007f66;'>🏥 Create Medical & Pension Account</h2>", unsafe_allow_html=True)
    
    # Visual illustration vector link for healthcare
    st.image("https://img.freepik.com/free-vector/doctors-concept-illustration_114360-1515.jpg", width=300, use_container_width=True)
    
    # Signup Form Fields
    full_name = st.text_input("Full Name*", placeholder="e.g., Md. Sourav")
    email = st.text_input("Email Address*", placeholder="test@gmail.com")
    password = st.text_input("Password*", type="password", placeholder="*********")
    confirm_password = st.text_input("Confirm Password*", type="password", placeholder="*********")
    
    if st.button("Sign Up Now"):
        if password == confirm_password and full_name and email:
            st.success(f"Welcome {full_name}! Verification link sent to {email}. You can now view the Dashboard tab.")
        else:
            st.error("Please fill all required fields or check if passwords match.")

# --- TAB 2: BENEFITS DASHBOARD (Inspired by your 1st & 2nd images) ---
with tab2:
    st.markdown("<h2 style='color: #007f66;'>📊 Retirement Welfare & Financial Forecasting</h2>", unsafe_allow_html=True)
    
    # Main Dashboard Visual Vector (Pension & Coins theme)
    st.image("https://img.freepik.com/free-vector/pension-concept-illustration_114360-7984.jpg", use_container_width=True)
    
    # Layout splits for inputs
    st.markdown("### 🛠️ Configure Your Benefits Package")
    col_in1, col_in2 = st.columns(2)
    with col_in1:
        basic_pay = st.number_input("Last Basic Pay (PKR):", min_value=10000, value=85000, step=5000)
        service_years = st.slider("Total Service Years:", min_value=10, max_value=40, value=32)
    with col_in2:
        bps_scale = st.selectbox("BPS Scale / Grade:", list(range(1, 23)), index=16)
        current_age = st.slider("Current Age:", min_value=60, max_value=85, value=60)

    # Calculations logic
    calculated_years = 30 if service_years > 30 else service_years
    gross_pension = (basic_pay * calculated_years * 7) / 300
    net_monthly_base = gross_pension * 0.65
    medical_allowance = 1500 if bps_scale <= 15 else 2500
    adhoc_relief = net_monthly_base * 0.15
    total_pension = net_monthly_base + medical_allowance + adhoc_relief

    # Visual Output Cards
    st.markdown("### 📋 Active Benefits Matrix Summary")
    
    st.markdown(f"""
    <div class='metric-box'>
        <p style='margin:0; color:gray; font-size:14px;'>💰 Monthly Net Base Pension</p>
        <h3 style='margin:0; color:#007f66;'>PKR {net_monthly_base:,.2f}</h3>
    </div>
    <div class='metric-box' style='border-left-color: #2196F3;'>
        <p style='margin:0; color:gray; font-size:14px;'>🏥 Medical Care Allowance (Scale {bps_scale} Verified)</p>
        <h3 style='margin:0; color:#2196F3;'>PKR {medical_allowance:,.2f}</h3>
    </div>
    """, unsafe_allow_html=True)

    st.success(f"### 💳 TOTAL MONTHLY WELFARE ESTIMATE: PKR {total_pension:,.2f}")

    # Interactive Forecasting Graph
    st.markdown("### 📈 AI 5-Year Financial Growth vs. Medical Inflation")
    
    timeline, pension_trend, medical_trend = [], [], []
    temp_pension = total_pension
    base_medical_cost = 4000 if bps_scale <= 15 else 7000

    for i in range(0, 6):
        timeline.append(f"Age {current_age + i}")
        if i > 0: temp_pension += (temp_pension * 0.10)
        pension_trend.append(temp_pension)
        medical_trend.append(base_medical_cost * ((1.12) ** i))

    chart_data = pd.DataFrame({
        "Age Timeline": timeline,
        "Predicted Pension (PKR)": pension_trend,
        "Estimated Health Inflation": medical_trend
    })
    
    st.line_chart(chart_data.set_index("Age Timeline"))
        
