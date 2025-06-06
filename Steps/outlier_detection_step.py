import logging
import sys, os
import pandas as pd
from zenml import Model, step, pipeline

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))
from src.outlier_detection import OutlierDetector, ZScoreOutlierDetection, IQROutlierDetection

from Logger import logging
from Exception import CustomizeExcep


@step 
def outlier_values(df: pd.DataFrame, column_name, method, strategy: str):

    logging.info('Starting the outlier detection')

    if df is None:

        logging.info('Data Frame is empty')

        raise CustomizeExcep('The data frame is empty', sys)
    
    if not isinstance(df, pd.DataFrame):

        logging.info('the data is not a data frame')

        raise CustomizeExcep('Data is not Data frame')
    
    if column_name not in df.columns:

        logging.info('Coulmns are not exost in data frames')

        raise CustomizeExcep('Coulmns are not exost in data frames', sys)
    
    df_numeric = df.select_dtypes(include = [int, float])

    if strategy == 'Zscore':

        logging.info('Z score outlier method')

        outlier_detector = OutlierDetector(ZScoreOutlierDetection(ther=3))

        outliers = outlier_detector.detect_outliers(df_numeric)
        df_cleaned = outlier_detector.handling_outliers(df_numeric, method )

        logging.info('Method is now complete')

        return df_cleaned

    elif strategy == 'IQR':

        logging.info('IQR outlier method')

        outlier_detector = OutlierDetector(IQROutlierDetection())

        outliers = outlier_detector.detect_outliers(df_numeric)
        df_cleaned = outlier_detector.handling_outliers(df_numeric, method)

        logging.info('IQR outlier is complete')

        return df_cleaned

    