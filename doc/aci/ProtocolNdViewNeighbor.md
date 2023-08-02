# Node Protocol - ND

## Nei view

```
# iserver get aci proto nd --apic apic11 --node bl205-eu-spdc --view nei

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

Protocol ND - Neighbor [#0]
---------------------------
None
```

Developer

```
# iserver get aci proto nd --apic apic11 --node bl205-eu-spdc --view nei

{
    "duration": 2153,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 389,
        "disconnect_time": 0,
        "mo_time": 1527,
        "total_time": 1916
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

True	389	-	connect apic11o.emea-sp.cisco.com:443
True	297	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	300	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/nd query query-target=children&rsp-subtree-include=health,fault-count
True	311	25	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-205/ndDom query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	331	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/nd/inst query query-target=subtree&target-subtree-class=ndAdjEp
True	288	34	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-205/ndIf query rsp-subtree=children&rsp-subtree-class=ndIf,ndIfStats&rsp-subtree-include=required
```

[[Back]](./ProtocolNd.md)