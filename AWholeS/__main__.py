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
    print(f"Current Security failures for your account {get_current_account_id()}:")
    print("\n")
    print(show_failed_security_checks())
    print(show_failed_security_checks_with_account_id(account_id=get_current_account_id()))
