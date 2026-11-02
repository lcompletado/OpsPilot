from validation import validate_target
import sys

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

def main():
    display_banner(application_name, version, description)

    target = input_target()
    is_valid_target = validate_target(target)

    if is_valid_target:
        show_target(target)
        print("Valid target. Starting diagnostics...")
        return 0
    else:
        print("Invalid target.")
        return 1

if __name__ == "__main__":
    sys.exit(main())