# Node Interface - SVI

## Filter by interface id

```
# iserver get aci intf svi --apic apic11 --node bl205-eu-spdc --id vlan35

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------------+------------+------------+--------+-----------+------+----------------+
| Node                | Interface | Admin State | Oper State | Type       | Medium | Multicast | MTU  | Fabric Encap   |
+---------------------+-----------+-------------+------------+------------+--------+-----------+------+----------------+
| pod-1/bl205-eu-spdc | vlan35    | up          | up         | bd-regular | bcast  | no        | 9000 | vxlan-16613250 | 
+---------------------+-----------+-------------+------------+------------+--------+-----------+------+----------------+
```

Developer

```
# iserver get aci intf svi --apic apic11 --node bl205-eu-spdc --id vlan35

{
    "duration": 1621,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 401,
        "disconnect_time": 0,
        "mo_time": 1025,
        "total_time": 1426
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

True	401	-	connect apic11o.emea-sp.cisco.com
True	297	13	apic11o.emea-sp.cisco.com class fabricNode
True	425	38	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	303	61	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4Addr
```

[[Back]](./InterfaceSvi.md)