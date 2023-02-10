import inquirer

from AWholeS.sts.sts_calls import get_current_account_id
from AWholeS.trusted_advisor.trusted_advisor import TrustedAdvisor


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
