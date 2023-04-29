import requests

def api(url: str) -> dict:
    response = requests.get(url)
    return response.json()

def fix(price: str) -> float:
    return float(price) if '.' in price else int(price)

def get(irl: str='USD', coin: str='BTC') -> dict:
    # binance = api(f'https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{irl.upper()}T')['price']
    kraken = list(api(f'https://api.kraken.com/0/public/Ticker?pair={coin.upper()}{irl.upper()}')['result'].values())[0]['a'][0]
    # bitstamp = api(f'https://www.bitstamp.net/api/v2/ticker/{coin.lower()}{irl.lower()}')['last']

    return {
        # 'binance': fix(binance),
        'kraken': fix(kraken),
        # 'bitstamp': fix(bitstamp),
    }

if __name__ == '__main__':
    while True:
        irl = input('Enter irl currency: ')
        coin = input('Enter coin: ')
        print(get(irl, coin))
