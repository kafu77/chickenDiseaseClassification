from dataclasses import dataclass
from pathlib import Path

#Data ingestion entity
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    

#Model entity configuration
@dataclass(frozen=True)
class BaseModelEntityConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int

#Callbacks entity configuration
@dataclass(frozen=True)
class PrepareCallbacksEntityConfig:
    root_dir: Path
    tensorboard_root_log_dir: Path
    checkpoint_model_filepath: Path


#Training entity  configurations
@dataclass(frozen=True)
class TrainingEntityConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list