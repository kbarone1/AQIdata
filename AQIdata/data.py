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


    def read_data(self):

        files = os.listdir(self.data_dir())
        files = [os.path.join(self.data_dir(), file) for file in files]

        dfs = [pd.read_csv(file) for file in files]
        df = pd.concat(dfs).reset_index(drop=True)

        return df


if __name__ == '__main__':

    d = Data()

    df = d.read_data()
