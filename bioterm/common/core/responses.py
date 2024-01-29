BACKEND_CONTROLLER_RESPONSES = {
    "REG_SUCCESS": {
        "detail": "Controller successfully registered.",
        "status_code": 200,
    },
    "REG_SUCCESS_CONTROLLERKNOWN": {
        "detail": "Controller already registered.",
        "status_code": 200,
    },
    "REG_ERROR_WRONG_CONFIG": {
        "detail": "Controller registration failed. Wrong APIKEY or UUID.",
        "status_code": 400,
    },
    "REG_ERROR_UUIDFORMAT": {
        "detail": "Controller registration failed. Malformatted UUID.",
        "status_code": 400,
    },
}

BACKEND_DEVICE_RESPONSES = {
    "REG_SUCCESS": {
        "detail": "Device successfully registered.",
        "status_code": 200,
    },
    "REG_SUCCESS_DEVICEKNOWN": {
        "detail": "Device already registered.",
        "status_code": 200,
    },
    "REG_ERROR_UUIDFORMAT": {
        "detail": "Device registration failed. Malformatted UUID.",
        "status_code": 400,
    },
    "REG_ERROR_DEVICECONFIG": {
        "detail": (
            "Device registration failed. "
            "Device configuration does not match registered device."
        ),
        "status_code": 400,
    },
    "REG_ERROR_WRONGCONTROLLER": {
        "detail": (
            "Device registration failed. Device registered at other controller."
        ),
        "status_code": 400,
    },
}
