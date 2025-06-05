from abc import ABC, abstractmethod
import pandas as pd
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))

from Logger import logging

from sklearn.preprocessing import LabelEncoder
from sklearn.experimental import enable_iterative_imputer 
from sklearn.impute import IterativeImputer, KNNImputer
from sklearn.ensemble import RandomForestClassifier

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))

class MissingVa(ABC):
    
    @abstractmethod
    
    def apply(self, df: pd.DataFrame):
        
        """
        inspect take Data Frame (df)
        
        return ==> Inspection either stat or general describtion
        
        """

        pass
    
class DropHighMV(MissingVa):
    
    def apply(self, df: pd.DataFrame):
        
        """
        inspect take Data Frame (df)
        
        return ==> Inspection general describtion
        
        """
        
        values = (df.isnull().sum() / len(df)) * 100

        to_drop = values[values > 90].index

        df = df.drop(columns= to_drop)

        logging.info('Columns with over 90 percent of missing values will be dropped')

        return df

class Single_Imputation(MissingVa):
    
    def apply(self, df: pd.DataFrame):
        
        """
        inspect take Data Frame (df)
        
        return ==> Inspection stat  describtion
        
        """

        df = DropHighMV().apply(df)

        imputed_values = {}  

        num_cols = df.select_dtypes(include=['number']).columns

        for col in num_cols:
            if df[col].isna().any():
                skewness = df[col].skew()
                mode_value = df[col].mode()[0]
                mean_value = df[col].mean()
                median_value = df[col].median()

                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                outliers = ((df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))).sum()

                if abs(skewness) > 1:
                    if mode_value == 0 and df[col].value_counts(normalize=True).iloc[0] > 0.3:
                        impute_value = mode_value
                        method = "Mode (0)"
                    else:
                        impute_value = median_value
                        method = "Median"
                elif outliers > 0:
                    impute_value = median_value
                    method = "Median"
                else:
                    impute_value = mean_value
                    method = "Mean"

                imputed_values[col] = (impute_value, method)
                df[col].fillna(impute_value, inplace=True)
                print(f"Column: {col} | Imputation Method: {method} | Imputed Value: {impute_value:.2f}")
        
        cat_cols = df.select_dtypes(exclude=['number']).columns

        for col in cat_cols:

            if df[col].isnull().sum() > 0:

                not_missing = df[df[col].notnull()]
                missing = df[df[col].isnull()]
                predictors = [c for c in df.columns if c not in [col, 'SalePrice'] and df[c].isnull().sum() == 0]

                temp = df[predictors].copy()
                for pc in predictors:
                    if temp[pc].isnull().sum() > 0:
                        temp[pc].fillna(temp[pc].mode()[0], inplace=True)

                temp_encoded = temp.copy()
                for pc in predictors:
                    le = LabelEncoder()
                    temp_encoded[pc] = le.fit_transform(temp[pc].astype(str))

                X_train = temp_encoded.loc[not_missing.index]
                y_train = not_missing[col]

                le_target = LabelEncoder()

                y_train_enc = le_target.fit_transform(y_train.astype(str))

                X_missing = temp_encoded.loc[missing.index]
                
                clf = RandomForestClassifier(n_estimators=100, random_state=0)
                clf.fit(X_train, y_train_enc)

                y_pred_enc = clf.predict(X_missing)
                y_pred = le_target.inverse_transform(y_pred_enc)
                df.loc[missing.index, col] = y_pred
            
        logging.info(" DataFrame is successfully Imputed")

        return df

