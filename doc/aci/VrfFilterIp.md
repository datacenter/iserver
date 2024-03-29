# Virtual Routing and Forwarding (VRF)

## Filter by vrf's associated bridge domain IP address

VRFs associated with bridge domain with IP subnet that contains provided IP address will be shown.

```
# iserver get aci vrf --apic apic21 --address 10.58.24.209

Apic: apic21 (mode:online, cache:off)

VRF [#1]
--------

+--------+---------+------------------+----------+---------+----------------+---------------+------------------------------+-------------------+-----------------+--------------------+
| Health | Faults  | VRF              | Class ID | VNID    | PCE Preference | PCE Direction | Associated EPG               | Associated BD     | BD Subnets      | Associated L3Out   |
+--------+---------+------------------+----------+---------+----------------+---------------+------------------------------+-------------------+-----------------+--------------------+
| 100    | 0 0 0 0 | common/Infra_VRF | 49153    | 2818048 | unenforced     | ingress       | k8s/k8s_ANP/bmk8s_1          | common/Infra_BD   | 10.58.24.78/28  | common/Infra_L3out | 
|        |         |                  |          |         |                |               | k8s/k8s_ANP/bmk8s_2          | k8s/bmk8s_1_BD    | 10.58.24.94/28  |                    | 
|        |         |                  |          |         |                |               | k8s/k8s_ANP/bmk8s_prov       | k8s/bmk8s_2_BD    | 10.58.29.94/28  |                    | 
|        |         |                  |          |         |                |               | k8s/k8s_ANP/MGMT             | k8s/bmk8s_prov_BD | 10.58.24.126/28 |                    | 
|        |         |                  |          |         |                |               | k8s/k8s_ANP/vk8s_1           | k8s/bml3outk8s_BD | 10.58.25.174/28 |                    | 
|        |         |                  |          |         |                |               | k8s/k8s_ANP/vk8s_2           | k8s/MGMT_BD       | 10.58.24.174/28 |                    | 
|        |         |                  |          |         |                |               | k8s/k8s_ANP/vk8s_3           | k8s/vk8s_1_BD     | 10.58.24.190/28 |                    | 
|        |         |                  |          |         |                |               | k8s/k8s_ANP/vk8s_4           | k8s/vk8s_2_BD     | 10.58.24.206/28 |                    | 
|        |         |                  |          |         |                |               | k8s/k8s_ANP/backbone1        | k8s/vk8s_3_BD     | 10.58.24.222/28 |                    | 
|        |         |                  |          |         |                |               | k8s/k8s_ANP/csr1_lan         | k8s/vk8s_4_BD     | 10.58.24.110/28 |                    | 
|        |         |                  |          |         |                |               | k8s/k8s_ANP/csr2_lan         | k8s/vl3outk8s_BD  | 10.58.25.158/27 |                    | 
|        |         |                  |          |         |                |               | k8s/k8s_ANP/csr_b2b          | k8s/VM2VM_BD      |                 |                    | 
|        |         |                  |          |         |                |               | k8s/k8s_ANP/site1_lan        | vEPC_demo/MGMT_BD |                 |                    | 
|        |         |                  |          |         |                |               | k8s/k8s_ANP/site1_pe         |                   |                 |                    | 
|        |         |                  |          |         |                |               | k8s/k8s_ANP/site2_lan        |                   |                 |                    | 
|        |         |                  |          |         |                |               | k8s/k8s_ANP/site2_pe         |                   |                 |                    | 
|        |         |                  |          |         |                |               | vEPC_demo/vEPG_ANP/vEPG_MGMT |                   |                 |                    | 
+--------+---------+------------------+----------+---------+----------------+---------------+------------------------------+-------------------+-----------------+--------------------+
```

Developer

```
# iserver get aci vrf --apic apic21 --address 10.58.24.209

{
    "duration": 4836,
    "apic": {
        "read": true,
        "success": 9,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 8,
        "connect_time": 439,
        "disconnect_time": 0,
        "mo_time": 3206,
        "total_time": 3645
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

True	439	-	connect apic21o.emea-sp.cisco.com:443
True	442	23	apic21o.emea-sp.cisco.com:443 class fvCtx query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	458	35	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	383	15	apic21o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	352	18	apic21o.emea-sp.cisco.com:443 class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
True	457	86	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	439	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	338	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	337	154	apic21o.emea-sp.cisco.com:443 class fvLocale
```

[[Back]](./Vrf.md)