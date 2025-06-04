from abc import ABC, abstractmethod
import pandas as pd

# I need two inspection, general info (number of rows, columns, null values ...)
# I need the second inspection statistical inspection (means, variance, ...)

class Inspection(ABC):
    
    @abstractmethod
    
    def inspec(self, df: pd.DataFrame):
        
        """
        inspect take Data Frame (df)
        
        return ==> Inspection either stat or general describtion
        
        """
        
        pass
    
class General_inspec(Inspection):
    
    def inspec(self, df: pd.DataFrame):
        
        """
        inspect take Data Frame (df)
        
        return ==> Inspection general describtion
        
        """
        
        print('General describtion to the data frame', df.info())

class Stat_inspec(Inspection):
    
    def inspec(self, df: pd.DataFrame):
        
        """
        inspect take Data Frame (df)
        
        return ==> Inspection stat  describtion
        
        """
        print('=== Numerical datatype statistical describtion ===')
        
        print(df.describe())
        
        print('\n=== Categorical datatype statistical describtion ===')

        print(df.describe(include=["O"]))

class switch_btw_describtion:
    
    def __init__(self, strategy: Inspection):
        
        """
        inspect take Data Frame (df)
        
        return ==> initializing the strategy 
        
        """
        
        self._stratgey = strategy
    
    def set_strategty(self, strategy: Inspection):
        
        """
        set_strategty take strategy class
        
        return ==> set a new strategy
        
        """
        
        self._stratgey = strategy
    
    def apply_strategy(self, Df: pd.DataFrame):
        
        """
        apply_strategy take Data Frame (df)
        
        return ==> Execute the strategy to data frame
        
        """
        
        self._stratgey.inspec(Df)

"""
if __name__ == '__main':
    
    df = pd.read_csv("/home/amine/Desktop/Projects/Real_Estatet_endtoend/src/extracted_data/AmesHousing.csv") #Read the csv file and store values in df
    
    strategy = switch_btw_describtion(General_inspec()) # initialize theswitch class and take general inspect as a strategy
    
    strategy.apply_strategy(df) # Execute the strategy
    
    strategy.set_strategty(Stat_inspec()) # Set a New strategy which the stat stratgy
    
    strategy.apply_strategy(df) # execute the new strategy
"""