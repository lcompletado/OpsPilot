from validation import validate_target
from network import resolve_host, check_tcp
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
        "port": port_text
    }

def show_diagnostics(diagnostics):
    print("\n--- Diagnostic Results ---")
    print(f"Host: {diagnostics['host']}")
    print(f"Resolved IP: {diagnostics['ip_address']}")
    print(f"Port: {diagnostics['port']}")
    print(f"DNS: {diagnostics['dns']}")
    print(f"TCP: {diagnostics['tcp']}")

def main():
    display_banner(application_name, version, description)

    target = input_target()
    is_valid_target = validate_target(target)

    if not is_valid_target:
        print("Invalid target.")
        return 1

    show_target(target)
    print("Valid target. Starting diagnostics...")

    # Start the diagnostic report with what we already know.
    diagnostics = {
        "host": target["host"],
        "ip_address": None,
        "port": target["port"],
        "dns": "FAILED",
        "tcp": None
    }

    # DNS resolution
    ip_address = resolve_host(target["host"])

    if ip_address is None:
        print("DNS Check: FAILED")
        show_diagnostics(diagnostics)
        return 1

    diagnostics["ip_address"] = ip_address
    diagnostics["dns"] = "PASS"

    print("DNS Check: PASS")
    print(f"Resolved IP: {ip_address}")

    # TCP connectivity check
    tcp_result = check_tcp(
        ip_address,
        target["port"]
    )

    diagnostics["tcp"] = tcp_result

    print(f"TCP Check: {tcp_result}")
    show_diagnostics(diagnostics)

    if tcp_result == "CONNECTED":
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())