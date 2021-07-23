# backtrader

## prepare
```shell
pip install matplotlib==3.2.2
pip install backtrader
```

## data
download data from 'https://www.cryptodatadownload.com/data/binance/' being saved in Binance_BTCUSDT_1h.csv.raw
use preparecsv.py to prepare data into data/Binance_BTCUSDT_1h.csv
```shell
python pretreat.py ./data/Binance_BTCUSDT_1h.csv.raw ./data/Binance_BTCUSDT_1h.csv 
```

## execute
```shell
python main.py ./data/Binance_BTCUSDT_1h.csv 2021-01-01 2021-07-01
```
