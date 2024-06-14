import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure  import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:                 # Input Arguments -> Output Argument Type
    """
    Reads yaml file and returns
    
    Args: 
        path_to_yaml: Path input
    
    Raises: 
        ValueError: If file is empty
        e: empty file
        
    Returns: 
        ConfigBox: ConfigBox Type"""
    
    try:
        with open(path_to_yaml, 'r') as file:
            content= ConfigBox(yaml.safe_load(file))
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"Empty file: {path_to_yaml}") 
    except Exception as e: 
        return e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates directories
    
    Args: 
        path_to_directories: List of directories
        verbose: Boolean (Optional), Ignore if multiple dirs to be created
    
    Returns: 
        None"""
    
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created: {path}")

@ensure_annotations
def save_json(path_to_json: Path, data: dict):
    """
    Saves content to json file
    
    Args: 
        path_to_json (path): Path to json file
        data (dict): data to be saved in json
    
    Returns: 
        None"""
    
    with open(path_to_json, 'w') as file:
        json.dump(data, file)
        logger.info(f"Json file: {path_to_json} saved successfully")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
    

