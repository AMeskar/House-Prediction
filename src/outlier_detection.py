from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import os, sys

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))

from Logger import logging


class OutlierDetectionStrategy(ABC):
    @abstractmethod
    def detect_outliers(self, df: pd.DataFrame) -> pd.DataFrame:
        """

        """
        pass

class ZScoreOutlierDetection(OutlierDetectionStrategy):

    """
    
    """

    def __init__(self, ther = 3):
        
        self.ther = ther

    def detect_outliers(self, df: pd.DataFrame):

        """
        
        """

        logging.info(f'Detectiong Outliers using standard scaling with a threshold of {self.ther}')

        z_score = np.abs((df - df.mean()) / df.std())

        outliers = z_score > self.ther

        logging.info('Outlier is detected')

        return outliers
    

class IQROutlierDetection(OutlierDetectionStrategy):

    def detect_outliers(self, df: pd.DataFrame):
    
        logging.info('Detecting outliers using the IQR method')

        Q1 = df.quantile(0.25)
        Q3 = df.quantile(0.75)
        IQR = Q3 - Q1
        
        outliers = (df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))

        logging.info('Detecting outliers is Completed')

        return outliers
    
class OutlierDetector:
    def __init__(self, strategy: OutlierDetectionStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: OutlierDetectionStrategy):
        logging.info("Switching outlier detection strategy.")
        self._strategy = strategy

    def detect_outliers(self, df: pd.DataFrame) -> pd.DataFrame:

        logging.info("Executing outlier detection strategy.")

        return self._strategy.detect_outliers(df)
    
    def handling_outliers(self, df: pd.DataFrame, method: str):

        outliers = self.detect_outliers(df)

        if method == 'remove':

            logging.info('The dataframe will start removing outliers')

            df_cleaned = df[(~outliers).all(axis=1)]

            logging.info('Rmoving is completed')

            return df_cleaned

        if method == 'capping':

            logging.info('The dataframe will start capping outliers')

            df_cleaned = df.clip(lower=df.quantile(0.01), upper=df.quantile(0.99), axis=1)

            return df_cleaned

        else : 

            logging.warning(f"Unknown method '{method}'. No outlier handling performed.")

            return df
        
    def visualising_outliers(self, df: pd.DataFrame, features):

        logging.info(f"Visualizing outliers for features: {features}")

        for feature in features:
            plt.figure(figsize=(10, 6))
            sns.boxplot(x=df[feature])
            plt.title(f"Boxplot of {feature}")
            plt.show()

        logging.info("Outlier visualization completed.")

if __name__ == "__main__":

    df = pd.read_csv("/Users/meskara/Desktop/Github/Real_Estatet_endtoend/src/extracted_data/AmesHousing.csv")
    df_numeric = df.select_dtypes(include=[np.number]).dropna()

    outlier_detector = OutlierDetector(ZScoreOutlierDetection(ther=3))

    outliers = outlier_detector.detect_outliers(df_numeric)
    df_cleaned = outlier_detector.handling_outliers(df_numeric, method= "remove")

    print(df_cleaned.shape)
    outlier_detector.visualising_outliers(df_cleaned, features=["SalePrice", "Gr Liv Area"])

