# Policy - Port Channel

## Usage specific output

```
# iserver get aci policy lacp --apic apic11 --name default --view usage

Apic: apic11

+-------------+------+-----------------+-----------------+-----------------+
| Policy Name | Node | Interface Count | Ref Policy Type | Ref Policy Name |
+-------------+------+-----------------+-----------------+-----------------+
| default     |      |                 | Access Infra    | infra           | 
|             |      |                 | VMM Domain      | EU-SPDC-CDC     | 
|             |      |                 | VMM Domain      | EU-SPDC-R3DC    | 
+-------------+------+-----------------+-----------------+-----------------+
```

Developer

```
# iserver get aci policy lacp --apic apic11 --name default --view usage

{
    "duration": 22240,
    "apic": {
        "read": true,
        "success": 48,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 47,
        "connect_time": 387,
        "disconnect_time": 0,
        "mo_time": 21582,
        "total_time": 21969
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

True	387	-	connect apic11o.emea-sp.cisco.com
True	309	27	apic11o.emea-sp.cisco.com class lacpLagPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	456	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-podZZ-LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	439	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod4A-LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	405	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-EU-SPDC-CDC_lacpLagPol query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	530	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-P3_LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	461	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod1a-LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	475	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-nidemo-dummy query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	418	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	460	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-P3_LACP_ON_PXE query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	460	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod0-LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	484	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-system-mac-pinning-physical-nic-load query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	450	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-EU-SPDC-R3DC_lacpLagPol query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	484	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-active query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	538	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-system-lacp-active query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	463	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-system-lacp-passive query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	460	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-EU-SPDC-R4CDC_lacpLagPol query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	488	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-MAC-Pinning query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	498	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-system-static-on query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	485	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-active-PXE query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	481	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-cvim1-installer-lacpnosuspend query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	464	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-EU-SPDC-R4DC_lacpLagPol query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	546	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-cvim1-LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	464	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-Passive-1-16 query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	473	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-Active-1-16 query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	501	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-cvim1-installer-lacp query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	488	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod4a-LACP_ON query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	460	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-system-mac-pinning query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	462	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-MAC-Pinning-PhysPortLoad query rsp-subtree-include=full-deployment&target-path=L2IfPolToEthIf
True	473	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod1a-LACP_ON query rsp-subtree-include=full-deployment&target-node=202&target-path=L2IfPolToEthIf
True	468	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod1a-LACP_ON query rsp-subtree-include=full-deployment&target-node=201&target-path=L2IfPolToEthIf
True	421	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=301&target-path=L2IfPolToEthIf
True	444	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=202&target-path=L2IfPolToEthIf
True	386	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=302&target-path=L2IfPolToEthIf
True	415	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=206&target-path=L2IfPolToEthIf
True	400	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=102&target-path=L2IfPolToEthIf
True	422	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=201&target-path=L2IfPolToEthIf
True	408	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=101&target-path=L2IfPolToEthIf
True	406	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-default query rsp-subtree-include=full-deployment&target-node=205&target-path=L2IfPolToEthIf
True	492	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-active query rsp-subtree-include=full-deployment&target-node=205&target-path=L2IfPolToEthIf
True	497	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-active query rsp-subtree-include=full-deployment&target-node=301&target-path=L2IfPolToEthIf
True	494	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-active query rsp-subtree-include=full-deployment&target-node=302&target-path=L2IfPolToEthIf
True	485	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-active query rsp-subtree-include=full-deployment&target-node=206&target-path=L2IfPolToEthIf
True	457	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-Active-1-16 query rsp-subtree-include=full-deployment&target-node=201&target-path=L2IfPolToEthIf
True	526	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-LACP-Active-1-16 query rsp-subtree-include=full-deployment&target-node=202&target-path=L2IfPolToEthIf
True	484	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod4a-LACP_ON query rsp-subtree-include=full-deployment&target-node=201&target-path=L2IfPolToEthIf
True	492	1	apic11o.emea-sp.cisco.com mo uni/infra/lacplagp-pod4a-LACP_ON query rsp-subtree-include=full-deployment&target-node=202&target-path=L2IfPolToEthIf
True	310	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyLacp.md)