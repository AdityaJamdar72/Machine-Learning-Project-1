import sys
import pickle
from sklearn.preprocessing import StandardScaler
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class predict_pipe:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            self.model_path = r"C:\Users\Aditya\Desktop\ML_Project\artifacts\model.pkl"
            self.preprocessor_path = r"C:\Users\Aditya\Desktop\ML_Project\artifacts\preprocessor.pkl"

            self.model = load_object(self.model_path)
            self.preprocessor = load_object(self.preprocessor_path)

            scaled_data = self.preprocessor.transform(features)
            preds = self.model.predict(scaled_data)

            return preds

        except Exception as e:
            raise CustomException(e, sys)
            


class CustomData:
    def __init__(self,gender,race_ethnicity,parental_level_ofeducation,lunch,test_preparation_course,reading_score,writing_score):
        self.gender=gender
        self.race_ethnicity=race_ethnicity
        self.parental_level_ofeducation=parental_level_ofeducation
        self.lunch=lunch
        self.test_preparation_course=test_preparation_course
        self.reading_score=reading_score
        self.writing_score=writing_score
    
    def get_dataframe(self):
        try:
            dict_data={
            "gender":self.gender,
            "race/ethnicity":self.race_ethnicity,
            "parental level of education":self.parental_level_ofeducation,
            "lunch":self.lunch,
            "test preparation course":self.test_preparation_course,
            "reading score":self.reading_score,
            "writing score":self.writing_score}

            return pd.DataFrame([dict_data])
        except Exception as e:
            raise CustomException(e,sys)
        
        