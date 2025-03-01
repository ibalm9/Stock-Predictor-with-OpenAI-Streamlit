import streamlit as st
import plotly.graph_objects as go
from stock_analyzer import analyze_stock
from utils import get_stock_data, prepare_stock_analysis_prompt
import time

# Page configuration
st.set_page_config(
    page_title="AI Stock Predictor",
    page_icon="📈",
    layout="wide"
)

# Load custom CSS
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Main title
st.title("🤖 AI Stock Predictor")
st.markdown("---")

# Sidebar
st.sidebar.header("Stock Selection")
stock_symbol = st.sidebar.text_input("Enter Stock Symbol (e.g., AAPL, GOOGL)", "AAPL")
analyze_button = st.sidebar.button("Analyze Stock")

# Main content area
if analyze_button:
    try:
        with st.spinner("Fetching stock data..."):
            stock_data, stock_info = get_stock_data(stock_symbol)
        
        # Display stock chart
        fig = go.Figure(data=[go.Candlestick(
            x=stock_data.index,
            open=stock_data['Open'],
            high=stock_data['High'],
            low=stock_data['Low'],
            close=stock_data['Close']
        )])
        
        fig.update_layout(
            title=f"{stock_info.get('longName', stock_symbol)} Stock Price",
            yaxis_title="Price (USD)",
            template="plotly_white",
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # AI Analysis
        with st.spinner("Analyzing stock data with AI..."):
            prompt = prepare_stock_analysis_prompt(stock_data, stock_info)
            analysis = analyze_stock(prompt)
            
            # Display prediction
            prediction_color = "stock-up" if analysis["prediction"] == "up" else "stock-down"
            
            st.markdown(
                f"""
                <div class="prediction-card">
                    <h2>AI Prediction</h2>
                    <p>Direction: <span class="{prediction_color}">{analysis["prediction"].upper()}</span></p>
                    <p>Confidence: {analysis["confidence"]*100:.1f}%</p>
                    <p>Target Price: ${analysis["target_price"]}</p>
                    <p>Timeframe: {analysis["timeframe"]}</p>
                    <h3>Analysis:</h3>
                    <p>{analysis["reasoning"]}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        
else:
    st.info("👈 Enter a stock symbol and click 'Analyze Stock' to begin")
    
# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>This is an AI-powered stock prediction tool. Please use this information as part of your research, not as financial advice.</p>
</div>
""", unsafe_allow_html=True)
