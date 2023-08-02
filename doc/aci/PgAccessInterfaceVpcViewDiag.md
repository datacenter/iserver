# Policy Group - Access Interface - Leaf Access PC/VPC

## Diag view

```
# iserver get aci pg access intf vpc --apic apic21 --when 30d --view diag

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

Policy Group - Access Interface PC/VPC - Fault Records last 30d [#8]
--------------------------------------------------------------------

+---------------------+-----+-------+------------------------+-------------------------------+------------------+--------------------------------------------------------------------------------+
| PG Name             | Sev | Code  | Cause                  | Created Time                  | Lifecycle        | Description                                                                    |
+---------------------+-----+-------+------------------------+-------------------------------+------------------+--------------------------------------------------------------------------------+
| k8s_ocp_bm_1_PolGrp | --  | F2705 | interface-vpc-impaired | 2023-07-06T11:25:35.230+02:00 |                  | Fault delegate: vPC k8s_ocp_bm_1_PolGrp is impaired in Pod 1 node 2208 fabric  | 
|                     |     |       |                        |                               |                  | hostname cl2208-eu-spdc                                                        | 
| k8s_ocp_bm_1_PolGrp | --  | F2705 | interface-vpc-impaired | 2023-07-06T10:25:34.716+02:00 | retaining        | Fault delegate: vPC k8s_ocp_bm_1_PolGrp is impaired in Pod 1 node 2208 fabric  | 
|                     |     |       |                        |                               |                  | hostname cl2208-eu-spdc                                                        | 
| k8s_ocp_bm_1_PolGrp | Maj | F2705 | interface-vpc-impaired | 2023-07-06T10:23:25.497+02:00 | soaking-clearing | Fault delegate: vPC k8s_ocp_bm_1_PolGrp is impaired in Pod 1 node 2208 fabric  | 
|                     |     |       |                        |                               |                  | hostname cl2208-eu-spdc                                                        | 
| k8s_ocp_bm_1_PolGrp | Maj | F2705 | interface-vpc-impaired | 2023-07-06T10:23:22.145+02:00 | soaking          | Fault delegate: vPC k8s_ocp_bm_1_PolGrp is impaired in Pod 1 node 2208 fabric  | 
|                     |     |       |                        |                               |                  | hostname cl2208-eu-spdc                                                        | 
| k8s_ocp_bm_2_PolGrp | --  | F2705 | interface-vpc-impaired | 2023-07-06T11:25:35.232+02:00 |                  | Fault delegate: vPC k8s_ocp_bm_2_PolGrp is impaired in Pod 1 node 2208 fabric  | 
|                     |     |       |                        |                               |                  | hostname cl2208-eu-spdc                                                        | 
| k8s_ocp_bm_2_PolGrp | --  | F2705 | interface-vpc-impaired | 2023-07-06T10:25:34.718+02:00 | retaining        | Fault delegate: vPC k8s_ocp_bm_2_PolGrp is impaired in Pod 1 node 2208 fabric  | 
|                     |     |       |                        |                               |                  | hostname cl2208-eu-spdc                                                        | 
| k8s_ocp_bm_2_PolGrp | Maj | F2705 | interface-vpc-impaired | 2023-07-06T10:23:25.432+02:00 | soaking-clearing | Fault delegate: vPC k8s_ocp_bm_2_PolGrp is impaired in Pod 1 node 2208 fabric  | 
|                     |     |       |                        |                               |                  | hostname cl2208-eu-spdc                                                        | 
| k8s_ocp_bm_2_PolGrp | Maj | F2705 | interface-vpc-impaired | 2023-07-06T10:23:22.032+02:00 | soaking          | Fault delegate: vPC k8s_ocp_bm_2_PolGrp is impaired in Pod 1 node 2208 fabric  | 
|                     |     |       |                        |                               |                  | hostname cl2208-eu-spdc                                                        | 
+---------------------+-----+-------+------------------------+-------------------------------+------------------+--------------------------------------------------------------------------------+

Policy Group - Access Interface PC/VPC - Event Logs last 30d [#0]
-----------------------------------------------------------------
None

Policy Group - Access Interface PC/VPC - Audit Logs last 30d [#0]
-----------------------------------------------------------------
None
```

Developer

```
# iserver get aci pg access intf vpc --apic apic21 --when 30d --view diag

{
    "duration": 10807,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 385,
        "disconnect_time": 0,
        "mo_time": 9229,
        "total_time": 9614
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

True	385	-	connect apic21o.emea-sp.cisco.com:443
True	489	19	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsCdpIfPol,infraRsMcpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsLacpPol,infraRsMonIfInfraPol,infraAccBndlSubgrp,infraRsStpIfPol,infraRsAttEntP,infraRsSpanVSrcGrp,infraRsSpanVDestGrp,infraRsL2IfPol,infraRsStormctrlIfPol,infraRsQosEgressDppIfPol,infraRsQosIngressDppIfPol,infraRsQosSdIfPol,infraRsQosPfcIfPol,infraRsQosEgressDppIfPol,infraRsL2PortSecurityPol,infraRsFcIfPol,infraRsMacsecIfPol
True	385	6	apic21o.emea-sp.cisco.com:443 class infraAccBndlGrp query rsp-subtree-include=faults,no-scoped,subtree
True	6170	1000	apic21o.emea-sp.cisco.com:443 class infraAccBndlGrp query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	903	19	apic21o.emea-sp.cisco.com:443 class infraAccBndlGrp query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
True	1282	1046	apic21o.emea-sp.cisco.com:443 class infraAccBndlGrp query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./PgAccessInterfaceVpc.md)