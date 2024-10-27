from CNN_CLASSIFIER import logger
from CNN_CLASSIFIER.pipeline.STAGE_01_DATA_INGESTION import DataIngestionTrainingPipeline
from CNN_CLASSIFIER.pipeline.STAGE_02_PREPARE_BASE_MODEL import PrepareBaseModelTrainingPipeline

STAGE_NAME="DATA INGESTION STAGE"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started >>>>>>")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed >>>>>>")

except Exception as e:
    logger.info(e)
    raise e

STAGE_NAME="PREPARE BASE MODEL"

try:
    logger.info(f"**************")
    logger.info(f">>>>>>>{STAGE_NAME} started <<<<<<<<")
    prepare_base_model=PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>>>>>>{STAGE_NAME} completed <<<<<<<<<<")

except Exception as e:
    raise e
