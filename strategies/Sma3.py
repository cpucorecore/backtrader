import backtrader as bt


class Sma3(bt.Strategy):
    params = dict(
        pfast=5,
        pmiddle=13,
        pslow=34
    )

    def __init__(self):
        self.sma5 = bt.ind.SMA(period=self.p.pfast)
        self.sma13 = bt.ind.SMA(period=self.p.pmiddle)
        self.sma34 = bt.ind.SMA(period=self.p.pslow)

    def next(self):
        if not self.position:
            if self.sma5 > self.sma13 > self.sma34:
                self.buy()
        else:
            if self.sma5 < self.sma34:
                self.close()
