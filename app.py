import streamlit as st
import pandas as pd

# Page Configuration for Premium Mobile-Responsive View
st.set_page_config(page_title="Health Welfare Portal", page_icon="🩺", layout="centered")

# --- CUSTOM ULTRA-PREMIUM MEDICAL & EASYPAISA GREEN THEME ---
st.markdown("""
<style>
    /* Clean Mobile App Canvas Background */
    .stApp { background-color: #f4f7f6; }
    
    /* Hide Default Streamlit Layout Elements */
    header { visibility: hidden; }
    .stDeployButton { display: none !important; }
    footer { visibility: hidden; }
    
    /* Uniform Form Wrapper */
    .clean-container {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.02);
        border: 1px solid #e2e8f0;
        margin-bottom: 20px;
    }

    /* Strict Authentication Shield Layout */
    .login-box {
        background-color: #ffffff;
        padding: 35px;
        border-radius: 24px;
        box-shadow: 0 10px 30px rgba(0, 102, 67, 0.05);
        border: 1px solid #e6f0ec;
        text-align: center;
        margin-top: 30px;
    }
    
    /* Easypaisa Premium Green Action Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #006643 0%, #004d32 100%) !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        border: none !important;
        height: 50px;
        font-weight: 600;
        font-size: 16px;
        width: 100%;
        box-shadow: 0 4px 15px rgba(0, 102, 67, 0.2);
    }
    
    /* Verified Medical Identity Shield Badge */
    .profile-card {
        background-color: #ffffff;
        padding: 15px 20px;
        border-radius: 14px;
        border-left: 5px solid #006643;
        box-shadow: 0 2px 8px rgba(0,0,0,0.01);
        margin-bottom: 25px;
    }
    
    /* THE EXACT EASYPAISA WALLET CARD COMPONENT */
    .easypaisa-card {
        background: linear-gradient(135deg, #006643 0%, #024f35 100%);
        color: #ffffff;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0, 102, 67, 0.15);
        margin-bottom: 25px;
    }
    
    /* Pure CSS Decorative Medical Icon Vector */
    .medical-shield-logo {
        font-size: 65px;
        background: #e6f0ec;
        width: 110px;
        height: 110px;
        line-height: 110px;
        border-radius: 50%;
        margin: 0 auto 20px auto;
        color: #006643;
    }
    
    /* Grid Analytics Cards (Inspired by Replit layout inside your screenshots) */
    .grid-asset-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.01);
        border: 1px solid #edf2f7;
    }
</style>
""", unsafe_allow_html=True)

# --- ENGINE SESSION ACCESS CONTROLLER ---
if 'is_unlocked' not in st.session_state:
    st.session_state['is_unlocked'] = False
if 'user_data' not in st.session_state:
    st.session_state['user_data'] = {"name": "", "email": ""}

# --- SCREEN 1: LOCKED SIGN-IN PORTAL (Direct & Clean Shield Form) ---
if not st.session_state['is_unlocked']:
    st.markdown("<div style='max-width: 460px; margin: 0 auto;'>", unsafe_allow_html=True)
    st.markdown("<div class='login-box'>", unsafe_allow_html=True)
    
    # 100% Reliable Code Vector (No broken web URLs)
    st.markdown("<div class='medical-shield-logo'>🩺</div>", unsafe_allow_html=True)
    
    st.markdown("<h2 style='color: #0f172a; font-weight: 700; margin: 0 0 5px 0;'>Health Portal Secure Access</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748b; font-size: 13px; margin-bottom: 25px;'>Enter credentials to access active retirement telemetry asset modules.</p>", unsafe_allow_html=True)
    
    # Secure Inputs Layout
    u_name = st.text_input("Officer Full Name", placeholder="e.g., Dr. Alina Khan")
    u_email = st.text_input("Registered Departmental Email", placeholder="username@health.gov.pk")
    u_pin = st.text_input("Secure Vault Access PIN", type="password", placeholder="••••••••")
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Authorize & Sign In"):
        if u_name and u_email and u_pin:
            st.session_state['is_unlocked'] = True
            st.session_state['user_data']['name'] = u_name
            st.session_state['user_data']['email'] = u_email
            st.rerun()
        else:
            st.error("🔒 Access Denied: All validation attributes must be completed.")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- SCREEN 2: DYNAMIC HEALTH WELFARE ANALYTICS DASHBOARD ---
