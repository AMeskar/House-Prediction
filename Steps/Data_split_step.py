from zenml import Model, step, pipeline
import sys, os
import pandas as pd
from typing import Tuple
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))

from Logger import logging
from Exception import CustomizeExcep
from src.Data_split import Split, Spliting_dat

@step 
def split_data(df: pd.DataFrame, target: str) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series] :

    if df is None:

        logging.info('Data frame is empty')
    
    if df is not isinstance(df, pd.DataFrame):

        logging.info('Data is not a data frame')

    strategy = Split(strategy = Spliting_dat())

    x_train, x_test, y_train, y_test = strategy.split(df, 'SalePrice')

    return x_train, x_test, y_train, y_test
    