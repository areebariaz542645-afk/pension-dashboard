import streamlit as st
import collections
import random

# Core Page Setup optimized for mobile app view
st.set_page_config(page_title="Cyber-Hunt: Endless AI", layout="centered", initial_sidebar_state="collapsed")

# Advanced Cyberpunk UI Stylesheet
st.markdown("""
    <style>
    body { background-color: #05050a; color: #a9b7c6; font-family: 'Courier New', Courier, monospace; }
    .block-container { padding-top: 0.5rem !important; max-width: 440px !important; margin: auto; }
    
    /* Main Cinematic Arcade Header */
    .arcade-title {
        text-align: center;
        background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        font-size: 34px;
        letter-spacing: 3px;
        margin-bottom: 0px;
        text-shadow: 0 0 20px rgba(0, 242, 254, 0.6);
    }
    
    /* Live Stats Dashboard Dashboard (HUD) */
    .hud-container {
        display: flex;
        justify-content: space-between;
        background: #0d0e15;
        border: 1px solid #1f4068;
        border-radius: 12px;
        padding: 8px 15px;
        margin-bottom: 12px;
        box-shadow: inset 0 0 10px rgba(0,255,245,0.1);
    }
    .hud-stat { font-size: 13px; font-weight: bold; color: #00fff5; }
    .hud-val { color: #ffffff; font-size: 14px; }

    /* Tactical Combat Grid Frame */
    .matrix-frame {
        display: flex;
        flex-direction: column;
        align-items: center;
        background: radial-gradient(circle, #100c24 0%, #05020f 100%);
        border: 2px solid #4facfe;
        border-radius: 20px;
        padding: 14px;
        box-shadow: 0 0 35px rgba(79, 172, 254, 0.35);
        margin-bottom: 12px;
    }
    .matrix-row { display: flex; justify-content: center; }
    .matrix-cell {
        width: 44px; height: 44px; margin: 3px; border-radius: 10px;
        background: rgba(26, 26, 46, 0.8); border: 1px solid #1f4068;
        display: flex; align-items: center; justify-content: center;
        transition: all 0.15s ease-in-out;
    }
    
    /* High-Attraction Animated Neon Entity Node Glows */
    .node-player { background: #00fff5; border: 2px solid #ffffff; box-shadow: 0 0 18px #00fff5, inset 0 0 8px rgba(0,0,0,0.3); }
    .node-monster { background: #ff0055; border: 2px solid #ffffff; box-shadow: 0 0 18px #ff0055, inset 0 0 8px rgba(0,0,0,0.3); }
    .node-target { background: #ffcc00; border: 2px solid #ffffff; box-shadow: 0 0 18px #ffcc00, inset 0 0 8px rgba(0,0,0,0.3); }
    .node-wall { background: #22252a; border: 1px solid #3a3f47; box-shadow: inset 0 0 5px rgba(0,0,0,0.8); }
    
    .sprite-icon { font-size: 22px; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.5)); }

    /* Compact Integrated Mobile Controller Overlay */
    .dpad-container { background: #0d0e15; border: 1px solid #1f4068; border-radius: 18px; padding: 10px; }
    .btn-core button {
        width: 100% !important; height: 45px !important;
        background: linear-gradient(135deg, #1f4068, #0d0e15) !important;
        color: #00fff5 !important; border: 1px solid #00fff5 !important;
        font-weight: bold !important; font-size: 20px !important; border-radius: 10px !important;
        box-shadow: 0 0 8px rgba(0,255,245,0.15) !important;
    }
    
    /* System Command Layout */
    .btn-sys button {
        background: linear-gradient(135deg, #ff0055, #95103c) !important; color: #fff !important;
        font-weight: bold !important; border-radius: 10px !important; border: none !important;
        box-shadow: 0 4px 12px rgba(255,0,85,0.2) !important;
    }
    .btn-next button {
        background: linear-gradient(135deg, #00ff66, #009944) !important; color: #000 !important;
        font-weight: 900 !important; border-radius: 10px !important; border: none !important;
        box-shadow: 0 4px 12px rgba(0,255,102,0.3) !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='arcade-title'>CYBER-HUNT</h1>", unsafe_allow_html=True)

# 1. High-Performance AI Core Engine (BFS)
def calculate_ai_route(monster, player, grid_size, walls):
    queue = collections.deque([[monster]])
    visited = {monster} | set(walls)
    while queue:
        path = queue.popleft()
        r, c = path[-1]
        if (r, c) == player:
            return path[1] if len(path) > 1 else monster
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < grid_size and 0 <= nc < grid_size and (nr, nc) not in visited:
                queue.append(path + [(nr, nc)])
                visited.add((nr, nc))
    return monster

# 2. State Controller for Procedural Generation & High Scores
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.high_score = 0
    st.session_state.streak = 0

def build_procedural_map():
    # Dynamic difficulty mechanics based on current session score
    st.session_state.grid_size = 5 if st.session_state.score < 5 else 6
    g_size = st.session_state.grid_size
    
    st.session_state.player = (0, 0)
    st.session_state.monster = (g_size - 1, g_size - 1)
    
    # Generate unpredictable target destinations
    st.session_state.treasure = (random.randint(1, g_size-2), random.randint(1, g_size-2))
    
    # Calculate obstacle wall density based on score scaling
    st.session_state.walls = []
    num_walls = min(st.session_state.score + 1, 4) if g_size == 5 else min(st.session_state.score, 6)
    
    while len(st.session_state.walls) < num_walls:
        w = (random.randint(0, g_size-1), random.randint(0, g_size-1))
        if w not in [st.session_state.player, st.session_state.monster, st.session_state.treasure]:
            st.session_state.walls.append(w)
            
    st.session_state.moves = 0
    st.session_state.game_state = "LIVE" # LIVE, WASTED, STAGE_CLEAR

if 'game_state' not in st.session_state:
    build_procedural_map()

def trigger_game_over():
    st.session_state.game_state = "WASTED"
    if st.session_state.score > st.session_state.high_score:
        st.session_state.high_score = st.session_state.score
    st.session_state.streak = 0

def step_engine(dr, dc):
    if st.session_state.game_state != "LIVE":
        return
        
    g_size = st.session_state.grid_size
    r, c = st.session_state.player
    nr, nc = r + dr, c + dc
    
    if 0 <= nr < g_size and 0 <= nc < g_size and (nr, nc) not in st.session_state.walls:
        st.session_state.player = (nr, nc)
        st.session_state.moves += 1
        
        # Victory check
        if st.session_state.player == st.session_state.treasure:
            st.session_state.score += 1
            st.session_state.streak += 1
            st.session_state.game_state = "STAGE_CLEAR"
            return
            
        # Dynamic AI Scaling Intelligence Loop
        monster_ticks = True
        # On early scores, AI exhibits occasional calculation latency (slow mode)
        if st.session_state.score < 3 and st.session_state.moves % 3 == 0:
            monster_ticks = False
            
        if monster_ticks:
            st.session_state.monster = calculate_ai_route(
                st.session_state.monster, st.session_state.player, g_size, st.session_state.walls
            )
            
        if st.session_state.monster == st.session_state.player:
            trigger_game_over()

# 3. Render Real-Time HUD Dashboard Panel
st.markdown(f"""
    <div class='hud-container'>
        <div class='hud-stat'>SCORE: <span class='hud-val'>{st.session_state.score:02d}</span></div>
        <div class='hud-stat'>STREAK: <span class='hud-val'>🔥{st.session_state.streak}</span></div>
        <div class='hud-stat'>BEST: <span class='hud-val'>{st.session_state.high_score:02d}</span></div>
    </div>
""", unsafe_allow_html=True)

# 4. Generate Procedural Graphics Grid Layout
grid_html = "<div class='matrix-frame'>"
for r in range(st.session_state.grid_size):
    grid_html += "<div class='matrix-row'>"
    for c in range(st.session_state.grid_size):
        if (r, c) == st.session_state.player:
            grid_html += "<div class='matrix-cell node-player'><span class='sprite-icon'>🛸</span></div>"
        elif (r, c) == st.session_state.monster:
            grid_html += "<div class='matrix-cell node-monster'><span class='sprite-icon'>👾</span></div>"
        elif (r, c) == st.session_state.treasure:
            grid_html += "<div class='matrix-cell node-target'><span class='sprite-icon'>💎</span></div>"
        elif (r, c) in st.session_state.walls:
            grid_html += "<div class='matrix-cell node-wall'><span class='sprite-icon'>🚧</span></div>"
        else:
            grid_html += "<div class='matrix-cell'></div>"
    grid_html += "</div>"
grid_html += "</div>"

st.markdown(grid_html, unsafe_allow_html=True)

# 5. Immersive Action Alerts & Screen States
if st.session_state.game_state == "WASTED":
    st.error("💀 SYSTEM TERMINATED // WASTED. The AI entity overrode your core dashboard.")
elif st.session_state.game_state == "STAGE_CLEAR":
    st.balloons()
    st.success(f"⚡ DATA CORE ACQUIRED! Next stage initialized.")
    st.markdown("<div class='btn-next'>", unsafe_allow_html=True)
    if st.button("LOAD NEXT PROCEDURAL SECTOR ▶", use_container_width=True):
        build_procedural_map()
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# 6. Optimized Mobile Arcade D-Pad Controls
st.markdown("<div class='dpad-container'>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    cc1, cc2, cc3 = st.columns([1, 2, 1])
    with cc2:
        st.markdown("<div class='btn-core'>", unsafe_allow_html=True)
        if st.button("▲", key="up"): step_engine(-1, 0)
        st.markdown("</div>", unsafe_allow_html=True)
    
    cl1, cl2, cl3 = st.columns([1.5, 1, 1.5])
    with cl1:
        st.markdown("<div class='btn-core'>", unsafe_allow_html=True)
        if st.button("◀", key="left"): step_engine(0, -1)
        st.markdown("</div>", unsafe_allow_html=True)
    with cl2:
        st.markdown("<p style='text-align:center; font-size:16px; margin-top:8px; color:#4facfe;'>⌖</p>", unsafe_allow_html=True)
    with cl3:
        st.markdown("<div class='btn-core'>", unsafe_allow_html=True)
        if st.button("▶", key="right"): step_engine(0, 1)
        st.markdown("</div>", unsafe_allow_html=True)
        
    cd1, cd2, cd3 = st.columns([1, 2, 1])
    with cd2:
        st.markdown("<div class='btn-core'>", unsafe_allow_html=True)
        if st.button("▼", key="down"): step_engine(1, 0)
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# System Master Reboot Row
st.write(" ")
st.markdown("<div class='btn-sys'>", unsafe_allow_html=True)
if st.button("🔄 REBOOT SYSTEM CORE (RESET SCORE)", use_container_width=True):
    st.session_state.score = 0
    st.session_state.streak = 0
    build_procedural_map()
    st.rerun()
st.markdown("</div>", unsafe_allow_html=True)
                