else:
    # Action Navbar Grid Layout
    col_nav, col_btn = st.columns([4, 1])
    with col_nav:
        st.markdown("<h2 style='color: #0f172a; font-weight: 700; margin: 0;'>🩺 Department Dashboard</h2>", unsafe_allow_html=True)
    with col_btn:
        if st.button("Sign Out"):
            st.session_state['is_unlocked'] = False
            st.rerun()
            
    st.markdown("<hr style='margin: 15px 0 25px 0; border: 0; border-top: 1px solid #e2e8f0;'>", unsafe_allow_html=True)

    # 1. Department Verified Profile Shield Badge
    st.markdown(f"""
    <div class='profile-card'>
        <p style='margin:0; color:#006643; font-size:11px; font-weight:600; letter-spacing:0.5px;'>🛡️ GOVERNMENT WELFARE DEPT VALIDATED TOKEN</p>
        <p style='margin:4px 0 0 0; font-weight:700; color:#0f172a;'>Officer identity: {st.session_state['user_data']['name']}</p>
        <p style='margin:2px 0 0 0; color:#64748b; font-size:12px;'>Gateway Address: {st.session_state['user_data']['email']}</p>
    </div>
    """, unsafe_allow_html=True)

    # 2. Tuning Control Panel Container Block
    st.markdown("<div class='clean-container'>", unsafe_allow_html=True)
    st.markdown("<p style='color: #006643; font-weight: 600; margin: 0 0 15px 0;'>⚙️ Parameter Configuration Grid</p>", unsafe_allow_html=True)
    col_in1, col_in2 = st.columns(2)
    with col_in1:
        basic_pay = st.number_input("Last Basic Pay Matrix (PKR)", min_value=10000, value=85000, step=5000)
        service_years = st.slider("Total Audited Service Tenure (Years)", min_value=10, max_value=40, value=32)
    with col_in2:
        bps_scale = st.selectbox("Verified BPS Scale / Grade", list(range(1, 23)), index=16)
        current_age = st.slider("Active Retirement Age Parameter", min_value=60, max_value=85, value=60)
    st.markdown("</div>", unsafe_allow_html=True)

    # Internal Core Business Engine Matrix Calculations
    calculated_years = 30 if service_years > 30 else service_years
    gross_pension = (basic_pay * calculated_years * 7) / 300
    net_monthly_base = gross_pension * 0.65
    medical_allowance = 1500 if bps_scale <= 15 else 2500
    adhoc_relief = net_monthly_base * 0.15
    total_revenue = net_monthly_base + medical_allowance + adhoc_relief

    # 3. THE LIVE PREMIUM WALLET DISPLAY (Exact UI Matching to your uploaded screenshot)
    st.markdown(f"""
    <div class='easypaisa-card'>
        <p style='margin:0; font-size:12px; font-weight: 500; opacity:0.9; letter-spacing: 0.5px;'>🟢 AVAILABLE MONTHLY WELFARE BALANCE</p>
        <h1 style='margin:8px 0; font-size:38px; font-weight:700; letter-spacing: -0.5px;'>Rs. {total_revenue:,.2f}</h1>
        <p style='margin:0; font-size:11px; opacity:0.8;'>✓ Active Bank-Grade Welfare Account Distribution Pipeline Unlocked</p>
    </div>
    """, unsafe_allow_html=True)

    # 4. Clean Feature Grid Display Matrix with Proper Medical/Finance Icons 
    st.markdown("### 📱 Active Benefit Feature Matrix")
    col_f1, col_f2, col_f3 = st.columns(3)
    with col_f1:
        st.markdown(f"""
        <div class='grid-asset-card'>
            <span style='font-size:30px;'>💰</span>
            <p style='margin:6px 0 2px 0; color:#64748b; font-size:12px; font-weight:500;'>Net Pension</p>
            <h5 style='margin:0; color:#0f172a; font-weight:700;'>Rs. {net_monthly_base:,.0f}</h5>
        </div>
        """, unsafe_allow_html=True)
    with col_f2:
        st.markdown(f"""
        <div class='grid-asset-card'>
            <span style='font-size:30px;'>🏥</span>
            <p style='margin:6px 0 2px 0; color:#64748b; font-size:12px; font-weight:500;'>Medical Fund</p>
            <h5 style='margin:0; color:#0f172a; font-weight:700;'>Rs. {medical_allowance:,.0f}</h5>
        </div>
        """, unsafe_allow_html=True)
    with col_f3:
        st.markdown(f"""
        <div class='grid-asset-card'>
            <span style='font-size:30px;'>⚡</span>
            <p style='margin:6px 0 2px 0; color:#64748b; font-size:12px; font-weight:500;'>Adhoc Relief</p>
            <h5 style='margin:0; color:#0f172a; font-weight:700;'>Rs. {adhoc_relief:,.0f}</h5>
        </div>
        """, unsafe_allow_html=True)

    # Data Calculation for 5-Year Trends Metrics
    timeline, pension_trend, medical_trend = [], [], []
    temp_pension = total_revenue
    base_medical_cost = 4000 if bps_scale <= 15 else 7000

    for i in range(0, 6):
        timeline.append(f"Age {current_age + i}")
        if i > 0: temp_pension += (temp_pension * 0.10)
        pension_trend.append(temp_pension)
        medical_trend.append(base_medical_cost * ((1.12) ** i))

    # 5. Real-Time Interactive Trends Graph Chart
    st.markdown("<br>### 📈 Actuarial Assets Growth Vector & Health Inflation Trends", unsafe_allow_html=True)
    chart_data = pd.DataFrame({
        "Timeline": timeline,
        "Total Pension Asset": pension_trend,
        "Healthcare Expense Trend": medical_trend
    })
    st.line_chart(chart_data.set_index("Timeline"))

    # 6. Detailed Numeric Future 5-Year Matrix Table (Perfect Alignment Grid)
    st.markdown("### 📊 Forecasted Future 5-Year Pension Compounding Matrix")
    matrix_data = []
    for i in range(1, 6):
        matrix_data.append({
            "Timeline Horizon": f"Year {i} (Age {current_age + i})",
            "Forecasted Monthly Pension": f"PKR {pension_trend[i]:,.2f}",
            "Estimated Healthcare Cost": f"PKR {medical_trend[i]:,.2f}",
            "Net Liquid Surplus Account": f"PKR {(pension_trend[i] - medical_trend[i]):,.2f}"
        })
    st.table(matrix_data)
    
