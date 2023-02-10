from pprint import pprint

import boto3

from AWholeS.iam.dataclasses import PoliciesOnRole


class IAM:
    def __init__(self):
        self._client = boto3.client("iam")

    def obtain_policies_on_role(self, role_name: str) -> PoliciesOnRole:
        attached_policies = []
        response_attached = self._client.list_attached_role_policies(
            RoleName=role_name,
        )
        is_truncated_managed = response_attached.get("IsTruncated", False)
        marker_managed = response_attached.get("Marker")
        attached_policies += response_attached.get("AttachedPolicies")
        while is_truncated_managed:
            response_attached = self._client.list_attached_role_policies(RoleName=role_name, Marker=marker_managed)
            is_truncated_managed = response_attached.get("IsTruncated", False)
            marker_managed = response_attached.get("Marker")
            attached_policies += response_attached.get("AttachedPolicies")

        policies_inline = []

        response_inline = self._client.list_role_policies(
            RoleName=role_name,
        )
        is_truncated_inline = response_inline.get("IsTruncated", False)
        marker_inline = response_inline.get("Marker")
        policies_inline += response_inline.get("PolicyNames")
        while is_truncated_inline:
            response_inline = self._client.list_role_policies(
                RoleName=role_name,
                Marker=marker_inline,
            )
            is_truncated_inline = response_inline.get("IsTruncated", False)
            marker_inline = response_inline.get("Marker")
            policies_inline += response_inline.get("PolicyNames")

        return PoliciesOnRole(attached_policies=attached_policies, inline_policies=policies_inline)

    def list_all_policies_on_role(self, policies_on_role: PoliciesOnRole) -> None:
        print("\nInline policies:\n")
        for inline_policy in policies_on_role.inline_policies:
            print(inline_policy)
        print("\nAttached policies:\n")
        for managed_policy in policies_on_role.attached_policies:
            print(managed_policy)

    def describe_permissions(self, policies: PoliciesOnRole, role_name: str):
        inline_policy_documents = []
        for inline_policy in policies.inline_policies:
            response = self._client.get_role_policy(RoleName=role_name, PolicyName=inline_policy)
            inline_policy_documents += [response.get("PolicyDocument")]

        managed_policy_documents = []
        for managed_policy in policies.attached_policies:
            version = (
                self._client.get_policy(PolicyArn=managed_policy.get("PolicyArn")).get("Policy").get("DefaultVersionId")
            )
            document = self._client.get_policy_version(PolicyArn=managed_policy.get("PolicyArn"), VersionId=version)
            managed_policy_documents += [document.get("PolicyVersion").get("Document")]

        pprint(inline_policy_documents)
        pprint(managed_policy_documents)
