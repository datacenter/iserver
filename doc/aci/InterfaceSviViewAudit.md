# Node Interface - SVI

## Audit view

```
# iserver get aci intf svi
    --apic apic21
    --when 180d
    --node cl2208-eu-spdc
    --name vlan30
    --view audit

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: cl2208-eu-spdc

Interface SVI - Audit Logs last 180d [#0]
-----------------------------------------
None
```

Developer

```
# iserver get aci intf svi
    --apic apic21
    --when 180d
    --node cl2208-eu-spdc
    --name vlan30
    --view audit

{
    "duration": 1962,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 391,
        "disconnect_time": 0,
        "mo_time": 1451,
        "total_time": 1842
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

True	391	-	connect apic21o.emea-sp.cisco.com:443
True	297	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	362	19	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	261	29	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/ipv4Addr
True	531	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/sviIf query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./InterfaceSvi.md)