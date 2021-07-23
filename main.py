import sys
from _datetime import datetime
import backtrader as bt
import backtrader.feeds as btfeeds

from strategies.SmaCross import SmaCross
from strategies.Sma3 import Sma3
from strategies.Sma3x import Sma3x

initcash = 10000
if __name__ == '__main__':
    bt.indicators.MovingAverageSimple
    if len(sys.argv) != 4:
        print('python main.py dataFile fromDate toDate')
        print('eg: python main.py ./abc.csv 2021-01-01 2021-01-31')
        sys.exit()

    csvfilepath = sys.argv[1]
    fromdate = datetime.fromisoformat(sys.argv[2])
    todate = datetime.fromisoformat(sys.argv[3])

    cerebro = bt.Cerebro()
    cerebro.broker.setcash(initcash)

    data = btfeeds.GenericCSVData(
        dataname=csvfilepath,
        fromdate=fromdate,
        todate=todate,

        datetime=0,
        open=1,
        high=2,
        low=3,
        close=4,
        volume=5,
        openinterest=-1
    )

    cerebro.adddata(data)
    cerebro.addstrategy(Sma3)
    cerebro.run()
    cerebro.plot(style='candle')
