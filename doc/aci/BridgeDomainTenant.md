# Bridge Domain

## Filter by bridge domain's tenant name

```
# iserver get aci bd --apic apic21 --tenant k8s

Apic: apic21 (mode:online, cache:off)

+-------------------+--------------------+-------+----------------+-------------------------+---------------------------+
| Bridge Domain     | Subnet             | Usage | EPG            | VRF                     | L3Out                     |
+-------------------+--------------------+-------+----------------+-------------------------+---------------------------+
| k8s/bmk8s_1_BD    | 10.58.24.78/28     | 1/14  | k8s/bmk8s_1    | common/Infra_VRF        | common/Infra_L3out        | 
+-------------------+--------------------+-------+----------------+-------------------------+---------------------------+
| k8s/bmk8s_2_BD    | 10.58.24.94/28     | 1/14  | k8s/bmk8s_2    | common/Infra_VRF        | common/Infra_L3out        | 
+-------------------+--------------------+-------+----------------+-------------------------+---------------------------+
| k8s/bmk8s_prov_BD | 10.58.29.94/28     | 5/14  | k8s/bmk8s_prov | common/Infra_VRF        | common/Infra_L3out        | 
+-------------------+--------------------+-------+----------------+-------------------------+---------------------------+
| k8s/bml3outk8s_BD | 10.58.24.126/28    | 1/14  |                | common/Infra_VRF        | k8s/bml3_k8s              | 
+-------------------+--------------------+-------+----------------+-------------------------+---------------------------+
| k8s/MGMT_BD       | 10.58.25.174/28    | 1/14  | k8s/MGMT       | common/Infra_VRF        | common/Infra_L3out        | 
+-------------------+--------------------+-------+----------------+-------------------------+---------------------------+
| k8s/SRIoV_A_BD    | 15.20.16.254/24    | 2/254 | k8s/SRIoV_A    | k8s/k8s_SRIoV_VRF       |                           | 
+-------------------+--------------------+-------+----------------+-------------------------+---------------------------+
| k8s/SRIoV_B_BD    | 15.20.17.254/24    | 2/254 | k8s/SRIoV_B    | k8s/k8s_SRIoV_VRF       |                           | 
+-------------------+--------------------+-------+----------------+-------------------------+---------------------------+
| k8s/Test          | 169.169.169.254/24 | 1/254 | k8s/Test       | common/Infra_privIP_VRF | common/Infra_L3out        | 
|                   | 169.169.170.254/24 | 1/254 |                |                         | common/Infra_privIP_L3out | 
+-------------------+--------------------+-------+----------------+-------------------------+---------------------------+
| k8s/vk8s_1_BD     | 10.58.24.174/28    | 1/14  | k8s/vk8s_1     | common/Infra_VRF        | common/Infra_L3out        | 
+-------------------+--------------------+-------+----------------+-------------------------+---------------------------+
| k8s/vk8s_2_BD     | 10.58.24.190/28    | 1/14  | k8s/vk8s_2     | common/Infra_VRF        | common/Infra_L3out        | 
+-------------------+--------------------+-------+----------------+-------------------------+---------------------------+
| k8s/vk8s_3_BD     | 10.58.24.206/28    | 1/14  | k8s/vk8s_3     | common/Infra_VRF        | common/Infra_L3out        | 
+-------------------+--------------------+-------+----------------+-------------------------+---------------------------+
| k8s/vk8s_4_BD     | 10.58.24.222/28    | 1/14  | k8s/vk8s_4     | common/Infra_VRF        | common/Infra_L3out        | 
+-------------------+--------------------+-------+----------------+-------------------------+---------------------------+
| k8s/vl3outk8s_BD  | 10.58.24.110/28    | 1/14  |                | common/Infra_VRF        | k8s/vl3_k8s               | 
+-------------------+--------------------+-------+----------------+-------------------------+---------------------------+
| k8s/VM2VM_BD      |                    |       | k8s/backbone1  | common/Infra_VRF        | common/Infra_L3out        | 
|                   |                    |       | k8s/csr1_lan   |                         |                           | 
|                   |                    |       | k8s/csr2_lan   |                         |                           | 
|                   |                    |       | k8s/csr_b2b    |                         |                           | 
|                   |                    |       | k8s/site1_lan  |                         |                           | 
|                   |                    |       | k8s/site1_pe   |                         |                           | 
|                   |                    |       | k8s/site2_lan  |                         |                           | 
|                   |                    |       | k8s/site2_pe   |                         |                           | 
+-------------------+--------------------+-------+----------------+-------------------------+---------------------------+
```

Developer

```
# iserver get aci bd --apic apic21 --tenant k8s

{
    "duration": 2284,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 433,
        "disconnect_time": 0,
        "mo_time": 1206,
        "total_time": 1639
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

True	433	-	connect apic21o.emea-sp.cisco.com
True	420	36	apic21o.emea-sp.cisco.com class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	379	37	apic21o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	407	93	apic21o.emea-sp.cisco.com class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
```

[[Back]](./BridgeDomain.md)