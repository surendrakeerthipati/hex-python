from adapters.router import hex_routes
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext

# Set POWERTOOLS_SERVICE_NAME environment variable to represent service
tracer = Tracer(service="hex-api")
logger = Logger(service="hex-api")

app = APIGatewayRestResolver()
app.include_router(router=hex_routes.router)


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    return app.resolve(event, context)
