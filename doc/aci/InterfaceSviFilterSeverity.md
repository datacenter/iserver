# Node Interface - SVI

## Filter by severity

```
# iserver get aci intf svi
    --apic apic21
    --node cl2208-eu-spdc
    --severity major
    --when 180d
    --view fault

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: cl2208-eu-spdc

Interface SVI - Faults [#0]
---------------------------
None
```

Developer

```
# iserver get aci intf svi
    --apic apic21
    --node cl2208-eu-spdc
    --severity major
    --when 180d
    --view fault

{
    "duration": 1828,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 378,
        "disconnect_time": 0,
        "mo_time": 1307,
        "total_time": 1685
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

True	378	-	connect apic21o.emea-sp.cisco.com:443
True	285	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	373	19	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	269	29	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/ipv4Addr
True	380	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l2BD query rsp-subtree-include=faults,no-scoped,subtree
```

[[Back]](./InterfaceSvi.md)