application_name = "OpsPilot"
version = "0.1"
description = "Infrastructure Diagnostics Tool"

print("========================")
print(f"        {application_name}")
print("========================")
print(description)
print(f"Version: {version}")

target = input("Enter target: ").strip()

if target == "":
    print("No target provided. Exiting.")
elif len(target) <= 3:
    print("Target is too short. Exiting.")
else:
    print("Starting diagnostics...")