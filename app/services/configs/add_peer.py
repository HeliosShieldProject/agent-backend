import ipaddress
import subprocess

from pydantic import BaseModel

from app.core.enums import Error
from app.dto.service_response import Response


class Data(BaseModel):
    public_key: str


async def add_peer(ip: ipaddress.IPv4Address) -> Response[Data]:
    async def inner():
        public_key = subprocess.run("sh", "./scripts/add_peer.sh", ip, capture_output=True, text=True).strip()
        assert public_key is None
        return Response(data=Data(public_key=public_key))

    try:
        return await inner()
    except AssertionError:
        return Response(error=Error.FAILED_TO_ADD_PEER)
    except Exception:
        return Response(error=Error.UNEXPECTED_ERROR)
