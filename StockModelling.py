import math
import matplotlib.pyplot as plt
import numpy as np
import random
from pandas_datareader import data
import seaborn as sns

apple = data.DataReader('AAPL', 'yahoo',start='1/1/2009')
apple.head()
time_elapsed = (apple.index[-1] - apple.index[0]).days

total_growth = (apple['Adj Close'][-1] / apple['Adj Close'][1])
number_of_years = time_elapsed / 365.0
cagr = total_growth ** (1/number_of_years) - 1
std_dev = apple['Adj Close'].pct_change().std()
number_of_trading_days = 252
std_dev = std_dev * math.sqrt(number_of_trading_days)


print ("cagr (mean returns) : ", str(round(cagr,4)))
print ("std_dev (standard deviation of return : )", str(round(std_dev,4)))

daily_return_percentages = np.random.normal(cagr/number_of_trading_days, std_dev/math.sqrt(number_of_trading_days),number_of_trading_days+1)
price_series = [apple['Adj Close'][-1]]

for j in daily_return_percentages:
    price_series.append(price_series[-1] * j)


number_of_trials = 3000


closing_prices = []

for i in range(number_of_trials):

    daily_return_percentages = np.random.normal(cagr/number_of_trading_days, std_dev/math.sqrt(number_of_trading_days),
number_of_trading_days)+1
    price_series = [apple['Adj Close'][-1]]

    for j in daily_return_percentages:

        price_series.append(price_series[-1] * j)


    closing_prices.append(price_series[-1])


    plt.plot(price_series)



plt.show()
sns.displot(closing_prices,kde=False, bins=100)


plt.show()