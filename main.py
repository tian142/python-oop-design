import random


class Investment:
    _max_ROI = 2
    _min_ROI = 0
    portofolio_ROI = []

    def __init__(self, amount, years):
        self.amount = int(amount)
        self.years = int(years)

    def calculate_ROI(self):
        ROI = self.amount * \
            (random.randint(Investment._min_ROI, Investment._max_ROI) / 100) * self.years
        print(str(round(ROI, 2)))
        Investment.portofolio_ROI.append(str(round(ROI, 2)))
        print(Investment.portofolio_ROI)

    def __secret_Intel(self):
        print("if your ROI less than 2 percent/year, you are losing money to inflation ")

    def displaySecretIntel(self):
        self.__secret_Intel()


class Stock(Investment):
    _max_ROI = 17.1
    _min_ROI = -17.1

    def __init__(self, amount, years):
        self.amount = int(amount)
        self.years = int(years)

    def calculate_ROI(self):
        ROI = self.amount * \
            (random.randint(int(self._min_ROI), int(
                self._max_ROI)) / 100) * self.years
        print(str(round(ROI, 2)))
        Investment.portofolio_ROI.append(str(round(ROI, 2)))
        print(Investment.portofolio_ROI)

    def __secret_Intel(self):
        print(" 90 percent of traders fail to make money when trading the stock market")

    def displaySecretIntel(self):
        self.__secret_Intel()


class Options(Investment):
    _max_ROI = 50
    _min_ROI = -50

    def __init__(self, amount, years):
        self.amount = int(amount)
        self.years = int(years)

    def calculate_ROI(self):
        ROI = self.amount * \
            (random.randint(int(self._min_ROI), int(
                self._max_ROI)) / 100) * self.years
        print(str(round(ROI, 2)))
        Investment.portofolio_ROI.append(str(round(ROI, 2)))
        print(Investment.portofolio_ROI)

    def __secret_Intel(self):
        print("A call options means you are betting the stock will go up, a put option means you are betting the stock will go down")

    def displaySecretIntel(self):
        self.__secret_Intel()


class Crypto(Investment):
    _max_ROI = 363.6
    _min_ROI = -100

    def __init__(self, amount, years):
        self.amount = int(amount)
        self.years = int(years)

    def calculate_ROI(self):
        ROI = self.amount * \
            (random.randint(int(self._min_ROI), int(
                self._max_ROI)) / 100) * self.years
        print(str(round(ROI, 2)))
        Investment.portofolio_ROI.append(str(round(ROI, 2)))
        print(Investment.portofolio_ROI)

    def __secret_Intel(self):
        print("Bitcoin had an average annual return of 363.6%!!!")

    def displaySecretIntel(self):
        self.__secret_Intel()


US_bond = Investment(100, 1)
US_bond.calculate_ROI()
US_bond = Investment(100, 1)
US_bond.calculate_ROI()
US_bond.displaySecretIntel()


AAPL = Stock(100, 1)
AAPL.calculate_ROI()
AAPL = Stock(100, 1)
AAPL.calculate_ROI()
AAPL.displaySecretIntel()

TSLA_C_500_2021 = Options(100, 1)
TSLA_C_500_2021.calculate_ROI()
TSLA_C_500_2021 = Options(100, 1)
TSLA_C_500_2021.calculate_ROI()
TSLA_C_500_2021.displaySecretIntel()

BTC = Crypto(100, 1)
BTC.calculate_ROI()
BTC = Crypto(100, 1)
BTC.calculate_ROI()
BTC.displaySecretIntel()
