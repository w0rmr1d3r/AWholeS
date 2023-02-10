from dataclasses import dataclass


@dataclass
class FailedSecurityChecks:
    error_checks: list
    warning_checks: list
