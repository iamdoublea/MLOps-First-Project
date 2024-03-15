## we are using this Shell script to create an environment

# echo is used to print a particular message.
# $ is used to write any Variable
# 
echo [$(date)]: "START"

echo [$(date)]: "Creating env with python 3.8 version "

# Creating an virtual environment
# conda create: This is the command to create a new Conda environment.
# --prefix ./env: This specifies the prefix or installation directory for the new environment. In this case, ./env indicates a directory named env in the current working directory where the environment will be created.
# python=3.8: This specifies the Python version to be installed in the environment. The = sign is used to specify the version. If you just use python, Conda will try to install the default Python version available, which might not be 3.8.
# -y: This is an optional flag that automatically confirms any prompts during the installation process. It's useful for scripting or automation purposes.

conda create --prefix ./env python=3.8 -y


echo [$(date)]: "Activating the environment"

# to activate the environment
source activate ./env

echo [$(date)]: "Installing the dev environment"

pip install -r requirements_dev.txt

echo [$(date)]: "End"