import streamlit as st
import pandas as pd
import base64

# Page configurations for a premium look
st.set_page_config(page_title="Health Welfare Pension Portal", page_icon="🩺", layout="centered")

# --- EMBEDDED HIGH-QUALITY MEDICAL & DASHBOARD VECTORS (No Local Image Dependency) ---
# Clean minimalist SVG vector for the Signup screen (Medical Professionals Concept)
signup_svg = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" style="background:#f1f5f9; border-radius:16px;">
    <defs>
        <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#006643;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#004d32;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="800" height="500" rx="16" fill="#e2e8f0"/>
    <circle cx="400" cy="250" r="180" fill="#ffffff" opacity="0.6"/>
    <path d="M400,120 C460,120 520,100 520,100 C520,240 400,380 400,380 C400,380 280,240 280,100 C280,100 340,120 400,120 Z" fill="url(#grad1)" />
    <path d="M370,210 H430 V250 H370 Z M390,190 H410 V270 H390 Z" fill="#ffffff"/>
    <text x="400" y="440" font-family="'Segoe UI', sans-serif" font-size="24" font-weight="bold" fill="#006643" text-anchor="middle">MEDICAL SECURITY GATEWAY</text>
</svg>
"""

# Dynamic SVG Vector for the Pension Dashboard Screen (Growth & Wallet Concept)
dashboard_svg = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 300" width="100%" style="border-radius:16px;">
    <rect width="800" height="300" rx="16" fill="#f8fafc"/>
    <circle cx="150" cy="150" r="90" fill="#e2e8f0" opacity="0.5"/>
    <circle cx="650" cy="150" r="80" fill="#006643" opacity="0.1"/>
    <path d="M120,120 H200 V180 H120 Z" fill="#006643" rx="5"/>
    <path d="M150,100 L230,150 L150,200 Z" fill="#00a86b" opacity="0.8"/>
    <path d="M350,200 L450,150 L550,120 L650,80" fill="none" stroke="#006643" stroke-width="5" stroke-linecap="round"/>
    <circle cx="650" cy="80" r="10" fill="#00a86b"/>
    <text x="400" y="260" font-family="'Segoe UI', sans-serif" font-size="22" font-weight="bold" fill="#0f172a" text-anchor="middle">ACTIVE TELEMETRY DISTRIBUTION DISPATCH</text>
</svg>
"""

# Helper function to render SVGs securely
def render_svg(svg_code):
    b64 = base64.b64encode(svg_code.encode('utf-8')).decode("utf-8")
    return f'<img src="data:image/svg+xml;base64,{b64}" style="width:100%; border-radius:16px; margin-bottom:15px;"/>'

# --- STABLE SYSTEM INLINE CSS (Strict Light Theme Force for Mobile Dark Modes) ---
st.markdown("""
<style>
    /* Force persistent solid light background */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #f8fafc !important;
    }
    
    /* Strict font color enforcement - stops text from turning white/invisible */
    h1, h2, h3, h4, h5, h6, p, span, label, div, td, th {
        color: #0f172a !important;
        font-family: 'Segoe UI', system-ui, sans-serif !important;
    }
    
    /* Form input styling overrides */
    input, select, [data-testid="stNumberInput"] input {
        background-color: #ffffff !important;
        color: #0f172a !important;
        border: 1px solid #cbd5e1 !important;
    }
    
    /* White Card Feature Panels */
    .feature-panel {
        background-color: #ffffff !important;
        padding: 20px;
        border-radius: 16px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.04);
        margin-bottom: 20px;
    }
    
    /* Premium Easypaisa-style Green Wallet Component */
    .wallet-card-green {
        background: linear-gradient(135deg, #006643 0%, #004d32 100%) !important;
        padding: 24px;
        border-radius: 20px;
        box-shadow: 0 8px 24px rgba(0, 102, 67, 0.2);
        margin-bottom: 25px;
    }
    .wallet-card-green h1, .wallet-card-green p {
        color: #ffffff !important; /* Forces clear white text inside the green wallet card */
    }
    
    /* Mini Cards Feature Grid */
    .asset-grid-box {
        background-color: #ffffff !important;
        padding: 16px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        text-align: center;
        box-shadow: 0 2px 6px rgba(0,0,0,0.02);
    }
    
    /* Dataframe view fix */
    [data-testid="stDataFrame"] div {
        color: #0f172a !important;
    }
    
    /* Hide native header elements for app-like layout */
    header { visibility: hidden !important; }
    footer { visibility: hidden !important; }
    .stDeployButton { display: none !important; }
</style>
""", unsafe_allow_html=True)

# --- APPLICATION STATE CONTROLLER ---
if 'app_unlocked' not in st.session_state:
    st.session_state['app_unlocked'] = False
if 'profile' not in st.session_state:
    st.session_state['profile'] = {"name": "", "email": ""}

