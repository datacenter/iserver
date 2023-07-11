# Node Interface - SVI

## Filter by MAC address

```
# iserver get aci intf svi --apic apic21 --node cl2208-eu-spdc --mac 22ff

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: cl2208-eu-spdc

Interface SVI State [#4]
------------------------

+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+-----------------+
| Node                 | Health | Faults  | Interface | Admin | Oper | Type | Medium | Mcast | MTU  | VLAN | Access Encap | Fabric Encap   | MAC               | IPv4            |
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+-----------------+
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan4     | up    | up   | Reg  | bcast  | no    | 9000 | 4    | --           | vxlan-15106000 | 00:22:BD:BB:22:FF | 10.58.29.94/28  | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan6     | up    | up   | Reg  | bcast  | no    | 9000 | 6    | --           | vxlan-14680068 | 00:22:BD:B8:22:FF | 10.58.24.94/28  | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan9     | up    | up   | Reg  | bcast  | no    | 9000 | 9    | --           | vxlan-14745597 | 00:22:BD:C8:22:FF | 10.58.24.190/28 | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan24    | up    | up   | Reg  | bcast  | no    | 9000 | 24   | --           | vxlan-15466407 | 00:22:BD:EE:22:FF | 10.58.25.174/28 | 
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+-----------------+
```

Developer

```
# iserver get aci intf svi --apic apic21 --node cl2208-eu-spdc --mac 22ff

{
    "duration": 1658,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 398,
        "disconnect_time": 0,
        "mo_time": 1005,
        "total_time": 1403
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

True	398	-	connect apic21o.emea-sp.cisco.com:443
True	310	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	396	20	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	299	29	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/ipv4Addr
```

[[Back]](./InterfaceSvi.md)