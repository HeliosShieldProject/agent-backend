from pydantic import BaseModel, Field, ConfigDict
import ipaddress


class CreateConfigResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    private_key: str = Field(alias="privateKey")
    user_ip: ipaddress.IPv4Address = Field(alias="userIp")
