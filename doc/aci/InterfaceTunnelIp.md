# Node Interface - Tunnel

## Filter by IP address

```
# iserver get aci intf tun --apic apic11 --node bl205-eu-spdc --ip 10.3.192.67

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------+------+-------+-------------+----------+----------------+-------------+-----------+------+
| Node                | Interface | Admin | Oper | Layer | Tunnel Type | Type     | Source         | Destination | VRF       | MTU  |
+---------------------+-----------+-------+------+-------+-------------+----------+----------------+-------------+-----------+------+
| pod-1/bl205-eu-spdc | tunnel6   | up    | up   | l3    | ivxlan      | physical | 10.3.192.64/32 | 10.3.192.67 | overlay-1 | 9000 | 
+---------------------+-----------+-------+------+-------+-------------+----------+----------------+-------------+-----------+------+
```

[[Back]](./InterfaceTunnel.md)