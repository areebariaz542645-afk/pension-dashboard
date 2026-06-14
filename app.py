import streamlit as st
import pandas as pd

# Page Config for perfect mobile view
st.set_page_config(page_title="Health Pension Portal", page_icon="🩺", layout="centered")

# --- ULTRA-SECURE FORCED VISIBILITY CSS (Fixes Blank Tabs & White-out Text) ---
st.markdown("""
<style>
    /* Pure Light-Grey Canvas for everyone */
    .stApp { background-color: #f4f7f6 !important; }
    
    /* Strict global text override so NO element goes blank or white */
    .stApp, div, p, h1, h2, h3, h4, h5, h6, span, label {
        color: #0f172a !important; 
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Hide top header lines */
    header { visibility: hidden; }
    .stDeployButton { display: none !important; }
    footer { visibility: hidden; }
    
    /* Clean Solid White Container Blocks */
    .premium-container {
        background-color: #ffffff !important;
        padding: 20px;
        border-radius: 14px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
        border: 1px solid #cbd5e1;
        margin-bottom: 20px;
    }
    
    /* Easypaisa Premium Green Button Style */
    .stButton>button {
        background: linear-gradient(135deg, #006643 0%, #004d32 100%) !important;
        color: #ffffff !important;
        border-radius: 10px !important;
        border: none !important;
        height: 48px;
        font-weight: 600;
        width: 100%;
    }
    
    /* EXACT EASYPAISA WALLET BRANDING CARD */
    .easypaisa-wallet {
        background: linear-gradient(135deg, #006643 0%, #01442d 100%) !important;
        padding: 22px;
        border-radius: 18px;
        box-shadow: 0 6px 18px rgba(0, 102, 67, 0.15);
        margin-bottom: 22px;
    }
    .easypaisa-wallet h1, .easypaisa-wallet p, .easypaisa-wallet span {
        color: #ffffff !important; /* Forces wallet text to stay crystal white */
    }

    /* Grid Feature Blocks (Like Replit Layout) */
    .metric-grid-card {
        background-color: #ffffff !important;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        border: 1px solid #e2e8f0;
        box-shadow: 0 2px 6px rgba(0,0,0,0.01);
    }
    
    /* Input Box Visibility Force */
    input, select {
        color: #0f172a !important;
        background-color: #ffffff !important;
    }
</style>
""", unsafe_allow_html=True)

# --- LOCK/UNLOCK SESSION STATE ENGINE ---
if 'is_unlocked' not in st.session_state:
    st.session_state['is_unlocked'] = False
if 'user_data' not in st.session_state:
    st.session_state['user_data'] = {"name": "", "email": ""}

# --- SCREEN 1: DEPT SIGN-IN SHIELD ---
if not st.session_state['is_unlocked']:
    st.markdown("<div style='max-width: 440px; margin: 0 auto;'>", unsafe_allow_html=True)
    st.markdown("<div class='premium-container' style='margin-top: 50px; text-align: center;'>", unsafe_allow_html=True)
    
    # Secure Code Graphic (No broken Image URLs anymore)
    st.markdown("<div style='font-size: 55px; margin-bottom: 10px;'>🏥</div>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-weight: 700; margin: 0;'>Health Welfare Login</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 13px; color: #64748b !important; margin-bottom: 20px;'>Enter departmental token attributes below.</p>", unsafe_allow_html=True)
    
    u_name = st.text_input("Officer Name", placeholder="e.g., Dr. Alina Khan")
    u_email = st.text_input("Official Email", placeholder="alina@health.gov.pk")
    u_pin = st.text_input("Access PIN", type="password", placeholder="••••••••")
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Secure Authorization Link"):
        if u_name and u_email and u_pin:
            st.session_state['is_unlocked'] = True
            st.session_state['user_data']['name'] = u_name
            st.session_state['user_data']['email'] = u_email
            st.rerun()
        else:
            st.error("🔒 Please complete all authorization fields.")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- SCREEN 2: ACTIVE DIGITAL PORTAL (UNLOCKED) ---
