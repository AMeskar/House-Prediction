from zenml import Model, step, pipeline
import os, sys

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))

from Steps.Ingestion import Ingest_step
from Steps.Handling_MV_step import missing_value

@pipeline(

    model = Model(
        name = 'PriceHouse_Predictor'
    ),
)
def ml_pipeline(file_path: str):

    df = Ingest_step(file_path= file_path)

    df_imputed = missing_value(df, 'Iterative')

    return df
