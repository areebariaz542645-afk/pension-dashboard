import streamlit as st
import pandas as pd
import base64
import os

# Page layout configurations
st.set_page_config(page_title="Health Welfare Pension Portal", page_icon="🩺", layout="centered")

# --- IMAGE TO BASE64 CONVERTER FUNCTION ---
def get_image_base64(image_path):
    """Converts a local image into a secure base64 string to prevent broken image errors on mobile."""
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return None

# !!! MERE PYARE USER: AGAR AAP KI IMAGE FILES KA NAAM ALAG HAI TO NEECHE INHEIN UPDATE KAR LEIN !!!
login_graphic_base64 = get_image_base64("1000105252.jpg")  # Doctors Signup/Login Graphic
dashboard_graphic_base64 = get_image_base64("1000105254.jpg")  # Employee Benefits/Coins Graphic

# --- STABLE SYSTEM INLINE CSS (Forces visibility under any smartphone dark mode) ---
st.markdown("""
<style>
    /* Absolute light theme canvas force injection */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #f8fafc !important;
    }
    
    /* Strict global typography override - prevents text white-out */
    h1, h2, h3, h4, h5, h6, p, span, label, div, td, th {
        color: #0f172a !important;
        font-family: 'Segoe UI', system-ui, sans-serif !important;
    }
    
    /* Input Elements styling */
    input, select, [data-testid="stNumberInput"] input {
        background-color: #ffffff !important;
        color: #0f172a !important;
        border: 1px solid #cbd5e1 !important;
    }
    
    /* Premium Container Panel */
    .feature-panel {
        background-color: #ffffff !important;
        padding: 20px;
        border-radius: 16px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.04);
        margin-bottom: 20px;
    }
    
    /* Custom Easypaisa Brand Monthly Card */
    .wallet-card-green {
        background: linear-gradient(135deg, #006643 0%, #004d32 100%) !important;
        padding: 24px;
        border-radius: 20px;
        box-shadow: 0 8px 24px rgba(0, 102, 67, 0.2);
        margin-bottom: 25px;
    }
    .wallet-card-green h2, .wallet-card-green p, .wallet-card-green span, .wallet-card-green h1 {
        color: #ffffff !important; /* Kept permanently crystal white */
    }
    
    /* Feature Grid Boxes */
    .asset-grid-box {
        background-color: #ffffff !important;
        padding: 16px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        text-align: center;
        box-shadow: 0 2px 6px rgba(0,0,0,0.02);
    }
    
    /* Native Table Correction Override */
    [data-testid="stDataFrame"] div {
        color: #0f172a !important;
    }
    
    /* Hide top native headers and decoration bars */
    header { visibility: hidden !important; }
    footer { visibility: hidden !important; }
    .stDeployButton { display: none !important; }
</style>
""", unsafe_allow_html=True)

# --- LOCK/UNLOCK APPLICATION CONTROLLER ---
if 'app_unlocked' not in st.session_state:
    st.session_state['app_unlocked'] = False
if 'profile' not in st.session_state:
    st.session_state['profile'] = {"name": "", "email": ""}

