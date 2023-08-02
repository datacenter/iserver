# Policy Group - Access Interface - Leaf Access Port

## Fault history view

```
# iserver get aci pg access intf port --apic apic21 --when any --view hfault

Apic: apic21 (mode:online, cache:off)

Policy Group - Access Interface Port - Fault Records last 10y [#0]
------------------------------------------------------------------
None
```

Developer

```
# iserver get aci pg access intf port --apic apic21 --when any --view hfault

{
    "duration": 1593,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 435,
        "disconnect_time": 0,
        "mo_time": 898,
        "total_time": 1333
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

True	435	-	connect apic21o.emea-sp.cisco.com:443
True	357	8	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccPortGrp&rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsAttEntP,infraRsCdpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsMonIfInfraPol,infraRsStpIfPol,infraRsMcpIfPol,infraRsStormctrlIfPol
True	541	0	apic21o.emea-sp.cisco.com:443 class infraAccPortGrp query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
```

[[Back]](./PgAccessInterfacePort.md)