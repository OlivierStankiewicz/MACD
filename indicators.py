def EMA(data, n, p0):
    alpha = 2 / (n+1)

    nominator = 0
    denominator = 0

    index = p0

    for i in range(n+1):
        if index < 0:
            break
        
        nominator += data[index] * (1 - alpha)**i
        denominator += (1 - alpha)**i
        index -= 1

    return nominator / denominator


def MACD(data):
    macd = []
    for i in range(len(data)):
        macd.append(EMA(data, 12, i) - EMA(data, 26, i))

    return macd


def Signal(macd):
    signal = []
    for i in range(len(macd)):
        signal.append(EMA(macd, 9, i))

    return signal

def buySellPoints(macd, signal):
    points = ['']
    for i in range(1, len(macd)):
        if macd[i]>signal[i] and macd[i-1]<signal[i-1]:
            points.append('buy')
        elif macd[i]<signal[i] and macd[i-1]>signal[i-1]:
            points.append('sell')
        else:
            points.append('')

    return points