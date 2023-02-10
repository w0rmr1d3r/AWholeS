from dataclasses import dataclass
from typing import Optional


@dataclass
class PoliciesOnRole:
    attached_policies: Optional[list[dict]]
    inline_policies: Optional[list[str]]
