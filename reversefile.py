from collections import deque

srcFile = './data/Binance_BTCUSDT_d.csv.raw'
dstFile = './data/Binance_BTCUSDT_d.csv'

dstFp = open(dstFile, 'x')

with open(srcFile, 'r', encoding='utf-8') as fb:
    dq = deque(fb)

while dq:
    last_row = dq.pop()
    dstFp.write(last_row)

dstFp.flush()
dstFp.close()
fb.close()
