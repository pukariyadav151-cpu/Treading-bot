import logging
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from config import ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL

logger = logging.getLogger(__name__)

class BrokerClient:
    def __init__(self):
        try:
            self.client = TradingClient(
                api_key=ALPACA_API_KEY,
                secret_key=ALPACA_SECRET_KEY,
                base_url=ALPACA_BASE_URL
            )
            logger.info("Connected to Alpaca")
        except Exception as e:
            logger.error(f"Broker error: {e}")
            self.client = None
    
    def get_account(self):
        try:
            account = self.client.get_account()
            return {
                'buying_power': float(account.buying_power),
                'cash': float(account.cash),
                'portfolio_value': float(account.portfolio_value),
                'unrealized_pl': float(account.unrealized_pl),
            }
        except Exception as e:
            logger.error(f"Account error: {e}")
            return None
    
    def get_positions(self):
        try:
            positions = self.client.get_all_positions()
            return [{
                'symbol': p.symbol,
                'qty': float(p.qty),
                'avg_fill_price': float(p.avg_fill_price),
                'current_price': float(p.current_price),
            } for p in positions]
        except Exception as e:
            logger.error(f"Positions error: {e}")
            return []
    
    def place_market_order(self, symbol, qty, side='buy'):
        try:
            order_side = OrderSide.BUY if side.lower() == 'buy' else OrderSide.SELL
            order_request = MarketOrderRequest(
                symbol=symbol,
                qty=int(qty),
                side=order_side,
                time_in_force=TimeInForce.DAY
            )
            order = self.client.submit_order(order_request)
            logger.info(f"Order: {side.upper()} {qty} {symbol}")
            return {'order_id': order.id, 'symbol': order.symbol}
        except Exception as e:
            logger.error(f"Order error: {e}")
            return None
