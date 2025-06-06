import logging
import sys, os
import pandas as pd
from zenml import Model, step, pipeline

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))
from src.outlier_detection import OutlierDetector, ZScoreOutlierDetection, IQROutlierDetection

from Logger import logging
from Exception import CustomizeExcep


@step 
def outlier_values(df: pd.DataFrame, column_name, strategy: str):

    logging.info('Starting the outlier detection')

    if df is None:

        logging.info('Data Frame is empty')

        raise CustomizeExcep('The data frame is empty', sys)
    
    if not isinstance(df, pd.DataFrame):

        logging.info('the data is not a data frame')

        raise CustomizeExcep('Data is not Data frame')
    
    if column_name not in df.columns:

        logging.info()

    if strategy == 'Zscore':

        pass

    if strategy == 'IQR':

        pass

    pass
    