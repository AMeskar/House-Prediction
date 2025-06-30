from zenml import Model, step, pipeline
import os, sys

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))

from Steps.Ingestion import Ingest_step
from Steps.Handling_MV_step import missing_value
from Steps.feature_engineer_step import feature_eng
from Steps.outlier_detection_step import outlier_values 
from Steps.Data_split_step import split_data
from Steps.Model_building_step import model_building

@pipeline(

    model = Model(
        name = 'PriceHouse_Predictor',
        version = None,
        license = 'Apache 2.0',
        description = 'Real Estate model predictor'
    ),
)
def ml_pipeline():

    """Define an end-to-end machine learning pipeline."""

    # Data Ingestion Step
    raw_data = Ingest_step(
        file_path="/Users/meskara/Desktop/Github/Real_Estatet_endtoend/data/archive.zip"
    )

    # Handling Missing Values Step
    filled_data = missing_value(raw_data, strategy = 'Single Imputation')

    # Feature Engineering Step
    engineered_data = feature_eng(
        filled_data, strategy="log", features=["Gr Liv Area", "SalePrice"]
    )

    clean_data = outlier_values(engineered_data, column_name="SalePrice", method = 'remove', strategy = 'Zscore'
    )

    x_train, x_test, y_train, y_test = split_data(clean_data, 'SalePrice')

    model = model_building(x_train, y_train)


    return model


if __name__ == "__main__":
    # Running the pipeline
    run = ml_pipeline()
