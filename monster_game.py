import streamlit as st
import collections
import random

# Core Page Setup optimized for mobile viewport
st.set_page_config(page_title="Mystic Hunt", layout="centered", initial_sidebar_state="collapsed")

# Mystical Forest Neon Theme Stylesheet
st.markdown("""
    <style>
    body { background-color: #0d1b15; color: #e0f2e9; font-family: 'Courier New', Courier, monospace; }
    .block-container { padding-top: 1rem !important; max-width: 420px !important; margin: auto; }
    
    /* Nature Neon Title */
    .nature-title {
        text-align: center;
        background: linear-gradient(135deg, #a8ff78 0%, #78ffd6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        font-size: 36px;
        letter-spacing: 2px;
        margin-bottom: 10px;
        text-shadow: 0 0 15px rgba(120, 255, 214, 0.4);
    }
    
    /* Home Screen Menu styling */
    .main-menu-card {
        background: linear-gradient(180deg, rgba(20, 50, 35, 0.9) 0%, rgba(10, 30, 20, 0.95) 100%);
        border: 2px solid #a8ff78;
        border-radius: 20px;
        padding: 30px 20px;
        text-align: center;
        box-shadow: 0 0 30px rgba(168, 255, 120, 0.25);
        margin-top: 20px;
    }
    
    /* Live Stats Dashboard (HUD) */
    .hud-container {
        display: flex;
        justify-content: space-between;
        background: #08120e;
        border: 1px solid #2d5a44;
        border-radius: 12px;
        padding: 8px 15px;
        margin-bottom: 15px;
    }
    .hud-stat { font-size: 13px; font-weight: bold; color: #a8ff78; }

    /* Interactive Grid Box */
    .grid-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        background: rgba(10, 25, 18, 0.9);
        border: 2px solid #78ffd6;
        border-radius: 20px;
        padding: 12px;
        box-shadow: 0 0 25px rgba(120, 255, 214, 0.2);
        margin-bottom: 15px;
    }
    
    /* Direct Grid Cell Button Override for Touch Movement */
    .stButton > button.grid-btn {
        width: 50px !important; height: 50px !important;
        margin: 2px !important; padding: 0px !important;
        background: #142d22 !important; border: 1px solid #254d3b !important;
        border-radius: 10px !important; font-size: 24px !important;
        transition: all 0.1s ease;
    }
    .stButton > button.grid-btn:active { transform: scale(0.92); }
    
    /* Neon Glow Overrides for Dynamic Entities */
    .stButton > button.cell-player { background: #78ffd6 !important; border: 2px solid #ffffff !important; box-shadow: 0 0 15px #78ffd6; }
    .stButton > button.cell-monster { background: #ff4b4b !important; border: 2px solid #ffffff !important; box-shadow: 0 0 15px #ff4b4b; }
    .stButton > button.cell-treasure { background: #ffcc00 !important; border: 2px solid #ffffff !important; box-shadow: 0 0 15px #ffcc00; }
    .stButton > button.cell-wall { background: #3d5a4c !important; border: 1px solid #527865 !important; }

    /* Interface Utility Navigation Buttons */
    .menu-btn button {
        background: linear-gradient(135deg, #a8ff78, #78ffd6) !important; color: #050a07 !important;
        font-weight: 900 !important; font-size: 18px !important; border-radius: 12px !important; border: none !important;
        padding: 10px !important; box-shadow: 0 4px 15px rgba(120,255,214,0.3) !important;
    }
    .sys-btn button {
        background: transparent !important; color: #ff4b4b !important;
        border: 1px solid #ff4b4b !important; font-weight: bold !important; border-radius: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='nature-title'>MYSTIC HUNT</h1>", unsafe_allow_html=True)

# 1. State Initializers
if 'screen' not in st.session_state:
    st.session_state.screen = "HOME"  # HOME, PLAYING
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.high_score = 0

# BFS Pathfinding Algorithm for AI Monster
def get_ai_next_step(monster, player, grid_size, walls):
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

def init_procedural_level():
    st.session_state.grid_size = 5 if st.session_state.score < 5 else 6
    g_size = st.session_state.grid_size
    st.session_state.player = (0, 0)
    st.session_state.monster = (g_size - 1, g_size - 1)
    st.session_state.treasure = (random.randint(1, g_size-2), random.randint(1, g_size-2))
    
    # Generate random environmental walls
    st.session_state.walls = []
    num_walls = min(st.session_state.score + 1, 4)
    while len(st.session_state.walls) < num_walls:
        w = (random.randint(0, g_size-1), random.randint(0, g_size-1))
        if w not in [st.session_state.player, st.session_state.monster, st.session_state.treasure]:
            st.session_state.walls.append(w)
            
    st.session_state.game_status = "LIVE"

def handle_cell_touch(target_r, target_c):
    if st.session_state.game_status != "LIVE":
        return
        
    pr, pc = st.session_state.player
    # Validate step calculation (Only allow adjacent orthogonal moves)
    if abs(pr - target_r) + abs(pc - target_c) == 1:
        if (target_r, target_c) in st.session_state.walls:
            return # Blocked by obstacle
            
        # Move Player
        st.session_state.player = (target_r, target_c)
        
        # Check Win state
        if st.session_state.player == st.session_state.treasure:
            st.session_state.score += 1
            st.session_state.game_status = "WON"
            return
            
        # Move AI Monster
        st.session_state.monster = get_ai_next_step(
            st.session_state.monster, st.session_state.player, st.session_state.grid_size, st.session_state.walls
        )
        
        # Check Lose state
        if st.session_state.monster == st.session_state.player:
            st.session_state.game_status = "WASTED"
            if st.session_state.score > st.session_state.high_score:
                st.session_state.high_score = st.session_state.score

# 2. SCREEN VIEW MANAGER
if st.session_state.screen == "HOME":
    st.markdown("""
        <div class='main-menu-card'>
            <h3 style='color: #78ffd6; margin-bottom: 5px;'>WELCOME TO THE UNTAMED FOREST</h3>
            <p style='font-size: 13px; color: #a2bcae; margin-bottom: 25px;'>Outsmart the AI core entity using direct touch grid movements.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write(" ")
    st.markdown("<div class='menu-btn'>", unsafe_allow_html=True)
    if st.button("⚔️ START MISSION", use_container_width=True):
        st.session_state.score = 0
        init_procedural_level()
        st.session_state.screen = "PLAYING"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.screen == "PLAYING":
    # Display Scoreboard HUD
    st.markdown(f"""
        <div class='hud-container'>
            <div class='hud-stat'>SCORE: <span style='color:#fff;'>{st.session_state.score:02d}</span></div>
            <div class='hud-stat'>STAGE: <span style='color:#fff;'>0{st.session_state.score + 1}</span></div>
            <div class='hud-stat'>BEST: <span style='color:#fff;'>{st.session_state.high_score:02d}</span></div>
        </div>
    """, unsafe_allow_html=True)
    
    # Render Interactive Matrix Grid
    g_size = st.session_state.grid_size
    
    # We use native Streamlit Columns to generate clean layouts
    for r in range(g_size):
        cols = st.columns(g_size)
        for c in range(g_size):
            with cols[c]:
                # Assign dynamic classes for styling
                btn_class = "grid-btn"
                label = ""
                
                if (r, c) == st.session_state.player:
                    btn_class += " cell-player"
                    label = "🛸"
                elif (r, c) == st.session_state.monster:
                    btn_class += " cell-monster"
                    label = "👾"
                elif (r, c) == st.session_state.treasure:
                    btn_class += " cell-treasure"
                    label = "💎"
                elif (r, c) in st.session_state.walls:
                    btn_class += " cell-wall"
                    label = "🚧"
                
                # Render cell button
                st.button(
                    label, 
                    key=f"cell_{r}_{c}", 
                    on_click=handle_cell_touch, 
                    args=(r, c),
                    help=None
                )
                
                # Apply CSS directly injection via layout trick
                st.markdown(f"<script>document.getElementById('cell_{r}_{c}').className += ' {btn_class}';</script>", unsafe_allow_html=True)

    # Status System Notifications 
    if st.session_state.game_status == "WASTED":
        st.error("💀 SYSTEM TERMINATED // WASTED. The Monster caught you.")
        st.markdown("<div class='menu-btn'>", unsafe_allow_html=True)
        if st.button("🔄 RESTART LEVEL", use_container_width=True):
            init_procedural_level()
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
        
    elif st.session_state.game_status == "WON":
        st.balloons()
        st.success("⚡ CORE ACQUIRED! Path to next sector open.")
        st.markdown("<div class='menu-btn'>", unsafe_allow_html=True)
        if st.button("NEXT SECTOR ▶", use_container_width=True):
            init_procedural_level()
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    # Home Navigation Utility Row
    st.write(" ")
    st.markdown("<div class='sys-btn'>", unsafe_allow_html=True)
    if st.button("🏠 RETURN TO MAIN MENU", use_container_width=True):
        st.session_state.screen = "HOME"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    
