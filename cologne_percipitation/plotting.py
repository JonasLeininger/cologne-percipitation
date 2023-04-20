import matplotlib.pyplot as plt
import pandas as pd

def plot_2station_percipitation_per_day(data_station1: pd.DataFrame, data_station2: pd.DataFrame):
    df_concat = pd.concat((data_station1, data_station2))
    by_row_index = df_concat.groupby(df_concat.index)
    df_means = by_row_index.mean()
    df_means.head()

    fig, (ax1, ax2) = plt.subplots(2, 1, constrained_layout=True, sharey=True, figsize=(14, 8))
    ax1.scatter(data_station1.index, data_station1['prcp'])
    ax1.plot(data_station1.index, data_station1['prcp'], color='b')
    ax1.scatter(data_station2.index, data_station2['prcp'], color='g')
    ax1.plot(data_station2.index, data_station2['prcp'], color='g')
    ax1.set_xlabel('time')
    ax1.set_ylabel('[mm]')

    ax2.scatter(df_means.index, df_means['prcp'])
    ax2.plot(df_means.index, df_means['prcp'], color='r')
    ax2.set_xlabel('time')
    ax2.set_ylabel('[mm]')
    plt.show()
