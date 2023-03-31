import asyncio
import random

class MarketDataFetcher:
    async def fetch(self, symbol):
        await asyncio.sleep(random.random() * 5)  # Simulate a random delay
        return {'symbol': symbol, 'price': random.uniform(100, 200)}

class TradingSignalProcessor:
    async def process(self, market_data):
        await asyncio.sleep(random.random() * 5)  # Simulate a random delay
        return {'symbol': market_data['symbol'], 'signal': random.choice(['BUY', 'SELL'])}

class OrderManager:
    async def submit(self, order):
        await asyncio.sleep(random.random() * 5)  # Simulate a random delay
        return {'symbol': order['symbol'], 'status': 'SUBMITTED'}

    async def cancel(self, order):
        await asyncio.sleep(random.random() * 5)  # Simulate a random delay
        return {'symbol': order['symbol'], 'status': 'CANCELLED'}

class PositionManager:
    async def manage(self):
        await asyncio.sleep(random.random() * 5)  # Simulate a random delay
        return {'positions': [{'symbol': 'AAPL', 'quantity': 100, 'price': 150.0}]}

async def main():
    symbols = ['AAPL', 'GOOG', 'AMZN', 'FB']
    market_data_fetcher = MarketDataFetcher()
    trading_signal_processor = TradingSignalProcessor()
    order_manager = OrderManager()
    position_manager = PositionManager()

    tasks = [asyncio.create_task(market_data_fetcher.fetch(symbol)) for symbol in symbols]
    market_data = await asyncio.gather(*tasks)

    tasks = [asyncio.create_task(trading_signal_processor.process(data)) for data in market_data]
    trading_signals = await asyncio.gather(*tasks)

    orders = []
    for signal in trading_signals:
        if signal['signal'] == 'BUY':
            orders.append({'symbol': signal['symbol'], 'side': 'BUY', 'quantity': 100, 'price': market_data[symbols.index(signal['symbol'])]['price']})
        elif signal['signal'] == 'SELL':
            orders.append({'symbol': signal['symbol'], 'side': 'SELL', 'quantity': 100, 'price': market_data[symbols.index(signal['symbol'])]['price']})

    tasks = [asyncio.create_task(order_manager.submit(order)) for order in orders]
    submitted_orders = await asyncio.gather(*tasks)

    tasks = [asyncio.create_task(order_manager.cancel(order)) for order in orders if order['price'] < market_data[symbols.index(order['symbol'])]['price']]
    cancelled_orders = await asyncio.gather(*tasks)

    position_data = await position_manager.manage()
    positions = position_data['positions']
    print('Open positions:')
    for position in positions:
        print(f'{position["symbol"]}: {position["quantity"]} @ {position["price"]}')

asyncio.run(main())