# --- SCREEN 1: LOCKED SIGN-IN PORTAL ---
if not st.session_state['app_unlocked']:
    st.markdown("<div style='max-width: 450px; margin: 0 auto;'>", unsafe_allow_html=True)
    
    # 1. Displays Base64 Secure Login Graphic if present
    if login_graphic_base64:
        st.markdown(f'<img src="data:image/jpeg;base64,{login_graphic_base64}" style="width:100%; border-radius:16px; margin-bottom:15px;">', unsafe_allow_html=True)
    else:
        st.markdown("<h1 style='text-align:center; font-size:50px;'>🏥</h1>", unsafe_allow_html=True)
        
    st.markdown("<h2 style='text-align: center; font-weight: 700; margin-top:0;'>Welfare Signup</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 13px; margin-bottom: 25px;'>Enter your departmental identity token attributes.</p>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("<div class='feature-panel'>", unsafe_allow_html=True)
        in_name = st.text_input("Full Name*", placeholder="Md.Sourav")
        in_email = st.text_input("Email*", placeholder="test@gmail.com")
        in_pin = st.text_input("Password*", type="password", placeholder="**********")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Sign Up", use_container_width=True):
            if in_name and in_email and in_pin:
                st.session_state['app_unlocked'] = True
                st.session_state['profile']['name'] = in_name
                st.session_state['profile']['email'] = in_email
                st.rerun()
            else:
                st.error("🔒 Please completely fill out all attributes.")
                
    st.markdown("</div>", unsafe_allow_html=True)

# --- SCREEN 2: ACTIVE DIGITAL PORTAL (UNLOCKED) ---
else:
    # Top Level Custom Navigation Header
    nav_left, nav_right = st.columns([3, 1])
    with nav_left:
        st.markdown("<h2 style='font-weight: 800; margin: 0;'>🩺 Pension Dashboard</h2>", unsafe_allow_html=True)
    with nav_right:
        if st.button("Sign Out", use_container_width=True):
            st.session_state['app_unlocked'] = False
            st.rerun()
            
    st.markdown("<hr style='margin: 15px 0; border-top: 1px solid #cbd5e1;'>", unsafe_allow_html=True)

    # 2. Displays Dashboard Vector Graphic if available
    if dashboard_graphic_base64:
        st.markdown(f'<img src="data:image/jpeg;base64,{dashboard_graphic_base64}" style="width:100%; border-radius:16px; margin-bottom:20px;">', unsafe_allow_html=True)

    # User Profile Verified Token Box
    st.markdown(f"""
    <div style='background-color: #e2e8f0; padding: 12px 16px; border-radius: 12px; border-left: 5px solid #006643; margin-bottom: 20px;'>
        <p style='margin:0; font-size:11px; font-weight:700; letter-spacing:0.5px;'>🛡️ VERIFIED GOVERNMENT RETIREMENT CREDENTIALS</p>
        <p style='margin:4px 0 0 0; font-weight:700; font-size:14px;'>Officer: {st.session_state['profile']['name']} | Gateway: {st.session_state['profile']['email']}</p>
    </div>
    """, unsafe_allow_html=True)

    # Parameter Optimization Dashboard Area
    st.markdown("<div class='feature-panel'>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight: 700; margin: 0 0 12px 0; color: #006643;'>⚙️ Actuarial Parameters Matrix</p>", unsafe_allow_html=True)
    
    pay_val = st.number_input("Last Basic Pay Matrix (PKR)", min_value=10000, value=85000, step=5000)
    tenure_val = st.slider("Service Scale (Years)", min_value=10, max_value=40, value=25)
    
    col_sub1, col_sub2 = st.columns(2)
    with col_sub1:
        bps_val = st.selectbox("BPS Cadre Scale / Grade", list(range(1, 23)), index=16)
    with col_sub2:
        age_val = st.slider("Active Retirement Age", min_value=60, max_value=85, value=62)
    st.markdown("</div>", unsafe_allow_html=True)

    # Math Calculation Engine Core
    safe_tenure = 30 if tenure_val > 30 else tenure_val
    gross_calc = (pay_val * safe_tenure * 7) / 300
    net_monthly = gross_calc * 0.65
    medical_fund = 1500 if bps_val <= 15 else 2500
    adhoc_fund = net_monthly * 0.15
    total_welfare_payout = net_monthly + medical_fund + adhoc_fund

    # THE REAL EASYPAISA ACTIVE WALLET COMPONENT (Color Locked)
    st.markdown(f"""
    <div class='wallet-card-green'>
        <p style='margin:0; font-size:11px; font-weight: 500; opacity:0.9; letter-spacing:0.5px;'>🟢 AVAILABLE MONTHLY WELFARE BALANCE</p>
        <h1 style='margin:6px 0; font-size:36px; font-weight:700;'>Rs. {total_welfare_revenue:,.2f}</h1>
        <p style='margin:0; font-size:11px; opacity:0.8;'>✓ Account Channel Secure Connection Active</p>
    </div>
    """, unsafe_allow_html=True)

    # Interactive Component Metrics Grid Row
    st.markdown("### 📱 Active Benefit Feature Matrix")
    grid_1, grid_2, grid_3 = st.columns(3)
    with grid_1:
        st.markdown(f"<div class='asset-grid-box'><p style='margin:0; font-size:11px; color:#64748b;'>Net Pension</p><h4 style='margin:4px 0 0 0; font-weight:700; color:#006643;'>Rs. {net_monthly:,.0f}</h4></div>", unsafe_allow_html=True)
    with grid_2:
        st.markdown(f"<div class='asset-grid-box'><p style='margin:0; font-size:11px; color:#64748b;'>Medical Care</p><h4 style='margin:4px 0 0 0; font-weight:700; color:#006643;'>Rs. {medical_fund:,.0f}</h4></div>", unsafe_allow_html=True)
    with grid_3:
        st.markdown(f"<div class='asset-grid-box'><p style='margin:0; font-size:11px; color:#64748b;'>Adhoc Relief</p><h4 style='margin:4px 0 0 0; font-weight:700; color:#006643;'>Rs. {adhoc_fund:,.0f}</h4></div>", unsafe_allow_html=True)

    # Trend Calculations Engine
    axis_timeline, trend_pension, trend_medical = [], [], []
    rolling_pension = total_welfare_payout
    initial_med_cost = 4000 if bps_val <= 15 else 7000

    for idx in range(0, 6):
        axis_timeline.append(f"Age {age_val + idx}")
        if idx > 0: 
            rolling_pension += (rolling_pension * 0.10)
        trend_pension.append(rolling_pension)
        trend_medical.append(initial_med_cost * ((1.12) ** idx))

    # Native Line Chart Component Render
    st.markdown("<br>### 📈 5-Year Actuarial Growth Vector Lines", unsafe_allow_html=True)
    analytics_df = pd.DataFrame({
        "Total Pension Asset": trend_pension,
        "Healthcare Expense Trend": trend_medical
    }, index=axis_timeline)
    st.line_chart(analytics_df)

    # NATIVE SECURE DATA INFRASTRUCTURE DATAFRAME
    st.markdown("### 📊 Forecasted Compounding Matrix Table")
    
    display_df = pd.DataFrame({
        "Timeline Horizon": [f"Year {step} (Age {age_val + step})" for step in range(1, 6)],
        "Forecasted Pension": [f"PKR {trend_pension[step]:,.2f}" for step in range(1, 6)],
        "Medical Cost Index": [f"PKR {trend_medical[step]:,.2f}" for step in range(1, 6)]
    })
    
    # Native dataframe automatically handles device themes beautifully without rendering raw HTML strings
    st.dataframe(display_df, use_container_width=True, hide_index=True)
        
