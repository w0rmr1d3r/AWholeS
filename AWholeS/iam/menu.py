import inquirer

from AWholeS.iam.iam import IAM
from AWholeS.sts.sts_calls import get_current_assumed_role


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
