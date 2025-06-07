from abc import ABC, abstractmethod
import pandas as pd
import zipfile
import os, sys
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.base import RegressorMixin
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))

from Logger import logging
from Exception import CustomizeExcep
from src.Data_split import Split, Spliting_dat


class ModelBuild(ABC):

    def Model(self, X_train: pd.DataFrame, y_train: pd.Series):

        """
        
        """

        pass


class LinearRegressionStartegy(ModelBuild):

    def Model(self, X_train: pd.DataFrame, y_train: pd.Series):

        """
        
        """

        logging.info('Starting th model building')

        if X_train is not None:
            logging.info('X train is empty')
        
        if y_train is not None:
            logging.info('y train is empty')
        
        logging.info('Creating the Pipeline')
        
        pipeline = Pipeline(
            [
                ("scaler", StandardScaler()),  
                ("model", LinearRegression()), 
            ]
        )

        logging.info('fitting the model')

        pipeline.fit(X_train, y_train)

        logging.info('The model is fitted')

        return pipeline


class XgBoostRegressorStartegy(ModelBuild):

    def Model(self, X_train: pd.DataFrame, y_train: pd.Series):

        """
        
        """

        logging.info('Starting th model building')

        if X_train is not None:
            logging.info('X train is empty')
        
        if y_train is not None:
            logging.info('y train is empty')
        
        logging.info('Creating the Pipeline')
        
        pipeline = Pipeline(
            [
                ("scaler", StandardScaler()),  
                ("model", RandomForestRegressor()), 
            ]
        )

        logging.info('fitting the model')

        pipeline.fit(X_train, y_train)

        logging.info('The model is fitted')

        return pipeline
    
class RFRegressionStartegy(ModelBuild):

    def Model(self, X_train: pd.DataFrame, y_train: pd.Series):

        """
        
        """

        logging.info('Starting th model building')

        if X_train is not None:
            logging.info('X train is empty')
        
        if y_train is not None:
            logging.info('y train is empty')
        
        logging.info('Creating the Pipeline')
        
        pipeline = Pipeline(
            [
                ("scaler", StandardScaler()),  
                ("model", XGBRegressor()), 
            ]
        )

        logging.info('fitting the model')

        pipeline.fit(X_train, y_train)

        logging.info('The model is fitted')

        return pipeline

class file_ext: 

    def __init__(self, strategy: ModelBuild):
        """
        
        """
        self._strategy = strategy

    def set_strategy(self, strategy: ModelBuild):
        """
        
        """
        logging.info("Switching data splitting strategy.")
        self._strategy = strategy

    def fit_model(self, X_train: pd.DataFrame, y_train: pd.Series):
        """
        
        """
        logging.info("Splitting data using the selected strategy.")
        return self._strategy.Model(X_train, y_train)
"""        
if __name__ == '__main__': 
  
    df = pd.read_csv("/Users/meskara/Desktop/Github/Real_Estatet_endtoend/src/extracted_data/AmesHousing.csv") 

    obj = Split(Spliting_dat()) 
    
    X_train, X_test, y_train, y_test = obj.split(df, 'SalePrice')

    strategy = file_ext(LinearRegressionStartegy()) 
    
    pipeline = strategy.fit_model(X_train, y_train) """