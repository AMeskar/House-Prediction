from abc import ABC, abstractmethod
import pandas as pd
import zipfile
import os, sys
sys.path.append(os.getcwd())

from Logger import logging
from Exception import CustomizeExcep

# First of all an abstract class with the biseline function

class ingest(ABC):

    @abstractmethod
    def ingest_data(self, file_path: str) -> pd.DataFrame:
        # this function basically take a path and transform it into a data frame, of course after processing
        pass

# we will create a class that chick weither a file is actually exist or not

# After checking the file we need to extract the data and store the data into a list of csv's

class extract_file(ingest):

    def ingest_data(self, file_path: str) -> pd.DataFrame:

        if not file_path.endswith('.zip'):

            raise ValueError('This file is either corrupted or is not a zip file')

        with zipfile.ZipFile(file_path, 'r') as zip_ref:

            zip_ref.extractall('Extracted_data')

        extract_file = os.listdir('Extracted_data')

        csv_file = [f for f in extract_file if f.endswith('.csv')]

        if len(csv_file) == 0:

            raise ValueError('There no cv in the zip file')
        
        elif len(csv_file) > 1 :

            raise ValueError('ATTENTION: theres more than one csv file. Please specifiy which one u will work with')

        csv = os.path.join('Extracted_data', csv_file[0])

        df = pd.read_csv(csv)

        return df

class file_ext: 

    @staticmethod

    def ext(file_extenstion: str) -> ingest :

        # If the file extension meet the criteria it will directed to the extracton file class
        try:

            if file_extenstion  == '.zip': return extract_file()

            else: 

                raise ValueError('Unsupported file type. Only .zip files are allowed.')
        
        except Exception as e:

            logging.error("An error occurred during file type dispatch.", exc_info = True)

            raise CustomizeExcep(e)
        

"""
if __name__ == '__main__': # The main function, I have no idea why but looks like if this is the main function it will strat
            
    file_path = "/home/amine/Desktop/Projects/Real_Estatet_endtoend/data/archive.zip"

    file_exten = os.path.splitext(file_path)[1] # without [1], ('/home/amine/Desktop/Projects/Real_Estatet_endtoend/data/archive', '.zip') split text into path and extension

    obj = file_ext.ext(file_extenstion=file_exten) # it will gave u the object if its correct so this is that will be used for returning data frame

    df = obj.ingest_data(file_path)

    print(df.head(5))

    pass

"""