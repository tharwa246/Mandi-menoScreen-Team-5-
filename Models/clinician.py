
from Models.enums import user_role
from dataclasses import dataclass


# the dataclass decorator shortens how you would make an object normally instead of being redundant it automatically does it for you
@dataclass
class Clinician:
    unique_id: str
    firstname: str
    lastname: str
    username: str
    role: user_role = user_role.ADMIN
    is_Active: bool = True



    # just returns clinician info
    @property
    def fullname(self) -> str:
        if not self.is_active:
            permission_status = "No Access (Account Inactive)"
        else:
            permission_status = "Standard Clinical Access"
        return (
            f"firstname: {self.first_name}\n"
            f"role: {self.role.value}\n"
            f"permission: {permission_status}"
        )
    