# MLOps-DVC Project Setup

1. Clone the repository:  
`git clone https://github.com/naufalsutrisna/MLOps-DVC.git && cd MLOps-DVC`

2. Initialize Git and DVC:  
`git init && dvc init`

3. Download Dataset:  
`wget --no-check-certificate 'https://drive.google.com/uc?export=download&id=1p5PU4EVDHdcIOkUxsCkkxC0zfFRPR3z9' -O iris.csv`
`mv iris.csv data/`

4. Add the dataset to DVC:  
`dvc add data/iris.csv`

5. Create `.gitignore`:  
`touch .gitignore`

6. Add the files to Git:  
`git add data/iris.csv.dvc .gitignore && git commit -m "Add Iris dataset"`

7. Train the model:  
`python3 script/training.py`

8. Add the trained model to DVC:  
`dvc add model/iris_model.pkl`

9. Commit the trained model:  
`git add model/iris_model.pkl.dvc && git commit -m "Add trained model version 1"`

10. Preprocess the dataset:  
`python3 script/preprocessing.py`

11. Add the updated dataset to DVC:  
`dvc add data/iris.csv`

12. Commit the updated dataset:  
`git add data/iris.csv.dvc && git commit -m "Update dataset with target column renamed to 'target'"`

13. Retrain the model with the updated dataset:  
`python3 script/training.py`

14. Add the updated model to DVC:  
`dvc add model/iris_model.pkl`

15. Commit the updated model:  
`git add model/iris_model.pkl.dvc && git commit -m "Update model with new dataset"`

16. View commit history for dataset and model:  
`git log -- data/iris.csv.dvc && git log -- model/iris_model.pkl.dvc`
