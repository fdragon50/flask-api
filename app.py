from flask import Flask, jsonify
import yfinance as yf

app = Flask(__name__)

@app.route('/get_price/<ticker>', methods=['GET'])
def get_price(ticker):
    try:
        stock = yf.Ticker(ticker)
        current_price = stock.history(period="1d")["Close"].iloc[-1]
        return jsonify({"ticker": ticker, "price": current_price})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
