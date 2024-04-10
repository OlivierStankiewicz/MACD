from matplotlib import pyplot

def plotStockQuote(data, buy_sell = None, save = None):
    pyplot.figure(figsize=(10, 6))
    pyplot.plot(data['Date'], data['Close'], label='Zamknięcie', color='black')
    pyplot.title('Wykres notowań BNB')
    pyplot.xlabel('Data')
    pyplot.ylabel('Cena [$]')
    pyplot.grid(True)
    pyplot.xticks(rotation=45)

    if buy_sell != None and len(buy_sell) > 0:
        buy_points = []
        sell_points = []
        for i, point in enumerate(buy_sell):
            if i>=data.index[0] and i<=data.index[-1]:
                if point == 'buy':
                    buy_points.append({'Date': data['Date'][i], "Value": data['Close'][i]})
                elif point == 'sell':
                    sell_points.append({'Date': data['Date'][i], "Value": data['Close'][i]})

        pyplot.scatter([point['Date'] for point in buy_points], [point['Value'] for point in buy_points], color='green', marker='^', s=70, label='Kupno', zorder=5)
        pyplot.scatter([point['Date'] for point in sell_points], [point['Value'] for point in sell_points], color='red', marker='v', s=70, label='Sprzedaż', zorder=5)

    pyplot.legend()
    pyplot.tight_layout()

    if save is not None:
        pyplot.savefig(save)


def plotMACDandSIGNAL(macd, signal, data,  buy_sell, save = None):
    pyplot.figure(figsize=(10, 6))
    pyplot.plot(data['Date'], macd, label='MACD', color='blue')
    pyplot.plot(data['Date'], signal, label='SIGNAL', color='red')
    pyplot.title('MACD+SIGNAL')
    pyplot.xlabel('Data')
    pyplot.ylabel('Wartość wskaźnika')
    pyplot.grid(True)
    pyplot.xticks(rotation=45)

    if len(buy_sell) > 0:
        buy_points = []
        sell_points = []
        for i, point in enumerate(buy_sell):
            if i>=data.index[0] and i<=data.index[-1]:
                if point == 'buy':
                    buy_points.append({'Date': data['Date'][i], "Value": macd[i - data.index[0]]})
                elif point == 'sell':
                    sell_points.append({'Date': data['Date'][i], "Value": macd[i - data.index[0]]})

        pyplot.scatter([point['Date'] for point in buy_points], [point['Value'] for point in buy_points], color='green', marker='^', s=70, label='Kupno', zorder=5)
        pyplot.scatter([point['Date'] for point in sell_points], [point['Value'] for point in sell_points], color='red', marker='v', s=70, label='Sprzedaż', zorder=5)

    pyplot.legend()
    pyplot.tight_layout()

    
    if save is not None:
        pyplot.savefig(save)


def plotTransactions(data, wallet_history, stock_history, save = None):
    fig, (ax1, ax2) = pyplot.subplots(nrows=2, figsize=(10, 9))

    ax1.plot(data['Date'], wallet_history, label='kapitał', color='green')
    ax1.set_title('Kapitał')
    ax1.set_xlabel('Data')
    ax1.set_ylabel('Kwota [$]')
    ax1.ticklabel_format(style='plain', axis='y')
    ax1.grid(True)
    ax1.tick_params(axis='x', rotation=45)
    ax1.legend()

    ax2.plot(data['Date'], stock_history, label='ilość BNB', color='black')
    ax2.set_title('Ilość BNB')
    ax2.set_xlabel('Data')
    ax2.set_ylabel('Ilość')
    ax2.grid(True)
    ax2.tick_params(axis='x', rotation=45)
    ax2.legend()

    pyplot.tight_layout() 

    if save is not None:
        pyplot.savefig(save)