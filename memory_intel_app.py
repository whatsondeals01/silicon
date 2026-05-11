import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Silicon Memory Intel", page_icon="💾", layout="wide")

def calculate_landed_cost(usd_price, shipping_sgd=15.00):
    rate = 1.35 
    cif_sgd = (usd_price * rate) + shipping_sgd
    gst = cif_sgd * 0.09 if cif_sgd > 400 else 0.00
    return {"cif": round(cif_sgd, 2), "gst": round(gst, 2), "total": round(cif_sgd + gst, 2)}

st.title("💾 Silicon Memory Intelligence Hub")
st.caption("Market Status: May 2026 | Singapore | Target: TLT Hub Infrastructure")

# GST THRESHOLD ALERT
price_usd = st.number_input("Unit Price (USD)", value=280.0)
res = calculate_landed_cost(price_usd)

if 390 <= res['cif'] <= 400:
    st.warning(f"⚠️ GST DANGER ZONE: CIF is S${res['cif']}. Price increase of <$6 USD triggers 9% tax.")

st.metric("Total Landed (SGD)", f"S${res['total']}", delta="GST Exempt" if res['gst'] == 0 else "Tax Applied")

st.header("📈 2026 Supercycle Trend")
dates = pd.date_range(start="2024-01-01", periods=24, freq='ME')
st.line_chart(pd.DataFrame({"Price": np.random.randn(24).cumsum()}, index=dates))

st.header("🧠 128GB Equivalence & Next Steps")
eq_data = {
    "Metric": ["Target Model", "GST Strategy", "Cooling Req", "Build Path"],
    "64GB Tier": ["32B (Qwen 3)", "Single Order", "Standard", "Mini PC"],
    "128GB Tier": ["70B (Llama 3.3)", "Split 2x64GB", "Active/High", "Custom Desktop"]
}
st.table(pd.DataFrame(eq_data))
