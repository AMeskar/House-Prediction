from zenml import Model, step, pipeline
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))

from Logger import logging
from Exception import CustomizeExcep
from src.Ingest_data import  file_ext

@step
def Ingest_step(file_path: str) :

    ext = '.zip'

    obj = file_ext.ext(file_extenstion= ext)

    df = obj.ingest_data(file_path= file_path)

    return df
