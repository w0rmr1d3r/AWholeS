import boto3
from botocore.exceptions import ClientError

from AWholeS.ec2 import obtain_all_available_regions


def search_stack_by_name(stack_name: str):
    for region in obtain_all_available_regions():
        try:
            client = boto3.client("cloudformation", region_name=region)
            client.describe_stacks(
                StackName=stack_name,
                # is NextToken necessary?
                # NextToken='string'
            )
            print(f"{region} - EXISTS")
        except ClientError:
            print(f"{region} - does not exist")
