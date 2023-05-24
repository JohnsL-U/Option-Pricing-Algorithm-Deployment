                                                                      
from flask import Flask, render_template, request
import math
from scipy.stats import norm

app = Flask(__name__)


def black_scholes_call(S, K, T, r, q, sigma):
    # S: spot price
    # K: strike price
    # T: time to maturity
    # r: interest rate
    # q: dividend yield
    # sigma: volatility of underlying asset

    d1 = (math.log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = (math.log(S / K) + (r - q - 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))

    call = (S * math.exp(-q * T) * norm.cdf(d1, 0.0, 1.0) - K * math.exp(-r * T) * norm.cdf(d2, 0.0, 1.0))

    return call


def black_scholes_put(S, K, T, r, q, sigma):

    d1 = (math.log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = (math.log(S / K) + (r - q - 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))

    put = (K * math.exp(-r * T) * norm.cdf(-d2, 0.0, 1.0) - S * math.exp(-q * T) * norm.cdf(-d1, 0.0, 1.0))
    
    return put


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        S = float(request.form['S'])
        K = float(request.form['K'])
        T = float(request.form['T']) / 365
        r = float(request.form['r'])
        q = float(request.form['q'])
        sigma = float(request.form['sigma'])
        call_price = black_scholes_call(S, K, T, r, q, sigma)
        put_price = black_scholes_put(S, K, T, r, q, sigma)
        return render_template('index.html', call_price=call_price, put_price=put_price)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    