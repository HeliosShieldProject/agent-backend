user_ip=$(wc -l < $1)

mkdir -p temp
cd temp

wg genkey | tee privatekey | wg pubkey > publickey
wg set wg0 peer $(cat publickey)
ip -4 route add $2/32 dev wg0
cat privatekey

cd ..
rm -rf temp
