import streamlit as st

# Page config
st.set_page_config(
    page_title="KJ GPT Auto UI",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 KJ GPT Auto")
st.caption("Streamlit UI")

# Sidebar
st.sidebar.header("Settings")

model = st.sidebar.selectbox(
    "Model",
    ["gpt-4", "gpt-3.5-turbo"]
)

temperature = st.sidebar.slider(
    "Temperature",
    0.0,
    1.0,
    0.5
)

max_steps = st.sidebar.number_input(
    "Max Steps",
    min_value=1,
    max_value=50,
    value=10
)

# Goal input
goal = st.text_area(
    "Enter your goal",
    height=120,
    placeholder="Example: Research the best GPU for machine learning"
)

# Run button
run = st.button("🚀 Run")

st.divider()

# Output box
st.subheader("Output")

output = st.text_area(
    "",
    height=300,
    key="output_box",
    placeholder="Agent output will appear here..."
)

if run:
    if goal.strip() == "":
        st.warning("Please enter a goal")
    else:
        result = f"Processing goal:\n\n{goal}\n\nModel: {model}\nTemperature: {temperature}\nSteps: {max_steps}"
        st.session_state.output_box = result