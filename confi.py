import os
from dotenv import load_dotenv

load_dotenv()

ALPACA_API_KEY = os.getenv('ALPACA_API_KEY')
ALPACA_SECRET_KEY = os.getenv('ALPACA_SECRET_KEY')
ALPACA_BASE_URL = os.getenv('ALPACA_BASE_URL', 'https://paper-api.alpaca.markets')

TRADING_SYMBOLS = os.getenv('TRADING_SYMBOLS', 'AAPL,GOOGL,MSFT').split(',')
INITIAL_CAPITAL = float(os.getenv('INITIAL_CAPITAL', 10000))
RISK_PER_TRADE = float(os.getenv('RISK_PER_TRADE', 0.02))
MAX_POSITIONS = int(os.getenv('MAX_POSITIONS', 5))

RSI_PERIOD = int(os.getenv('RSI_PERIOD', 14))
RSI_OVERBOUGHT = int(os.getenv('RSI_OVERBOUGHT', 70))
RSI_OVERSOLD = int(os.getenv('RSI_OVERSOLD', 30))

MACD_FAST = int(os.getenv('MACD_FAST', 12))
MACD_SLOW = int(os.getenv('MACD_SLOW', 26))
MACD_SIGNAL = int(os.getenv('MACD_SIGNAL', 9))

STOP_LOSS_PERCENT = 0.05
TAKE_PROFIT_PERCENT = 0.10
MAX_DRAWDOWN = 0.20

MARKET_OPEN = '09:30'
MARKET_CLOSE = '16:00'
CHECK_INTERVAL = 60

LOG_LEVEL = 'INFO'
LOG_FILE = 'trading_bot.log'
