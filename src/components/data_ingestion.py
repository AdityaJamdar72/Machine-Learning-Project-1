import os
import sys
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
import pandas as pd
from sklearn.model_selection import train_test_split

@dataclass
class dataingestionconfig:
    train_path=os.path.join("artifacts","train.csv")
    test_psth=os.path.join("artifacts","test.csv")
    raw_path=os.path.join("artifacts","raw_data.csv")


class dataIngestion:
    def __init__(self):
        self.ingestion_config=dataingestionconfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion start")
        
        try:
            df=pd.read_csv(r"C:\Users\Aditya\Desktop\ML_Project\notebook\Data_sets\StudentsPerformance.csv")
            logging.info("Data Import Done ")

            os.makedirs(os.path.dirname(self.ingestion_config.train_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_path,index=False)

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=26)

            train_set.to_csv(self.ingestion_config.train_path,index=False)
            test_set.to_csv(self.ingestion_config.test_psth,index=False)
            logging.info("Train Test Split Done")
            return (
                self.ingestion_config.train_path,
                self.ingestion_config.test_psth
            )

        except  Exception as e:
            raise CustomException(e,sys)
        

if __name__=="__main__":
    obj=dataIngestion()
    obj.initiate_data_ingestion()