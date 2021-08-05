import ipaddress

ip = '192.168.0.1'
ip_rede = '192.168.0.0/24'

endereco = ipaddress.ip_address(ip)

rede = ipaddress.ip_network(ip_rede, strict=False)

print(endereco)
print(endereco + 100)
print(endereco + 2000)

for ip_rede in rede:
    print(ip_rede)
