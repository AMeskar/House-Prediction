from zenml import Model, step, pipeline
import sys, os
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))

from Logger import logging
from Exception import CustomizeExcep
from src.Ingest_data import  file_ext
from src.Handling_MV import Single_Imputation, KNN_imputation, Iterative_imputation, switch_btw_methods

@step 
def missing_value(df: pd.DataFrame, strategy: str):

    if strategy in 'Single Imputation':
        
        obj = switch_btw_methods(Single_Imputation())

        df = obj.apply_strategy(df) 

    elif strategy in 'KNN':

        obj = switch_btw_methods(KNN_imputation())

        df = obj.apply_strategy(df) 

    elif strategy in 'Iterative':
    
        obj = switch_btw_methods(Iterative_imputation())

        df = obj.apply_strategy(df) 

    else:
        
        raise CustomizeExcep('Method you Mention is Unavailable', sys)