# Policy - Port Channel

## Interface specific output

```
# iserver get aci policy lacp --apic apic11 --name default --view intf

Apic: apic11

+-------------+------+-----------+
| Policy Name | Node | Interface |
+-------------+------+-----------+
| default     |      |           | 
+-------------+------+-----------+
```

Developer

```
# iserver get aci policy lacp --apic apic11 --name default --view intf

{
    "duration": 22340,
    "apic": {
        "read": true,
        "success": 48,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 47,
        "connect_time": 386,
        "disconnect_time": 0,
        "mo_time": 21664,
        "total_time": 22050
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

True	386	-	connect apic11o.emea-sp.cisco.com
True	319	27	apic11o.emea-sp.cisco.com class lacpLagPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	441	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-podZZ-LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	471	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod4A-LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	402	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-EU-SPDC-CDC_lacpLagPol query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	456	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-P3_LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	458	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod1a-LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	468	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-nidemo-dummy query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	394	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	459	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-P3_LACP_ON_PXE query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	510	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod0-LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	462	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-system-mac-pinning-physical-nic-load query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	380	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-EU-SPDC-R3DC_lacpLagPol query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	503	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-active query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	513	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-system-lacp-active query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	456	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-system-lacp-passive query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	456	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-EU-SPDC-R4CDC_lacpLagPol query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	483	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-MAC-Pinning query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	458	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-system-static-on query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	476	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-active-PXE query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	474	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-cvim1-installer-lacpnosuspend query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	525	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-EU-SPDC-R4DC_lacpLagPol query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	492	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-cvim1-LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	448	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-Passive-1-16 query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	481	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-Active-1-16 query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	466	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-cvim1-installer-lacp query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	499	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod4a-LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	485	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-system-mac-pinning query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	461	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-MAC-Pinning-PhysPortLoad query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	531	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod1a-LACP_ON query rsp-subtree-include=full-deployment&target-node=202&target-path=L2IfPolToEthIf
True	493	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod1a-LACP_ON query rsp-subtree-include=full-deployment&target-node=201&target-path=L2IfPolToEthIf
True	429	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=301&target-path=L2IfPolToEthIf
True	407	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=202&target-path=L2IfPolToEthIf
True	409	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=302&target-path=L2IfPolToEthIf
True	430	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=206&target-path=L2IfPolToEthIf
True	431	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=102&target-path=L2IfPolToEthIf
True	454	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=201&target-path=L2IfPolToEthIf
True	443	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=101&target-path=L2IfPolToEthIf
True	393	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=205&target-path=L2IfPolToEthIf
True	537	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-active query rsp-subtree-include=full-deployment&target-node=205&target-path=L2IfPolToEthIf
True	502	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-active query rsp-subtree-include=full-deployment&target-node=301&target-path=L2IfPolToEthIf
True	517	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-active query rsp-subtree-include=full-deployment&target-node=302&target-path=L2IfPolToEthIf
True	530	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-active query rsp-subtree-include=full-deployment&target-node=206&target-path=L2IfPolToEthIf
True	482	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-Active-1-16 query rsp-subtree-include=full-deployment&target-node=201&target-path=L2IfPolToEthIf
True	489	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-Active-1-16 query rsp-subtree-include=full-deployment&target-node=202&target-path=L2IfPolToEthIf
True	509	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod4a-LACP_ON query rsp-subtree-include=full-deployment&target-node=201&target-path=L2IfPolToEthIf
True	471	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod4a-LACP_ON query rsp-subtree-include=full-deployment&target-node=202&target-path=L2IfPolToEthIf
True	311	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyLacp.md)