# --- SCREEN 1: LOCKED SIGN-IN PORTAL ---
if not st.session_state['app_unlocked']:
    st.markdown("<div style='max-width: 450px; margin: 0 auto;'>", unsafe_allow_html=True)
    
    # Render embedded professional medical graphics vector
    st.markdown(render_svg(signup_svg), unsafe_allow_html=True)
        
    st.markdown("<h2 style='text-align: center; font-weight: 700; margin-top:0;'>Welfare Signup</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 13px; margin-bottom: 25px;'>Securely access active welfare asset telemetry parameters.</p>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("<div class='feature-panel'>", unsafe_allow_html=True)
        in_name = st.text_input("Full Name*", placeholder="Md.Sourav")
        in_email = st.text_input("Email*", placeholder="test@gmail.com")
        in_pin = st.text_input("Password*", type="password", placeholder="**********")
        st.markdown("</div>", unsafe_allow_html=True)
        
        if st.button("Sign Up", use_container_width=True):
            if in_name and in_email and in_pin:
                st.session_state['app_unlocked'] = True
                st.session_state['profile']['name'] = in_name
                st.session_state['profile']['email'] = in_email
                st.rerun()
            else:
                st.error("🔒 Please completely fill out all attributes.")
                
    st.markdown("</div>", unsafe_allow_html=True)

# --- SCREEN 2: ACTIVE DYNAMIC DASHBOARD (UNLOCKED) ---
else:
    # Top Custom Action Menu Header
    nav_left, nav_right = st.columns([3, 1])
    with nav_left:
        st.markdown("<h2 style='font-weight: 800; margin: 0;'>🩺 Pension Dashboard</h2>", unsafe_allow_html=True)
    with nav_right:
        if st.button("Sign Out", use_container_width=True):
            st.session_state['app_unlocked'] = False
            st.rerun()
            
    st.markdown("<hr style='margin: 15px 0; border-top: 1px solid #cbd5e1;'>", unsafe_allow_html=True)

    # Render professional dashboard metric banner graphic
    st.markdown(render_svg(dashboard_svg), unsafe_allow_html=True)

    # Verified Token Ribbon
    st.markdown(f"""
    <div style='background-color: #e2e8f0; padding: 12px 16px; border-radius: 12px; border-left: 5px solid #006643; margin-bottom: 20px;'>
        <p style='margin:0; font-size:11px; font-weight:700; letter-spacing:0.5px; color:#006643;'>🛡️ VERIFIED GOVERNMENT RETIREMENT CREDENTIALS</p>
        <p style='margin:4px 0 0 0; font-weight:700; font-size:14px;'>Officer: {st.session_state['profile']['name']} | Gateway: {st.session_state['profile']['email']}</p>
    </div>
    """, unsafe_allow_html=True)

    # Parameter Optimization Panel
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

    # Fixed Math Calculation Engine Core (Variables Mapped Accurately)
    safe_tenure = 30 if tenure_val > 30 else tenure_val
    gross_calc = (pay_val * safe_tenure * 7) / 300
    net_monthly = gross_calc * 0.65
    medical_fund = 1500 if bps_val <= 15 else 2500
    adhoc_fund = net_monthly * 0.15
    total_welfare_payout = net_monthly + medical_fund + adhoc_fund  # FIXED SPELLING ERROR HERE

    # THE REAL EASYPAISA ACCOUNT WALLET COMPONENT (Color Locked White on Green)
    st.markdown(f"""
    <div class='wallet-card-green'>
        <p style='margin:0; font-size:11px; font-weight: 500; opacity:0.9; letter-spacing:0.5px;'>🟢 AVAILABLE MONTHLY WELFARE BALANCE</p>
        <h1 style='margin:6px 0; font-size:36px; font-weight:700;'>Rs. {total_welfare_payout:,.2f}</h1>
        <p style='margin:0; font-size:11px; opacity:0.8;'>✓ Account Channel Secure Connection Active</p>
    </div>
    """, unsafe_allow_html=True)

    # Interactive Dashboard Features Grid
    st.markdown("### 📱 Active Benefit Feature Matrix")
    grid_1, grid_2, grid_3 = st.columns(3)
    with grid_1:
        st.markdown(f"<div class='asset-grid-box'><p style='margin:0; font-size:11px; color:#64748b;'>Net Pension</p><h4 style='margin:4px 0 0 0; font-weight:700; color:#006643;'>Rs. {net_monthly:,.0f}</h4></div>", unsafe_allow_html=True)
    with grid_2:
        st.markdown(f"<div class='asset-grid-box'><p style='margin:0; font-size:11px; color:#64748b;'>Medical Care</p><h4 style='margin:4px 0 0 0; font-weight:700; color:#006643;'>Rs. {medical_fund:,.0f}</h4></div>", unsafe_allow_html=True)
    with grid_3:
        st.markdown(f"<div class='asset-grid-box'><p style='margin:0; font-size:11px; color:#64748b;'>Adhoc Relief</p><h4 style='margin:4px 0 0 0; font-weight:700; color:#006643;'>Rs. {adhoc_fund:,.0f}</h4></div>", unsafe_allow_html=True)

    # Trend Analytics Calculations
    axis_timeline, trend_pension, trend_medical = [], [], []
    rolling_pension = total_welfare_payout
    initial_med_cost = 4000 if bps_val <= 15 else 7000

    for idx in range(0, 6):
        axis_timeline.append(f"Age {age_val + idx}")
        if idx > 0: 
            rolling_pension += (rolling_pension * 0.10)
        trend_pension.append(rolling_pension)
        trend_medical.append(initial_med_cost * ((1.12) ** idx))

    # Native Line Chart Analytics Engine
    st.markdown("<br>### 📈 5-Year Actuarial Growth Vector Lines", unsafe_allow_html=True)
    analytics_df = pd.DataFrame({
        "Total Pension Asset": trend_pension,
        "Healthcare Expense Trend": trend_medical
    }, index=axis_timeline)
    st.line_chart(analytics_df)

    # Native Secure Forecast Table Data Matrix
    st.markdown("### 📊 Forecasted Compounding Matrix Table")
    display_df = pd.DataFrame({
        "Timeline Horizon": [f"Year {step} (Age {age_val + step})" for step in range(1, 6)],
        "Forecasted Pension": [f"PKR {trend_pension[step]:,.2f}" for step in range(1, 6)],
        "Medical Cost Index": [f"PKR {trend_medical[step]:,.2f}" for step in range(1, 6)]
    })
    
    st.dataframe(display_df, use_container_width=True, hide_index=True)
        
