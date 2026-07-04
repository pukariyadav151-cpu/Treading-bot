import logging
from config import RISK_PER_TRADE, STOP_LOSS_PERCENT, TAKE_PROFIT_PERCENT

logger = logging.getLogger(__name__)

class RiskManager:
    @staticmethod
    def calculate_position_size(balance, entry_price, stop_loss_price):
        try:
            risk_amount = balance * RISK_PER_TRADE
            price_diff = abs(entry_price - stop_loss_price)
            if price_diff == 0:
                return 0
            return int(risk_amount / price_diff)
        except Exception as e:
            logger.error(f"Position size error: {e}")
            return 0
    
    @staticmethod
    def calculate_stop_loss(entry_price):
        return entry_price * (1 - STOP_LOSS_PERCENT)
    
    @staticmethod
    def calculate_take_profit(entry_price):
        return entry_price * (1 + TAKE_PROFIT_PERCENT)
