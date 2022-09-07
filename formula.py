def get_lot(pair,entry,sl):

    if pair in ["GBPUSD","USDCHF"]:
        lot = 1/((entry-sl)*10000)
        return lot
    else:
        lot = 1/((entry-sl)*100)
        return lot

def get_pip(pair,entry,exit):

    if pair in ["GBPUSD","USDCHF"]:
        pip = (entry-exit)*10000
        return pip
    else:
        pip = (entry-exit)*100
        return pip


def get_profit(lot,pip):
    profit = lot*100*pip
    return profit

def calculate_profit(pair,entry,exit,sl):
    if pair in ["USDJPY","EURJPY","CADJPY","CHFJPY","NZDJPY","AUDJPY"]:
        lot = 1/((entry-sl)*100)
        pip = (entry-exit)*100
        profit = lot*100*pip
        return profit

        
    else:
        lot = 1/((entry-sl)*10000)
        pip = (entry-exit)*10000
        profit = lot*100*pip
        return profit