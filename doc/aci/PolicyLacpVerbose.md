# Policy - Port Channel

## Verbose output

```
# iserver get aci policy lacp --apic apic11 --name default --view verbose

Apic: apic11

Port Channel Policy Properties
------------------------------
- Policy Name  : default
- TF           : False
- Mode         : off
- Control      :
	Fast Select Hot Standby Ports
	Graceful Convergence
	Suspend Individual Ports
- Min Links    : 1
- Max Links    : 16
- Interfaces   : 0
- Ref Policies : 3


+--------------+--------------+--------------+
| Policy Name  | Policy Type  | Policy Class |
+--------------+--------------+--------------+
| infra        | Access Infra | infraInfra   | 
| EU-SPDC-CDC  | VMM Domain   | vmmDomP      | 
| EU-SPDC-R3DC | VMM Domain   | vmmDomP      | 
+--------------+--------------+--------------+
```

Developer

```
# iserver get aci policy lacp --apic apic11 --name default --view verbose

{
    "duration": 22290,
    "apic": {
        "read": true,
        "success": 48,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 47,
        "connect_time": 401,
        "disconnect_time": 0,
        "mo_time": 21592,
        "total_time": 21993
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

True	401	-	connect apic11o.emea-sp.cisco.com
True	315	27	apic11o.emea-sp.cisco.com class lacpLagPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	458	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-podZZ-LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	459	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod4A-LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	411	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-EU-SPDC-CDC_lacpLagPol query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	454	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-P3_LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	484	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod1a-LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	461	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-nidemo-dummy query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	434	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	494	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-P3_LACP_ON_PXE query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	475	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod0-LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	463	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-system-mac-pinning-physical-nic-load query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	389	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-EU-SPDC-R3DC_lacpLagPol query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	503	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-active query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	511	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-system-lacp-active query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	472	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-system-lacp-passive query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	500	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-EU-SPDC-R4CDC_lacpLagPol query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	500	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-MAC-Pinning query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	463	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-system-static-on query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	455	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-active-PXE query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	478	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-cvim1-installer-lacpnosuspend query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	511	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-EU-SPDC-R4DC_lacpLagPol query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	468	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-cvim1-LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	471	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-Passive-1-16 query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	484	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-Active-1-16 query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	454	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-cvim1-installer-lacp query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	500	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod4a-LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	468	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-system-mac-pinning query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	475	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-MAC-Pinning-PhysPortLoad query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	501	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod1a-LACP_ON query rsp-subtree-include=full-deployment&target-node=202&target-path=L2IfPolToEthIf
True	508	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod1a-LACP_ON query rsp-subtree-include=full-deployment&target-node=201&target-path=L2IfPolToEthIf
True	464	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=301&target-path=L2IfPolToEthIf
True	403	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=202&target-path=L2IfPolToEthIf
True	418	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=302&target-path=L2IfPolToEthIf
True	408	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=206&target-path=L2IfPolToEthIf
True	397	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=102&target-path=L2IfPolToEthIf
True	422	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=201&target-path=L2IfPolToEthIf
True	393	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=101&target-path=L2IfPolToEthIf
True	389	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=205&target-path=L2IfPolToEthIf
True	503	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-active query rsp-subtree-include=full-deployment&target-node=205&target-path=L2IfPolToEthIf
True	486	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-active query rsp-subtree-include=full-deployment&target-node=301&target-path=L2IfPolToEthIf
True	493	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-active query rsp-subtree-include=full-deployment&target-node=302&target-path=L2IfPolToEthIf
True	503	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-active query rsp-subtree-include=full-deployment&target-node=206&target-path=L2IfPolToEthIf
True	542	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-Active-1-16 query rsp-subtree-include=full-deployment&target-node=201&target-path=L2IfPolToEthIf
True	461	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-Active-1-16 query rsp-subtree-include=full-deployment&target-node=202&target-path=L2IfPolToEthIf
True	485	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod4a-LACP_ON query rsp-subtree-include=full-deployment&target-node=201&target-path=L2IfPolToEthIf
True	505	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod4a-LACP_ON query rsp-subtree-include=full-deployment&target-node=202&target-path=L2IfPolToEthIf
True	301	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyLacp.md)