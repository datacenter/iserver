# Policy Group - Access Interface VPC

## Policy specific output (default)

```
# iserver get aci pg access intf vpc --apic apic11 --name HX*

Apic: apic11 (mode:online, cache:off)

+-----------------+-------------------------+------------+------------+-------------+-------------+-----------+---------+---------+--------------+---------------+---------------+
| Name            | Attached Entity Profile | CDP        | Link Level | LLDP        | LACP        | Link Flap | MCP     | STP     | L2           | Storm Control | Port Security |
+-----------------+-------------------------+------------+------------+-------------+-------------+-----------+---------+---------+--------------+---------------+---------------+
| HX1-FI-A_PolGrp | HX1_AAEP                | CDP_enable | Inherit    | LLDP_enable | LACP-active | default   | default | default | L2-local_Pol | default       | default       | 
| HX1-FI-B_PolGrp | HX1_AAEP                | CDP_enable | Inherit    | LLDP_enable | LACP-active | default   | default | default | L2-local_Pol | default       | default       | 
+-----------------+-------------------------+------------+------------+-------------+-------------+-----------+---------+---------+--------------+---------------+---------------+
```

Developer

```
# iserver get aci pg access intf vpc --apic apic11 --name HX*

{
    "duration": 1396,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 438,
        "disconnect_time": 0,
        "mo_time": 534,
        "total_time": 972
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

True	438	-	connect apic11o.emea-sp.cisco.com
True	534	37	apic11o.emea-sp.cisco.com mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree=children&rsp-subtree-class=infraRsCdpIfPol,infraRsMcpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsLacpPol,infraRsMonIfInfraPol,infraAccBndlSubgrp,infraRsStpIfPol,infraRsAttEntP,infraRsSpanVSrcGrp,infraRsSpanVDestGrp,infraRsL2IfPol,infraRsStormctrlIfPol,infraRsQosEgressDppIfPol,infraRsQosIngressDppIfPol,infraRsQosSdIfPol,infraRsQosPfcIfPol,infraRsQosEgressDppIfPol,infraRsL2PortSecurityPol,infraRsFcIfPol,infraRsMacsecIfPol
```

[[Back]](./PgAccessInterfaceVpc.md)