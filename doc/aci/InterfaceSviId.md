# Node Interface - SVI

## Filter by interface id

```
# iserver get aci intf svi --apic apic11 --node bl205-eu-spdc --id vlan35

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------------+------------+-------------+--------+-----------+------+----------------+
| Node                | Interface | Admin State | Oper State | Type        | Medium | Multicast | MTU  | Fabric Encap   |
+---------------------+-----------+-------------+------------+-------------+--------+-----------+------+----------------+
| pod-1/bl205-eu-spdc | vlan35    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15040482 | 
+---------------------+-----------+-------------+------------+-------------+--------+-----------+------+----------------+
```

Developer

```
# iserver get aci intf svi --apic apic11 --node bl205-eu-spdc --id vlan35

{
    "duration": 1805,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 427,
        "disconnect_time": 0,
        "mo_time": 1157,
        "total_time": 1584
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
    }
}

Log: apic
----------

True	427	-	connect apic11o.emea-sp.cisco.com
True	330	11	apic11o.emea-sp.cisco.com class fabricNode
True	512	38	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	315	61	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4Addr
```

[[Back]](./InterfaceSvi.md)