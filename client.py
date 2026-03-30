with open("trading_bot/bot/client.py", "w") as f:
    f.write("""
from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

def get_client():
    return Client(
        os.getenv("BINANCE_API_KEY"),
        os.getenv("BINANCE_API_SECRET"),
        testnet=True
    )
""")
