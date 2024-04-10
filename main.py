import pandas
from matplotlib import pyplot
import plots, indicators, algorithm
from copy import deepcopy

def dateToId(data, date):
    date = pandas.to_datetime(date)
    for i in range(len(data)):
        if data[i] == date:
            return i
    
    return None

def shortenData(data, start, end):
    newData = deepcopy(data)
    newData = newData.loc[start:end-1]
    return newData

# import data
data = pandas.read_csv("bnb_v_d.csv", nrows = 1000)
data['Date'] = pandas.to_datetime(data['Date'])

# calculate macd, signal and crossing points
macd = indicators.MACD(data['Close'])
signal = indicators.Signal(macd)
buy_sell = indicators.buySellPoints(macd, signal)

# main charts
plots.plotStockQuote(data, save="glowne/Notowanie_BNB.png")
plots.plotMACDandSIGNAL(macd, signal, data, buy_sell, save="glowne/MACD_SIGNAL.png")
plots.plotStockQuote(data, buy_sell, save="glowne/Notowanie_z_punktami_bs")
#pyplot.show()

# buy/sell charts of specific periods
periods = [
    ["2023-01-10", "2023-06-01"],
    ["2021-10-15", "2022-02-01"],
    ["2022-05-15", "2022-08-15"]
]

for period in periods:
    start = dateToId(data['Date'], period[0])
    end = dateToId(data['Date'], period[1])
    newData = shortenData(data, start, end+1)
    plots.plotStockQuote(newData, buy_sell, save=f"notowania_i_wskazniki/okres_{period[0]}_do_{period[1]}_notowanie.png")
    plots.plotMACDandSIGNAL(macd[start:end+1], signal[start:end+1], newData, buy_sell, save=f"notowania_i_wskazniki/okres_{period[0]}_do_{period[1]}_wskazniki.png")
    #pyplot.show()

# trading algorithm
periods = [
    ["2021-07-11", "2022-04-05"],
    ["2022-04-05", "2023-04-05"],
    ["2023-04-05", "2024-04-05"]
]

print("CAŁY OKRES")
wallet_history, stock_history = algorithm.trade(data, buy_sell)
plots.plotTransactions(data, wallet_history, stock_history, save="transakcje/caly_okres_transakcje.png")
#pyplot.show()

print("WARTOŚĆ 1000 BNB NA KONIEC OKRESU")
print("TO BY SIĘ STAŁO GDYBY KUPIĆ 1000 BNB NA POCZĄTKU I TRZYMAĆ")
diamond_hands = 1000*data['Close'][data.index[-1]]
print(f'Kapitał końcowy: {diamond_hands}$')
print(f'Wynik: {diamond_hands - 1000*data["Close"][0]}$\n')

for period in periods:
    start = dateToId(data['Date'], period[0])
    end = dateToId(data['Date'], period[1])
    newData = shortenData(data, start, end+1)
    wallet_history, stock_history = algorithm.trade(newData, buy_sell)
    plots.plotTransactions(newData, wallet_history, stock_history, save=f"transakcje/okres_{period[0]}_do_{period[1]}_transakcje.png")
    #pyplot.show()
