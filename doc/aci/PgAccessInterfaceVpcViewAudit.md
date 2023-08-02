# Policy Group - Access Interface - Leaf Access PC/VPC

## Audit view

```
# iserver get aci pg access intf vpc --apic apic21 --when 30d --view audit

Apic: apic21 (mode:online, cache:off)

Policy Group - Access Interface PC/VPC - Audit Logs last 30d [#0]
-----------------------------------------------------------------
None
```

Developer

```
# iserver get aci pg access intf vpc --apic apic21 --when 30d --view audit

{
    "duration": 3105,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 437,
        "disconnect_time": 0,
        "mo_time": 1804,
        "total_time": 2241
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

True	437	-	connect apic21o.emea-sp.cisco.com:443
True	518	19	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsCdpIfPol,infraRsMcpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsLacpPol,infraRsMonIfInfraPol,infraAccBndlSubgrp,infraRsStpIfPol,infraRsAttEntP,infraRsSpanVSrcGrp,infraRsSpanVDestGrp,infraRsL2IfPol,infraRsStormctrlIfPol,infraRsQosEgressDppIfPol,infraRsQosIngressDppIfPol,infraRsQosSdIfPol,infraRsQosPfcIfPol,infraRsQosEgressDppIfPol,infraRsL2PortSecurityPol,infraRsFcIfPol,infraRsMacsecIfPol
True	1286	1046	apic21o.emea-sp.cisco.com:443 class infraAccBndlGrp query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./PgAccessInterfaceVpc.md)