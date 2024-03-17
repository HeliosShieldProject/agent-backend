import ipaddress

from pydantic import BaseModel

from app.core.enums import Error
from app.dto.service_response import Response
from app.env import ENV


class Data(BaseModel):
    ip: ipaddress.IPv4Address


async def get_available_ip(used_ips: list[ipaddress.IPv4Address]) -> Response[Data]:
    async def inner():
        subnet = ipaddress.ip_network(ENV.WIREGUARD_CLIENT_SUBNET)
        available_ips = list(subnet.hosts())[1:]  # exclude wireguard address
        if len(available_ips) == len(used_ips):
            raise ValueError("No available IP addresses")
        for ip in available_ips:
            if ip not in used_ips:
                return Response(data=Data(ip=ip))

    try:
        return await inner()
    except ValueError:
        return Response(error=Error.NO_IP_AVAILABLE)
    except Exception:
        return Response(error=Error.UNEXPECTED_ERROR)
