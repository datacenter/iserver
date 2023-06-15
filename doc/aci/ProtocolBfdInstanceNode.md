# Node Protocol - BFD

## Get BFD instance summary from selected node

```
# iserver get aci proto bfd --apic apic11 --node cl201-eu-spdc --view instance

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

+---------------------+---------+-------------+-----------------+
| Node                | Admin   | Echo Intf   | Session Summary |
+---------------------+---------+-------------+-----------------+
| pod-1/cl201-eu-spdc | enabled | unspecified | 0/0             | 
+---------------------+---------+-------------+-----------------+
```

Developer

```
# iserver get aci proto bfd --apic apic11 --node cl201-eu-spdc --view instance

{
    "duration": 2101,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 462,
        "disconnect_time": 0,
        "mo_time": 1360,
        "total_time": 1822
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

True	462	-	connect apic11o.emea-sp.cisco.com
True	353	13	apic11o.emea-sp.cisco.com class fabricNode
True	331	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst
True	327	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	349	15	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
```

[[Back]](./ProtocolBfd.md)