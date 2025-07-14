import streamlit as st

st.set_page_config(page_title="TradingView Index Charts", layout="centered")

st.title("📈 TradingView Index Chart Viewer")
st.write("Select an index to view its live chart from TradingView.")

# Dropdown for index selection
index_options = {
    "Nifty 50": "NSE:NIFTY",
    "Sensex": "BSE:SENSEX",
    "S&P 500": "SP:SPX",
    "NASDAQ 100": "NASDAQ:NDX",
    "Dow Jones": "DJI",
    "FTSE 100": "OANDA:UK100GBP",
    "DAX 40": "XETR:DAX",
    "Nikkei 225": "TVC:NI225",
    "Hang Seng": "HKEX:HSI"
}

selected_index = st.selectbox("Choose an Index", list(index_options.keys()))
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
