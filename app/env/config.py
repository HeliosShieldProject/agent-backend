import os
from pydantic import BaseModel
from dotenv import load_dotenv


class EnvData(BaseModel):
    AGENT_BACKEND_PORT: int
    WIREGUARD_CLIENT_SUBNET: str


def load_environment() -> EnvData:
    load_dotenv()
    return EnvData(
        AGENT_BACKEND_PORT=int(os.getenv("AGENT_BACKEND_PORT")),
        WIREGUARD_CLIENT_SUBNET=os.getenv("WIREGUARD_CLIENT_SUBNET"),
    )


ENV = load_environment()
