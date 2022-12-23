import boto3


# This method is in the README.md
# If updated or move, update the docs accordingly
def show_all_available_regions():
    """
    Prints current available regions
    :return: None
    """
    client = boto3.client("ec2")
    for region in client.describe_regions()["Regions"]:
        print(region["RegionName"])


def show_all_regions():
    """
    Prints current available regions

    :return: None
    """
    client = boto3.client("ec2")
    for region in client.describe_regions(AllRegions=True)["Regions"]:
        print(region["RegionName"])
