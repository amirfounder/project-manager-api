from datetime import datetime
from flask import abort
from src.utils.utils import responsify


DEFAULT_ERROR_MESSAGE = 'There was an error.'


def throw_exception(statusCode: int, error: str, errorMessage: str):
    timestamp = datetime.now().isoformat()
    response = {
        'timestamp': timestamp,
        'statusCode': statusCode,
        'error': error,
        'errorMessage': errorMessage
    }
    response = responsify(response)

    abort(response)


def throw_not_found(errorMessage: str):
    throw_exception(
        404,
        'Not Found',
        errorMessage or DEFAULT_ERROR_MESSAGE
    )


def throw_server_error(errorMessage: str):
    throw_exception(
        500,
        'Server Error',
        errorMessage or DEFAULT_ERROR_MESSAGE
    )


def throw_service_unavailable(errorMessage: str):
    throw_exception(
        503,
        'Service Unavailable',
        errorMessage or DEFAULT_ERROR_MESSAGE
    )


def throw_bad_request(errorMessage: str):
    throw_exception(
        400,
        'Bad Request',
        errorMessage or DEFAULT_ERROR_MESSAGE
    )


def throw_conflict(errorMessage: str):
    throw_exception(
        409,
        'Conflict',
        errorMessage or DEFAULT_ERROR_MESSAGE
    )
