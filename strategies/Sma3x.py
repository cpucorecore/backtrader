import backtrader as bt


class Sma3x(bt.Strategy):
    params = dict(
        pfast=5,
        pmiddle=13,
        pslow=34,
        p1=0.05,  # 纠缠比例
        p2=0.1  # 发散比例
    )

    def __init__(self):
        self.sma5 = bt.ind.SMA(period=self.p.pfast)
        self.sma13 = bt.ind.SMA(period=self.p.pmiddle)
        self.sma34 = bt.ind.SMA(period=self.p.pslow)
        self.smaX_distance_avg = \
            (abs(self.sma5 - self.sma13) + abs(self.sma13 - self.sma34) + abs(self.sma5 - self.sma34)) / 3

    def next(self):
        if not self.position:
            if (self.sma5 - self.sma13) > (self.sma34 * self.params.p2) and \
                    (self.sma13 - self.sma34) > (self.sma34 * self.params.p2):  # 向上发散买入
                self.buy()

        if self.position:
            # 连续3天纠缠卖出
            if self.smaX_distance_avg < self.sma34 * self.params.p1 and \
                    self.smaX_distance_avg[-1] < self.sma34 * self.params.p1 and \
                    self.smaX_distance_avg[-2] < self.sma34 * self.params.p1:
                self.close()
