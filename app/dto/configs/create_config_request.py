import ipaddress

from pydantic import BaseModel, ConfigDict, Field


class CreateConfigRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    used_ips: list[ipaddress.IPv4Address] = Field(alias="usedIps")
