from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily, Stations
import pandas as pd


class TwoStationWeaterData():

    def __init__(self, station_airport, station_stammheim) -> None:
        self.station_airport = station_airport
        self.station_stammheim = station_stammheim

    def get_data_in_time_interval(self, start_date, end_date):
        data_airport = Daily(self.station_airport, start_date, end_date)
        data_airport = data_airport.fetch()
        data_stammheim = Daily(self.station_stammheim, start_date, end_date)
        data_stammheim = data_stammheim.fetch()
        df_concat = pd.concat((data_airport, data_stammheim))
        by_row_index = df_concat.groupby(df_concat.index)
        df_means = by_row_index.mean()
        return data_airport, data_stammheim, df_means
