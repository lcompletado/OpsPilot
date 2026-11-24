def validate_target_port(port):
    try:
        port = int(port)

        if 1 <= port <= 65535:
            return port

    except (ValueError, TypeError):
        return None

    return None


def validate_target(target):
    required_fields = [
        "name",
        "host",
        "port",
        "scheme",
        "path"
    ]

    for field in required_fields:
        if field not in target:
            return False

    if not isinstance(target["name"], str):
        return False

    if not isinstance(target["host"], str):
        return False

    if not isinstance(target["scheme"], str):
        return False

    if not isinstance(target["path"], str):
        return False

    if target["name"].strip() == "":
        return False

    if target["host"].strip() == "":
        return False

    if len(target["name"]) < 3:
        return False

    if target["scheme"] not in ["http", "https"]:
        return False

    if not target["path"].startswith("/"):
        return False

    port = validate_target_port(target["port"])

    if port is None:
        return False

    target["port"] = port

    return True