# Node Interface - SVI

## Filter by IP address

```
# iserver get aci intf svi
    --apic apic21
    --node cl2208-eu-spdc
    --address 10.58.29.94

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: cl2208-eu-spdc

Interface SVI - State [#1]
--------------------------

+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+----------------+
| Node                 | Health | Faults  | Interface | Admin | Oper | Type | Medium | Mcast | MTU  | VLAN | Access Encap | Fabric Encap   | MAC               | IPv4           |
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+----------------+
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan4     | up    | up   | Reg  | bcast  | no    | 9000 | 4    | --           | vxlan-15106000 | 00:22:BD:BB:22:FF | 10.58.29.94/28 | 
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+----------------+
```

Developer

```
# iserver get aci intf svi
    --apic apic21
    --node cl2208-eu-spdc
    --address 10.58.29.94

{
    "duration": 1418,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 388,
        "disconnect_time": 0,
        "mo_time": 907,
        "total_time": 1295
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

True	388	-	connect apic21o.emea-sp.cisco.com:443
True	277	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	363	19	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	267	29	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/ipv4Addr
```

[[Back]](./InterfaceSvi.md)