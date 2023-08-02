# Policy Group - Access Interface - Leaf Access PC/VPC

## Fault history view

```
# iserver get aci pg access intf vpc --apic apic21 --when 30d --view hfault

Apic: apic21 (mode:online, cache:off)

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
```

Developer

```
# iserver get aci pg access intf vpc --apic apic21 --when 30d --view hfault

{
    "duration": 8178,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 431,
        "disconnect_time": 0,
        "mo_time": 6777,
        "total_time": 7208
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

True	431	-	connect apic21o.emea-sp.cisco.com:443
True	509	19	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsCdpIfPol,infraRsMcpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsLacpPol,infraRsMonIfInfraPol,infraAccBndlSubgrp,infraRsStpIfPol,infraRsAttEntP,infraRsSpanVSrcGrp,infraRsSpanVDestGrp,infraRsL2IfPol,infraRsStormctrlIfPol,infraRsQosEgressDppIfPol,infraRsQosIngressDppIfPol,infraRsQosSdIfPol,infraRsQosPfcIfPol,infraRsQosEgressDppIfPol,infraRsL2PortSecurityPol,infraRsFcIfPol,infraRsMacsecIfPol
True	6268	1000	apic21o.emea-sp.cisco.com:443 class infraAccBndlGrp query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
```

[[Back]](./PgAccessInterfaceVpc.md)