from abc import ABC, abstractmethod
import pandas as pd
import zipfile
import os, sys
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.base import RegressorMixin

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))

from Logger import logging
from Exception import CustomizeExcep
from src.Data_split import Split, Spliting_dat
from src.Model_building import ModelBuilding, LinearRegressionStartegy

class ModelEval(ABC):

    def Model_Evaluation(self, model: RegressorMixin, X_test: pd.DataFrame, y_test: pd.Series):

        """
        
        """

        pass
    
class RFRegressionStartegy(ModelEval):

    def Model_Evaluation(self, model: RegressorMixin, X_test: pd.DataFrame, y_test: pd.Series):

        """
        
        """

        logging.info('Model Evaluation start')

        y_pred = model.predict(X_test)

        r_square = r2_score(y_true= y_test, y_pred= y_pred)

        mse = mean_squared_error(y_true= y_test, y_pred= y_pred)

        metrics = {'Mean Square Error': mse, 'R Square Error': r_square}

        logging.info(f'metrics = {metrics}')
        logging.info('Evaluation is ended')

        return metrics

class ModelEvaluation: 

    def __init__(self, strategy: ModelEval):
        """
        
        """
        self._strategy = strategy

    def set_strategy(self, strategy: ModelEval):
        """
        
        """
        logging.info("Switching data splitting strategy.")
        self._strategy = strategy

    def Eval_model(self, model: RegressorMixin, X_test: pd.DataFrame, y_test: pd.Series):
        """
        
        """
        logging.info("Evaluating model using the selected strategy.")
        return self._strategy.Model_Evaluation(model, X_test, y_test)
    
        
"""if __name__ == '__main__': 
  
    model = ModelBuilding(LinearRegressionStartegy())

    X_test = 
    y_test =

    model_evaluate = ModelEvaluation(RFRegressionStartegy())
    evaluation_metrics = model_evaluate.Eval_model(model, X_test, y_test)
    print(evaluation) """