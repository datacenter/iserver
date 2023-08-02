# Node Interface - Tunnel

## Filter by IP subnet

```
# iserver get aci intf tun
    --apic apic21
    --node bl2205-eu-spdc
    --subnet 10.5.240.0/24

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface Tunnel - State [#2]
-----------------------------

+----------------------+--------+---------+-----------+-------+------+-------+--------+----------+------+-------------+-------------+-----------+------+---------------+----------------+
| Node                 | Health | Faults  | Interface | Admin | Oper | Layer | Encap  | Type     | Req  | Src IP      | Dest IP     | VRF       | MTU  | Keepalive Int | Keepalive Retr |
+----------------------+--------+---------+-----------+-------+------+-------+--------+----------+------+-------------+-------------+-----------+------+---------------+----------------+
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | tunnel2   | up    | up   | l3    | ivxlan | Physical | isis | 10.5.216.66 | 10.5.240.34 | overlay-1 | 9000 | 10            | 3              | 
+----------------------+--------+---------+-----------+-------+------+-------+--------+----------+------+-------------+-------------+-----------+------+---------------+----------------+
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | tunnel3   | up    | up   | l3    | ivxlan | Physical | isis | 10.5.216.66 | 10.5.240.35 | overlay-1 | 9000 | 10            | 3              | 
+----------------------+--------+---------+-----------+-------+------+-------+--------+----------+------+-------------+-------------+-----------+------+---------------+----------------+
```

Developer

```
# iserver get aci intf tun
    --apic apic21
    --node bl2205-eu-spdc
    --subnet 10.5.240.0/24

{
    "duration": 1274,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 436,
        "disconnect_time": 0,
        "mo_time": 707,
        "total_time": 1143
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

True	436	-	connect apic21o.emea-sp.cisco.com:443
True	339	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	368	22	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/tunnelIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
```

[[Back]](./InterfaceTunnel.md)