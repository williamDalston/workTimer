import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

import numpy as np
import pandas as pd

fname = cbook.get_sample_data('msft.csv', asfileobj=False)
with cbook.get_sample_data('msft.csv') as file:
    msft = pd.read_csv(file)

pd.plotting.register_matplotlib_converters()

with cbook.get_sample_data('msft.csv') as file:
    msft = pd.read_csv(file, parse_dates=['Date'])

    msft.plot(0, [5, 6], subplots=True)

    msft.plot("Date", ["Volume", "Adj. Close*"], subplots=True)

    fig, axs = plt.subplots(2, sharex=True)
    msft.plot("Date", "Volume", ax=axs[0], logy=True)
    msft.plot("Date", "Adj. Close*", ax=axs[1])

fig, axs = plt.subplots(2, sharex=True)
msft.plot(0, 5, ax=axs[0], logy=True)
msft.plot(0, 6, ax=axs[1])

msft.plot("Date", ["Open", "High", "Low", "Close"])

fig, axs = plt.subplots(2, sharex=True)
axs[0].bar(msft.iloc[:, 0], msft.iloc[:, 5])
axs[1].plot(msft.iloc[:, 0], msft.iloc[:, 6])
fig.autofmt_xdate()

fname2 = cbook.get_sample_data('data_x_x2_x3.csv', asfileobj=False)
with cbook.get_sample_data('data_x_x2_x3.csv') as file:
    array = np.loadtxt(file)

fig, axs = plt.subplots(2, sharex=True)
axs[0].plot(array[:, 0], array[:, 1])
axs[0].set(ylabel='$f(x)=x^2$')
axs[1].plot(array[:, 0], array[:, 2])
axs[1].set(xlabel='$x$', ylabel='$f(x)=x^3$')

fig, ax = plt.subplots()
ax.plot(array[:, 0], array[:, 1])
ax.plot(array[:, 0], array[:, 2])
ax.set(xlabel='$x$', ylabel='$f(x)=x^3$')

plt.show()