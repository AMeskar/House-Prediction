from abc import ABC, abstractmethod
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Plot(ABC):

    def Plot_Corr_Pair(self, df: pd.DataFrame):

        self.heatmap(df)
        self.pairplot(df)

    @abstractmethod

    def heatmap(self, df: pd.DataFrame):

        pass

    @abstractmethod

    def pairplot(self, df: pd.DataFrame):

        pass

class Execution(Plot):

    def heatmap(self, df: pd.DataFrame):

        plt.figure(figsize=(12, 10))
        sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
        plt.title("Correlation Heatmap")

        return plt.show()
    
    def pairplot(self, df: pd.DataFrame):

        sns.pairplot(df)
        plt.suptitle("Pair Plot of Selected Features", y=1.02)

        return plt.show()

"""
if __name__=="__main__":

    df = pd.read_csv("/Users/meskara/Desktop/Github/Real_Estatet_endtoend/src/extracted_data/AmesHousing.csv")
    df = df[['SalePrice', 'Gr Liv Area', 'Overall Qual', 'Total Bsmt SF', 'Year Built']]
    missing = Execution()
    missing.Plot_Corr_Pair(df)
"""