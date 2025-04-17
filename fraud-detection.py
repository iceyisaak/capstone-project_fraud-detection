# Streamlit Documentation: https://docs.streamlit.io/


import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os 
import json

# Title/Text
st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Load model function with proper caching and error handling
@st.cache_resource

def load_model():
    model_path = "xgb_model_balanced.pkl"
    try:
        if not os.path.exists(model_path):
            st.error(f"Model file not found: {model_path}")
            return None
        
        with open(model_path, "rb") as f:
            model = pickle.load(f)
        return model
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None


# Load Model
model = load_model()

# Read JSON from a file
with open('feature_stats.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #4267B2;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #1E3A8A;
    }
    .description {
        font-size: 1rem;
        color: #4B5563;
    }
    .highlight {
        background-color: #F3F4F6;
        padding: 20px;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-header">🚨 ML Fraud Detection</p>', unsafe_allow_html=True)
st.markdown('<p class="description">Credit Card Fraud Detection</p>', unsafe_allow_html=True)

st.subheader("Enter the Input for Fraud Detection")



Time = st.slider(
        "Time", 
        min_value=float(data['Time']['Min']), 
        max_value=float(data['Time']['Max']),
        value=float(data['Time']['Mean']), 
        step=0.01
    )
Amount = st.slider(
         "Amount", 
        min_value=float(data['Amount']['Min']), 
        max_value=float(data['Amount']['Max']),
        value=float(data['Amount']['Mean']), 
        step=0.01
    )


with st.expander("See Encoded Parameters"):
    col1, col2 = st.columns(2)

    with col1: 
        V1 = st.slider(
            "V1", 
            min_value=float(data['V1']['Min']), 
            max_value=float(data['V1']['Max']),
            value=float(data['V1']['Mean']), 
            step=0.01
        )
        V2 = st.slider(
            "V2", 
            min_value=float(data['V2']['Min']), 
            max_value=float(data['V2']['Max']),
            value=float(data['V2']['Mean']), 
            step=0.01
        )
        V3 = st.slider(
            "V3", 
            min_value=float(data['V3']['Min']), 
            max_value=float(data['V3']['Max']),
            value=float(data['V3']['Mean']), 
            step=0.01
        )
        V4 = st.slider(
            "V4", 
            min_value=float(data['V4']['Min']), 
            max_value=float(data['V4']['Max']),
            value=float(data['V4']['Mean']), 
            step=0.01
        )
        V5 = st.slider(
            "V5", 
            min_value=float(data['V5']['Min']), 
            max_value=float(data['V5']['Max']),
            value=float(data['V5']['Mean']), 
            step=0.01
        )
        V6 = st.slider(
            "V6", 
            min_value=float(data['V6']['Min']), 
            max_value=float(data['V6']['Max']),
            value=float(data['V6']['Mean']), 
            step=0.01
        )
        V7 = st.slider(
            "V7", 
            min_value=float(data['V7']['Min']), 
            max_value=float(data['V7']['Max']),
            value=float(data['V7']['Mean']), 
            step=0.01
        )
        V8 = st.slider(
            "V8", 
            min_value=float(data['V8']['Min']), 
            max_value=float(data['V8']['Max']),
            value=float(data['V8']['Mean']), 
            step=0.01
        )
        V9 = st.slider(
            "V9", 
            min_value=float(data['V9']['Min']), 
            max_value=float(data['V9']['Max']),
            value=float(data['V9']['Mean']), 
            step=0.01
        )
        V10 = st.slider(
            "V10", 
            min_value=float(data['V10']['Min']), 
            max_value=float(data['V10']['Max']),
            value=float(data['V10']['Mean']), 
            step=0.01
        )
        V11 = st.slider(
            "V11", 
            min_value=float(data['V11']['Min']), 
            max_value=float(data['V11']['Max']),
            value=float(data['V11']['Mean']), 
            step=0.01
        )
        V12 = st.slider(
            "V12", 
            min_value=float(data['V12']['Min']), 
            max_value=float(data['V12']['Max']),
            value=float(data['V12']['Mean']), 
            step=0.01
        )
        V13 = st.slider(
            "V13", 
            min_value=float(data['V13']['Min']), 
            max_value=float(data['V13']['Max']),
            value=float(data['V13']['Mean']), 
            step=0.01
        )
        V14 = st.slider(
            "V14", 
            min_value=float(data['V14']['Min']), 
            max_value=float(data['V14']['Max']),
            value=float(data['V14']['Mean']), 
            step=0.01
        )
        

    

   

    with col2:
        V15 = st.slider(
            "V15", 
            min_value=float(data['V15']['Min']), 
            max_value=float(data['V15']['Max']),
            value=float(data['V15']['Mean']), 
            step=0.01
        )
        V16 = st.slider(
            "V16", 
            min_value=float(data['V16']['Min']), 
            max_value=float(data['V16']['Max']),
            value=float(data['V16']['Mean']), 
            step=0.01
        )
        V17 = st.slider(
            "V17", 
            min_value=float(data['V17']['Min']), 
            max_value=float(data['V17']['Max']),
            value=float(data['V17']['Mean']), 
            step=0.01
        )
        V18 = st.slider(
            "V18", 
            min_value=float(data['V18']['Min']), 
            max_value=float(data['V18']['Max']),
            value=float(data['V18']['Mean']), 
            step=0.01
        )
        V19 = st.slider(
            "V19", 
            min_value=float(data['V19']['Min']), 
            max_value=float(data['V19']['Max']),
            value=float(data['V19']['Mean']), 
            step=0.01
        )
        V20 = st.slider(
            "V20", 
            min_value=float(data['V20']['Min']), 
            max_value=float(data['V20']['Max']),
            value=float(data['V20']['Mean']), 
            step=0.01
        )
        V21 = st.slider(
            "V21", 
            min_value=float(data['V21']['Min']), 
            max_value=float(data['V21']['Max']),
            value=float(data['V21']['Mean']), 
            step=0.01
        )
        V22 = st.slider(
            "V22", 
            min_value=float(data['V22']['Min']), 
            max_value=float(data['V22']['Max']),
            value=float(data['V22']['Mean']), 
            step=0.01
        )
        V23 = st.slider(
            "V23", 
            min_value=float(data['V23']['Min']), 
            max_value=float(data['V23']['Max']),
            value=float(data['V23']['Mean']), 
            step=0.01
        )
        V24 = st.slider(
            "V24", 
            min_value=float(data['V24']['Min']), 
            max_value=float(data['V24']['Max']),
            value=float(data['V24']['Mean']), 
            step=0.01
        )
        V25 = st.slider(
            "V25", 
            min_value=float(data['V25']['Min']), 
            max_value=float(data['V25']['Max']),
            value=float(data['V25']['Mean']), 
            step=0.01
        )
        V26 = st.slider(
            "V26", 
            min_value=float(data['V26']['Min']), 
            max_value=float(data['V26']['Max']),
            value=float(data['V26']['Mean']), 
            step=0.01
        )
        V27 = st.slider(
            "V27", 
            min_value=float(data['V27']['Min']), 
            max_value=float(data['V27']['Max']),
            value=float(data['V27']['Mean']), 
            step=0.01
        )
        V28 = st.slider(
            "V28", 
            min_value=float(data['V28']['Min']), 
            max_value=float(data['V28']['Max']),
            value=float(data['V28']['Mean']), 
            step=0.01
        )



input_data = pd.DataFrame({
            'Time': [Time],
            'Amount': [Amount],
            'V1': [V1],
            'V2':[V2],
            'V3':[V3],
            'V4': [V4],
            'V5':[V5],
            'V6':[V6],
            'V7': [V7],
            'V8':[V8],
            'V9':[V9],
            'V10': [V10],
            'V11':[V11],
            'V12':[V12],
            'V13': [V13],
            'V14':[V14],
            'V15':[V15],
            'V16': [V16],
            'V17':[V17],
            'V18':[V18],
            'V19': [V19],
            'V20':[V20],
            'V21':[V21],
            'V22': [V22],
            'V23':[V23],
            'V24':[V24],
            'V25': [V25],
            'V26':[V26],
            'V27':[V27],
            'V28':[V28],
        })



if st.button("Predict"):
    try:
        result = model.predict(input_data)
        if result[0] == 0:
            st.success(f"No Fraud Detected.")
        if result[0] == 1:
            st.success(f"Fraud Detected!")
    except Exception as e:
        st.error(f"Prediction failed: {str(e)}")
    