import logging
from indicators import TechnicalIndicators

logger = logging.getLogger(__name__)

class TradingStrategy:
    @staticmethod
    def rsi_strategy(data):
        try:
            signal = 'HOLD'
            rsi = data['RSI'].iloc[-1]
            
            if rsi < 30:
                signal = 'BUY'
            elif rsi > 70:
                signal = 'SELL'
            
            return signal, {'rsi': rsi}
        except Exception as e:
            logger.error(f"Error in RSI strategy: {e}")
            return 'HOLD', {}
    
    @staticmethod
    def macd_strategy(data):
        try:
            signal = 'HOLD'
            if len(data) < 2:
                return signal, {}
            
            macd_curr = data['MACD'].iloc[-1]
            signal_curr = data['MACD_Signal'].iloc[-1]
            macd_prev = data['MACD'].iloc[-2]
            signal_prev = data['MACD_Signal'].iloc[-2]
            
            if macd_prev <= signal_prev and macd_curr > signal_curr:
                signal = 'BUY'
            elif macd_prev >= signal_prev and macd_curr < signal_curr:
                signal = 'SELL'
            
            return signal, {'macd': macd_curr}
        except Exception as e:
            logger.error(f"Error in MACD strategy: {e}")
            return 'HOLD', {}
    
    @staticmethod
    def combined_strategy(data):
        try:
            rsi_signal, _ = TradingStrategy.rsi_strategy(data)
            macd_signal, _ = TradingStrategy.macd_strategy(data)
            
            buy_count = sum([1 for s in [rsi_signal, macd_signal] if s == 'BUY'])
            sell_count = sum([1 for s in [rsi_signal, macd_signal] if s == 'SELL'])
            
            if buy_count >= 1:
                return 'BUY', {'rsi': rsi_signal, 'macd': macd_signal}
            elif sell_count >= 1:
                return 'SELL', {'rsi': rsi_signal, 'macd': macd_signal}
            
            return 'HOLD', {'rsi': rsi_signal, 'macd': macd_signal}
        except Exception as e:
            logger.error(f"Error in combined strategy: {e}")
            return 'HOLD', {}
    
    @staticmethod
    def analyze_symbol(data, strategy_name='combined'):
        try:
            data = TechnicalIndicators.add_all_indicators(data)
            data = data.dropna()
            
            if len(data) < 2:
                return 'HOLD', {}
            
            if strategy_name == 'rsi':
                return TradingStrategy.rsi_strategy(data)
            elif strategy_name == 'macd':
                return TradingStrategy.macd_strategy(data)
            else:
                return TradingStrategy.combined_strategy(data)
        except Exception as e:
            logger.error(f"Error analyzing: {e}")
            return 'HOLD', {}
