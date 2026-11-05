from validation import validate_target
from network import resolve_host, check_tcp
from config import load_config
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

def run_diagnostics(target):
    if not validate_target(target):
        return {
            "host": target.get("host"),
            "ip_address": None,
            "port": target.get("port"),
            "dns": None,
            "tcp": None,
            "status": "INVALID"
        }

    diagnostics = {
        "host": target["host"],
        "ip_address": None,
        "port": target["port"],
        "dns": "FAILED",
        "tcp": None,
        "status": "FAILED"
    }

    ip_address = resolve_host(target["host"])

    if ip_address is None:
        diagnostics["status"] = "FAILED"
        return diagnostics

    diagnostics["ip_address"] = ip_address
    diagnostics["dns"] = "PASS"

    tcp_result = check_tcp(
        ip_address,
        target["port"]
    )

    diagnostics["tcp"] = tcp_result

    if tcp_result == "CONNECTED":
        diagnostics["status"] = "SUCCESS"

    return diagnostics


def show_diagnostics(diagnostics):
    print("\n--- Diagnostic Results ---")
    print(f"Host: {diagnostics['host']}")
    print(f"Resolved IP: {diagnostics['ip_address']}")
    print(f"Port: {diagnostics['port']}")
    print(f"DNS: {diagnostics['dns']}")
    print(f"TCP: {diagnostics['tcp']}")
    print(f"Status: {diagnostics['status']}")


def main():
    display_banner(application_name, version, description)

    config = load_config()

    if config is None:
        print("Failed to load configuration.")
        return 1

    targets = config.get("targets", [])

    if not isinstance(targets, list):
        print("Invalid configuration: 'targets' must be a list.")
        return 1

    if not targets:
        print("No targets found in configuration.")
        return 1

    results = []
    all_successful = True
    invalid_targets = 0

    for target in targets:
        if not isinstance(target, dict):
            print("Invalid target configuration: target must be an object.")
            invalid_targets += 1
            all_successful = False
            continue

        diagnostics = run_diagnostics(target)

        results.append(diagnostics)

        show_diagnostics(diagnostics)

        if diagnostics["status"] != "SUCCESS":
            all_successful = False

    total = len(targets)
    successful = 0
    failed = invalid_targets

    for result in results:
        if result["status"] == "SUCCESS":
            successful += 1
        else:
            failed += 1

    print("\n--- Run Summary ---")
    print(f"Total: {total}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")

    if all_successful:
        return 0

    return 1

if __name__ == "__main__":
    sys.exit(main())