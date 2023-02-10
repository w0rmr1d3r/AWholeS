import inquirer

from AWholeS.cloudformation.menu import cloudformation_menu
from AWholeS.ec2.ec2 import show_all_regions, show_all_available_regions
from AWholeS.iam.menu import iam_menu
from AWholeS.sts.sts_calls import (
    get_current_arn,
    get_current_assumed_role,
)
from AWholeS.trusted_advisor.menu import trusted_advisor_menu


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


menu()
