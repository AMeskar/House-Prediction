from abc import ABC, abstractmethod
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# I need two inspection, general info (number of rows, columns, null values ...)
# I need the second inspection statistical inspection (means, variance, ...)

class BiVariate(ABC):
    
    @abstractmethod
    
    def Apply_Method(self, df: pd.DataFrame, feature1: str , feature2: str):
        
        """

        """
        
        pass
    
class Scatter_Analyze(BiVariate):
    
    def Apply_Method(self, df: pd.DataFrame, feature1: str , feature2: str):
        
        """

        """
        
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x = feature1, y = feature2, data= df)
        plt.title(f"{feature1} vs {feature2}")
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.show()

class BoxPlot_Analyze(BiVariate):
    
    def Apply_Method(self, df: pd.DataFrame, feature1: str , feature2: str):
        
        """

        """

        plt.figure(figsize=(10, 6))
        sns.boxenplot(x = feature1, y = feature2, data= df)
        plt.title(f"{feature1} vs {feature2}")
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.show()

class switch_btw_plot:
    
    def __init__(self, strategy: BiVariate):
        
        """

        """
        
        self._stratgey = strategy
    
    def set_strategty(self, strategy: BiVariate):
        
        """

        """
        
        self._stratgey = strategy
    
    def Apply_Method(self, df: pd.DataFrame, feature1: str , feature2: str):
        
        """

        """
        
        self._stratgey.Apply_Method(df, feature1, feature2)

"""
if __name__ =='__main__':
    
    df = pd.read_csv("/Users/meskara/Desktop/Github/Real_Estatet_endtoend/src/extracted_data/AmesHousing.csv") #Read the csv file and store values in df
    
    strategy = switch_btw_describtion(Scatter_Analyze()) # initialize theswitch class and take general inspect as a strategy
    
    strategy.Apply_Method(df, 'Gr Liv Area', 'SalePrice') # Execute the strategy
    
    strategy.set_strategty(BoxPlot_Analyze()) # Set a New strategy which the stat stratgy
    
    strategy.Apply_Method(df, 'Overall Qual', 'SalePrice') # execute the new strategy
"""