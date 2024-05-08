import os
import yaml
from WeatherApp import logger
import json
from ensure import ensure_annotation
import joblib
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError
import base64
from box import config_box

@ensure_annotation

def read_yaml(yaml_path: str) -> config_box:
    """
    Reads a yaml file and returns a config_box object.
    """
    try:
       with open(yaml_path, 'r') as f:
        config = yaml.safe_load(f)
        logger.info(f"Loaded config from {yaml_path} successfully.")
        return config_box(config)
    except BoxValueError:
       raise ValueError(f"Could not load config from {yaml_path}.")
    except Exception as e:
       raise e

@ensure_annotation

def save_json(json_path: str, data: Any):
    """
    Saves a json file.
    """
    with open(json_path, 'w') as f:
        json.dump(data, f, indent=4)
    
    logger.info(f"Saved data to {json_path} successfully.")