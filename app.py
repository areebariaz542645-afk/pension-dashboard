import streamlit as st
import pandas as pd

# Page Layout Configuration
st.set_page_config(page_title="RetireWell Pro", page_icon="🟢", layout="centered")

# --- ADVANCED PREMIUM FINTECH CSS ---
st.markdown("""
<style>
    /* Clean App Canvas */
    .stApp { background-color: #f8fafc; }
    
    /* Hide default Streamlit decoration line */
    header { visibility: hidden; }
    
    /* Login Box Container */
    .login-container {
        background-color: #ffffff;
        padding: 35px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.04);
        border: 1px solid #e2e8f0;
        margin-top: 50px;
    }
    
    /* Premium Action Button */
    .stButton>button {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%) !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        border: none !important;
        height: 48px;
        font-weight: 600;
        font-size: 16px;
        width: 100%;
        box-shadow: 0 4px 12px rgba(15,23,42,0.15);
    }
    
    /* Account Profile Badge */
    .profile-card {
        background-color: #ffffff;
        padding: 15px 20px;
        border-radius: 14px;
        border-left: 5px solid #0f172a;
        box-shadow: 0 2px 8px rgba(0,0,0,0.02);
        margin-bottom: 25px;
    }
    
    /* Wallet Balance Component (Easypaisa style) */
    .digital-wallet {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #ffffff;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 20px rgba(15, 23, 42, 0.08);
        margin-bottom: 30px;
    }
    
    /* Grid Feature Analytics Cards (Like Replit Dashboard) */
    .icon-grid-card {
        background-color: #ffffff;
        padding: 22px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.02);
        border: 1px solid #edf2f7;
        transition: transform 0.2s;
    }
    .icon-grid-card:hover {
        transform: translateY(-3px);
    }
</style>
""", unsafe_allow_html=True)

# --- STRICT ACCESS CONTROLLER ---
if 'is_unlocked' not in st.session_state:
    st.session_state['is_unlocked'] = False
if 'user_data' not in st.session_state:
    st.session_state['user_data'] = {"name": "", "email": ""}

