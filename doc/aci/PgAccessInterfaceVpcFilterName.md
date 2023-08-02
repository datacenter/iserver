# Policy Group - Access Interface - Leaf Access PC/VPC

## Filter by name

```
# iserver get aci pg access intf vpc --apic apic21 --name HX*

Apic: apic21 (mode:online, cache:off)

Policy Group - Access Interface PC/VPC [#2]
-------------------------------------------

+---------+-----------------+----------+------------+------------+-------------+-------------+-----------+---------+---------+--------------+------------+----------+
| Faults  | Name            | AAEP     | CDP        | Link Level | LLDP        | LACP        | Link Flap | MCP     | STP     | L2           | Storm Ctrl | Port Sec |
+---------+-----------------+----------+------------+------------+-------------+-------------+-----------+---------+---------+--------------+------------+----------+
| 0 0 0 0 | HX1-FI-A_PolGrp | HX1_AAEP | CDP-enable | Inherit    | LLDP-enable | LACP-active | default   | default | default | L2-local_Pol | default    | default  | 
| 0 0 0 0 | HX1-FI-B_PolGrp | HX1_AAEP | CDP-enable | Inherit    | LLDP-enable | LACP-active | default   | default | default | L2-local_Pol | default    | default  | 
+---------+-----------------+----------+------------+------------+-------------+-------------+-----------+---------+---------+--------------+------------+----------+
```

Developer

```
# iserver get aci pg access intf vpc --apic apic21 --name HX*

{
    "duration": 1195,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 414,
        "disconnect_time": 0,
        "mo_time": 499,
        "total_time": 913
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

True	414	-	connect apic21o.emea-sp.cisco.com:443
True	499	19	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsCdpIfPol,infraRsMcpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsLacpPol,infraRsMonIfInfraPol,infraAccBndlSubgrp,infraRsStpIfPol,infraRsAttEntP,infraRsSpanVSrcGrp,infraRsSpanVDestGrp,infraRsL2IfPol,infraRsStormctrlIfPol,infraRsQosEgressDppIfPol,infraRsQosIngressDppIfPol,infraRsQosSdIfPol,infraRsQosPfcIfPol,infraRsQosEgressDppIfPol,infraRsL2PortSecurityPol,infraRsFcIfPol,infraRsMacsecIfPol
```

[[Back]](./PgAccessInterfaceVpc.md)