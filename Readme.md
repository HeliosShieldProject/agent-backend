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

# test add peer
. ./scripts/add_peer.sh 10.0.0.2
```
