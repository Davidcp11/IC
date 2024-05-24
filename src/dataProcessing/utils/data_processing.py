import pandas as pd


class DataProcessing:
    def __init__(self, data):
        self.data = data
        self.data['Date'] = pd.to_datetime(self.data['Date'])

    def get_by_date_range(self, start_date, end_date):
        mask = ((self.data['Date'] >= start_date) & (self.data['Date'] <= end_date))
        return self.data.loc[mask]


if __name__ == '__main__':
    df = pd.read_csv('../../dataset/prices_data/BBAS3.SA.csv')
    data_processed = DataProcessing(df)
    print(data_processed.get_by_date_range('2022-01-01', '2022-01-06'))