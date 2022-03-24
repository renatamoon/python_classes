    # SUCCESS = 0 - Nada
    # INVALID_BUCKET_NAME = 1 - InternaServerError 500
    # INTERNAL_HEIMDALL_ERROR = 2 - InternaServerError 500
    # INVALID_TOKEN = 3 - Unauthorized 401


map_errors = {
    "SUCCESS": 200,
    "INVALID_BUCKET_NAME": 500,
    "INTERNAL_HEIMDALL_ERROR": 500,
    "INVALID_TOKEN": 401
}

