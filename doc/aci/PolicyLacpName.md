# Policy - Port Channel

## Filter by name

```
# iserver get aci policy lacp --apic apic11 --name default

Apic: apic11 (mode:online, cache:off)

+-------------+----+------+-------------------------------+-----------+-----------+------------+--------------+
| Policy Name | TF | Mode | Control                       | Min Links | Max Links | Interfaces | Ref Policies |
+-------------+----+------+-------------------------------+-----------+-----------+------------+--------------+
| default     |    | off  | Fast Select Hot Standby Ports | 1         | 16        | 0          | 3            | 
|             |    |      | Graceful Convergence          |           |           |            |              | 
|             |    |      | Suspend Individual Ports      |           |           |            |              | 
+-------------+----+------+-------------------------------+-----------+-----------+------------+--------------+
```

Developer

```
# iserver get aci policy lacp --apic apic11 --name default

{
    "duration": 26445,
    "apic": {
        "read": true,
        "success": 50,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 49,
        "connect_time": 422,
        "disconnect_time": 0,
        "mo_time": 25453,
        "total_time": 25875
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

True	422	-	connect apic11o.emea-sp.cisco.com
True	347	27	apic11o.emea-sp.cisco.com class lacpLagPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	478	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-podZZ-LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	604	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod4A-LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	412	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-EU-SPDC-CDC_lacpLagPol query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	498	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-P3_LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	703	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod1a-LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	507	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-nidemo-dummy query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	437	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	578	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-P3_LACP_ON_PXE query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	621	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod0-LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	598	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-system-mac-pinning-physical-nic-load query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	448	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-EU-SPDC-R3DC_lacpLagPol query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	567	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-active query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	496	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-system-lacp-active query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	523	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-system-lacp-passive query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	568	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-EU-SPDC-R4CDC_lacpLagPol query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	550	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-MAC-Pinning query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	606	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-system-static-on query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	508	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-active-PXE query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	513	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-cvim1-installer-lacpnosuspend query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	473	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-EU-SPDC-R4DC_lacpLagPol query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	890	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-cvim1-LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	571	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-Passive-1-16 query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	506	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-Active-1-16 query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	509	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-cvim1-installer-lacp query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	506	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod4a-LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	495	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-system-mac-pinning query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	552	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-MAC-Pinning-PhysPortLoad query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	569	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod1a-LACP_ON query rsp-subtree-include=full-deployment&target-node=202&target-path=L2IfPolToEthIf
True	598	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod1a-LACP_ON query rsp-subtree-include=full-deployment&target-node=201&target-path=L2IfPolToEthIf
True	430	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=210&target-path=L2IfPolToEthIf
True	439	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=301&target-path=L2IfPolToEthIf
True	530	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=202&target-path=L2IfPolToEthIf
True	450	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=302&target-path=L2IfPolToEthIf
True	426	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=206&target-path=L2IfPolToEthIf
True	434	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=209&target-path=L2IfPolToEthIf
True	451	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=102&target-path=L2IfPolToEthIf
True	484	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=201&target-path=L2IfPolToEthIf
True	440	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=101&target-path=L2IfPolToEthIf
True	429	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=205&target-path=L2IfPolToEthIf
True	573	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-active query rsp-subtree-include=full-deployment&target-node=205&target-path=L2IfPolToEthIf
True	525	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-active query rsp-subtree-include=full-deployment&target-node=301&target-path=L2IfPolToEthIf
True	515	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-active query rsp-subtree-include=full-deployment&target-node=302&target-path=L2IfPolToEthIf
True	554	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-active query rsp-subtree-include=full-deployment&target-node=206&target-path=L2IfPolToEthIf
True	507	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-Active-1-16 query rsp-subtree-include=full-deployment&target-node=201&target-path=L2IfPolToEthIf
True	604	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-Active-1-16 query rsp-subtree-include=full-deployment&target-node=202&target-path=L2IfPolToEthIf
True	512	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod4a-LACP_ON query rsp-subtree-include=full-deployment&target-node=201&target-path=L2IfPolToEthIf
True	593	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod4a-LACP_ON query rsp-subtree-include=full-deployment&target-node=202&target-path=L2IfPolToEthIf
True	326	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyLacp.md)