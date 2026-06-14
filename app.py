import streamlit as st
import pandas as pd
import base64

# Strict page config for modern dashboard rendering
st.set_page_config(page_title="Welfare Pension Portal", page_icon="🩺", layout="centered")

# --- CLEAN PERSISTENT LIGHT THEME FORCE MATRIX ---
# Completely eliminates system-generated black tabs, borders, and input boxes
st.markdown("""
<style>
    /* Force main container to pure light grey/white background */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #f8fafc !important;
    }
    
    /* Strict global typography override - stops text and headings from whiteout/blackout glitches */
    h1, h2, h3, h4, h5, h6, p, span, label, div, td, th {
        color: #0f172a !important;
        font-family: 'Segoe UI', system-ui, sans-serif !important;
    }
    
    /* Clean custom white card input panel - removes raw system black containers */
    .clean-card {
        background-color: #ffffff !important;
        padding: 22px;
        border-radius: 16px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.03);
        margin-bottom: 20px;
    }
    
    /* Premium Easypaisa Identity Green Wallet Card (Color-Locked) */
    .easypaisa-wallet {
        background: linear-gradient(135deg, #006643 0%, #004d32 100%) !important;
        padding: 24px;
        border-radius: 20px;
        box-shadow: 0 8px 24px rgba(0, 102, 67, 0.15);
        margin-top: 10px;
        margin-bottom: 25px;
    }
    .easypaisa-wallet h1, .easypaisa-wallet p {
        color: #ffffff !important; /* Kept crystal white inside green layout */
    }
    
    /* Grid Box Elements for mini features */
    .mini-grid-box {
        background-color: #ffffff !important;
        padding: 14px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        text-align: center;
    }
    
    /* Input and Select Field Strict Overrides (Removes native dark grey focus frames) */
    div[data-baseweb="input"] input, div[data-baseweb="select"] {
        background-color: #ffffff !important;
        color: #0f172a !important;
        border-radius: 8px !important;
    }
    
    /* Completely flattens and styles buttons to prevent strange dark shadow fragments */
    button, .stButton>button {
        background-color: #006643 !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        padding: 10px 20px !important;
    }
    
    /* Specific styling rule to clear black text/background on tables */
    [data-testid="stDataFrame"] * {
        color: #0f172a !important;
    }
    
    /* Hides redundant decoration lines and status trackers */
    header { visibility: hidden !important; }
    footer { visibility: hidden !important; }
    .stDeployButton { display: none !important; }
</style>
""", unsafe_allow_html=True)

# --- EMBEDDED DESIGN ILLUSTRATION ENGINES ---
signup_graphic = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%">
    <rect width="800" height="450" rx="16" fill="#e2e8f0"/>
    <circle cx="400" cy="225" r="140" fill="#ffffff" opacity="0.7"/>
    <path d="M400,110 C450,110 500,90 500,90 C500,220 400,340 400,340 C400,340 300,220 300,90 C300,90 350,110 400,110 Z" fill="#006643" />
    <path d="M375,190 H425 V225 H375 Z M392,175 H408 V240 H392 Z" fill="#ffffff"/>
    <text x="400" y="395" font-family="'Segoe UI', sans-serif" font-size="24" font-weight="bold" fill="#006643" text-anchor="middle">MEDICAL RETIREMENT PORTAL</text>
</svg>
"""

dashboard_graphic = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 260" width="100%">
    <rect width="800" height="260" rx="16" fill="#ffffff" stroke="#e2e8f0" stroke-width="2"/>
    <path d="M200,180 L350,130 L500,110 L650,60" fill="none" stroke="#006643" stroke-width="6" stroke-linecap="round"/>
    <circle cx="650" cy="60" r="12" fill="#00a86b"/>
    <text x="400" y="220" font-family="'Segoe UI', sans-serif" font-size="20" font-weight="bold" fill="#0f172a" text-anchor="middle">ACTIVE TELEMETRY REALTIME GRID</text>
</svg>
"""

def get_svg_display(svg_string):
    b64 = base64.b64encode(svg_string.encode('utf-8')).decode("utf-8")
    return f'<img src="data:image/svg+xml;base64,{b64}" style="width:100%; border-radius:16px; margin-bottom:20px;"/>'

# --- SECURITY APP ROUTER ---
if 'unlocked' not in st.session_state:
    st.session_state['unlocked'] = False
if 'user' not in st.session_state:
    st.session_state['user'] = {"name": "", "email": ""}

