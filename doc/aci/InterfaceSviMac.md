# Node Interface - SVI

## Filter by MAC address

```
# iserver get aci intf svi --apic apic11 --node bl205-eu-spdc --mac 19ff

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------------+------------+-------------+--------+-----------+------+----------------+
| Node                | Interface | Admin State | Oper State | Type        | Medium | Multicast | MTU  | Fabric Encap   |
+---------------------+-----------+-------------+------------+-------------+--------+-----------+------+----------------+
| pod-1/bl205-eu-spdc | vlan13    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16023531 | 
| pod-1/bl205-eu-spdc | vlan15    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15990757 | 
| pod-1/bl205-eu-spdc | vlan17    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15957988 | 
| pod-1/bl205-eu-spdc | vlan2     | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16285610 | 
| pod-1/bl205-eu-spdc | vlan23    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16613266 | 
| pod-1/bl205-eu-spdc | vlan3     | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15925228 | 
| pod-1/bl205-eu-spdc | vlan32    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15990761 | 
| pod-1/bl205-eu-spdc | vlan49    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15040482 | 
| pod-1/bl205-eu-spdc | vlan57    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14909413 | 
| pod-1/bl205-eu-spdc | vlan59    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14909414 | 
| pod-1/bl205-eu-spdc | vlan65    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15761410 | 
| pod-1/bl205-eu-spdc | vlan68    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16089048 | 
| pod-1/bl205-eu-spdc | vlan70    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15695752 | 
+---------------------+-----------+-------------+------------+-------------+--------+-----------+------+----------------+
```

Developer

```
# iserver get aci intf svi --apic apic11 --node bl205-eu-spdc --mac 19ff

{
    "duration": 2251,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 394,
        "disconnect_time": 0,
        "mo_time": 982,
        "total_time": 1376
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

True	394	-	connect apic11o.emea-sp.cisco.com
True	294	13	apic11o.emea-sp.cisco.com class fabricNode
True	392	38	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	296	61	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4Addr
```

[[Back]](./InterfaceSvi.md)