def validate_target_port(port_text):
    try:
        port = int(port_text)
        if 1 <= port <= 65535:
            return port
    except ValueError:
        print("Port must be an integer and between 1 and 65535.")
    return None

def validate_target(target):
    if target["name"] == "" or target["host"] == "" or target["port"] == "":
        return False
    if len(target["name"]) < 3:
        return False

    port = validate_target_port(target["port"])

    if port is None:
        return False

    target["port"] = port  # Update the port to be an integer
    return True