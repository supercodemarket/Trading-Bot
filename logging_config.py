with open("trading_bot/bot/logging_config.py", "w") as f:
    f.write("""
import logging

def setup_logging():
    logging.basicConfig(
        filename="trading_bot.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
""")
  
