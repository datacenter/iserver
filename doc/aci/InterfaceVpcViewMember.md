# Node Interface - Virtual Port Channel (VPC)

## Member view

```
# iserver get aci intf vpc --apic apic21 --node bl2205-eu-spdc --view member

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface Virtual Port Channel - Members [#0]
---------------------------------------------
None
```

Developer

```
# iserver get aci intf vpc --apic apic21 --node bl2205-eu-spdc --view member

{
    "duration": 1763,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 388,
        "disconnect_time": 0,
        "mo_time": 1229,
        "total_time": 1617
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

True	388	-	connect apic21o.emea-sp.cisco.com:443
True	269	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	285	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	413	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	262	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vlanCktEp
```

[[Back]](./InterfaceVpc.md)