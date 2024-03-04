import os    ## to interact with the operating system 
from pathlib import Path  ## to create system compatible path of our system
import logging
# we need to create a list of file to work with

list_of_files = [
".github/workflows/.gitkeep", #will use this for continous integration and deployement
"src/__init__.py",  #the folder inside src or source folder
"src/components/__init__.py" ,  #will have all steps and stages of data ml, also component is the part of the training pipelinbe
"src/components/data_ingestion.py",
"src/components/data_transformation.py",
"src/components/model_trainer.py",
"src/components/model_evaluation.py",
"src/pipepline/__init__.py",
"src/pipepline/training_pipeline.py",
"src/pipepline/prediction_pipeline.py",
"src/utils/__init__.py"
"src/utils/utils.py",
"src/logger/logging.py",
"src/exception/exception.py"
"tests/unit/__init__.py",  # for unit or seperate tests
"tests/integration/__init__.py", # for integrated test
"init_setup.sh", # a shell script
"requirements.txt", # requirements for production environment
"requirements_dev.txt", # requirements for development environment
"setup.py",
"setup.cfg",
"pyproject.toml",
"tox.init",
"experiments/experiments.ipynb"
]

for filepath in list_of_files:
    filepath=Path(filepath)  ##we are making a system compatile path
    filedr,filename=os.path.split(filepath) #this split the path into directory and filename
    if filedr != "":
        os.makedirs(filedr,exist_ok=True)
        logging.info(f"Creating directory: {filedr} for file: {filename}")

    if (not os.path.exists(filepath) or (os.path.getsize(filepath)==0)):
        with open(filepath,"w") as f:
            pass #to create an empty file





