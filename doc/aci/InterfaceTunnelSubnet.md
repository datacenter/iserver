# Node Interface - Tunnel

## Filter by IP subnet

```
# iserver get aci intf tun
    --apic apic11
    --node bl205-eu-spdc
    --subnet 172.16.30.0/24

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------+------+-------+-------------+-------------------------------+----------------+---------------+-----------+------+
| Node                | Interface | Admin | Oper | Layer | Tunnel Type | Type                          | Source         | Destination   | VRF       | MTU  |
+---------------------+-----------+-------+------+-------+-------------+-------------------------------+----------------+---------------+-----------+------+
| pod-1/bl205-eu-spdc | tunnel16  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical | 10.3.192.64/32 | 172.16.30.88  | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel17  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical | 10.3.192.64/32 | 172.16.30.121 | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel18  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical | 10.3.192.64/32 | 172.16.30.161 | overlay-1 | 9000 | 
+---------------------+-----------+-------+------+-------+-------------+-------------------------------+----------------+---------------+-----------+------+
```

[[Back]](./InterfaceTunnel.md)