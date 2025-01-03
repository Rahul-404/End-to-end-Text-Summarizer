import os
from src.textSummarizer.logging import logger
from src.textSummarizer.config.configuration import DataValidationConfig
import pandas as pd

class DataValidation:

    def __init__(self, config:DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = None

            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum-dataset"))
            
            for file in all_files:
                if file.split('.')[0]  not in self.config.ALL_REQUIRED_FILES:
                    validation_status = False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation status: {validation_status}")
            return validation_status
        except Exception as e:
            raise e
        
    def remove_null_rows(self):
        try:
            data_path = os.path.join("artifacts", "data_ingestion", "samsum-dataset")
            all_files = os.listdir(data_path)

            for file in all_files:

                data = pd.read_csv(os.path.join(data_path, file))
                print(int(data.isna().sum().sum()), file)

                if data.isna().sum().sum() > 0:
                    with open(self.config.STATUS_FILE, "a") as f:
                        f.write(f"\nMissing in {file}: {int(data.isna().sum().sum())}")
                    data.dropna(axis=0, inplace=True)
                    data.to_csv(os.path.join(data_path, file))
                else:
                    with open(self.config.STATUS_FILE, "a") as f:
                        f.write(f"\nMissing in {file}: {int(data.isna().sum().sum())}")
        except Exception as e:
            raise e