import os 
import sys
from sklearn.metrics import r2_score 
from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import (
    RandomForestRegressor,
    AdaBoostRegressor,
    GradientBoostingRegressor)
from xgboost import XGBRegressor # type: ignore
from src.utils import evaluate_model,save_object
from src.exception import CustomException


class Modeltrainconfig:
    model_object_file_path=os.path.join("artifacts","model.pkl")

class Modeltrain:
    def __init__(self):
       self.train_model=Modeltrainconfig()
    
    def initiate_model_train(self,X_train,y_train,X_test,y_test):
        try:
           
            models={
                "LinearRegression":LinearRegression(),
                "Ridge":Ridge(),
                "Lasso":Lasso(),
                "SupportVectorRegression":SVR(),
                "KNN":KNeighborsRegressor(),
                "Decision Tree":DecisionTreeRegressor(),
                "RandomForest":RandomForestRegressor(),
                "Adaboost": AdaBoostRegressor(),
                "Gradient Boost":GradientBoostingRegressor(),
                "XG Boost":XGBRegressor()}
            
            params={
                "LinearRegression"
            }
        
            model_report:dict=evaluate_model(X_train=X_train,X_test=X_test,y_train=y_train,y_test=y_test,models=models)
    

            best_score_model=max(sorted(list(model_report.values())))

            best_model_name = max(model_report, key=model_report.get)

            best_model=models[best_model_name]

            predicted=best_model.predict(X_test)

            best_r2=r2_score(y_test,predicted)


            save_object(
                file_path=self.train_model.model_object_file_path,
                obj=best_model
            )

            return best_r2
        
        except Exception as e:
            raise CustomException(e,sys)