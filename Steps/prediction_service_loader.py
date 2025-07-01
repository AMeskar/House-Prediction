from zenml import step
from zenml.integrations.mlflow.model_deolyers import MLFlowModelDeployer

import os, sys
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))

from Logger import logging
from Exception import CustomizeExcep

@step(enable_cache = False)
def prediction_service_loader(pipeline_name: str, step_name:str) -> MLFlowModelDeployer:

    model_deployer = MLFlowModelDeployer.get_active_model_deployer()

    exesting_services = model_deployer.find_model_server(
        pipeline_name = pipeline_name,
        pipeline_step_name= step_name
    )

    if not exesting_services:
        raise CustomizeExcep(RuntimeError(
            f"No Mlflow prediction service deployed by the "
            f"{step_name} step in the {pipeline_name}"
            f"pipeline is currently"
            f"running."
        ))
    
    return exesting_services[0]