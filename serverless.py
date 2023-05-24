import json
import math
import boto3


def norm_cdf(x):
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0


def black_scholes_call(S, K, T, r, q, sigma):
    # S: spot price
    # K: strike price
    # T: time to maturity
    # r: interest rate
    # q: dividend yield
    # sigma: volatility of underlying asset

    d1 = (math.log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = (math.log(S / K) + (r - q - 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))

    call = (S * math.exp(-q * T) * norm_cdf(d1) - K * math.exp(-r * T) * norm_cdf(d2))

    return call


def black_scholes_put(S, K, T, r, q, sigma):
    d1 = (math.log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = (math.log(S / K) + (r - q - 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))

    put = (K * math.exp(-r * T) * norm_cdf(-d2) - S * math.exp(-q * T) * norm_cdf(-d1))

    return put


def lambda_handler(event, context):
    s3 = boto3.client('s3')
    input_bucket = 'swe590s3bucket' 
    input_key = 'input.json'
    response = s3.get_object(Bucket=input_bucket, Key=input_key)
    file_content = response['Body'].read().decode('utf-8')
    data = json.loads(file_content)
    

    S = data['S']
    K = data['K']
    T = data['T']
    r = data['r']
    q = data['q']
    sigma = data['sigma']

    call_price = black_scholes_call(S, K, T, r, q, sigma)
    put_price = black_scholes_put(S, K, T, r, q, sigma)

    # Prepare the result as a JSON object
    result = {
        "S": S,
        "K": K,
        "T": T,
        "r": r,
        "q": q,
        "sigma": sigma,
        "call_price": call_price,
        "put_price": put_price
    }

    # Convert the JSON object to a string
    result_str = json.dumps(result)

    # Write the results to an S3 bucket
    output_bucket = 'swe590bucket2'
    output_key = 'output.json'
    s3.put_object(Body=result_str, Bucket=output_bucket, Key=output_key)
