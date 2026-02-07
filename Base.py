import streamlit as st
import random

# Sample Data
districts = ["Adilabad", "Hyderabad", "Nizamabad", "Warangal", "Khammam", "Karimnagar"]
spokes = ["Spoke A", "Spoke B", "Spoke C", "Spoke D", "Spoke E"]
tests = ["Blood Test", "X-Ray", "MRI", "CT Scan", "Glucose Test"]

st.title("Database Search Portal")

# 1. Database Selection (Radio Buttons)
# Radio buttons allow single selection from a list
database = st.radio(
    "Select Database",
    ["Production", "Testing", "Archive"],
    horizontal=True
)

# 2. Select District (Dropdown with Search)
# st.selectbox has a built-in search feature; just type to filter
col1, col2 = st.columns([3, 1])
with col1:
    selected_district = st.selectbox("Select District", districts, key="dist_box")
with col2:
    if st.button("Random District"):
        st.session_state.dist_box = random.choice(districts)
        st.rerun()

# 3. Select Spokes (Dropdown with Search)
col3, col4 = st.columns([3, 1])
with col3:
    selected_spoke = st.selectbox("Select Spokes", spokes, key="spoke_box")
with col4:
    if st.button("Random Spoke"):
        st.session_state.spoke_box = random.choice(spokes)
        st.rerun()

# 4. Select Tests (Dropdown with Search)
col5, col6 = st.columns([3, 1])
with col5:
    selected_test = st.selectbox("Select Tests", tests, key="test_box")
with col6:
    if st.button("Random Test"):
        st.session_state.test_box = random.choice(tests)
        st.rerun()

# Display Selections
st.divider()
st.subheader("Current Selection Summary")
st.write(f"**Database:** {database}")
st.write(f"**District:** {selected_district}")
st.write(f"**Spoke:** {selected_spoke}")
st.write(f"**Test:** {selected_test}")
