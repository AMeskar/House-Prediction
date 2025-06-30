import pandas as pd
from typing import Tuple

from zenml import step

import mlflow

from sklearn.pipeline import Pipeline

import os, sys
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))
from Logger import logging
from Exception import CustomizeExcep

from src.Model_evaluated import ModelEvaluation, RFRegressionStartegy

@step(enable_cache = False)
def model_evaluating(trained_model: Pipeline, X_test: pd.DataFrame, y_test: pd.Series) -> Tuple[dict, float] :
    
    """

    """
    # Type Error check
    if not isinstance(X_test, pd.DataFrame):
        logging.info('This is not the right type of X_train')
        CustomizeExcep(TypeError)
    if not isinstance(y_test, pd.Series):
        logging.info('This is not the right type of y_train')
        CustomizeExcep(TypeError)

    logging.info('Applying preprocesisng to the test data')

    X_test_prepro = trained_model.named_steps['preprocessor'].transform(X_test)

    evaluator = ModelEvaluation(RFRegressionStartegy())

    evaluation = evaluator.Eval_model(
        trained_model.named_steps['Model'], X_test_prepro, y_test
    )

    if not isinstance(evaluation, dict):

        raise CustomizeExcep(TypeError)
    
    mse = evaluation.get('Mean Square Error', None)
    return evaluation, mse