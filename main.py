from src.CNNClassifier.logging import logger

# Log some messages
logger.info("Welcome to custom log")
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.debug('This is a debug message')

from src.CNNClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

# Create Data Ingestion 
STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e