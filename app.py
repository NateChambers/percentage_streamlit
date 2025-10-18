import streamlit as st

# --- Page setup ---
st.set_page_config(page_title="💯 Percentage Calculator", layout="centered")

# --- Custom CSS for dark mode style ---
st.markdown("""
    <style>
    body {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    .stApp {
        background-color: #0E1117;
    }
    h1, h2, h3, h4 {
        color: #F8F9FA !important;
        text-align: center;
    }
    .stTextInput > div > div > input {
        background-color: #262730;
        color: white;
        border: 1px solid #555;
        border-radius: 6px;
    }
    .stNumberInput > div > div > input {
        background-color: #262730;
        color: white;
        border: 1px solid #555;
        border-radius: 6px;
    }
    .stTextInput label, .stNumberInput label {
        color: #E5E5E5;
        font-weight: 600;
    }
    .result-box {
        background-color: #1E1E1E;
        color: #00C853;
        padding: 12px;
        text-align: center;
        border-radius: 8px;
        border: 1px solid #333;
        font-size: 1.3em;
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<h1>💯 Percentage Calculator</h1>", unsafe_allow_html=True)
st.write("Easily calculate percentages — all live and beautiful in dark mode.")

# --- Inputs ---
col1, col2 = st.columns(2)
with col1:
    number = st.text_input("Enter a number:", value="0")

with col2:
    percentage = st.number_input(
        "Enter percentage (%):",
        min_value=0.01,
        max_value=100.00,
        step=0.01,
        format="%.2f",
    )

# --- Computation ---
try:
    num_value = float(number)
    result = num_value * (percentage / 100)
    result_str = f"{result:.4f}"
except ValueError:
    result_str = "Invalid input"

# --- Display result ---
st.markdown(f"<div class='result-box'>Result: {result_str}</div>", unsafe_allow_html=True)
