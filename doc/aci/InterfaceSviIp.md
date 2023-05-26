# Node Interface - SVI

## Filter by IP address

```
# iserver get aci intf svi
    --apic apic11
    --node bl205-eu-spdc
    --ip 15.3.64.128 -o addr

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------------+------------+---------+-------------------+----------------+
| Node                | Interface | Admin State | Oper State | Vlan ID | MAC               | IPv4           |
+---------------------+-----------+-------------+------------+---------+-------------------+----------------+
| pod-1/bl205-eu-spdc | vlan1     | up          | up         | 1       | 00:22:BD:3D:C3:CC | 15.3.64.254/24 | 
+---------------------+-----------+-------------+------------+---------+-------------------+----------------+
```

[[Back]](./InterfaceSvi.md)