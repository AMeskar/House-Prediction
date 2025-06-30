import pandas as pd
from typing import Annotated

from zenml import step, Model, ArtifactConfig
from zenml.client import Client

import mlflow

from sklearn.pipeline import Pipeline
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import  ColumnTransformer
from sklearn.linear_model import LinearRegression

import os, sys
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))
from Logger import logging
from Exception import CustomizeExcep

#experiment_tracker = Client().active_stack.experiment_tracker

model = Model(
    name= 'PriceHouse_Predictor',
    version = None,
    licence = 'Apache 2.0',
    description = 'Real Estate price model predictor'
)

@step(enable_cache = False, model = model)
def model_building(X_train: pd.DataFrame, y_train: pd.Series) -> Annotated[Pipeline, ArtifactConfig(name='sklearn_piepline', is_model_artifact= False)] :
    
    """

    """
    # Type Error check
    if not isinstance(X_train, pd.DataFrame):
        logging.info('This is not the right type of X_train')
        CustomizeExcep(TypeError)
    if not isinstance(y_train, pd.Series):
        logging.info('This is not the right type of y_train')
        CustomizeExcep(TypeError)
    
    # Seperate numerical and categorical 
    numerical_data = X_train.select_dtypes(include='number').columns
    categorical_data = X_train.select_dtypes(exclude='number').columns

    logging.info(f'Numerical data columns {numerical_data}')
    logging.info(f'Categorical data columns {categorical_data}')

    # Pipeline
    numerical_Transformer = IterativeImputer(initial_strategy='median')
    categorical_Transformer = Pipeline(
        steps=[
            ('Iterative Imputation', IterativeImputer(initial_strategy='most_frequent')),
            ('One Hot Encoding', OneHotEncoder(handle_unknown='ignore'))
        ]
    )

    #Transform fit
    preprocessor = ColumnTransformer(
        transformers= [
            ('numeric data', numerical_Transformer, numerical_data),
            ('categorical data', categorical_Transformer, categorical_data)
        ]
    )
    pipeline = Pipeline(steps=[('preprocessor', preprocessor), ('Model', LinearRegression())])

    if not mlflow.active_run():
        mlflow.start_run()
    
    try: 
        mlflow.sklearn.autolog()

        logging.info('Building and Training the linear regression model')
        pipeline.fit(X_train, y_train)
        logging.info('Model training complete')

        one_hot_encoder = (
            pipeline.named_steps['preprocessor'].transformers_[1][1].named_steps['One Hot Encoding']
        )
        one_hot_encoder.fit(X_train[categorical_data])
        expected_columns = numerical_data.tolist() + list(
            one_hot_encoder.get_feature_names_out(categorical_data)
        )
        logging.info(f'Model expects the following columns: {expected_columns}')

    except Exception as e:

        raise CustomizeExcep(e)
    
    finally:
        mlflow.end_run()
    
    return pipeline