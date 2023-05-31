# Node Interface - SVI

## Filter by MAC address

```
# iserver get aci intf svi --apic apic11 --node bl205-eu-spdc --mac 19ff

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------------+------------+-------------+--------+-----------+------+----------------+
| Node                | Interface | Admin State | Oper State | Type        | Medium | Multicast | MTU  | Fabric Encap   |
+---------------------+-----------+-------------+------------+-------------+--------+-----------+------+----------------+
| pod-1/bl205-eu-spdc | vlan11    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15761410 | 
| pod-1/bl205-eu-spdc | vlan19    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14909414 | 
| pod-1/bl205-eu-spdc | vlan30    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15925228 | 
| pod-1/bl205-eu-spdc | vlan32    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15695752 | 
| pod-1/bl205-eu-spdc | vlan34    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16285610 | 
| pod-1/bl205-eu-spdc | vlan35    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15040482 | 
| pod-1/bl205-eu-spdc | vlan39    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15990761 | 
| pod-1/bl205-eu-spdc | vlan40    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15957988 | 
| pod-1/bl205-eu-spdc | vlan41    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14909413 | 
| pod-1/bl205-eu-spdc | vlan48    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16023531 | 
| pod-1/bl205-eu-spdc | vlan5     | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15990757 | 
| pod-1/bl205-eu-spdc | vlan53    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16613266 | 
| pod-1/bl205-eu-spdc | vlan7     | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16089048 | 
+---------------------+-----------+-------------+------------+-------------+--------+-----------+------+----------------+
```

Developer

```
# iserver get aci intf svi --apic apic11 --node bl205-eu-spdc --mac 19ff

{
    "duration": 1772,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 401,
        "disconnect_time": 0,
        "mo_time": 1163,
        "total_time": 1564
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

True	401	-	connect apic11o.emea-sp.cisco.com
True	310	11	apic11o.emea-sp.cisco.com class fabricNode
True	477	38	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	376	61	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4Addr
```

[[Back]](./InterfaceSvi.md)