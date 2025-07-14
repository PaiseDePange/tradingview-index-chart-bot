import streamlit as st

st.set_page_config(page_title="TradingView NSE Sectoral Chart Viewer", layout="centered")

st.title("📈 NSE Sectoral Indices Chart Viewer")
st.write("Select an NSE sectoral index to view its live TradingView chart.")

index_options = {
    "Nifty 50": "NSE:NIFTY",
    "Nifty Next 50": "NSE:NIFTYJUNIOR",
    "Nifty 100": "NSE:CNX100",
    "Nifty Midcap 50": "NSE:CNXMIDCAP",
    "Nifty Midcap 100": "NSE:CNXMIDPCAP100",
    "Nifty Smallcap 100": "NSE:CNXSMALLCAP",
    "Nifty Bank": "NSE:CNXBANK",
    "Nifty Auto": "NSE:CNXAUTO",
    "Nifty Financial Services": "NSE:CNXFINANCIAL",
    "Nifty FMCG": "NSE:CNXFMCG",
    "Nifty IT": "NSE:CNXIT",
    "Nifty Media": "NSE:CNXMEDIA",
    "Nifty Metal": "NSE:CNXMETAL",
    "Nifty Pharma": "NSE:CNXPHARMA",
    "Nifty PSU Bank": "NSE:CNXPSUBANK",
    "Nifty Private Bank": "NSE:CNXPRIVBANK",
    "Nifty Realty": "NSE:CNXREALTY",
    "Nifty Energy": "NSE:CNXENERGY",
    "Nifty Oil & Gas": "NSE:CNXOILGAS",
    "Nifty Healthcare": "NSE:CNXHEALTH",
    "Nifty Consumer Durables": "NSE:CNXCONSDEUR",
    "Nifty Services Sector": "NSE:CNXSERVICE"
}

selected = st.selectbox("Choose index:", list(index_options.keys()))
sym = index_options[selected]

iframe = f"""
<iframe 
    src="https://s.tradingview.com/widgetembed/?symbol={sym}&interval=D&...&theme=light"
    width="100%" height="500" frameborder="0" scrolling="no"></iframe>
"""
st.components.v1.html(iframe, height=500)
