def response_body(status_code, data=None, message=None, errors=None):
    messages = {
        "200": "OK",
        "201": "Created",
        "204": "No Content",
        "205": "Reset Content",
        "400": "Bad Request",
        "500": "Internal Server Error"
    }

    response = {
        "status": status_code,
        "message": message if message else messages.get(str(status_code), "Unknown Status"),
    }

    if status_code in (200, 201, 205, 204):
        response["data"] = data if data is not None else {}
    else:
        response["errors"] = errors if errors is not None else {}

    return response
