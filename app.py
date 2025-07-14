import streamlit as st

st.set_page_config(page_title="TradingView Index Charts", layout="centered")

st.title("📈 TradingView Index Chart Viewer")
st.write("Select an index or sector to view its live chart from TradingView.")

# Extended index list with NSE Sectoral Indices
index_options = {
    "Nifty 50": "NSE:NIFTY",
    "Nifty Next 50": "NSE:NIFTYJUNIOR",
    "Nifty 100": "NSE:CNX100",
    "Nifty 200": "NSE:NIFTY200",
    "Nifty 500": "NSE:NIFTY500",
    "Nifty Midcap 50": "NSE:CNXMIDCAP",
    "Nifty Midcap 100": "NSE:NIFTYMIDCAP100",
    "Nifty Smallcap 100": "NSE:NIFTYSMALLCAP100",
    "Nifty Bank": "NSE:BANKNIFTY",
    "Nifty Auto": "NSE:NIFTYAUTO",
    "Nifty Financial Services": "NSE:NIFTYFINANCE",
    "Nifty FMCG": "NSE:NIFTYFMCG",
    "Nifty IT": "NSE:CNXIT",
    "Nifty Media": "NSE:NIFTYMEDIA",
    "Nifty Metal": "NSE:NIFTYMETAL",
    "Nifty Pharma": "NSE:NIFTYPHARMA",
    "Nifty PSU Bank": "NSE:NIFTYPSUBANK",
    "Nifty Private Bank": "NSE:NIFTYPRIVATEBANK",
    "Nifty Realty": "NSE:NIFTYREALTY",
    "Nifty Energy": "NSE:NIFTYENERGY",
    "Nifty Oil & Gas": "NSE:NIFTYOILGAS",
    "Nifty Healthcare Index": "NSE:NIFTYHEALTHCARE",
    "Nifty Consumer Durables": "NSE:NIFTYCONSUMERDURABLES",
    "Nifty Commodities": "NSE:NIFTYCOMMODITIES",
    "Nifty Infrastructure": "NSE:NIFTYINFRA",
    "Nifty Services Sector": "NSE:NIFTYSERVSECTOR"
}

selected_index = st.selectbox("Choose an Index or Sector", list(index_options.keys()))
ticker = index_options[selected_index]

# Embed TradingView chart via iframe
tradingview_url = f"""
<iframe 
    src="https://s.tradingview.com/widgetembed/?frameElementId=tradingview_{ticker}&symbol={ticker}&interval=D&hidesidetoolbar=1&symboledit=1&saveimage=1&toolbarbg=f1f3f6&studies=[]&theme=light&style=1&timezone=Etc/UTC&withdateranges=1&hideideas=1&hidelegend=1" 
    width="100%" 
    height="500" 
    frameborder="0" 
    allowtransparency="true" 
    scrolling="no">
</iframe>
"""

st.components.v1.html(tradingview_url, height=500)
