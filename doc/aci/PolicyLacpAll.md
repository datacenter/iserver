# Policy - Port Channel

## Get all policies

```
# iserver get aci policy lacp --apic apic11

Apic: apic11

+--------------------------------------+----+-----------------+-------------------------------+-----------+-----------+------------+--------------+
| Policy Name                          | TF | Mode            | Control                       | Min Links | Max Links | Interfaces | Ref Policies |
+--------------------------------------+----+-----------------+-------------------------------+-----------+-----------+------------+--------------+
| cvim1-installer-lacp                 |    | active          | Fast Select Hot Standby Ports | 1         | 16        | 0          | 0            | 
|                                      |    |                 | Graceful Convergence          |           |           |            |              | 
|                                      |    |                 | Suspend Individual Ports      |           |           |            |              | 
| cvim1-installer-lacpnosuspend        |    | active          | Fast Select Hot Standby Ports | 1         | 16        | 0          | 0            | 
|                                      |    |                 | Graceful Convergence          |           |           |            |              | 
| cvim1-LACP_ON                        |    | active          | Fast Select Hot Standby Ports | 1         | 16        | 0          | 0            | 
|                                      |    |                 | Suspend Individual Ports      |           |           |            |              | 
| default                              |    | off             | Fast Select Hot Standby Ports | 1         | 16        | 0          | 3            | 
|                                      |    |                 | Graceful Convergence          |           |           |            |              | 
|                                      |    |                 | Suspend Individual Ports      |           |           |            |              | 
| EU-SPDC-CDC_lacpLagPol               |    | mac-pin         | Fast Select Hot Standby Ports | 1         | 16        | 0          | 1            | 
|                                      |    |                 | Graceful Convergence          |           |           |            |              | 
|                                      |    |                 | Suspend Individual Ports      |           |           |            |              | 
| EU-SPDC-R3DC_lacpLagPol              |    | mac-pin         | Fast Select Hot Standby Ports | 1         | 16        | 0          | 1            | 
|                                      |    |                 | Graceful Convergence          |           |           |            |              | 
|                                      |    |                 | Suspend Individual Ports      |           |           |            |              | 
| EU-SPDC-R4CDC_lacpLagPol             |    | mac-pin         | Fast Select Hot Standby Ports | 1         | 16        | 0          | 0            | 
|                                      |    |                 | Graceful Convergence          |           |           |            |              | 
|                                      |    |                 | Suspend Individual Ports      |           |           |            |              | 
| EU-SPDC-R4DC_lacpLagPol              |    | mac-pin         | Fast Select Hot Standby Ports | 1         | 16        | 0          | 0            | 
|                                      |    |                 | Graceful Convergence          |           |           |            |              | 
|                                      |    |                 | Suspend Individual Ports      |           |           |            |              | 
| LACP-active                          |    | active          | Suspend Individual Ports      | 1         | 16        | 14         | 7            | 
| LACP-Active-1-16                     |    | active          |                               | 1         | 16        | 2          | 2            | 
| LACP-active-PXE                      |    | active          | Fast Select Hot Standby Ports | 1         | 16        | 0          | 0            | 
|                                      |    |                 | Graceful Convergence          |           |           |            |              | 
|                                      |    |                 | Suspend Individual Ports      |           |           |            |              | 
| LACP-Passive-1-16                    |    | passive         | Fast Select Hot Standby Ports | 1         | 16        | 0          | 0            | 
|                                      |    |                 | Graceful Convergence          |           |           |            |              | 
|                                      |    |                 | Suspend Individual Ports      |           |           |            |              | 
| MAC-Pinning                          |    | mac-pin         | Fast Select Hot Standby Ports | 1         | 16        | 0          | 0            | 
|                                      |    |                 | Graceful Convergence          |           |           |            |              | 
|                                      |    |                 | Suspend Individual Ports      |           |           |            |              | 
| MAC-Pinning-PhysPortLoad             |    | mac-pin-nicload | Fast Select Hot Standby Ports | 1         | 16        | 0          | 0            | 
|                                      |    |                 | Graceful Convergence          |           |           |            |              | 
|                                      |    |                 | Suspend Individual Ports      |           |           |            |              | 
| nidemo-dummy                         |    | off             | Fast Select Hot Standby Ports | 1         | 16        | 0          | 0            | 
|                                      |    |                 | Graceful Convergence          |           |           |            |              | 
|                                      |    |                 | Suspend Individual Ports      |           |           |            |              | 
| P3_LACP_ON                           |    | active          | Fast Select Hot Standby Ports | 1         | 16        | 0          | 0            | 
|                                      |    |                 | Suspend Individual Ports      |           |           |            |              | 
| P3_LACP_ON_PXE                       |    | active          | Fast Select Hot Standby Ports | 1         | 16        | 0          | 0            | 
| pod0-LACP_ON                         |    | active          | Fast Select Hot Standby Ports | 1         | 16        | 0          | 1            | 
| pod1a-LACP_ON                        |    | active          | Fast Select Hot Standby Ports | 1         | 16        | 26         | 13           | 
| pod4A-LACP_ON                        |    | active          | Fast Select Hot Standby Ports | 1         | 16        | 28         | 0            | 
| pod4a-LACP_ON                        |    | active          | Fast Select Hot Standby Ports | 1         | 16        | 28         | 14           | 
| podZZ-LACP_ON                        |    | active          | Fast Select Hot Standby Ports | 1         | 16        | 0          | 0            | 
| system-lacp-active                   |    | active          | Fast Select Hot Standby Ports | 1         | 16        | 0          | 0            | 
|                                      |    |                 | Graceful Convergence          |           |           |            |              | 
| system-lacp-passive                  |    | passive         | Fast Select Hot Standby Ports | 1         | 16        | 0          | 0            | 
|                                      |    |                 | Graceful Convergence          |           |           |            |              | 
| system-mac-pinning                   |    | mac-pin         | Fast Select Hot Standby Ports | 1         | 16        | 0          | 0            | 
|                                      |    |                 | Graceful Convergence          |           |           |            |              | 
|                                      |    |                 | Suspend Individual Ports      |           |           |            |              | 
| system-mac-pinning-physical-nic-load |    | mac-pin-nicload | Fast Select Hot Standby Ports | 1         | 16        | 0          | 0            | 
|                                      |    |                 | Graceful Convergence          |           |           |            |              | 
|                                      |    |                 | Suspend Individual Ports      |           |           |            |              | 
| system-static-on                     |    | off             | Fast Select Hot Standby Ports | 1         | 16        | 0          | 0            | 
|                                      |    |                 | Graceful Convergence          |           |           |            |              | 
+--------------------------------------+----+-----------------+-------------------------------+-----------+-----------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy lacp --apic apic11

{
    "duration": 22185,
    "apic": {
        "read": true,
        "success": 48,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 47,
        "connect_time": 404,
        "disconnect_time": 0,
        "mo_time": 21417,
        "total_time": 21821
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
    }
}

Log: apic
----------

True	404	-	connect apic11o.emea-sp.cisco.com
True	349	27	apic11o.emea-sp.cisco.com class lacpLagPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	446	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-podZZ-LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	459	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod4A-LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	391	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-EU-SPDC-CDC_lacpLagPol query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	456	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-P3_LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	473	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod1a-LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	458	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-nidemo-dummy query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	405	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	444	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-P3_LACP_ON_PXE query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	511	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod0-LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	481	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-system-mac-pinning-physical-nic-load query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	395	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-EU-SPDC-R3DC_lacpLagPol query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	486	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-active query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	477	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-system-lacp-active query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	455	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-system-lacp-passive query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	464	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-EU-SPDC-R4CDC_lacpLagPol query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	479	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-MAC-Pinning query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	450	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-system-static-on query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	470	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-active-PXE query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	465	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-cvim1-installer-lacpnosuspend query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	535	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-EU-SPDC-R4DC_lacpLagPol query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	470	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-cvim1-LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	464	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-Passive-1-16 query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	460	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-Active-1-16 query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	463	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-cvim1-installer-lacp query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	471	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod4a-LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	471	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-system-mac-pinning query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	469	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-MAC-Pinning-PhysPortLoad query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	526	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod1a-LACP_ON query rsp-subtree-include=full-deployment&target-node=202&target-path=L2IfPolToEthIf
True	476	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod1a-LACP_ON query rsp-subtree-include=full-deployment&target-node=201&target-path=L2IfPolToEthIf
True	438	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=301&target-path=L2IfPolToEthIf
True	409	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=202&target-path=L2IfPolToEthIf
True	429	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=302&target-path=L2IfPolToEthIf
True	390	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=206&target-path=L2IfPolToEthIf
True	387	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=102&target-path=L2IfPolToEthIf
True	385	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=201&target-path=L2IfPolToEthIf
True	396	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=101&target-path=L2IfPolToEthIf
True	403	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=205&target-path=L2IfPolToEthIf
True	492	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-active query rsp-subtree-include=full-deployment&target-node=205&target-path=L2IfPolToEthIf
True	483	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-active query rsp-subtree-include=full-deployment&target-node=301&target-path=L2IfPolToEthIf
True	521	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-active query rsp-subtree-include=full-deployment&target-node=302&target-path=L2IfPolToEthIf
True	483	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-active query rsp-subtree-include=full-deployment&target-node=206&target-path=L2IfPolToEthIf
True	513	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-Active-1-16 query rsp-subtree-include=full-deployment&target-node=201&target-path=L2IfPolToEthIf
True	474	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-Active-1-16 query rsp-subtree-include=full-deployment&target-node=202&target-path=L2IfPolToEthIf
True	477	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod4a-LACP_ON query rsp-subtree-include=full-deployment&target-node=201&target-path=L2IfPolToEthIf
True	615	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod4a-LACP_ON query rsp-subtree-include=full-deployment&target-node=202&target-path=L2IfPolToEthIf
True	303	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyLacp.md)