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
    print(f"Target: {target}")

def validate_target(target):
    if target == "":
        return False
    elif len(target) < 3:
        return False
    else:
        return True

def main():
    display_banner(application_name, version, description)

    target = input("Enter target: ").strip()
    is_valid_target = validate_target(target)

    if is_valid_target:
        show_target(target)
        print("Valid target. Starting diagnostics...")
    else:
        print("Invalid target. Please enter a target with at least 3 characters.")


if __name__ == "__main__":
    main()