# Policy Group - Access Interface - Leaf Access Port

## Fault view

```
# iserver get aci pg access intf port --apic apic21 --view fault

Apic: apic21 (mode:online, cache:off)

Policy Group - Access Interface Port - Faults [#0]
--------------------------------------------------
None
```

Developer

```
# iserver get aci pg access intf port --apic apic21 --view fault

{
    "duration": 1351,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 380,
        "disconnect_time": 0,
        "mo_time": 674,
        "total_time": 1054
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

True	380	-	connect apic21o.emea-sp.cisco.com:443
True	361	8	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccPortGrp&rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsAttEntP,infraRsCdpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsMonIfInfraPol,infraRsStpIfPol,infraRsMcpIfPol,infraRsStormctrlIfPol
True	313	0	apic21o.emea-sp.cisco.com:443 class infraAccPortGrp query rsp-subtree-include=faults,no-scoped,subtree
```

[[Back]](./PgAccessInterfacePort.md)