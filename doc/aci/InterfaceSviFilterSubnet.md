# Node Interface - SVI

## Filter by IP subnet

```
# iserver get aci intf svi
    --apic apic21
    --node cl2208-eu-spdc
    --subnet 10.58.24.0/24

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: cl2208-eu-spdc

Interface SVI State [#6]
------------------------

+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+-----------------+
| Node                 | Health | Faults  | Interface | Admin | Oper | Type | Medium | Mcast | MTU  | VLAN | Access Encap | Fabric Encap   | MAC               | IPv4            |
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+-----------------+
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan2     | up    | up   | Reg  | bcast  | no    | 9000 | 2    | --           | vxlan-14680069 | 00:22:BD:B8:11:FF | 10.58.24.78/28  | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan6     | up    | up   | Reg  | bcast  | no    | 9000 | 6    | --           | vxlan-14680068 | 00:22:BD:B8:22:FF | 10.58.24.94/28  | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan9     | up    | up   | Reg  | bcast  | no    | 9000 | 9    | --           | vxlan-14745597 | 00:22:BD:C8:22:FF | 10.58.24.190/28 | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan11    | up    | up   | Reg  | bcast  | no    | 9000 | 11   | --           | vxlan-15335346 | 00:22:BD:C8:33:FF | 10.58.24.206/28 | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan15    | up    | up   | Reg  | bcast  | no    | 9000 | 15   | --           | vxlan-14843889 | 00:22:BD:C8:44:FF | 10.58.24.222/28 | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan37    | up    | up   | Reg  | bcast  | no    | 9000 | 37   | --           | vxlan-15007706 | 00:22:BD:C8:11:FF | 10.58.24.174/28 | 
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+-----------------+
```

Developer

```
# iserver get aci intf svi
    --apic apic21
    --node cl2208-eu-spdc
    --subnet 10.58.24.0/24

{
    "duration": 1728,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 420,
        "disconnect_time": 0,
        "mo_time": 1015,
        "total_time": 1435
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

True	420	-	connect apic21o.emea-sp.cisco.com:443
True	309	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	407	20	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	299	29	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/ipv4Addr
```

[[Back]](./InterfaceSvi.md)