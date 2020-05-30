import pandas as pd

import os

class Data:

    def __init__(self):

        pass

    def data_dir(self):
        '''
        Return the absolute path of the data dir
        '''

        return os.path.abspath(os.path.join(__file__, '../../data/'))

    def csvs(self):
        '''
        Return list of csv file names
        '''

        files = os.listdir(self.data_dir())
        files = [os.path.join(self.data_dir(), file) for file in files]

        return files

    def read_data(self):
        '''
        Return DataFrame after reading
        '''

        dfs = [pd.read_csv(file) for file in self.csvs()]
        df = pd.concat(dfs).reset_index(drop=True)

        return df

    def read_clean_data(self):
        '''
        Return DataFrame with clean observations
        '''

        df = self.read_data()

        df['Date'] = pd.to_datetime(df['Date'])
        df['Year'] = df['Date'].dt.year
        df['Month'] = df['Date'].dt.month

        return df


if __name__ == '__main__':

    d = Data()

    df = d.read_data()
