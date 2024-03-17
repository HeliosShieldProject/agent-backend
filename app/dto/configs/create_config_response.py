from pydantic import BaseModel, Field, ConfigDict
import ipaddress


class CreateConfigResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    public_key: str = Field(alias="publicKey")
    user_ip: ipaddress.IPv4Address = Field(alias="userIp")
