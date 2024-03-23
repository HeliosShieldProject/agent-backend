from fastapi import APIRouter, HTTPException
from app.dto.configs import CreateConfigResponse
from app.services.configs import get_available_ip, add_peer

router = APIRouter(prefix="/configs", tags=["configs"])


@router.post("", status_code=201)
async def create_config() -> CreateConfigResponse:
    ip_response = await get_available_ip()
    if not ip_response.data:
        raise HTTPException(status_code=304, detail=ip_response.error.value)

    peer_response = await add_peer(ip_response.data.ip)
    if not peer_response.data:
        raise HTTPException(status_code=304, detail=peer_response.error.value)
    return CreateConfigResponse(userIp=ip_response.data.ip, publicKey=peer_response.data.public_key)
