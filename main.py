import sys
from _datetime import datetime
import backtrader as bt
import backtrader.feeds as btfeeds


class SmaCross(bt.Strategy):
    # list of parameters which are configurable for the strategy
    params = dict(
        pfast=5,  # period for the fast moving average
        pslow=13   # period for the slow moving average
    )

    def __init__(self):
        sma1 = bt.ind.SMA(period=self.p.pfast)  # fast moving average
        sma2 = bt.ind.SMA(period=self.p.pslow)  # slow moving average
        self.crossover = bt.ind.CrossOver(sma1, sma2)  # crossover signal

    def next(self):
        if not self.position:  # not in the market
            if self.crossover > 0:  # if fast crosses slow to the upside
                self.buy()  # enter long

        elif self.crossover < 0:  # in the market & cross to the downside
            self.close()  # close long position


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
        todate=todate,

        datetime=0,
        open=1,
        high=2,
        low=3,
        close=4,
        volume=5
    )

    cerebro.adddata(data)
    cerebro.addstrategy(SmaCross)
    cerebro.run()
    print(cerebro.broker.getcash)
    cerebro.plot()
