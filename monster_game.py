import streamlit as st
import collections

# Page Theme and Title Setup
st.set_page_config(page_title="AI Pathfinding Game", layout="centered")
st.title("🤖 AI Monster Chase: Pathfinding Game")
st.write("Monster se bachein aur Treasure 🏆 tak pounchein! Monster har step par aapka rasta dhoond rha hai.")

# 1. AI Breadth-First Search (BFS) Algorithm for Shortest Path
def find_monster_move(monster, player, grid_size=6):
    queue = collections.deque([[monster]])
    seen = {monster}
    while queue:
        path = queue.popleft()
        r, c = path[-1]
        if (r, c) == player:
            return path[1] if len(path) > 1 else monster
        
        # 4 Possible Movements (Up, Down, Left, Right)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < grid_size and 0 <= nc < grid_size and (nr, nc) not in seen:
                queue.append(path + [(nr, nc)])
                seen.add((nr, nc))
    return monster

# 2. Grid Management using Session State
GRID_SIZE = 6

if 'player' not in st.session_state:
    st.session_state.player = (0, 0)      # Player starts top-left
    st.session_state.monster = (5, 5)     # Monster starts bottom-right
    st.session_state.treasure = (3, 3)    # Treasure is in the center
    st.session_state.game_over = False
    st.session_state.won = False

def reset_game():
    st.session_state.player = (0, 0)
    st.session_state.monster = (5, 5)
    st.session_state.game_over = False
    st.session_state.won = False

# 3. Game Logic and Movement Handler
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
            
        # Monster recalculates shortest path using AI Search
        st.session_state.monster = find_monster_move(st.session_state.monster, st.session_state.player)
        
        if st.session_state.monster == st.session_state.player:
            st.session_state.game_over = True

# 4. Rendering Visual Map
grid = [["⬜" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
grid[st.session_state.treasure[0]][st.session_state.treasure[1]] = "🏆"
grid[st.session_state.monster[0]][st.session_state.monster[1]] = "👹"
grid[st.session_state.player[0]][st.session_state.player[1]] = "🤠"

# Centered Board UI
for row in grid:
    st.markdown(f"<h3 style='text-align: center; letter-spacing: 10px;'>{' '.join(row)}</h3>", unsafe_allow_html=True)

st.write("---")

# Game Status Announcements
if st.session_state.won:
    st.balloons()
    st.success("🎉 Mubarak ho! Aapne AI Monster ko chakma de kar Treasure jeet liya!")
elif st.session_state.game_over:
    st.error("💥 Oh ho! AI Monster ne aapko pakar liya. Game Over!")

# 5. Interactive Mobile-Friendly Buttons
st.write("### Game Controls:")
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("⬆️ Up", use_container_width=True): move_player(-1, 0)
with col2:
    if st.button("⬇️ Down", use_container_width=True): move_player(1, 0)
with col3:
    if st.button("⬅️ Left", use_container_width=True): move_player(0, -1)
with col4:
    if st.button("➡️ Right", use_container_width=True): move_player(0, 1)

st.write(" ")
if st.button("🔄 Restart Game", type="primary", use_container_width=True):
    reset_game()
  
