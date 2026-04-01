with open("trading_bot/bot/orders.py", "w") as f:
    f.write("""
from bot.client import get_client
import logging

client = get_client()

def place_market_order(symbol, side, quantity):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
        logging.info(f"Market Order Response: {order}")
        return order
    except Exception as e:
        logging.error(f"Market Order Error: {e}")
        raise

def place_limit_order(symbol, side, quantity, price):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )
        logging.info(f"Limit Order Response: {order}")
        return order
    except Exception as e:
        logging.error(f"Limit Order Error: {e}")
        raise
""")
