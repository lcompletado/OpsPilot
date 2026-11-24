import urllib.request
import urllib.error
import socket
import json


def check_http(url):
    try:
        response = urllib.request.urlopen(
            url,
            timeout=5
        )

        body = response.read().decode("utf-8")

        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            data = None

        return {
            "status_code": response.status,
            "result": "SUCCESS",
            "data": data
        }

    except urllib.error.HTTPError as error:
        return {
            "status_code": error.code,
            "result": "HTTP_ERROR",
            "data": None
        }

    except socket.timeout:
        return {
            "status_code": None,
            "result": "TIMEOUT",
            "data": None
        }

    except urllib.error.URLError:
        return {
            "status_code": None,
            "result": "ERROR",
            "data": None
        }

def classify_http(status_code, result):
    if result == "TIMEOUT":
        return "TIMEOUT"

    if result == "ERROR":
        return "ERROR"

    if status_code is None:
        return "ERROR"

    if 200 <= status_code < 300:
        return "HEALTHY"

    if 300 <= status_code < 400:
        return "REDIRECT"

    if 400 <= status_code < 500:
        return "CLIENT_ERROR"

    if 500 <= status_code < 600:
        return "SERVER_ERROR"

    return "UNKNOWN"