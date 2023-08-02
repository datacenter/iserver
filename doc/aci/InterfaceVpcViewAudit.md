# Node Interface - Virtual Port Channel (VPC)

## Audit view

```
# iserver get aci intf vpc
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view audit

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface Virtual Port Channel - Audit Logs last 10y [#0]
---------------------------------------------------------
None
```

Developer

```
# iserver get aci intf vpc
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view audit

{
    "duration": 2046,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 387,
        "disconnect_time": 0,
        "mo_time": 1504,
        "total_time": 1891
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

True	387	-	connect apic21o.emea-sp.cisco.com:443
True	278	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	273	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	427	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	259	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vlanCktEp
True	267	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vpcDom query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./InterfaceVpc.md)