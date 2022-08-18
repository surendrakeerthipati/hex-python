import os

from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext

from adapters.router import hex_routes

# Set POWERTOOLS_SERVICE_NAME environment variable to represent service
os.environ["POWERTOOLS_SERVICE_NAME"] = "hex-api"
tracer = Tracer()
logger = Logger()

app = APIGatewayRestResolver()
app.include_router(router=hex_routes.router)


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    return app.resolve(event, context)
