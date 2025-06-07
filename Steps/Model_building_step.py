from zenml import Model, step, pipeline
import sys, os
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))

from Logger import logging
from Exception import CustomizeExcep
from src.Ingest_data import  file_ext
from src.Handling_MV import Single_Imputation, KNN_imputation, Iterative_imputation, switch_btw_methods

@step 
def Model_build(df: pd.DataFrame, strategy: str):

    if strategy == 'Single Imputation':
        
        obj = switch_btw_methods(Single_Imputation())

        df = obj.apply_strategy(df) 
    
        logging.info('Data is imputed by Single Imputation method')

        return df 

    elif strategy == 'KNN':

        obj = switch_btw_methods(KNN_imputation())

        df = obj.apply_strategy(df) 

        logging.info('Data is imputed by Single Imputation method')

        return df 

    elif strategy == 'Iterative':
    
        obj = switch_btw_methods(Iterative_imputation())

        df = obj.apply_strategy(df) 

        logging.info('Data is imputed by Single Imputation method')

        return df 
        
    else:

        logging.info('Method Mention is not included in our code')
        
        raise CustomizeExcep('Method you Mention is Unavailable', sys)
    