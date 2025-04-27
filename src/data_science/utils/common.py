import os
import yaml
import json
import joblib
from typing import Any
from pathlib import Path
from box import ConfigBox
from ensure import ensure_annotations
from box.exceptions import BoxValueError

from src.data_science import logger

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox object.
    
    Args:
        path_to_yaml (Path): Path to the YAML file.
        
    Returns:
        ConfigBox: Contents of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """
    Creates list of directories if they do not exist.
    
    Args:
        path_to_directories (list): List of path to the directory to be created.
        verbose (bool): If True, logs the creation of directories.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict) -> None:
    """
    Saves a dictionary to a JSON file.
    
    Args:
        path (Path): Path to the JSON file.
        data (dict): Dictionary to be saved.
        
    Returns:
        None
    """
    with open(path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    logger.info(f"JSON file saved successfully at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads a JSON file and returns its contents as a ConfigBox object.
    
    Args:
        path (Path): Path to the JSON file.
        
    Returns:
        ConfigBox: Contents of the JSON file as a ConfigBox object.
    """
    with open(path, 'r') as json_file:
        content = json.load(json_file)
    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path) -> None:
    """
    Saves data to a binary file using joblib.
    
    Args:
        data (Any): Data to be saved.
        path (Path): Path to the binary file.
        
    Returns:
        None
    """
    joblib.dump(data, path)
    logger.info(f"Binary file saved successfully at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads data from a binary file using joblib.
    
    Args:
        path (Path): Path to the binary file.
        
    Returns:
        Any: Loaded data.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded successfully from: {path}")
    return data
