import pandas as pd
import numpy as np
from src.logger.logging import logging
from src.exception.exception import customexception


import os
import sys
from dataclasses import dataclass
from pathlib import Path # we use to create a system independent path

from src.utils.utils import save_object,evaluate_model

from sklearn.linear_model import LinearRegression,Ridge,Lasso,ElasticNet





@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def initiate_model_training(self,train_array,test_array):
        try:
            logging.info("Splitting Dependencies and Independent variables")
            X_train,y_train,X_test,y_test = (
            train_array[:,:-1],
            train_array[:,-1],
            test_array[:,:-1],
            test_array[:,-1]
            )

            models={
                'LinearRegression':LinearRegression(),
                'Lasso':Lasso(),
                'Ridge':Ridge(),
                'ElasticNet':ElasticNet()

            }


            model_report:dict=evaluate_model(X_train,y_train,X_test,y_test)
            print(model_report)
            print('\n=====================')
            logging.info(f"Model Report : {model_report}")

            #to get the best model score from the dictionary
            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model]

            print(f"Best model found, Model name = {best_model_name}")
            print("\n====================")
            logging.info(f"Best Model Found, Model name : {best_model_name}")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

        except Exception as e:
            logging.info()
            raise customexception(e,sys)
        


