# Virtual Routing and Forwarding (VRF)

## Verbose output

Get selected vrf details
- VRF properties
- associated EPGs
- associated bridge domains

```
# iserver get aci vrf --apic apic21 --name Infra_VRF --view verbose

Apic: apic21 (mode:online, cache:off)

+------------------+----------------+---------------+----------+---------+----------------+-------------------+-----------------+--------------------+
| VRF              | PCE Preference | PCE Direction | Class ID | VNID    | Associated EPG | Associated BD     | BD Subnets      | Associated L3Out   |
+------------------+----------------+---------------+----------+---------+----------------+-------------------+-----------------+--------------------+
| common/Infra_VRF | unenforced     | ingress       | 49153    | 2818048 |                | common/Infra_BD   | 10.58.24.78/28  | common/Infra_L3out | 
|                  |                |               |          |         |                | k8s/bmk8s_1_BD    | 10.58.24.94/28  |                    | 
|                  |                |               |          |         |                | k8s/bmk8s_2_BD    | 10.58.29.94/28  |                    | 
|                  |                |               |          |         |                | k8s/bmk8s_prov_BD | 10.58.24.126/28 |                    | 
|                  |                |               |          |         |                | k8s/bml3outk8s_BD | 10.58.25.174/28 |                    | 
|                  |                |               |          |         |                | k8s/MGMT_BD       | 10.58.24.174/28 |                    | 
|                  |                |               |          |         |                | k8s/vk8s_1_BD     | 10.58.24.190/28 |                    | 
|                  |                |               |          |         |                | k8s/vk8s_2_BD     | 10.58.24.206/28 |                    | 
|                  |                |               |          |         |                | k8s/vk8s_3_BD     | 10.58.24.222/28 |                    | 
|                  |                |               |          |         |                | k8s/vk8s_4_BD     | 10.58.24.110/28 |                    | 
|                  |                |               |          |         |                | k8s/vl3outk8s_BD  | 10.58.25.158/27 |                    | 
|                  |                |               |          |         |                | k8s/VM2VM_BD      |                 |                    | 
|                  |                |               |          |         |                | vEPC_demo/MGMT_BD |                 |                    | 
+------------------+----------------+---------------+----------+---------+----------------+-------------------+-----------------+--------------------+

VRF Properties
--------------
- Name                                  : Infra_VRF
- Tenant                                : common
- Data Plane Learning                   : enabled
- Multicast                             : permit
- Policy Control Enforcement Direction  : ingress
- Policy Control Enforcement Preference : unenforced
- Bridge Domain Enforcement Status      : no
- Class ID                              : 49153
- VNID                                  : 2818048
- Endpoints Count                       : 52


Associated Bridge Domains
-------------------------

+-------------------+-----------------+-------+------------------+--------------------+
| Bridge Domain     | Subnet          | Usage | VRF              | L3Out              |
+-------------------+-----------------+-------+------------------+--------------------+
| common/Infra_BD   |                 |       | common/Infra_VRF |                    | 
+-------------------+-----------------+-------+------------------+--------------------+
| k8s/bmk8s_1_BD    | 10.58.24.78/28  | 1/14  | common/Infra_VRF | common/Infra_L3out | 
+-------------------+-----------------+-------+------------------+--------------------+
| k8s/bmk8s_2_BD    | 10.58.24.94/28  | 1/14  | common/Infra_VRF | common/Infra_L3out | 
+-------------------+-----------------+-------+------------------+--------------------+
| k8s/bmk8s_prov_BD | 10.58.29.94/28  | 5/14  | common/Infra_VRF | common/Infra_L3out | 
+-------------------+-----------------+-------+------------------+--------------------+
| k8s/bml3outk8s_BD | 10.58.24.126/28 | 1/14  | common/Infra_VRF | k8s/bml3_k8s       | 
+-------------------+-----------------+-------+------------------+--------------------+
| k8s/MGMT_BD       | 10.58.25.174/28 | 1/14  | common/Infra_VRF | common/Infra_L3out | 
+-------------------+-----------------+-------+------------------+--------------------+
| k8s/vk8s_1_BD     | 10.58.24.174/28 | 2/14  | common/Infra_VRF | common/Infra_L3out | 
+-------------------+-----------------+-------+------------------+--------------------+
| k8s/vk8s_2_BD     | 10.58.24.190/28 | 1/14  | common/Infra_VRF | common/Infra_L3out | 
+-------------------+-----------------+-------+------------------+--------------------+
| k8s/vk8s_3_BD     | 10.58.24.206/28 | 2/14  | common/Infra_VRF | common/Infra_L3out | 
+-------------------+-----------------+-------+------------------+--------------------+
| k8s/vk8s_4_BD     | 10.58.24.222/28 | 2/14  | common/Infra_VRF | common/Infra_L3out | 
+-------------------+-----------------+-------+------------------+--------------------+
| k8s/vl3outk8s_BD  | 10.58.24.110/28 | 1/14  | common/Infra_VRF | k8s/vl3_k8s        | 
+-------------------+-----------------+-------+------------------+--------------------+
| k8s/VM2VM_BD      |                 |       | common/Infra_VRF | common/Infra_L3out | 
+-------------------+-----------------+-------+------------------+--------------------+
| vEPC_demo/MGMT_BD | 10.58.25.158/27 | 1/30  | common/Infra_VRF | common/Infra_L3out | 
+-------------------+-----------------+-------+------------------+--------------------+

Associated L3 Outs
------------------

+--------------------+------+-----+-----+------+-------+------------------+-------------+
| L3Out              | MPLS | PIM | BGP | OSPF | EIGRP | VRF              | L3 Domain   |
+--------------------+------+-----+-----+------+-------+------------------+-------------+
| common/Infra_L3out | X    | X   | V   | X    | X     | common/Infra_VRF | Infra_L3Dom | 
|                    |      |     |     |      |       |                  |             | 
+--------------------+------+-----+-----+------+-------+------------------+-------------+
```

Developer

```
# iserver get aci vrf --apic apic21 --name Infra_VRF --view verbose

{
    "duration": 4790,
    "apic": {
        "read": true,
        "success": 9,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 8,
        "connect_time": 458,
        "disconnect_time": 0,
        "mo_time": 3099,
        "total_time": 3557
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

True	458	-	connect apic21o.emea-sp.cisco.com:443
True	345	23	apic21o.emea-sp.cisco.com:443 class fvCtx
True	413	36	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	346	15	apic21o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree=children&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	361	18	apic21o.emea-sp.cisco.com:443 class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
True	413	93	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	499	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	366	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	356	152	apic21o.emea-sp.cisco.com:443 class fvLocale
```

[[Back]](./Vrf.md)