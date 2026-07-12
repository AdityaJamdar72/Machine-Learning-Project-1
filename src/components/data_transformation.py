import os
import sys
import pickle
from typing import Self

from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.compose import ColumnTransformer 
import pandas as pd
from dataclasses import dataclass
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import numpy as np
from src.utils import save_object

from src.exception import CustomException
from src.logger import logging

@dataclass
class TransformationConfig:
    preprocessor_obj_file=os.path.join("artifacts","preprocessor.pkl") # type: ignore


class Transformation:
    def __init__(self):
        self.processor=TransformationConfig()

    def get_transformation_object(self):
        try:
            self.cat_col=['gender','race/ethnicity','parental level of education','lunch','test preparation course']
            self.num_col=["reading score","writing score"]

            self.cat_transformer=Pipeline(
             [("fill_Missing_val",SimpleImputer(strategy="most_frequent")),
             ("encoding",OneHotEncoder())])

            self.num_transformer=Pipeline(
             [("fill_missing_val",SimpleImputer(strategy="median")),
             ("scaling",StandardScaler(),)] )

            self.preprocessing=ColumnTransformer(
              [
                ("Numerical_col",self.num_transformer,self.num_col),
                ("Categorical column",self.cat_transformer,self.cat_col)
            ])

            return self.preprocessing
    
        except Exception as e:
            raise CustomException(e,sys)
   
    def initiate_transformation(self,train_path,test_path):
        try:
            #reading train and test data from file path
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Data read done")

            #Create processor Object and target Column
            processor_obj=self.get_transformation_object()
            target_col="math score"
        
            ## Create train feature
            input_feature_train_df=train_df.drop(columns=[target_col])
            output_feature_train_df=train_df[target_col]
          
            ## Create Test feature
            input_feature_test_df=test_df.drop(columns=[target_col])
            output_feature_test_df=test_df[target_col]
        
            # Create a train and file Object
            train_file_obj=processor_obj.fit_transform(input_feature_train_df)
            test_file_obj=processor_obj.transform(input_feature_test_df)
        
            #Create a train and test array 
            train_arr=np.c_[train_file_obj,np.array(output_feature_train_df)]
            test_arr=np.c_[test_file_obj,np.array(output_feature_test_df)]
        
            save_object(file_path=self.processor.preprocessor_obj_file,obj=processor_obj)
         

            return (
            train_arr,
            test_arr,
            self.processor) 
        except Exception as e:
            raise CustomException(e,sys)
            
       

