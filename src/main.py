application_name = "OpsPilot"
version = "0.1"
description = "Infrastructure Diagnostics Tool"

def display_banner(application_name, version, description):
    print("========================")
    print(f"        {application_name}")
    print("========================")
    print(description)
    print(f"Version: {version}")

def show_target(target):
    print(f"Target Name: {target['name']}")
    print(f"Target Host: {target['host']}")
    print(f"Target Port: {target['port']}")

def input_target():
    name = input("Enter target name: ").strip()
    host = input("Enter target host: ").strip()
    port_text = input("Enter target port: ").strip()

    return {
        "name": name,
        "host": host,
        "port": port_text }

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

def main():
    display_banner(application_name, version, description)

    target = input_target()
    is_valid_target = validate_target(target)

    if is_valid_target:
        show_target(target)
        print("Valid target. Starting diagnostics...")
    else:
        print("Invalid target.")

if __name__ == "__main__":
    main()