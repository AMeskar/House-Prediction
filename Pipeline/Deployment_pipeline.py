import os

from Pipeline.Training_pipeline import ml_pipeline
from Steps.Dynamic_importer import dynamic_importer
from Steps.prediction_service_loader import prediction_service_loader

from zenml import pipeline
from zenml.integrations.mlflow.steps import mlflow_model_deployer_step

requirements_txt = os.path.join(os.path.dirname(__file__), 'requirements.txt')

@pipeline
def continuous_deployement_pipeline():

    model = ml_pipeline()

    mlflow_model_deployer_step(workers= 3, deploy_decision = True, model= model)

@pipeline(enable_cache = False)
def inference_pipeline():

    batch_data = dynamic_importer()

    model_deplyment_service = prediction_service_loader(
        pipeline_name= 'continuous_deployement_pipeline',
        step_name = 'mlflow_model_deployer_step',
    )

    