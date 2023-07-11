# Node Interface - SVI

## Filter by access encapsulation

```
# iserver get aci intf svi --apic apic21 --node cl2208-eu-spdc --access vlan-8*

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: cl2208-eu-spdc

Interface SVI State [#4]
------------------------

+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+----------------------+
| Node                 | Health | Faults  | Interface | Admin | Oper | Type | Medium | Mcast | MTU  | VLAN | Access Encap | Fabric Encap   | MAC               | IPv4                 |
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+----------------------+
| pod-1/cl2208-eu-spdc | 99     | 0 0 0 1 | vlan27    | up    | up   | Ext  | bcast  | no    | 1500 | 27   | vlan-813     | vxlan-15269821 | 00:22:BD:F8:19:FF | 169.254.3.1/24 (pri) | 
|                      |        |         |           |       |      |      |        |       |      |      |              |                |                   | 169.254.3.254/24     | 
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+----------------------+
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan28    | up    | up   | Ext  | bcast  | no    | 1500 | 28   | vlan-811     | vxlan-14942183 | 00:22:BD:F8:19:FF | 169.254.1.254/24     | 
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+----------------------+
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan29    | up    | up   | Ext  | bcast  | no    | 1500 | 29   | vlan-810     | vxlan-15040476 | 00:22:BD:F8:19:FF | 169.254.0.254/24     | 
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+----------------------+
| pod-1/cl2208-eu-spdc | 99     | 0 0 0 1 | vlan30    | up    | up   | Ext  | bcast  | no    | 1500 | 30   | vlan-812     | vxlan-15237056 | 00:22:BD:F8:19:FF | 169.254.2.1/24 (pri) | 
|                      |        |         |           |       |      |      |        |       |      |      |              |                |                   | 169.254.2.254/24     | 
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+----------------------+
```

Developer

```
# iserver get aci intf svi --apic apic21 --node cl2208-eu-spdc --access vlan-8*

{
    "duration": 1777,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 427,
        "disconnect_time": 0,
        "mo_time": 1044,
        "total_time": 1471
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

True	427	-	connect apic21o.emea-sp.cisco.com:443
True	314	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	459	20	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	271	29	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/ipv4Addr
```

[[Back]](./InterfaceSvi.md)