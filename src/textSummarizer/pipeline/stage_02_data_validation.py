from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.data_validation import DataValidation
from src.textSummarizer.logging import logger

class DataValidationPipeline:

    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(data_validation_config)
            data_validation.validate_all_files_exist()
        except Exception as e:
            raise e

STAGE_NAME = "Data Validation Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)