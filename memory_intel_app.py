import streamlit as st
import pandas as pd
import numpy as np
import requests
import datetime

# --- CONFIG & APP SETUP ---
st.set_page_config(page_title="Silicon Memory Intel", page_icon="💾", layout="wide")

def get_exchange_rate():
    # Returns a fixed 2026 proxy rate or could be linked to an API
    return 1.35 

def calculate_landed_cost(usd_price, shipping_sgd=12.00):
    rate = get_exchange_rate()
    cif_sgd = (usd_price * rate) + shipping_sgd
    
    # Singapore 2026 GST Logic: 9% if CIF > S$400
    gst_rate = 0.09
    gst_amount = cif_sgd * gst_rate if cif_sgd > 400 else 0.00
    total_landed = cif_sgd + gst_amount
    
    return {
        "cif_sgd": round(cif_sgd, 2),
        "gst": round(gst_amount, 2),
        "total": round(total_landed, 2),
        "tax_applied": gst_amount > 0
    }

# --- UI SECTION ---
st.title("💾 Silicon Memory Intelligence Hub")
st.caption(f"Market Status: May 2026 | Location: Singapore | Target: TLT Hub Infrastructure")

col1, col2 = st.columns([1, 2])

with col1:
    st.header("🛒 Landed Cost Calculator")
    unit_usd = st.number_input("Unit Price (USD)", value=280.0, step=10.0)
    ship_sgd = st.number_input("Shipping to SG (SGD)", value=15.0)
    
    result = calculate_landed_cost(unit_usd, ship_sgd)
    
    st.metric("Total Landed (SGD)", f"S${result['total']}")
    st.write(f"**CIF Value:** S${result['cif_sgd']}")
    st.write(f"**GST (9%):** S${result['gst']}")
    if not result['tax_applied']:
        st.success("Below S$400 threshold: GST Exempt (Air/Post)")
    else:
        st.warning("GST Applied (Exceeds S$400)")

with col2:
    st.header("📈 Historical Trends & Projection")
    # Simulated 2024-2026 Supercycle Data
    dates = pd.date_range(start="2024-01-01", periods=24, freq='M')
    ddr5_trend = [100, 95, 90, 110, 130, 180, 220, 310, 350, 420, 450, 480, 510, 530, 550, 520, 500, 490, 510, 530, 560, 590, 620, 650]
    
    df_trends = pd.DataFrame({"Date": dates, "DDR5 Price Index": ddr5_trend})
    st.line_chart(df_trends.set_index("Date"))
    st.info("Trend Note: Prices are rising 30-50% per quarter in 2026 due to HBM cannibalization.")

# --- LLM CAPABILITY TABLE ---
st.divider()
st.header("🧠 LLM Memory Equivalence (Local Inference)")
llm_data = {
    "Variant": ["DDR4 (Legacy)", "DDR5 (Mainstream)", "GDDR7 (GPU)", "DDR6 (Future)"],
    "Typical Bandwidth": ["~40 GB/s", "~90 GB/s", "~1500 GB/s", "TBD (2027+)"],
    "64GB Capacity Use Case": ["Background Scrapers", "32B Models (Qwen/Llama)", "Ultra-Fast 8B Weights", "Future-Proofing"],
    "Status": ["Expensive Scarcity", "Buying Sweet Spot", "Limited to eGPU", "Engineering Samples"]
}
st.table(pd.DataFrame(llm_data))