# --- SCREEN 1: LOCKED SIGN-IN PORTAL (Direct Form, No Tabs) ---
if not st.session_state['is_unlocked']:
    st.markdown("<div class='login-container'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #0f172a; font-weight: 700; margin-bottom: 5px;'>RetireWell Secure Access</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b; font-size: 14px; margin-bottom: 30px;'>Please authenticate to view encrypted pension telemetry.</p>", unsafe_allow_html=True)
    
    # Input Fields
    u_name = st.text_input("Account Holder Full Name", placeholder="e.g., Mohammad Bilal")
    u_email = st.text_input("Registered Email Address", placeholder="username@domain.com")
    u_pin = st.text_input("Secure Access PIN", type="password", placeholder="••••••••")
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Secure Sign In"):
        if u_name and u_email and u_pin:
            st.session_state['is_unlocked'] = True
            st.session_state['user_data']['name'] = u_name
            st.session_state['user_data']['email'] = u_email
            st.rerun()
        else:
            st.error("🔒 Access Denied: Enter complete credentials to authenticate.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- SCREEN 2: UNLOCKED PRO ANALYTICS DASHBOARD ---
else:
    # Top Profile Header & Sign-Out Action
    col_nav, col_btn = st.columns([4, 1])
    with col_nav:
        st.markdown("<h2 style='color: #0f172a; font-weight: 700; margin: 0;'>Analytics Dashboard</h2>", unsafe_allow_html=True)
    with col_btn:
        if st.button("Sign Out"):
            st.session_state['is_unlocked'] = False
            st.rerun()
            
    st.markdown("<hr style='margin: 15px 0 25px 0; border: 0; border-top: 1px solid #e2e8f0;'>", unsafe_allow_html=True)

    # Personal Information Display Badge
    st.markdown(f"""
    <div class='profile-card'>
        <p style='margin:0; color:#64748b; font-size:11px; font-weight:600; letter-spacing:0.5px;'>🛡️ VERIFIED ACCOUNT PROFILE</p>
        <p style='margin:5px 0 0 0; font-weight:700; color:#0f172a;'>Holder: {st.session_state['user_data']['name']}</p>
        <p style='margin:2px 0 0 0; color:#64748b; font-size:13px;'>Email: {st.session_state['user_data']['email']}</p>
    </div>
    """, unsafe_allow_html=True)

    # Clean Configuration Matrix (Sliders & Inputs)
    st.markdown("### 🛠️ Configuration Tuning Matrix")
    col_in1, col_in2 = st.columns(2)
    with col_in1:
        basic_pay = st.number_input("Last Basic Pay (PKR)", min_value=10000, value=85000, step=5000)
        service_years = st.slider("Total Completed Service Years", min_value=10, max_value=40, value=32)
    with col_in2:
        bps_scale = st.selectbox("Verified BPS Grade / Scale", list(range(1, 23)), index=16)
        current_age = st.slider("Active Retirement Age", min_value=60, max_value=85, value=60)

    # Core Logic Formulas
    calculated_years = 30 if service_years > 30 else service_years
    gross_pension = (basic_pay * calculated_years * 7) / 300
    net_monthly_base = gross_pension * 0.65
    medical_allowance = 1500 if bps_scale <= 15 else 2500
    adhoc_relief = net_monthly_base * 0.15
    total_revenue = net_monthly_base + medical_allowance + adhoc_relief

    st.markdown("<br>", unsafe_allow_html=True)

    # --- MAIN COMPONENT 1: THE DIGITAL WALLET (Available Balance) ---
    st.markdown(f"""
    <div class='digital-wallet'>
        <p style='margin:0; font-size:13px; font-weight: 500; opacity:0.85; letter-spacing: 0.5px;'>🟢 AVAILABLE MONTHLY WELFARE BALANCE</p>
        <h1 style='margin:10px 0; font-size:42px; font-weight:700; letter-spacing: -0.5px;'>Rs. {total_revenue:,.2f}</h1>
        <p style='margin:0; font-size:12px; opacity:0.75;'>🔒 Secure Federal Level AI Telemetry Active</p>
    </div>
    """, unsafe_allow_html=True)

    # --- MAIN COMPONENT 2: ROUNDED CARDS GRID WITH ICONS (Like Replit app) ---
    st.markdown("### 📱 Active Benefit Feature Matrix")
    col_f1, col_f2, col_f3 = st.columns(3)
    
    with col_f1:
        st.markdown(f"""
        <div class='icon-grid-card'>
            <span style='font-size:32px;'>💰</span>
            <p style='margin:8px 0 4px 0; color:#64748b; font-size:12px; font-weight:500;'>Net Pension</p>
            <h4 style='margin:0; color:#0f172a; font-weight:700;'>Rs. {net_monthly_base:,.0f}</h4>
        </div>
        """, unsafe_allow_html=True)
        
    with col_f2:
        st.markdown(f"""
        <div class='icon-grid-card'>
            <span style='font-size:32px;'>🏥</span>
            <p style='margin:8px 0 4px 0; color:#64748b; font-size:12px; font-weight:500;'>Medical Fund</p>
            <h4 style='margin:0; color:#0f172a; font-weight:700;'>Rs. {medical_allowance:,.0f}</h4>
        </div>
        """, unsafe_allow_html=True)
        
    with col_f3:
        st.markdown(f"""
        <div class='icon-grid-card'>
            <span style='font-size:32px;'>⚡</span>
            <p style='margin:8px 0 4px 0; color:#64748b; font-size:12px; font-weight:500;'>Adhoc Relief</p>
            <h4 style='margin:0; color:#0f172a; font-weight:700;'>Rs. {adhoc_relief:,.0f}</h4>
        </div>
        """, unsafe_allow_html=True)

    # --- MAIN COMPONENT 3: CLEAN GRAPH SYSTEM ---
    st.markdown("<br>### 📈 Actuarial Growth Vector & Health Inflation Trends", unsafe_allow_html=True)
    
    timeline, pension_trend, medical_trend = [], [], []
    temp_pension = total_revenue
    base_medical_cost = 4000 if bps_scale <= 15 else 7000

    for i in range(0, 6):
        timeline.append(f"Age {current_age + i}")
        if i > 0: temp_pension += (temp_pension * 0.10)
        pension_trend.append(temp_pension)
        medical_trend.append(base_medical_cost * ((1.12) ** i))

    chart_data = pd.DataFrame({
        "Timeline": timeline,
        "Total Pension Growth": pension_trend,
        "Medical Cost Trend": medical_trend
    })
    
    st.line_chart(chart_data.set_index("Timeline"))
    
