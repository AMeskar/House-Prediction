from zenml import Model, step, pipeline
import os, sys

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))

from Steps.Ingestion import Ingest_step

@pipeline(

    model = Model(
        name = 'PriceHouse_Predictor'
    ),
)
def ml_pipeline(file_path: str):

    df = Ingest_step(file_path="/Users/meskara/Desktop/Github/Real_Estatet_endtoend/data/archive.zip")

    return df
