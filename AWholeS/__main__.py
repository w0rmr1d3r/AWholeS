from AWholeS.ec2 import show_all_regions, show_all_available_regions
from AWholeS.sts_calls import get_current_arn, get_current_assumed_role, get_current_account_id
from AWholeS.trusted_advisor_security import show_failed_security_checks, show_failed_security_checks_with_account_id

# If this doesn't find modules, use:
# export PYTHONPATH=$PYTHONPATH:.
# Ref: https://stackoverflow.com/questions/37233140/python-module-not-found
if __name__ == "__main__":
    print("Running AWholeS...")
    print("\n")
    print("Your current ARN is:")
    print(get_current_arn())
    print("\n")
    print("Your current AssumedRole is:")
    print(get_current_assumed_role())
    print("\n")
    print("Showing all regions:")
    show_all_regions()
    print("\n")
    print("Showing current available regions:")
    show_all_available_regions()
    print("\n")
    print(f"Current Security failures for your account {get_current_account_id()}:")
    print("\n")
    show_failed_security_checks()
    print("\n")
    show_failed_security_checks_with_account_id(account_id=get_current_account_id())
