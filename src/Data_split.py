from abc import ABC, abstractmethod
import pandas as pd
import zipfile
import os, sys
from sklearn.model_selection import train_test_split

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))

from Logger import logging
from Exception import CustomizeExcep


class SplitData(ABC):

    def train_test(self, df: pd.DataFrame, target: str):

        """
        
        """

        pass


class Spliting_dat(SplitData):

    def __init__(self, test_size= 0.2, random_seed = 42):

        self.test_sie = test_size
        self.random_seed = random_seed

    def train_test(self, df: pd.DataFrame, target: str):

        """
        
        """

        logging.info('Starting the spliting of data')

        X = df.drop(columns=target)
        y = df[target]

        x_train, x_test, y_train, y_test = train_test_split(X, y, test_size= self.test_sie, random_state= self.random_seed)

        logging.info('Spliting is now complete')

        return x_train, x_test, y_train, y_test

class file_ext: 

    def __init__(self, strategy: Spliting_dat):
        """
        
        """
        self._strategy = strategy

    def set_strategy(self, strategy: Spliting_dat):
        """
        
        """
        logging.info("Switching data splitting strategy.")
        self._strategy = strategy

    def split(self, df: pd.DataFrame, target_column: str):
        """
        
        """
        logging.info("Splitting data using the selected strategy.")
        return self._strategy.train_test(df, target_column)
        
if __name__ == '__main__': 
  
    df = pd.read_csv("/Users/meskara/Desktop/Github/Real_Estatet_endtoend/src/extracted_data/AmesHousing.csv") 

    strategy = file_ext(Spliting_dat()) 
    
    x_train, x_test, y_train, y_test = strategy.split(df, 'SalePrice') 
        
    print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
