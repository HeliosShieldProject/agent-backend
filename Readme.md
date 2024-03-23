# Helios | Agent Backend

## Installation

> FastAPI

```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

> Wireguard

```bash 
sudo apt update && sudo apt upgrade -y
. ./scripts/setup_wireguard.sh
```

## Run

```bash
. ./sripts/start-dev.sh  # development
. ./sripts/start.sh  # production
```

## Test

```bash
# manual adding peer test
. ./scripts/add_peer.sh <subnet+peer>  # 10.0.0.2

# test with curl
curl -X POST "http://localhost:{AGENT_BACKEND_PORT}/configs"
```