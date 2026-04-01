with open("trading_bot/cli.py", "w") as f:
    f.write("""
from bot.orders import place_market_order, place_limit_order
from bot.validators import *
from bot.logging_config import setup_logging

setup_logging()

def run(symbol, side, order_type, quantity, price=None):
    try:
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)

        print("\\n📌 Order Request Summary:")
        print(symbol, side, order_type, quantity, price)

        if order_type == "MARKET":
            response = place_market_order(symbol, side, quantity)

        elif order_type == "LIMIT":
            if not price:
                raise ValueError("Price required for LIMIT order")

            response = place_limit_order(symbol, side, quantity, price)

        print("\\n✅ Order Successful!")
        print("Order ID:", response.get("orderId"))
        print("Status:", response.get("status"))
        print("Executed Qty:", response.get("executedQty"))

    except Exception as e:
        print("\\n❌ Order Failed:", str(e))
""")
