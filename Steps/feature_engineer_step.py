from zenml import Model, step, pipeline
import sys, os
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))

from Logger import logging
from Exception import CustomizeExcep
from src.feature_engineer import switch_btw_methods, LogScaling, MinMax_Scaling, Standar_Scaling, OneHot_encoding

@step 
def feature_eng(df: pd.DataFrame, strategy: str, features):

    if strategy == 'log':
        
        obj = switch_btw_methods(LogScaling(features = features))

        df = obj.apply_strategy(df) 
    
        logging.info('Data is scaled by log sclae method')

        return df 

    elif strategy == 'MinMax':

        obj = switch_btw_methods(MinMax_Scaling(features = features))

        df = obj.apply_strategy(df) 

        logging.info('Data is scaled by Min Max scale method')

        return df 

    elif strategy == 'Standard':
    
        obj = switch_btw_methods(Standar_Scaling(features = features))

        df = obj.apply_strategy(df) 

        logging.info('Data is scaled by Standard Scaling method')

        return df
    
    elif strategy == 'One':
    
        obj = switch_btw_methods(OneHot_encoding(features = features))

        df = obj.apply_strategy(df) 

        logging.info('Data is encoded by one hot encoding method')

        return df 
        
    else:

        logging.info('Method Mention is not included in our code')
        
        raise CustomizeExcep('Method you Mention is Unavailable', sys)
    