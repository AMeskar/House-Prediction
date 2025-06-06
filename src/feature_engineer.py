from abc import ABC, abstractmethod
import pandas as pd
import numpy as np
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))
from Logger import logging

from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder

class Feature_eng(ABC):
    
    @abstractmethod

    def apply_Transformation(self, df: pd.DataFrame):

        """
        
        """

        pass

class LogScaling(Feature_eng):
    
    def __init__(self, features):
        
        self.features = features

    def apply_Transformation(self, df: pd.DataFrame):

        """
        
        """

        logging.info(f'Scaling features {self.features} using log scale to remove skewness or minimize it')

        df_transform = df.copy()
        
        for feature in self.features :

            df_transform[feature] = np.log1p(df_transform[feature])
        
        logging.info('Logarithmic Scaling is now Complete')

        return df_transform

class Standar_Scaling(Feature_eng):

    def __init__(self, features):

        self.features = features
        self.scaler = StandardScaler()
 
    def apply_Transformation(self, df: pd.DataFrame):
        
        """
        inspect take Data Frame (df)
        
        return ==> Inspection stat  describtion
        
        """
        logging.info(f'Standard Scaling is setting up for {self.features}')
        df_transform = df.copy()
        df_transform[self.features] = self.scaler.fit_transform(df_transform[self.features])
        logging.info(f'Standard Scaling is Completed')

        return df_transform

class MinMax_Scaling(Feature_eng):

    def __init__(self, features):

        self.features = features
        self.scaler = MinMaxScaler()
        
    def apply_Transformation(self, df: pd.DataFrame):
        
        """
        inspect take Data Frame (df)
        
        return ==> Inspection stat  describtion
        
        """

        logging.info(f'Min Max Scaler is setting up for {self.features}')
        df_transform = df.copy()
        df_transform[self.features] = self.scaler.fit_transform(df_transform[self.features])
        logging.info('Scaling is now completed')

        return df_transform

class OneHot_encoding(Feature_eng):

    def __init__(self, features):

        self.features = features
        self.encoded = OneHotEncoder()
    
    def apply_Transformation(self, df: pd.DataFrame):
        
        """
        inspect take Data Frame (df)
        
        return ==> Inspection stat  describtion
        
        """

        logging.info(f'Apply One hot encoding fro our categorical data {self.features}')
        df_transform = df.copy()

        encoded_df = pd.DataFrame(
            self.encoded.fit_transform(df[self.features]).toarray(),
            columns=self.encoded.get_feature_names_out(self.features),
        )

        df_transform = df_transform.drop(columns= self.features).reset_index(drop= True)
        df_transform = pd.concat([df_transform, encoded_df], axis= 1)

        return df_transform

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
        
        return self._stratgey.apply_Transformation(Df)
    
"""   
if __name__=='__main__':
    
    df = pd.read_csv("/Users/meskara/Desktop/Github/Real_Estatet_endtoend/src/extracted_data/AmesHousing.csv") 

    strategy = switch_btw_methods(LogScaling(features= ['SalePrice', 'Gr Liv Area'])) 
    
    df_log = strategy.apply_strategy(df) 

    strategy.set_strategty(MinMax_Scaling(features=['SalePrice', 'Gr Liv Area'])) 
    
    df_MinMax = strategy.apply_strategy(df) 

    strategy.set_strategty(Standar_Scaling(features=['SalePrice', 'Gr Liv Area'])) 
    
    df_Scale = strategy.apply_strategy(df) 
    
    strategy.set_strategty(OneHot_encoding(features= ['Neighborhood'])) 
    
    df_OneHot = strategy.apply_strategy(df) 

    print(df_OneHot)"""
