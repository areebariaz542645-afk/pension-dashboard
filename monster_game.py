import streamlit as st
import collections

# Page Setup for Mobile View
st.set_page_config(page_title="AI Neon Monster Chase", layout="centered")

# Custom CSS for Cyberpunk Grid and Layout
st.markdown("""
    <style>
    .block-container { padding-top: 1rem; padding-bottom: 1rem; }
    .stButton > button {
        border-radius: 12px;
        background: linear-gradient(135deg, #1f4068, #162447);
        color: #e4e4e4;
        font-weight: bold;
        border: 1px solid #00fff5;
        box-shadow: 0 0 8px #00fff5;
        padding: 10px;
    }
    .grid-box {
        display: inline-block;
        width: 45px;
        height: 45px;
        line-height: 45px;
        text-align: center;
        font-size: 24px;
        margin: 2px;
        background-color: #1a1a2e;
        border: 1px solid #432b68;
        border-radius: 8px;
        box-shadow: inset 0 0 5px rgba(255,255,255,0.05);
    }
    .player-box { border: 2px solid #00fff5; box-shadow: 0 0 15px #00fff5; background: #0f3443; }
    .monster-box { border: 2px solid #ff007f; box-shadow: 0 0 15px #ff007f; background: #2d0c22; }
    .treasure-box { border: 2px solid #00ff66; box-shadow: 0 0 15px #00ff66; background: #0c2d1c; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: #00fff5; margin-bottom:0px;'>🤖 AI Monster Chase</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888; font-size:12px;'>Monster recalculates path using AI BFS Algorithm</p>", unsafe_allow_html=True)

# 1. AI Shortest Path Algorithm (BFS)
def find_monster_move(monster, player, grid_size=6):
    queue = collections.deque([[monster]])
    seen = {monster}
    while queue:
        path = queue.popleft()
        r, c = path[-1]
        if (r, c) == player:
            return path[1] if len(path) > 1 else monster
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < grid_size and 0 <= nc < grid_size and (nr, nc) not in seen:
                queue.append(path + [(nr, nc)])
                seen.add((nr, nc))
    return monster

GRID_SIZE = 6

# 2. Game State Initialization
if 'player' not in st.session_state:
    st.session_state.player = (0, 0)
    st.session_state.monster = (5, 5)
    st.session_state.treasure = (3, 3)
    st.session_state.game_over = False
    st.session_state.won = False

def reset_game():
    st.session_state.player = (0, 0)
    st.session_state.monster = (5, 5)
    st.session_state.game_over = False
    st.session_state.won = False

def move_player(dr, dc):
    if st.session_state.game_over or st.session_state.won:
        return
    r, c = st.session_state.player
    nr, nc = r + dr, c + dc
    if 0 <= nr < GRID_SIZE and 0 <= nc < GRID_SIZE:
        st.session_state.player = (nr, nc)
        if st.session_state.player == st.session_state.treasure:
            st.session_state.won = True
            return
        st.session_state.monster = find_monster_move(st.session_state.monster, st.session_state.player)
        if st.session_state.monster == st.session_state.player:
            st.session_state.game_over = True

# 3. Render Grid HTML
grid_html = "<div style='text-align: center; margin-bottom: 10px;'>"
for r in range(GRID_SIZE):
    grid_html += "<div style='display: block;'>"
    for c in range(GRID_SIZE):
        if (r, c) == st.session_state.player:
            grid_html += "<div class='grid-box player-box'>🤠</div>"
        elif (r, c) == st.session_state.monster:
            grid_html += "<div class='grid-box monster-box'>👹</div>"
        elif (r, c) == st.session_state.treasure:
            grid_html += "<div class='grid-box treasure-box'>🏆</div>"
        else:
            grid_html += "<div class='grid-box'>⬜</div>"
    grid_html += "</div>"
grid_html += "</div>"

st.markdown(grid_html, unsafe_allow_html=True)

# Status Announcements
if st.session_state.won:
    st.balloons()
    st.success("🎉 Mubarak ho! Aapne AI Monster ko hara diya!")
elif st.session_state.game_over:
    st.error("💥 Game Over! Monster ne pakar liya.")

# 4. Compact Mobile Controls Setup (No Scroll)
st.write(" ")
c1, c2, c3 = st.columns([1, 2, 1])

with c2:
    cc1, cc2, cc3 = st.columns(3)
    with cc2:
        if st.button("⬆️", key="up"): move_player(-1, 0)
    
    cl1, cl2, cl3 = st.columns(3)
    with cl1:
        if st.button("⬅️", key="left"): move_player(0, -1)
    with cl2:
        st.markdown("<p style='text-align:center; margin-top:8px; color:#555;'>🕹️</p>", unsafe_allow_html=True)
    with cl3:
        if st.button("➡️", key="right"): move_player(0, 1)
        
    cd1, cd2, cd3 = st.columns(3)
    with cd2:
        if st.button("⬇️", key="down"): move_player(1, 0)

st.write(" ")
if st.button("🔄 Restart Game", type="primary", use_container_width=True):
    reset_game()
    