class KNN_imputation(MissingVa):
    
    def apply(self, df: pd.DataFrame):
        
        """
        inspect take Data Frame (df)
        
        return ==> Inspection stat  describtion
        
        """

        df = DropHighMV().apply(df)

        imputer = KNNImputer(n_neighbors=5)

        num_cols = df.select_dtypes(include=['number']).columns

        df[num_cols] = imputer.fit_transform(df[num_cols])
        
        cat_cols = df.select_dtypes(exclude=['number']).columns

        for col in cat_cols:

            if df[col].isnull().sum() > 0:

                not_missing = df[df[col].notnull()]
                missing = df[df[col].isnull()]
                predictors = [c for c in df.columns if c not in [col, 'SalePrice'] and df[c].isnull().sum() == 0]

                temp = df[predictors].copy()
                for pc in predictors:
                    if temp[pc].isnull().sum() > 0:
                        temp[pc].fillna(temp[pc].mode()[0], inplace=True)

                temp_encoded = temp.copy()
                for pc in predictors:
                    le = LabelEncoder()
                    temp_encoded[pc] = le.fit_transform(temp[pc].astype(str))

                X_train = temp_encoded.loc[not_missing.index]
                y_train = not_missing[col]

                le_target = LabelEncoder()

                y_train_enc = le_target.fit_transform(y_train.astype(str))

                X_missing = temp_encoded.loc[missing.index]
                
                clf = RandomForestClassifier(n_estimators=100, random_state=0)
                clf.fit(X_train, y_train_enc)

                y_pred_enc = clf.predict(X_missing)
                y_pred = le_target.inverse_transform(y_pred_enc)
                df.loc[missing.index, col] = y_pred

        logging.info(" DataFrame is successfully Imputed")

        return df

class Iterative_imputation(MissingVa):
    
    def apply(self, df: pd.DataFrame):
        
        """
        inspect take Data Frame (df)
        
        return ==> Inspection stat  describtion
        
        """

        df = DropHighMV().apply(df)

        imputer = IterativeImputer()

        num_cols = df.select_dtypes(include=['number']).columns

        df[num_cols] = imputer.fit_transform(df[num_cols])
        
        cat_cols = df.select_dtypes(exclude=['number']).columns

        for col in cat_cols:

            if df[col].isnull().sum() > 0:

                not_missing = df[df[col].notnull()]
                missing = df[df[col].isnull()]
                predictors = [c for c in df.columns if c not in [col, 'SalePrice'] and df[c].isnull().sum() == 0]

                temp = df[predictors].copy()
                for pc in predictors:
                    if temp[pc].isnull().sum() > 0:
                        temp[pc].fillna(temp[pc].mode()[0], inplace=True)

                temp_encoded = temp.copy()
                for pc in predictors:
                    le = LabelEncoder()
                    temp_encoded[pc] = le.fit_transform(temp[pc].astype(str))

                X_train = temp_encoded.loc[not_missing.index]
                y_train = not_missing[col]

                le_target = LabelEncoder()

                y_train_enc = le_target.fit_transform(y_train.astype(str))

                X_missing = temp_encoded.loc[missing.index]
                
                clf = RandomForestClassifier(n_estimators=100, random_state=0)
                clf.fit(X_train, y_train_enc)

                y_pred_enc = clf.predict(X_missing)
                y_pred = le_target.inverse_transform(y_pred_enc)
                df.loc[missing.index, col] = y_pred
        
        logging.info(" DataFrame is successfully Imputed")

        return df


class switch_btw_methods:
    
    def __init__(self, strategy: MissingVa):
        
        """
        inspect take Data Frame (df)
        
        return ==> initializing the strategy 
        
        """
        
        self._stratgey = strategy
    
    def set_strategty(self, strategy: MissingVa):
        
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
        
        return self._stratgey.apply(Df)
"""
if __name__=='__main__':
    
    df = pd.read_csv("/Users/meskara/Desktop/Github/Real_Estatet_endtoend/src/extracted_data/AmesHousing.csv") 

    strategy = switch_btw_methods(Iterative_imputation()) 
    
    df = strategy.apply_strategy(df) 
    
    #strategy.set_strategty(RFClassifier_imputation()) 
    
    #strategy.apply_strategy(df) 

    print(df)
"""