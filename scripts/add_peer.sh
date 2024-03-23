user_ip=$1

mkdir -p temp
cd temp

wg genkey | tee privatekey | wg pubkey > publickey
wg set wg0 peer $(cat publickey) allowed-ips $1/32
ip -4 route add $1/32 dev wg0

echo "[Peer]" >> /etc/wireguard/wg0.conf
echo "PublicKey = $(cat publickey)" >> /etc/wireguard/wg0.conf
echo "AllowedIPs = $1/32" >> /etc/wireguard/wg0.conf
echo "" >> /etc/wireguard/wg0.conf

cat privatekey

cd ..
rm -rf temp
