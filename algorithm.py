def trade(data, buy_sell, initial_stocks = 1000):
    wallet = 0
    stocks = initial_stocks
    wallet_history = []
    stock_history = []
    for i in data.index:
        if buy_sell[i] == 'buy' and wallet != 0:
            stocks = wallet/data['Close'][i]
            wallet = 0

        elif buy_sell[i] == 'sell' and stocks != 0:
            wallet = stocks*data['Close'][i]
            stocks = 0

        wallet_history.append(wallet)
        stock_history.append(stocks)

    print(f'Działanie algorytmu w okresie {data["Date"][data.index[0]]} - {data["Date"][data.index[-1]]}')
    initial_value = stock_history[0] * data["Close"][data.index[0]]
    end_value = None
    print(f'Kapitał początkowy: {round(stock_history[0], 2)} BNB wartych wtedy: {round(initial_value, 2)}$')
    if stock_history[-1] != 0:
        end_value = stock_history[-1] * data["Close"][data.index[-1]]
        print(f'Kapitał końcowy: {round(stock_history[-1], 2)} BNB wartych: {round(end_value, 2)}$')
    else:
        end_value = wallet_history[-1]
        print(f'Kapitał końcowy: {round(end_value, 2)}$')

    print(f'Wynik: {round(end_value - initial_value, 2)}$\n')

    return wallet_history, stock_history