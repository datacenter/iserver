# Node Protocol - LLDP

## Fault history view

```
# iserver get aci proto lldp
    --apic apic11
    --node bl205-eu-spdc
    --view hfault
    --when 90d

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

Protocol LLDP - Fault Records last 90d [#0]
-------------------------------------------
None
Interface context: lldp
```

Developer

```
# iserver get aci proto lldp
    --apic apic11
    --node bl205-eu-spdc
    --view hfault
    --when 90d

{
    "duration": 1946,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 410,
        "disconnect_time": 0,
        "mo_time": 1311,
        "total_time": 1721
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

True	410	-	connect apic11o.emea-sp.cisco.com:443
True	313	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	338	13	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
True	296	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/lldp/inst query rsp-subtree-include=faults,no-scoped,subtree
True	364	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/lldp/inst query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
```

[[Back]](./ProtocolLldp.md)