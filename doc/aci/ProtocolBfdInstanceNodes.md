# Node Protocol - BFD

## Get BFD instance summary from selected nodes

```
# iserver get aci proto bfd
    --apic apic11
    --node cl201-eu-spdc
    --node bl
    --view instance

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc

+---------------------+---------+-------------+-----------------+-----------+-----------------+--------------------+
| Node                | Admin   | Echo Intf   | Session Summary | Interface | Interface State | Interface Sessions |
+---------------------+---------+-------------+-----------------+-----------+-----------------+--------------------+
| pod-1/bl205-eu-spdc | enabled | unspecified | 0/1             | lo3       | enabled         | 0/1                | 
| pod-1/bl206-eu-spdc | enabled | unspecified | 0/1             | lo2       | enabled         | 0/1                | 
| pod-1/cl201-eu-spdc | enabled | unspecified | 0/0             |           |                 |                    | 
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
    "duration": 3994,
    "apic": {
        "read": true,
        "success": 11,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 10,
        "connect_time": 445,
        "disconnect_time": 0,
        "mo_time": 3237,
        "total_time": 3682
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

True	445	-	connect apic11o.emea-sp.cisco.com
True	316	13	apic11o.emea-sp.cisco.com class fabricNode
True	322	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bfd/inst
True	325	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	334	8	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	304	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bfd/inst
True	331	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	322	12	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	338	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst
True	301	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	344	15	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
```

[[Back]](./ProtocolBfd.md)