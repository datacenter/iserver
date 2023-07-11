# Node Interface - SVI

## Filter by interface name

```
# iserver get aci intf svi --apic apic21 --node cl2208-eu-spdc --name vlan30

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: cl2208-eu-spdc

Interface SVI State [#1]
------------------------

+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+----------------------+
| Node                 | Health | Faults  | Interface | Admin | Oper | Type | Medium | Mcast | MTU  | VLAN | Access Encap | Fabric Encap   | MAC               | IPv4                 |
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+----------------------+
| pod-1/cl2208-eu-spdc | 99     | 0 0 0 1 | vlan30    | up    | up   | Ext  | bcast  | no    | 1500 | 30   | vlan-812     | vxlan-15237056 | 00:22:BD:F8:19:FF | 169.254.2.1/24 (pri) | 
|                      |        |         |           |       |      |      |        |       |      |      |              |                |                   | 169.254.2.254/24     | 
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+----------------------+
```

Developer

```
# iserver get aci intf svi --apic apic21 --node cl2208-eu-spdc --name vlan30

{
    "duration": 1870,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 431,
        "disconnect_time": 0,
        "mo_time": 1068,
        "total_time": 1499
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

True	431	-	connect apic21o.emea-sp.cisco.com:443
True	323	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	451	20	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	294	29	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/ipv4Addr
```

[[Back]](./InterfaceSvi.md)