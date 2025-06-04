from abc import ABC, abstractmethod
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class MissingValues(ABC):

    def Missing_values(self, df: pd.DataFrame):

        self.identify_MV(df)
        self.print_MV(df)
        self.visualise_MV_bar(df)
        self.visualise_MV_map(df)

    @abstractmethod

    def identify_MV(self, df: pd.DataFrame):

        pass

    @abstractmethod

    def print_MV(self, df: pd.DataFrame):

        pass


    @abstractmethod
    
    def visualise_MV_bar(self, df: pd.DataFrame):

        pass
    @abstractmethod
    
    def visualise_MV_map(self, df: pd.DataFrame):

        pass

class Analyse(MissingValues):

    def identify_MV(self, df: pd.DataFrame):

        Number_missing = df.isnull().sum()

        Number_missing_bypercent  = (df.isnull().sum() / len(df)) * 100

        return Number_missing, Number_missing_bypercent
    
    def print_MV(self, df):

        Number_missing, Number_missing_bypercent = self.identify_MV(df)

        print("Missing values per count",Number_missing.sort_values(ascending= False), '\n')

        print("Missing values per percentage",Number_missing_bypercent.sort_values(ascending= False), '\n')

    def visualise_MV_bar(self, df: pd.DataFrame):

        values, _ = self.identify_MV(df)

        value = sorted(values[values > 0], reverse= True)

        labels = sorted(values[values > 0].index.tolist(), reverse= True)

        plt.figure(figsize=(15, 7))
        bars = plt.bar(labels, value, edgecolor='black')

        plt.xlabel('Columns')
        plt.ylabel('Missing values count')
        plt.title('Missing Values Per Column')
        plt.xticks(fontsize = 20, rotation = 'vertical')
        plt.yticks(fontsize = 20)

        plt.grid(axis='y', linestyle='--', alpha=0.7)

        plt.tight_layout()

        return plt.show()

    def visualise_MV_map(self, df: pd.DataFrame):

        plt.figure(figsize=(15, 7))
        sns.heatmap(df.isnull(), cbar= False, cmap='viridis')

        plt.title('Missing Values Heatmap')

        return plt.show()
    
"""
if __name__=="__main__":

    df = pd.read_csv("/Users/meskara/Desktop/Github/Real_Estatet_endtoend/src/extracted_data/AmesHousing.csv")

    missing = Analyse()
    missing.Missing_values(df)
"""