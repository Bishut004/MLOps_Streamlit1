import os
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="Tourism Prediction App",
    page_icon="✈️",
    layout="wide")

st.title("Tourism Package Prediction")
st.write(
    "Fill the customer information below to predict "
    "whether the customer is likely to purchase a tourism package."
)

