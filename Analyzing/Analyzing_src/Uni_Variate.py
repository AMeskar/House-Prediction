from abc import ABC, abstractmethod
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# I need two inspection, general info (number of rows, columns, null values ...)
# I need the second inspection statistical inspection (means, variance, ...)

class UniVariate(ABC):
    
    @abstractmethod
    
    def Apply_Method(self, df: pd.DataFrame, feature: str):
        
        """

        """
        
        pass
    
class Numerical_Analyze(UniVariate):
    
    def Apply_Method(self, df: pd.DataFrame, feature: str):
        
        """

        """
        
        plt.figure(figsize=(10, 6))
        sns.histplot(df[feature], kde=True, bins=30)
        plt.title(f"Distribution of {feature}")
        plt.xlabel(feature)
        plt.ylabel("Frequency")
        plt.show()

class Categorical_Analyze(UniVariate):
    
    def Apply_Method(self, df: pd.DataFrame, feature: str):
        
        """

        """

        plt.figure(figsize=(10, 6))
        sns.countplot(x=feature, data=df, palette="muted")
        plt.title(f"Distribution of {feature}")
        plt.xlabel(feature)
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.show()

class switch_btw_Dtyp:
    
    def __init__(self, strategy: UniVariate):
        
        """

        """
        
        self._stratgey = strategy
    
    def set_strategty(self, strategy: UniVariate):
        
        """

        """
        
        self._stratgey = strategy
    
    def apply_strategy(self, Df: pd.DataFrame, feature: str):
        
        """

        """
        
        self._stratgey.Apply_Method(Df, feature)

"""
if __name__ =='__main__':
    
    df = pd.read_csv("/Users/meskara/Desktop/Github/Real_Estatet_endtoend/src/extracted_data/AmesHousing.csv") #Read the csv file and store values in df
    
    strategy = switch_btw_describtion(Numerical_Analyze()) # initialize theswitch class and take general inspect as a strategy
    
    strategy.apply_strategy(df, 'SalePrice') # Execute the strategy
    
    strategy.set_strategty(Categorical_Analyze()) # Set a New strategy which the stat stratgy
    
    strategy.apply_strategy(df, 'Neighborhood') # execute the new strategy
"""