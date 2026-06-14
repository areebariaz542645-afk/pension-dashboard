import streamlit as st
import pandas as pd

# Page setup for premium Healthcare Fintech experience
st.set_page_config(page_title="Health Dept Welfare Portal", page_icon="🩺", layout="centered")

# --- ADVANCED MEDICAL-TEAL & SLATE FINTECH CSS ---
st.markdown("""
<style>
    /* Clean App Canvas Background */
    .stApp { background-color: #f8fafc; }
    
    /* Strict removal of default streamlit header lines */
    header { visibility: hidden; }
    
    /* Premium Health Container Wrapper */
    .clean-container {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 18px;
        box-shadow: 0 10px 25px rgba(13, 148, 136, 0.03);
        border: 1px solid #e2e8f0;
        margin-bottom: 25px;
    }
    
    /* Healthcare Teal Premium Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #0d9488 0%, #115e59 100%) !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        border: none !important;
        height: 48px;
        font-weight: 600;
        font-size: 16px;
        width: 100%;
        box-shadow: 0 4px 12px rgba(13, 148, 136, 0.2);
    }
    
    /* Medical Verified Identity Badge */
    .profile-card {
        background-color: #ffffff;
        padding: 15px 20px;
        border-radius: 14px;
        border-left: 5px solid #0d9488;
        box-shadow: 0 2px 8px rgba(0,0,0,0.02);
        margin-bottom: 25px;
    }
    
    /* Digital Wallet Balance Component (Teal-Green Premium Gradient) */
    .digital-wallet {
        background: linear-gradient(135deg, #0f172a 0%, #0d9488 100%);
        color: #ffffff;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(13, 148, 136, 0.15);
        margin-bottom: 30px;
    }
    
    /* Grid Feature Display Blocks (Clean Medical Cards Layout) */
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

# --- SECURE SESSION CONTROLLER ---
if 'is_unlocked' not in st.session_state:
    st.session_state['is_unlocked'] = False
if 'user_data' not in st.session_state:
    st.session_state['user_data'] = {"name": "", "email": ""}

# --- SCREEN 1: STRICT SECURE SIGN-IN (Direct Medical Shield) ---
if not st.session_state['is_unlocked']:
    st.markdown("<div style='max-width: 500px; margin: 0 auto;'>", unsafe_allow_html=True)
    st.markdown("<div class='clean-container' style='margin-top: 40px;'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #0f172a; font-weight: 700; margin-bottom: 5px;'>Health Department Secure Portal</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b; font-size: 14px; margin-bottom: 25px;'>Authentication required to access encrypted pension telemetry.</p>", unsafe_allow_html=True)
    
    # Clean Medical Portal Login Illustration
    st.image("https://img.freepik.com/free-vector/doctor-character-background_1270-84.jpg", width=280)
    
    st.markdown("<br>", unsafe_allow_html=True)
    u_name = st.text_input("Officer Full Name", placeholder="e.g., Dr. Alina Khan")
    u_email = st.text_input("Registered Departmental Email", placeholder="alina@health.gov.pk")
    u_pin = st.text_input("Secure Vault Access PIN", type="password", placeholder="••••••••")
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Authorize & Secure Sign In"):
        if u_name and u_email and u_pin:
            st.session_state['is_unlocked'] = True
            st.session_state['user_data']['name'] = u_name
            st.session_state['user_data']['email'] = u_email
            st.rerun()
        else:
            st.error("🔒 Access Denied: Please fill out all departmental fields.")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- SCREEN 2: MEDICAL WELFARE ANALYTICS DASHBOARD (UNLOCKED) ---
else:
    # Navigation Title & Sign-Out Trigger
    col_nav, col_btn = st.columns([4, 1])
    with col_nav:
        st.markdown("<h2 style='color: #0f172a; font-weight: 700; margin: 0;'>🩺 Health Dept. Analytics</h2>", unsafe_allow_html=True)
    with col_btn:
        if st.button("Sign Out"):
            st.session_state['is_unlocked'] = False
            st.rerun()
            
    st.markdown("<hr style='margin: 15px 0 25px 0; border: 0; border-top: 1px solid #e2e8f0;'>", unsafe_allow_html=True)

    # 1. Verified Profile Identity Badge Box
    st.markdown(f"""
    <div class='profile-card'>
        <p style='margin:0; color:#0d9488; font-size:11px; font-weight:600; letter-spacing:0.5px;'>🛡️ HEALTH DEPARTMENT VERIFIED GATEWAY</p>
        <p style='margin:5px 0 0 0; font-weight:700; color:#0f172a;'>Officer: {st.session_state['user_data']['name']}</p>
        <p style='margin:2px 0 0 0; color:#64748b; font-size:13px;'>Gov Email: {st.session_state['user_data']['email']}</p>
    </div>
    """, unsafe_allow_html=True)

    # 2. Premium Medical Vector Illustration
    st.image("https://img.freepik.com/free-vector/medical-video-consultation-concept-illustration_114360-5025.jpg", use_container_width=True)

    # 3. Clean Parameter Calibration Panel
    st.markdown("<div class='clean-container'>", unsafe_allow_html=True)
    st.markdown("<p style='color: #0f172a; font-weight: 600; margin-top: 0;'>⚙️ Actuarial Parameter Calibration</p>", unsafe_allow_html=True)
    col_in1, col_in2 = st.columns(2)
    with col_in1:
        basic_pay = st.number_input("Last Basic Pay Matrix (PKR)", min_value=10000, value=85000, step=5000)
        service_years = st.slider("Total Audited Service Tenure (Years)", min_value=10, max_value=40, value=32)
    with col_in2:
        bps_scale = st.selectbox("Verified BPS Scale / Grade", list(range(1, 23)), index=16)
        current_age = st.slider("Active Retirement Age Parameter", min_value=60, max_value=85, value=60)
    st.markdown("</div>", unsafe_allow_html=True)

    # Math Logic Engine Formulas
    calculated_years = 30 if service_years > 30 else service_years
    gross_pension = (basic_pay * calculated_years * 7) / 300
    net_monthly_base = gross_pension * 0.65
    medical_allowance = 1500 if bps_scale <= 15 else 2500
    adhoc_relief = net_monthly_base * 0.15
    total_revenue = net_monthly_base + medical_allowance + adhoc_relief

    st.markdown("<br>", unsafe_allow_html=True)

    # 4. Premium Digital Wallet Header (Teal-Green & Slate Gradient Theme)
    st.markdown(f"""
    <div class='digital-wallet'>
        <p style='margin:0; font-size:13px; font-weight: 500; opacity:0.9; letter-spacing: 0.5px;'>🟢 NET UNLOCKED MONTHLY HEALTH WELFARE DISBURSEMENT</p>
        <h1 style='margin:10px 0; font-size:42px; font-weight:700; letter-spacing: -0.5px;'>Rs. {total_revenue:,.2f}</h1>
        <p style='margin:0; font-size:12px; opacity:0.8;'>🔒 Certified under Government Health Ordinance Regulations</p>
    </div>
    """, unsafe_allow_html=True)

    # 5. Icon Feature Analytics Matrix Grids (Teal Compliant)
    st.markdown("### 📱 Active Benefit Feature Matrix")
    col_f1, col_f2, col_f3 = st.columns(3)
    with col_f1:
        st.markdown(f"""
        <div class='icon-grid-card'>
            <span style='font-size:32px;'>💰</span>
            <p style='margin:8px 0 4px 0; color:#64748b; font-size:12px; font-weight:500;'>Net Pension Base</p>
            <h4 style='margin:0; color:#0f172a; font-weight:700;'>Rs. {net_monthly_base:,.0f}</h4>
        </div>
        """, unsafe_allow_html=True)
    with col_f2:
        st.markdown(f"""
        <div class='icon-grid-card'>
            <span style='font-size:32px;'>🩺</span>
            <p style='margin:8px 0 4px 0; color:#64748b; font-size:12px; font-weight:500;'>Medical Care Fund</p>
            <h4 style='margin:0; color:#0f172a; font-weight:700;'>Rs. {medical_allowance:,.0f}</h4>
        </div>
        """, unsafe_allow_html=True)
    with col_f3:
        st.markdown(f"""
        <div class='icon-grid-card'>
            <span style='font-size:32px;'>⚡</span>
            <p style='margin:8px 0 4px 0; color:#64748b; font-size:12px; font-weight:500;'>Adhoc Relief Fund</p>
            <h4 style='margin:0; color:#0f172a; font-weight:700;'>Rs. {adhoc_relief:,.0f}</h4>
        </div>
        """, unsafe_allow_html=True)

    # Data Calculation for Future 5 Years Chart & Table
    timeline, pension_trend, medical_trend = [], [], []
    temp_pension = total_revenue
    base_medical_cost = 4000 if bps_scale <= 15 else 7000

    for i in range(0, 6):
        timeline.append(f"Age {current_age + i}")
        if i > 0: temp_pension += (temp_pension * 0.10)
        pension_trend.append(temp_pension)
        medical_trend.append(base_medical_cost * ((1.12) ** i))

    # 6. Interactive Dual Line Growth Vector Chart
    st.markdown("<br>### 📈 Actuarial Assets Growth Vector & Health Inflation Trends", unsafe_allow_html=True)
    chart_data = pd.DataFrame({
        "Timeline": timeline,
        "Total Pension Asset": pension_trend,
        "Healthcare Expense Trend": medical_trend
    })
    st.line_chart(chart_data.set_index("Timeline"))

    # 7. Detailed Future 5-Year Data Forecasting Matrix Table
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
        
