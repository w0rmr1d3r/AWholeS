import inquirer

from AWholeS.cloudformation.cloudformation import search_stack_by_name


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
