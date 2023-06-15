# Node Protocol - ARP

## Verbose output

```
# iserver get aci proto bfd --apic apic11 --id 1090519045 --view verbose

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc
```

Developer

```
# iserver get aci proto bfd --apic apic11 --id 1090519045 --view verbose

{
    "duration": 2003,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 463,
        "disconnect_time": 0,
        "mo_time": 1343,
        "total_time": 1806
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

True	463	-	connect apic11o.emea-sp.cisco.com
True	345	13	apic11o.emea-sp.cisco.com class fabricNode
True	322	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst
True	339	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	337	15	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
```

[[Back]](./ProtocolBfd.md)