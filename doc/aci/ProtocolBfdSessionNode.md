# Node Protocol - BFD

## Get BFD sessions from selected node

```
# iserver get aci proto bfd --apic apic11 --node cl201-eu-spdc

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc
```

Developer

```
# iserver get aci proto bfd --apic apic11 --node cl201-eu-spdc

{
    "duration": 2145,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 544,
        "disconnect_time": 0,
        "mo_time": 1296,
        "total_time": 1840
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

True	544	-	connect apic11o.emea-sp.cisco.com
True	326	13	apic11o.emea-sp.cisco.com class fabricNode
True	302	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst
True	347	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	321	15	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
```

[[Back]](./ProtocolBfd.md)