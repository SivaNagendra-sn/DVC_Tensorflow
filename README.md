# Steps Followed in making the Pipeline for this project 

## Commands ------------------------

### create & activate a new -
```bash
conda create --prefix ./env python=3.7 -y
conda activate ./env
```

### Init Git Dvc -
```bash
git init
dvc init
```

### Folder Structure of this project
```bash
├─── artifacts
    ├─── basemodel
    ├─── callbacks
    ├─── checkpoints
    ├─── model
├─── config
     ├─── config.yaml
├─── data (Images)
    ├─── cat 
    ├─── dog
├─── logs
├─── src
    ├─── utils
         ├─── all_utils.py
         ├─── callbacks.py
         ├─── data_management.py
         ├─── models.py             
    ├─── stage_1_load_save.py
    ├─── stage_2_prepare_basemodel.py
    ├─── stage_3_prepare_callbacks.py
    ├─── stage_4_train.py
    ├─── stage_5_evaluate.py
├─── params.yaml
├─── requirements.txt
├─── setup.py
```
