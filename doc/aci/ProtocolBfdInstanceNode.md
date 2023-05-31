# Node Protocol - BFD

## Get BFD instance summary from selected node

```
# iserver get aci proto bfd --apic apic11 --node cl201-eu-spdc --view instance

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: cl201-eu-spdc

+---------------------+---------+-------------+-----------------+-----------+-----------------+--------------------+
| Node                | Admin   | Echo Intf   | Session Summary | Interface | Interface State | Interface Sessions |
+---------------------+---------+-------------+-----------------+-----------+-----------------+--------------------+
| pod-1/cl201-eu-spdc | enabled | unspecified | 4/5             | vlan469   | enabled         | 2/2                | 
|                     |         |             |                 | vlan468   | enabled         | 0/1                | 
+---------------------+---------+-------------+-----------------+-----------+-----------------+--------------------+
```

Developer

```
# iserver get aci proto bfd --apic apic11 --node cl201-eu-spdc --view instance

{
    "duration": 1612,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 387,
        "disconnect_time": 0,
        "mo_time": 1147,
        "total_time": 1534
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

True	387	-	connect apic11o.emea-sp.cisco.com
True	301	11	apic11o.emea-sp.cisco.com class fabricNode
True	280	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst
True	282	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	284	15	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
```

[[Back]](./ProtocolBfd.md)