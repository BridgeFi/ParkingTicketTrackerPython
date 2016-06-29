def success_response(data, msg):
    return {
        "data": data,
        "message": msg,
        "status": "success",
        "status_code": "200"
    }


def error_response(msg, status_code):
    return {
        "status": "error",
        "status_code": status_code,
        "message": msg
    }
