from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.data_classes import event_source, EventBridgeEvent


logger = Logger(service="testing-poc")


@event_source(data_class=EventBridgeEvent)
def lambda_handler(event: EventBridgeEvent, context):
    logger.info(event.detail)
    logger.info(event.detail_type)
    #  save event details to dynamo DB and send email