else:
    # Custom Header Nav Grid
    col_nav, col_btn = st.columns([3, 1])
    with col_nav:
        st.markdown("<h3 style='font-weight: 700; margin: 0;'>🩺 Pension Dashboard</h3>", unsafe_allow_html=True)
    with col_btn:
        if st.button("Sign Out"):
            st.session_state['is_unlocked'] = False
            st.rerun()
            
    st.markdown("<hr style='margin: 15px 0; border-top: 1px solid #cbd5e1;'>", unsafe_allow_html=True)

    # Parametric Calibration Controllers Panel
    st.markdown("<div class='premium-container'>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight: 600; margin: 0 0 12px 0; color: #006643 !important;'>⚙️ Actuarial Parameters Matrix</p>", unsafe_allow_html=True)
    col_in1, col_in2 = st.columns(2)
    with col_in1:
        basic_pay = st.number_input("Last Basic Pay (PKR)", min_value=10000, value=85000, step=5000)
        service_years = st.slider("Service Scale (Years)", min_value=10, max_value=40, value=32)
    with col_in2:
        bps_scale = st.selectbox("BPS Cadre Scale", list(range(1, 23)), index=16)
        current_age = st.slider("Active Retirement Age", min_value=60, max_value=85, value=60)
    st.markdown("</div>", unsafe_allow_html=True)

    # Core Calculations Engine
    calc_years = 30 if service_years > 30 else service_years
    gross_pension = (basic_pay * calc_years * 7) / 300
    net_monthly_base = gross_pension * 0.65
    medical_allowance = 1500 if bps_scale <= 15 else 2500
    adhoc_relief = net_monthly_base * 0.15
    total_welfare_revenue = net_monthly_base + medical_allowance + adhoc_relief

    # THE REAL EASYPAISA ACTIVE WALLET CARD COMPONENT
    st.markdown(f"""
    <div class='easypaisa-wallet'>
        <p style='margin:0; font-size:11px; font-weight: 500; opacity:0.95; letter-spacing:0.5px;'>🟢 AVAILABLE MONTHLY PENSION BALANCE</p>
        <h1 style='margin:6px 0; font-size:35px; font-weight:700;'>Rs. {total_welfare_revenue:,.2f}</h1>
        <p style='margin:0; font-size:11px; opacity:0.85;'>✓ Account Status: Validated Active Healthcare Distribution Account</p>
    </div>
    """, unsafe_allow_html=True)

    # Modern Grid Feature Cards Layout
    st.markdown("### 📱 Active Benefit Matrix")
    col_f1, col_f2, col_f3 = st.columns(3)
    with col_f1:
        st.markdown(f"""
        <div class='metric-grid-card'>
            <span style='font-size:26px;'>💰</span>
            <p style='margin:4px 0; font-size:12px; color:#64748b !important;'>Net Pension</p>
            <h5 style='margin:0; font-weight:700;'>Rs. {net_monthly_base:,.0f}</h5>
        </div>
        """, unsafe_allow_html=True)
    with col_f2:
        st.markdown(f"""
        <div class='metric-grid-card'>
            <span style='font-size:26px;'>💊</span>
            <p style='margin:4px 0; font-size:12px; color:#64748b !important;'>Medical Care</p>
            <h5 style='margin:0; font-weight:700;'>Rs. {medical_allowance:,.0f}</h5>
        </div>
        """, unsafe_allow_html=True)
    with col_f3:
        st.markdown(f"""
        <div class='metric-grid-card'>
            <span style='font-size:26px;'>⚡</span>
            <p style='margin:4px 0; font-size:12px; color:#64748b !important;'>Adhoc Relief</p>
            <h5 style='margin:0; font-weight:700;'>Rs. {adhoc_relief:,.0f}</h5>
        </div>
        """, unsafe_allow_html=True)

    # 5-Year Analytical Data Processing for Tables & Charts
    timeline, pension_trend, medical_trend = [], [], []
    temp_pension = total_welfare_revenue
    base_medical_cost = 4000 if bps_scale <= 15 else 7000

    for i in range(0, 6):
        timeline.append(f"Age {current_age + i}")
        if i > 0: temp_pension += (temp_pension * 0.10)
        pension_trend.append(temp_pension)
        medical_trend.append(base_medical_cost * ((1.12) ** i))

    # Real-Time Trends Chart Module
    st.markdown("<br>### 📈 5-Year Growth Trends Vectors", unsafe_allow_html=True)
    chart_df = pd.DataFrame({
        "Timeline": timeline,
        "Welfare Pension Trend": pension_trend,
        "Healthcare Expense Trend": medical_trend
    })
    st.line_chart(chart_df.set_index("Timeline"))

    # 100% VISIBLE SOLID CUSTOM TABLE (Guaranteed to fix the blank/invisible text issue)
    st.markdown("### 📊 Forecasted Compounding Matrix")
    
    html_table = """
    <div style='overflow-x:auto; margin-top:10px;'>
    <table style='width:100%; border-collapse: collapse; background-color: #ffffff !important; border-radius: 12px; overflow: hidden; border: 1px solid #cbd5e1;'>
        <tr style='background-color: #006643 !important; text-align: left;'>
            <th style='color: #ffffff !important; padding: 12px; font-weight:600;'>Timeline Horizon</th>
            <th style='color: #ffffff !important; padding: 12px; font-weight:600;'>Forecasted Pension</th>
            <th style='color: #ffffff !important; padding: 12px; font-weight:600;'>Healthcare Index</th>
        </tr>
    """
    for i in range(1, 6):
        row_bg = "#ffffff" if i % 2 == 0 else "#f8fafc"
        html_table += f"""
        <tr style='background-color: {row_bg} !important; border-bottom: 1px solid #e2e8f0;'>
            <td style='padding: 12px; color: #0f172a !important; font-weight: 500;'>Year {i} (Age {current_age + i})</td>
            <td style='padding: 12px; color: #006643 !important; font-weight: 700;'>PKR {pension_trend[i]:,.2f}</td>
            <td style='padding: 12px; color: #dc2626 !important; font-weight: 500;'>PKR {medical_trend[i]:,.2f}</td>
        </tr>
        """
    html_table += "</table></div>"
    st.markdown(html_table, unsafe_allow_html=True)
    