# --- SCREEN 1: WELFARE SIGNUP PORTAL ---
if not st.session_state['unlocked']:
    st.markdown("<div style='max-width: 440px; margin: 0 auto;'>", unsafe_allow_html=True)
    
    st.markdown(get_svg_display(signup_graphic), unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; font-weight: 700; margin-top:0;'>Welfare Signup</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 13px; margin-bottom: 20px; color:#64748b !important;'>Securely access active welfare asset telemetry parameters.</p>", unsafe_allow_html=True)
    
    # Text Inputs wrapped inside a single clean layout block
    st.markdown("<div class='clean-card'>", unsafe_allow_html=True)
    s_name = st.text_input("Full Name*", placeholder="Md.Sourav")
    s_email = st.text_input("Email*", placeholder="test@gmail.com")
    s_pin = st.text_input("Password*", type="password", placeholder="**********")
    st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("Sign Up", use_container_width=True):
        if s_name and s_email and s_pin:
            st.session_state['unlocked'] = True
            st.session_state['user']['name'] = s_name
            st.session_state['user']['email'] = s_email
            st.rerun()
        else:
            st.error("🔒 Please complete all mandatory credential configurations.")
            
    st.markdown("</div>", unsafe_allow_html=True)

# --- SCREEN 2: ACTIVE DYNAMIC DASHBOARD ---
else:
    col_nav_title, col_nav_btn = st.columns([3, 1])
    with col_nav_title:
        st.markdown("<h2 style='font-weight: 800; margin: 0;'>🩺 Pension Dashboard</h2>", unsafe_allow_html=True)
    with col_nav_btn:
        if st.button("Sign Out", use_container_width=True):
            st.session_state['unlocked'] = False
            st.rerun()
            
    st.markdown("<hr style='margin: 15px 0; border-top: 1px solid #e2e8f0;'>", unsafe_allow_html=True)
    st.markdown(get_svg_display(dashboard_graphic), unsafe_allow_html=True)

    # Authorized Status Alert Segment
    st.markdown(f"""
    <div style='background-color: #f1f5f9; padding: 12px 16px; border-radius: 12px; border-left: 5px solid #006643; margin-bottom: 20px;'>
        <p style='margin:0; font-size:11px; font-weight:700; color:#006643 !important; letter-spacing:0.5px;'>🛡️ VERIFIED GOVERNMENT RETIREMENT CREDENTIALS</p>
        <p style='margin:4px 0 0 0; font-weight:700; font-size:14px;'>Officer: {st.session_state['user']['name']} | Gateway: {st.session_state['user']['email']}</p>
    </div>
    """, unsafe_allow_html=True)

    # Actuarial Calculations Setup Form
    st.markdown("<div class='clean-card'>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight: 700; margin:0 0 12px 0; color:#006643;'>⚙️ Actuarial Parameters Matrix</p>", unsafe_allow_html=True)
    
    pay_input = st.number_input("Last Basic Pay Matrix (PKR)", min_value=10000, value=85000, step=5000)
    tenure_input = st.slider("Service Scale (Years)", min_value=10, max_value=40, value=25)
    
    col_cell1, col_cell2 = st.columns(2)
    with col_cell1:
        bps_input = st.selectbox("BPS Cadre Scale / Grade", list(range(1, 23)), index=16)
    with col_cell2:
        age_input = st.slider("Active Retirement Age", min_value=60, max_value=85, value=62)
    st.markdown("</div>", unsafe_allow_html=True)

    # Core Math Engine
    adjusted_tenure = 30 if tenure_input > 30 else tenure_input
    gross_pension_val = (pay_input * adjusted_tenure * 7) / 300
    net_pension_val = gross_pension_val * 0.65
    medical_pension_val = 1500 if bps_input <= 15 else 2500
    adhoc_pension_val = net_pension_val * 0.15
    total_welfare_revenue = net_pension_val + medical_pension_val + adhoc_pension_val

    # COLOR LOCKED EASYPAISA SMART CARD INTERFACE
    st.markdown(f"""
    <div class='easypaisa-wallet'>
        <p style='margin:0; font-size:11px; font-weight: 500; opacity:0.9; letter-spacing:0.5px;'>🟢 AVAILABLE MONTHLY WELFARE BALANCE</p>
        <h1 style='margin:6px 0; font-size:36px; font-weight:700;'>Rs. {total_welfare_revenue:,.2f}</h1>
        <p style='margin:0; font-size:11px; opacity:0.8;'>✓ Account Channel Secure Connection Active</p>
    </div>
    """, unsafe_allow_html=True)

    # Triple Matrix Metric Feature Grid
    st.markdown("### 📱 Active Benefit Feature Matrix")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"<div class='mini-grid-box'><p style='margin:0; font-size:11px; color:#64748b;'>Net Pension</p><h4 style='margin:4px 0 0 0; font-weight:700; color:#006643;'>Rs. {net_pension_val:,.0f}</h4></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='mini-grid-box'><p style='margin:0; font-size:11px; color:#64748b;'>Medical Care</p><h4 style='margin:4px 0 0 0; font-weight:700; color:#006643;'>Rs. {medical_pension_val:,.0f}</h4></div>", unsafe_allow_html=True)
    with c3:
        st.markdown(f"<div class='mini-grid-box'><p style='margin:0; font-size:11px; color:#64748b;'>Adhoc Relief</p><h4 style='margin:4px 0 0 0; font-weight:700; color:#006643;'>Rs. {adhoc_pension_val:,.0f}</h4></div>", unsafe_allow_html=True)

    # Compounding Array Generators
    timeline_axes, data_pension_array, data_medical_array = [], [], []
    rolling_sum = total_welfare_revenue
    initial_med_index = 4000 if bps_input <= 15 else 7000

    for index in range(0, 6):
        timeline_axes.append(f"Age {age_input + index}")
        if index > 0: 
            rolling_sum += (rolling_sum * 0.10)
        data_pension_array.append(rolling_sum)
        data_medical_array.append(initial_med_index * ((1.12) ** index))

    # Real-Time Trends Charts
    st.markdown("<br>### 📈 5-Year Actuarial Growth Vector Lines", unsafe_allow_html=True)
    chart_dataframe = pd.DataFrame({
        "Total Pension Asset": data_pension_array,
        "Healthcare Expense Trend": data_medical_array
    }, index=timeline_axes)
    st.line_chart(chart_dataframe)

    # Clean DataFrame Grid Forecast Matrix
    st.markdown("### 📊 Forecasted Compounding Matrix Table")
    display_matrix_df = pd.DataFrame({
        "Timeline Horizon": [f"Year {step} (Age {age_input + step})" for step in range(1, 6)],
        "Forecasted Pension": [f"PKR {data_pension_array[step]:,.2f}" for step in range(1, 6)],
        "Medical Cost Index": [f"PKR {data_medical_array[step]:,.2f}" for step in range(1, 6)]
    })
    st.dataframe(display_matrix_df, use_container_width=True, hide_index=True)
    
