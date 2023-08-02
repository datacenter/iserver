# Node Protocol - IS-IS

## Nei view

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc --view nei

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc
```

Developer

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc --view nei

{
    "duration": 2402,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 390,
        "disconnect_time": 0,
        "mo_time": 1895,
        "total_time": 2285
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

True	390	-	connect apic11o.emea-sp.cisco.com:443
True	1054	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	275	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/isis query query-target=children&rsp-subtree-include=health,fault-count
True	288	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	278	2	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1 query query-target=subtree&target-subtree-class=isisAdjEp&rsp-subtree=children&rsp-subtree-class=isisPeerIpAddr
```

[[Back]](./ProtocolIsis.md)