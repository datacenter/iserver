# Node Interface - Loopback

## Event view

```
# iserver get aci intf lb
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view event

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface Loopback - Event Logs last 10y [#0]
---------------------------------------------
None
```

Developer

```
# iserver get aci intf lb
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view event

{
    "duration": 2429,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 552,
        "disconnect_time": 0,
        "mo_time": 1665,
        "total_time": 2217
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

True	552	-	connect apic21o.emea-sp.cisco.com:443
True	395	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	396	10	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	388	24	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ipv4Addr
True	486	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l3LbRtdIf query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
```

[[Back]](./InterfaceLoopback.md)