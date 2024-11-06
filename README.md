# MLOps-DVC Project Setup

Clone the repository:  
`git clone https://github.com/naufalsutrisna/MLOps-DVC.git && cd MLOps-DVC`

Initialize Git and DVC:  
`git init && dvc init`

Download Dataset:
wget --no-check-certificate 'https://drive.google.com/uc?export=download&id=1p5PU4EVDHdcIOkUxsCkkxC0zfFRPR3z9' -O iris.csv
mv iris.csv data/

Add the dataset to DVC:  
`dvc add data/iris.csv`

Create `.gitignore`:  
`touch .gitignore`

Add the files to Git:  
`git add data/iris.csv.dvc .gitignore && git commit -m "Add Iris dataset"`

Train the model:  
`python3 script/training.py`

Add the trained model to DVC:  
`dvc add model/iris_model.pkl`

Commit the trained model:  
`git add model/iris_model.pkl.dvc && git commit -m "Add trained model version 1"`

Preprocess the dataset:  
`python3 script/preprocessing.py`

Add the updated dataset to DVC:  
`dvc add data/iris.csv`

Commit the updated dataset:  
`git add data/iris.csv.dvc && git commit -m "Update dataset with target column renamed to 'target'"`

Retrain the model with the updated dataset:  
`python3 script/training.py`

Add the updated model to DVC:  
`dvc add model/iris_model.pkl`

Commit the updated model:  
`git add model/iris_model.pkl.dvc && git commit -m "Update model with new dataset"`

View commit history for dataset and model:  
`git log -- data/iris.csv.dvc && git log -- model/iris_model.pkl.dvc`
