import sys
from _datetime import datetime
import backtrader as bt
import backtrader.feeds as btfeeds

from strategies.SmaCross import SmaCross

csvfilepath = 'data/Binance_BTCUSDT_1h.csv'
initcash = 1000000

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('python main.py fromDate toDate')
        print('eg: python main.py 2021-01-01 2021-01-31')
        sys.exit()

    fromdate = datetime.fromisoformat(sys.argv[1])
    todate = datetime.fromisoformat(sys.argv[2])

    cerebro = bt.Cerebro()
    cerebro.broker.setcash(initcash)

    data = btfeeds.GenericCSVData(
        dataname=csvfilepath,

        fromdate=fromdate,
        todate=todate
    )

    cerebro.adddata(data)
    cerebro.addstrategy(SmaCross)
    cerebro.run()
    cerebro.plot()
