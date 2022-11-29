from sklearn.base import TransformerMixin
from scipy.sparse import csr_matrix
from scipy.sparse import hstack as sparse_hstack
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import FeatureUnion
import numpy as np
import pandas as pd

class numeric_Transformer(TransformerMixin):
    '''
    Imputes all numeric columns with their medians on the training set.
    Parameters
    ----------
    None
    Returns
    ----------
    Sparse Matrix
            Matrix consisting of the numeric columns after imputation
            
    '''

    
    def __init__(self):
        txt_file = open("columns.txt", "r")
        file_content = txt_file.read()
        self.numeric_features = file_content.split("\n")
        txt_file.close()
        self.num_medians = np.zeros(len(file_content.split(",")))

    def fit(self, X, y=None):
        '''
        Learn the median values of the numeric columns
        Parameters
        ----------
        None
        Returns
        ----------
        self
        ''' 
        X = X.copy()
        self.num_medians = X.median()
        return self
    
    def transform(self, X, y=None):
        '''
        Transforms all anon numeric to a sparse matrix
        Parameters
        ----------
        None
        Returns
        ----------
        Sparse Matrix
            Matrix consisting of all numeric features after imputation with median values
        '''   
        X_copy = X.copy()        
        for col in X_copy:
            X_copy[col].fillna(self.num_medians[col], inplace=True)

        return X_copy
    
    def get_feature_names(self):
        '''
        returns a list of feature names consisting of each of the numeric_features.
        Parameters
        ----------
        None
        Returns
        ----------
        List
            A list of feature names
        '''   
        return [x.lower() for x in self.numeric_features]    
    
