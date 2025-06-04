from zenml import Model, step, pipeline
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))

from src.Ingest_data import  file_ext

@step

def Ingest_step(file_path: str) :

    ext = '.zitg'

    obj = file_ext.ext(ext)

    df = obj.ingest_data(file_path= file_path)

    return df