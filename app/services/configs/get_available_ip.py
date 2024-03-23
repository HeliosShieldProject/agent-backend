import ipaddress
import subprocess

from pydantic import BaseModel

from app.core.enums import Error
from app.dto.service_response import Response
from app.env import ENV


class Data(BaseModel):
    ip: ipaddress.IPv4Address


async def get_used_ips() -> list[ipaddress.IPv4Address]:
    raw_data = subprocess.run(["sh", "./scripts/get_allowed_ips.sh"], capture_output=True, text=True).stdout.strip()
    return [ipaddress.IPv4Interface(line.split("\t")[1]).ip for line in raw_data.split("\n") if line]


async def get_available_ip() -> Response[Data]:
    async def inner():
        used_ips = await get_used_ips()
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
