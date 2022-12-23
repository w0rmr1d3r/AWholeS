import inquirer

from AWholeS.cloudformation import search_stack_by_name
from AWholeS.ec2 import show_all_regions, show_all_available_regions
from AWholeS.iam import IAM
from AWholeS.sts_calls import (
    get_current_arn,
    get_current_assumed_role,
    get_current_account_id,
)
from AWholeS.trusted_advisor_security import TrustedAdvisor


def trusted_advisor_menu():
    ta = TrustedAdvisor()
    last_choice = None
    while True:
        choice = inquirer.list_input(
            "What do you want to run?",
            choices=["Failed security checks", "Data from check id", "exit"],
            default=last_choice,
        )
        if choice == "Failed security checks":
            print(f"Current Security failures for your account {get_current_account_id()}:")
            ta.show_failed_security_checks()
            print("\n")
        elif choice == "Data from check id":
            questions = [
                inquirer.Text("check_id", message="Type the check id"),
            ]
            answers = inquirer.prompt(questions)
            ta.describe_check_by_check_id(check_id=answers.get("check_id"))
            print("\n")
        elif choice == "exit":
            return
        last_choice = choice


def iam_menu():
    iam = IAM()
    last_choice = None
    while True:
        choice = inquirer.list_input(
            "What do you want to run?",
            choices=["List my policies", "Describe my policies", "exit"],
            default=last_choice,
        )
        if choice == "List my policies":
            print(f"Your policies:")
            policies = iam.obtain_policies_on_role(role_name=get_current_assumed_role())
            iam.list_all_policies_on_role(policies)
            print("\n")
        elif choice == "Describe my policies":
            print("Your permissions:")
            iam.describe_permissions(
                policies=iam.obtain_policies_on_role(role_name=get_current_assumed_role()),
                role_name=get_current_assumed_role(),
            )
            print("\n")
        elif choice == "exit":
            return
        last_choice = choice


def cloudformation_menu():
    last_choice = None
    while True:
        choice = inquirer.list_input(
            "What do you want to run?",
            choices=["Search stack by name", "exit"],
            default=last_choice,
        )
        if choice == "Search stack by name":
            print(f"Searching stack by name:")
            questions = [
                inquirer.Text("stack_name", message="Type the stack name"),
            ]
            answers = inquirer.prompt(questions)
            search_stack_by_name(stack_name=answers.get("stack_name"))
            print("\n")
        elif choice == "exit":
            return
        last_choice = choice


def menu() -> None:
    """
    Shows the menu with current options of the app.
    Each option should call a function besides exit.
    :return: None
    """
    last_choice = None
    while True:
        choice = inquirer.list_input(
            "What do you want to run?",
            choices=["CloudFormation", "EC2", "IAM", "STS", "Trusted Advisor", "test", "exit"],
            default=last_choice,
        )
        if choice == "CloudFormation":
            cloudformation_menu()
        elif choice == "EC2":
            print("Showing all regions:")
            show_all_regions()
            print("\n")
            print("Showing current available regions:")
            show_all_available_regions()
            print("\n")
        elif choice == "IAM":
            iam_menu()
        elif choice == "STS":
            print("Your current ARN is:")
            print(get_current_arn())
            print("\n")
            print("Your current AssumedRole is:")
            print(get_current_assumed_role())
            print("\n")
        elif choice == "Trusted Advisor":
            trusted_advisor_menu()
        elif choice == "test":
            print(f"TEST")
            # Add here what you want to test
            print("\n")
        elif choice == "exit":
            return
        last_choice = choice


# If this doesn't find modules, use:
# export PYTHONPATH=$PYTHONPATH:.
# Ref: https://stackoverflow.com/questions/37233140/python-module-not-found
if __name__ == "__main__":
    print("Running AWholeS...")
    menu()
