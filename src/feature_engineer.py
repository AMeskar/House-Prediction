from abc import ABC, abstractmethod
import pandas as pd
import numpy as np
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))
from Logger import logging


class Feature_eng(ABC):
    
    @abstractmethod
    
    def apply_transformation(self, df: pd.DataFrame):
        
        """
        inspect take Data Frame (df)
        
        return ==> Inspection either stat or general describtion
        
        """

        pass
    
class Log_Transformation(Feature_eng):
    
    def __init__(self, Features: str):
        
        """
        inspect take Data Frame (df)
        
        return ==> Inspection general describtion
        
        """
        
        self.Features = Features


class Standar_Scaling(Feature_eng):
    
    def apply_transformation(self, df: pd.DataFrame):
        
        """
        inspect take Data Frame (df)
        
        return ==> Inspection stat  describtion
        
        """

        logging.info('Scaling features using log scale to remove skewness or minimize it')
        df_scaled = np.log1p(df[self.Features])

class MinMax_Scaling(Feature_eng):
    
    def apply_transformation(self, df: pd.DataFrame):
        
        """
        inspect take Data Frame (df)
        
        return ==> Inspection stat  describtion
        
        """

        pass

class OneHot_encoding(Feature_eng):
    
    def apply_transformation(self, df: pd.DataFrame):
        
        """
        inspect take Data Frame (df)
        
        return ==> Inspection stat  describtion
        
        """

        pass


class switch_btw_methods:
    
    def __init__(self, strategy: Feature_eng):
        
        """
        inspect take Data Frame (df)
        
        return ==> initializing the strategy 
        
        """
        
        self._stratgey = strategy
    
    def set_strategty(self, strategy: Feature_eng):
        
        """
        set_strategty take strategy class
        
        return ==> set a new strategy
        
        """
        
        self._stratgey = strategy
    
    def apply_strategy(self, Df: pd.DataFrame):
        
        """
        apply_strategy take Data Frame (df)
        
        return ==> Execute the strategy to data frame
        
        """
        
        return self._stratgey.apply(Df)
    
"""
if __name__=='__main__':
    
    df = pd.read_csv("/Users/meskara/Desktop/Github/Real_Estatet_endtoend/src/extracted_data/AmesHousing.csv") 

    strategy = switch_btw_methods(Iterative_imputation()) 
    
    df = strategy.apply_strategy(df) 
    
    #strategy.set_strategty(RFClassifier_imputation()) 
    
    #strategy.apply_strategy(df) 

    print(df)
"""