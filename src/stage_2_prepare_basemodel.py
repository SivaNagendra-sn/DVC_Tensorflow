from src.utils.all_utils import read_yaml, create_directory
import argparse
import pandas as pd
import os
from tqdm import tqdm
import logging



def prepare_basemodel(config_path, params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    # Reading all Artifacts paths from Config file
    artifacts = config["artifacts"]
    artifacts_dir = artifacts["ARTIFACTS_DIR"]
    base_model_dir = artifacts["BASE_MODEL_DIRl_dir"]
    base_model_name = artifacts["BASE_MODEL_NAME"]

    base_model_dir_path = os.path.join(artifacts_dir, base_model_dir)

    # Creating directory for base model
    create_directory([base_model_dir_path])

    base_model_path = os.path.join(base_model_dir_path, base_model_name)

    model = get_VGG_16_model(input_shape =params["IMAGE_SIZE"], model_path = base_model_path)

if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")

    parsed_args = args.parse_args()

    try:
        logging.info("\n >>>>> Stage-2-started")
        prepare_basemodel(config_path=parsed_args.config, params_path=parsed_args.params)
        logging.info("Stage 2 completed! Base model is now created")
    except Exception as e:
        logging.exception(e)
        raise e
