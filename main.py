import datetime
import backtrader as bt
import backtrader.feeds as btfeeds


class SmaCross(bt.Strategy):
    # list of parameters which are configurable for the strategy
    params = dict(
        pfast=10,  # period for the fast moving average
        pslow=30   # period for the slow moving average
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


if __name__ == '__main__':
    cerebro = bt.Cerebro()  # create a "Cerebro" engine instance

    # Create a data feed
    # data = bt.feeds.YahooFinanceData(dataname='MSFT',
    #                                  fromdate=datetime(2011, 1, 1),
    #                                  todate=datetime(2012, 12, 31))

    data = btfeeds.GenericCSVData(
        dataname='./data/Binance_BTCUSDT_d.csv',

        datetime=1,
        high=4,
        low=5,
        open=3,
        close=6,
        volume=9
    )

    cerebro.adddata(data)  # Add the data feed

    cerebro.addstrategy(SmaCross)  # Add the trading strategy
    cerebro.run()  # run it all
    cerebro.plot()  # and plot it with a single command