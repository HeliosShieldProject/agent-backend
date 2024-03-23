import ipaddress
import subprocess

from pydantic import BaseModel

from app.core.enums import Error
from app.dto.service_response import Response


class Data(BaseModel):
    private_key: str


async def add_peer(ip: ipaddress.IPv4Address) -> Response[Data]:
    async def inner():
        private_key = subprocess.run(["sh", "./scripts/add_peer.sh", str(ip)], capture_output=True, text=True).stdout.strip()
        assert private_key is not None
        return Response(data=Data(private_key=private_key))

    try:
        return await inner()
    except AssertionError:
        return Response(error=Error.FAILED_TO_ADD_PEER)
    except Exception:
        return Response(error=Error.UNEXPECTED_ERROR)
