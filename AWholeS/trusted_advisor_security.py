import boto3


def describe_severity_levels():
    """
    Prints the response of describing the security levels for the account

    :return: None
    """
    client = boto3.client('support')
    response = client.describe_severity_levels(
        language='en'
    )
    print(response)


def describe_checks():
    """
    Prints information about Trusted Advisor Security Checks

    :return: None
    """
    try:
        client = boto3.client('support', region_name='us-east-1')
        response = client.describe_trusted_advisor_checks(language='en')
        for check in response.get("checks"):
            if check.get("category") == "security":
                print(f"{check.get('id')} - {check.get('name')} - {check.get('metadata')}")
    except Exception as e:
        print(e)


def obtain_security_checks() -> list:
    """
    Returns the entire list of Trusted Advisor Security checks

    :return: list
    """
    security_checks = []
    try:
        client = boto3.client('support', region_name='us-east-1')
        response = client.describe_trusted_advisor_checks(language='en')
        for check in response.get("checks"):
            if check.get("category") == "security":
                security_checks.append(check)
    except Exception as e:
        print(e)
    return security_checks


def describe_check_by_check_id(check_id: str):
    """
    Prints the response of describing a given check by its id

    :param check_id: Id of the check
    :return: None
    """
    try:
        client = boto3.client('support', region_name='us-east-1')
        response = client.describe_trusted_advisor_check_result(checkId=check_id, language='en')
        print(response)
    except Exception as e:
        print(e)


def show_failed_security_checks():
    """
    Prints a list of all failed Trusted Advisor Security Checks

    :return: None
    """
    client = boto3.client('support', region_name='us-east-1')

    for sec_check in obtain_security_checks():
        try:
            response = client.describe_trusted_advisor_check_result(checkId=sec_check.get("id"), language='en')
            check_status = response.get("result").get("status")
            if check_status in ["warning", "error"]:
                print(sec_check.get("name"))
        except Exception as e:
            print(e)


if __name__ == "__main__":
    show_failed_security_checks()
