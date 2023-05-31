# Node Protocol - BFD

## Get BFD instance summary from selected nodes

```
# iserver get aci proto bfd
    --apic apic11
    --node cl201-eu-spdc
    --node bl
    --view instance

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc

+---------------------+---------+-------------+-----------------+-----------+-----------------+--------------------+
| Node                | Admin   | Echo Intf   | Session Summary | Interface | Interface State | Interface Sessions |
+---------------------+---------+-------------+-----------------+-----------+-----------------+--------------------+
| pod-1/bl205-eu-spdc | enabled | unspecified | 0/1             | lo3       | enabled         | 0/1                | 
| pod-1/bl206-eu-spdc | enabled | unspecified | 0/1             | lo3       | enabled         | 0/1                | 
| pod-1/cl201-eu-spdc | enabled | unspecified | 4/5             | vlan469   | enabled         | 2/2                | 
|                     |         |             |                 | vlan468   | enabled         | 0/1                | 
+---------------------+---------+-------------+-----------------+-----------+-----------------+--------------------+
```

Developer

```
# iserver get aci proto bfd
    --apic apic11
    --node cl201-eu-spdc
    --node bl
    --view instance

{
    "duration": 3414,
    "apic": {
        "read": true,
        "success": 11,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 10,
        "connect_time": 397,
        "disconnect_time": 0,
        "mo_time": 2880,
        "total_time": 3277
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

True	397	-	connect apic11o.emea-sp.cisco.com
True	302	11	apic11o.emea-sp.cisco.com class fabricNode
True	271	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bfd/inst
True	289	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	287	8	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	280	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bfd/inst
True	276	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	290	12	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	323	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst
True	276	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	286	15	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
```

[[Back]](./ProtocolBfd.md)