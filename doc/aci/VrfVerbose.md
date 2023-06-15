# Virtual Routing and Forwarding (VRF)

## Verbose output

Get selected vrf details
- VRF properties
- associated EPGs
- associated bridge domains

```
# iserver get aci vrf --apic apic21 --name Infra_VRF --view verbose

Apic: apic21 (mode:online, cache:off)

+------------------+----------------+---------------+------------------------------+-------------------+-----------------+--------------------+
| VRF              | PCE Preference | PCE Direction | Associated EPG               | Associated BD     | BD Subnets      | Associated L3Out   |
+------------------+----------------+---------------+------------------------------+-------------------+-----------------+--------------------+
| common/Infra_VRF | unenforced     | ingress       | k8s/k8s_ANP/bmk8s_1          | common/Infra_BD   | 10.58.24.78/28  | common/Infra_L3out | 
|                  |                |               | k8s/k8s_ANP/bmk8s_2          | k8s/bmk8s_1_BD    | 10.58.24.94/28  |                    | 
|                  |                |               | k8s/k8s_ANP/bmk8s_prov       | k8s/bmk8s_2_BD    | 10.58.29.94/28  |                    | 
|                  |                |               | k8s/k8s_ANP/MGMT             | k8s/bmk8s_prov_BD | 10.58.24.126/28 |                    | 
|                  |                |               | k8s/k8s_ANP/vk8s_1           | k8s/bml3outk8s_BD | 10.58.25.174/28 |                    | 
|                  |                |               | k8s/k8s_ANP/vk8s_2           | k8s/MGMT_BD       | 10.58.24.174/28 |                    | 
|                  |                |               | k8s/k8s_ANP/vk8s_3           | k8s/vk8s_1_BD     | 10.58.24.190/28 |                    | 
|                  |                |               | k8s/k8s_ANP/vk8s_4           | k8s/vk8s_2_BD     | 10.58.24.206/28 |                    | 
|                  |                |               | k8s/k8s_ANP/backbone1        | k8s/vk8s_3_BD     | 10.58.24.222/28 |                    | 
|                  |                |               | k8s/k8s_ANP/csr1_lan         | k8s/vk8s_4_BD     | 10.58.24.110/28 |                    | 
|                  |                |               | k8s/k8s_ANP/csr2_lan         | k8s/vl3outk8s_BD  | 10.58.25.158/27 |                    | 
|                  |                |               | k8s/k8s_ANP/csr_b2b          | k8s/VM2VM_BD      |                 |                    | 
|                  |                |               | k8s/k8s_ANP/site1_lan        | vEPC_demo/MGMT_BD |                 |                    | 
|                  |                |               | k8s/k8s_ANP/site1_pe         |                   |                 |                    | 
|                  |                |               | k8s/k8s_ANP/site2_lan        |                   |                 |                    | 
|                  |                |               | k8s/k8s_ANP/site2_pe         |                   |                 |                    | 
|                  |                |               | vEPC_demo/vEPG_ANP/vEPG_MGMT |                   |                 |                    | 
+------------------+----------------+---------------+------------------------------+-------------------+-----------------+--------------------+

VRF Properties
--------------
- Name                                  : Infra_VRF
- Tenant                                : common
- Data Plane Learning                   : enabled
- Multicast                             : permit
- Policy Control Enforcement Direction  : ingress
- Policy Control Enforcement Preference : unenforced
- Bridge Domain Enforcement Status      : no
- Endpoints Count                       : 52

Associated EPGs
---------------

+----+------------------------------+-------------------+-----------------+-----------+----------+
| Up | EPG                          | Bridge Domain     | BD Subnets      | Endpoints | Contract |
+----+------------------------------+-------------------+-----------------+-----------+----------+
| V  | k8s/k8s_ANP/bmk8s_1          | k8s/bmk8s_1_BD    | 10.58.24.78/28  | 0         | V        | 
+----+------------------------------+-------------------+-----------------+-----------+----------+
| V  | k8s/k8s_ANP/bmk8s_2          | k8s/bmk8s_2_BD    | 10.58.24.94/28  | 0         | V        | 
+----+------------------------------+-------------------+-----------------+-----------+----------+
| V  | k8s/k8s_ANP/bmk8s_prov       | k8s/bmk8s_prov_BD | 10.58.29.94/28  | 4         | V        | 
+----+------------------------------+-------------------+-----------------+-----------+----------+
| V  | k8s/k8s_ANP/MGMT             | k8s/MGMT_BD       | 10.58.25.174/28 | 0         | V        | 
+----+------------------------------+-------------------+-----------------+-----------+----------+
| V  | k8s/k8s_ANP/vk8s_1           | k8s/vk8s_1_BD     | 10.58.24.174/28 | 8         | V        | 
+----+------------------------------+-------------------+-----------------+-----------+----------+
| V  | k8s/k8s_ANP/vk8s_2           | k8s/vk8s_2_BD     | 10.58.24.190/28 | 8         | V        | 
+----+------------------------------+-------------------+-----------------+-----------+----------+
| V  | k8s/k8s_ANP/vk8s_3           | k8s/vk8s_3_BD     | 10.58.24.206/28 | 8         | V        | 
+----+------------------------------+-------------------+-----------------+-----------+----------+
| V  | k8s/k8s_ANP/vk8s_4           | k8s/vk8s_4_BD     | 10.58.24.222/28 | 8         | V        | 
+----+------------------------------+-------------------+-----------------+-----------+----------+
| V  | k8s/k8s_ANP/backbone1        | k8s/VM2VM_BD      |                 | 2         |          | 
+----+------------------------------+-------------------+-----------------+-----------+----------+
| V  | k8s/k8s_ANP/csr1_lan         | k8s/VM2VM_BD      |                 | 1         |          | 
+----+------------------------------+-------------------+-----------------+-----------+----------+
| V  | k8s/k8s_ANP/csr2_lan         | k8s/VM2VM_BD      |                 | 1         |          | 
+----+------------------------------+-------------------+-----------------+-----------+----------+
| V  | k8s/k8s_ANP/csr_b2b          | k8s/VM2VM_BD      |                 | 0         |          | 
+----+------------------------------+-------------------+-----------------+-----------+----------+
| V  | k8s/k8s_ANP/site1_lan        | k8s/VM2VM_BD      |                 | 1         |          | 
+----+------------------------------+-------------------+-----------------+-----------+----------+
| V  | k8s/k8s_ANP/site1_pe         | k8s/VM2VM_BD      |                 | 2         |          | 
+----+------------------------------+-------------------+-----------------+-----------+----------+
| V  | k8s/k8s_ANP/site2_lan        | k8s/VM2VM_BD      |                 | 1         |          | 
+----+------------------------------+-------------------+-----------------+-----------+----------+
| V  | k8s/k8s_ANP/site2_pe         | k8s/VM2VM_BD      |                 | 2         |          | 
+----+------------------------------+-------------------+-----------------+-----------+----------+
| V  | vEPC_demo/vEPG_ANP/vEPG_MGMT | vEPC_demo/MGMT_BD | 10.58.25.158/27 | 6         | V        | 
+----+------------------------------+-------------------+-----------------+-----------+----------+

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
| k8s/vk8s_1_BD     | 10.58.24.174/28 | 1/14  | common/Infra_VRF | common/Infra_L3out | 
+-------------------+-----------------+-------+------------------+--------------------+
| k8s/vk8s_2_BD     | 10.58.24.190/28 | 1/14  | common/Infra_VRF | common/Infra_L3out | 
+-------------------+-----------------+-------+------------------+--------------------+
| k8s/vk8s_3_BD     | 10.58.24.206/28 | 1/14  | common/Infra_VRF | common/Infra_L3out | 
+-------------------+-----------------+-------+------------------+--------------------+
| k8s/vk8s_4_BD     | 10.58.24.222/28 | 1/14  | common/Infra_VRF | common/Infra_L3out | 
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
    "duration": 4026,
    "apic": {
        "read": true,
        "success": 9,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 8,
        "connect_time": 401,
        "disconnect_time": 0,
        "mo_time": 2965,
        "total_time": 3366
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

True	401	-	connect apic21o.emea-sp.cisco.com:443
True	391	23	apic21o.emea-sp.cisco.com:443 class fvCtx
True	378	36	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	410	93	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	367	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	361	54	apic21o.emea-sp.cisco.com:443 class fvAREpP query rsp-subtree=children&rsp-subtree-class=fvLocale
True	325	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	396	15	apic21o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree=children&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	337	18	apic21o.emea-sp.cisco.com:443 class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
```

[[Back]](./Vrf.md)