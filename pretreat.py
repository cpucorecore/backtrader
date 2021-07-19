# this script used to prepare data downloading from https://www.cryptodatadownload.com/data/binance/ for backtrader,
# you need to delete the first tow lines of donwloaded file manually

import sys
import csv
from datetime import (datetime, timezone)
from collections import deque

SRC_INDEX_OPEN = 3
SRC_INDEX_HIGH = 4
SRC_INDEX_LOW = 5
SRC_INDEX_CLOSE = 6
SRC_INDEX_VOLUME_IN_BTC = 7
SRC_INDEX_VOLUME_IN_USDT = 8
SRC_INDEX_TRADECOUNT = 9

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('pretreat.py srcFilePath dstFilePath')
        sys.exit()

    srcFilePath = sys.argv[1]
    dstFilePath = sys.argv[2]

    dq = deque([])
    lastLineDatetime = 0
    with open(srcFilePath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            timestamp = row[0]
            unixtimestamp = int(float(timestamp)) if '.' in timestamp else int(int(timestamp) / 1000)  # TODO unit test
            _datetime = datetime.fromtimestamp(unixtimestamp, timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

            # de-duplicate the same datetime line, and use the first duplicated line
            if lastLineDatetime == unixtimestamp:
                continue

            tradecount = row[SRC_INDEX_TRADECOUNT]
            tradecount = 'NaN' if 'NULL' == tradecount else tradecount
            t = (_datetime,
                 row[SRC_INDEX_OPEN],
                 row[SRC_INDEX_HIGH],
                 row[SRC_INDEX_LOW],
                 row[SRC_INDEX_CLOSE],
                 row[SRC_INDEX_VOLUME_IN_BTC],
                 tradecount,
                 row[SRC_INDEX_VOLUME_IN_USDT],
                 row[1],  # datetime in human
                 row[2])  # symbol, eg: BTC/USDT

            line = ','.join(t)
            dq.append(line)

            lastLineDatetime = unixtimestamp

    dstFp = open(dstFilePath, 'w')
    while dq:
        lastRow = dq.pop()
        dstFp.write(lastRow+'\n')

dstFp.flush()
dstFp.close()
