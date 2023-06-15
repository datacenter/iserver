# Node Interface - Tunnel

## Filter by interface id

```
# iserver get aci intf tun --apic apic11 --node bl205-eu-spdc --id tunnel16

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------+------+-------+--------+-----------------+-----+-------------+----------------+-----------+------+
| Node                | Interface | Admin | Oper | Layer | Encap  | Type            | Req | Source IP   | Destination IP | VRF       | MTU  |
+---------------------+-----------+-------+------+-------+--------+-----------------+-----+-------------+----------------+-----------+------+
| pod-1/bl205-eu-spdc | tunnel16  | up    | up   | l3    | ivxlan | Fabric External | bgp | 10.3.192.64 | 172.16.30.161  | overlay-1 | 9000 | 
|                     |           |       |      |       |        | Physical        |     |             |                |           |      | 
|                     |           |       |      |       |        | dci-ucast       |     |             |                |           |      | 
+---------------------+-----------+-------+------+-------+--------+-----------------+-----+-------------+----------------+-----------+------+
```

Developer

```
# iserver get aci intf tun --apic apic11 --node bl205-eu-spdc --id tunnel16

{
    "duration": 1115,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 411,
        "disconnect_time": 0,
        "mo_time": 605,
        "total_time": 1016
    },
    "error": {
        "read": false,
        "lines": 0
    },
    "info": {
        "read": false,
        "lines": 0
    },
    "debug": {
        "read": false,
        "lines": 0
    },
    "cache_hits": 0
}

Log: apic
----------

True	411	-	connect apic11o.emea-sp.cisco.com
True	300	13	apic11o.emea-sp.cisco.com class fabricNode
True	305	19	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/tunnelIf
```

[[Back]](./InterfaceTunnel.md)