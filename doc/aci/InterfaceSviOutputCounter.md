# Node Interface - SVI

## Verbose output

```
# iserver get aci intf svi --apic apic11 --node bl205-eu-spdc --view counter

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------------+------------+---------+----------+----------+-----------+---------+----------+--------+---------+
| Node                | Interface | Admin State | Oper State | Pkts In | Pkts Out | Mcast In | Mcast Out | Disc In | Disc Out | Err In | Err Out |
+---------------------+-----------+-------------+------------+---------+----------+----------+-----------+---------+----------+--------+---------+
| pod-1/bl205-eu-spdc | vlan1     | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan11    | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan13    | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan15    | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan17    | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan18    | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan19    | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan2     | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan20    | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan21    | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan22    | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan23    | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan25    | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan27    | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan29    | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan3     | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan30    | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan32    | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan33    | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan35    | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan37    | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan39    | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan40    | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan43    | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan44    | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan45    | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan49    | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan5     | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan56    | up          | up         | 10405   | 20692    | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan57    | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan59    | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan6     | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan61    | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan65    | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan67    | up          | up         | 62323   | 124430   | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan68    | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan70    | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan72    | up          | up         | 0       | 0        | 0        | 0         | 0       | 0        | 0      | 0       | 
+---------------------+-----------+-------------+------------+---------+----------+----------+-----------+---------+----------+--------+---------+
```

Developer

```
# iserver get aci intf svi --apic apic11 --node bl205-eu-spdc --view counter

{
    "duration": 1570,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 409,
        "disconnect_time": 0,
        "mo_time": 1000,
        "total_time": 1409
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

True	409	-	connect apic11o.emea-sp.cisco.com
True	303	13	apic11o.emea-sp.cisco.com class fabricNode
True	402	38	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	295	61	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4Addr
```

[[Back]](./InterfaceSvi.md)