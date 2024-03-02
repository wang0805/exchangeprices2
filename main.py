import ccxt
import streamlit as st


binance = ccxt.binance()
okx = ccxt.okx()
kraken = ccxt.kraken()

exchanges = [okx, kraken, binance]


def fetch_prices():

    # Initialize dictionaries to store bid and ask data for each exchange
    bids = {}
    asks = {}

    # Fetch order book data for each exchange and store the best bid and ask
    for exchange in exchanges:
        orderbook = exchange.fetch_order_book('USDC/USDT')
        bid = orderbook['bids'][0][0] if len(orderbook['bids']) > 0 else None
        ask = orderbook['asks'][0][0] if len(orderbook['asks']) > 0 else None
        bids[exchange.id] = bid
        asks[exchange.id] = ask

    # Find the exchange with the best bid and ask
    best_bid_exchange = max(bids, key=bids.get)
    best_ask_exchange = min(asks, key=asks.get)

    # Get the best bid and ask prices
    best_bid = bids[best_bid_exchange]
    best_ask = asks[best_ask_exchange]

    # print('Best Bid:')
    # print(best_bid_exchange, 'Bid Price:', best_bid)

    # print('Best Ask:')
    # print(best_ask_exchange, 'Ask Price:', best_ask)
    # data = {
    #     'Best Bid': best_bid,
    #     'Best Ask': best_ask,
    # }
    return best_bid, best_ask, best_bid_exchange, best_ask_exchange


# if __name__ == '__main__':
#     app.run(debug=True)

st.title('Stablecoin Pricer')

best_bid, best_ask, best_bid_exchange, best_ask_exchange = fetch_prices()
st.write(f"Best Bid: {best_bid}")
st.write(f"Best Ask: {best_ask}")

if st.button('Refresh'):
    best_bid, best_ask, best_bid_exchange, best_ask_exchange = fetch_prices()
    # st.write(f"Best Bid: {best_bid} from {best_bid_exchange}")
    # st.write(f"Best Ask: {best_ask} from {best_ask_exchange}")
    st.write(f"Best Bid: {best_bid}")
    st.write(f"Best Ask: {best_ask}")
