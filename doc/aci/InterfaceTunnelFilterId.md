# Node Interface - Tunnel

## Filter by interface id

```
# iserver get aci intf tun --apic apic21 --node bl2205-eu-spdc --id tunnel16

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface Tunnel - State [#1]
-----------------------------

+----------------------+--------+---------+-----------+-------+------+-------+--------+--------------------+------+-------------+------------+-----------+------+---------------+----------------+
| Node                 | Health | Faults  | Interface | Admin | Oper | Layer | Encap  | Type               | Req  | Src IP      | Dest IP    | VRF       | MTU  | Keepalive Int | Keepalive Retr |
+----------------------+--------+---------+-----------+-------+------+-------+--------+--------------------+------+-------------+------------+-----------+------+---------------+----------------+
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | tunnel16  | up    | up   | l3    | ivxlan | Physical           | isis | 10.5.216.66 | 10.5.80.65 | overlay-1 | 9000 | 10            | 3              | 
|                      |        |         |           |       |      |       |        | Proxy Anycast IPv6 |      |             |            |           |      |               |                | 
+----------------------+--------+---------+-----------+-------+------+-------+--------+--------------------+------+-------------+------------+-----------+------+---------------+----------------+
```

Developer

```
# iserver get aci intf tun --apic apic21 --node bl2205-eu-spdc --id tunnel16

{
    "duration": 1039,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 361,
        "disconnect_time": 0,
        "mo_time": 589,
        "total_time": 950
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

True	361	-	connect apic21o.emea-sp.cisco.com:443
True	264	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	325	22	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/tunnelIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
```

[[Back]](./InterfaceTunnel.md)