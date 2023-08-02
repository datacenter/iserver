# Policy Group - Access Interface - Leaf Access PC/VPC

## Fault view

```
# iserver get aci pg access intf vpc --apic apic21 --view fault

Apic: apic21 (mode:online, cache:off)

Policy Group - Access Interface PC/VPC - Faults [#6]
----------------------------------------------------

+---------------------+-----+-------+--------------------+-------------------------------+-----------+----------------------------------------------------------------------------+
| PG Name             | Sev | Code  | Cause              | Created Time                  | Lifecycle | Description                                                                |
+---------------------+-----+-------+--------------------+-------------------------------+-----------+----------------------------------------------------------------------------+
| ESX20-CDC-22_PolGrp | Maj | F1296 | interface-vpc-down | 2023-06-18T09:44:34.467+02:00 | raised    | Fault delegate: vPC ESX20-CDC-22_PolGrp is down in Pod 1 node 2201 fabric  | 
|                     |     |       |                    |                               |           | hostname cl2201-eu-spdc                                                    | 
| ESX20-CDC-22_PolGrp | Maj | F1296 | interface-vpc-down | 2023-06-18T09:18:19.916+02:00 | raised    | Fault delegate: vPC ESX20-CDC-22_PolGrp is down in Pod 1 node 2202 fabric  | 
|                     |     |       |                    |                               |           | hostname cl2202-eu-spdc                                                    | 
| ESX21-CDC-22_PolGrp | Maj | F1296 | interface-vpc-down | 2023-06-18T09:44:11.082+02:00 | raised    | Fault delegate: vPC ESX21-CDC-22_PolGrp is down in Pod 1 node 2207 fabric  | 
|                     |     |       |                    |                               |           | hostname cl2207-eu-spdc                                                    | 
| ESX21-CDC-22_PolGrp | Maj | F1296 | interface-vpc-down | 2023-06-18T09:16:15.179+02:00 | raised    | Fault delegate: vPC ESX21-CDC-22_PolGrp is down in Pod 1 node 2208 fabric  | 
|                     |     |       |                    |                               |           | hostname cl2208-eu-spdc                                                    | 
| k8s_ocp_bm_3_PolGrp | Maj | F1296 | interface-vpc-down | 2023-06-18T09:16:15.241+02:00 | raised    | Fault delegate: vPC k8s_ocp_bm_3_PolGrp is down in Pod 1 node 2208 fabric  | 
|                     |     |       |                    |                               |           | hostname cl2208-eu-spdc                                                    | 
| k8s_ocp_bm_3_PolGrp | Maj | F1296 | interface-vpc-down | 2023-06-18T09:44:11.056+02:00 | raised    | Fault delegate: vPC k8s_ocp_bm_3_PolGrp is down in Pod 1 node 2207 fabric  | 
|                     |     |       |                    |                               |           | hostname cl2207-eu-spdc                                                    | 
+---------------------+-----+-------+--------------------+-------------------------------+-----------+----------------------------------------------------------------------------+
```

Developer

```
# iserver get aci pg access intf vpc --apic apic21 --view fault

{
    "duration": 1685,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 442,
        "disconnect_time": 0,
        "mo_time": 892,
        "total_time": 1334
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

True	442	-	connect apic21o.emea-sp.cisco.com:443
True	505	19	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsCdpIfPol,infraRsMcpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsLacpPol,infraRsMonIfInfraPol,infraAccBndlSubgrp,infraRsStpIfPol,infraRsAttEntP,infraRsSpanVSrcGrp,infraRsSpanVDestGrp,infraRsL2IfPol,infraRsStormctrlIfPol,infraRsQosEgressDppIfPol,infraRsQosIngressDppIfPol,infraRsQosSdIfPol,infraRsQosPfcIfPol,infraRsQosEgressDppIfPol,infraRsL2PortSecurityPol,infraRsFcIfPol,infraRsMacsecIfPol
True	387	6	apic21o.emea-sp.cisco.com:443 class infraAccBndlGrp query rsp-subtree-include=faults,no-scoped,subtree
```

[[Back]](./PgAccessInterfaceVpc.md)