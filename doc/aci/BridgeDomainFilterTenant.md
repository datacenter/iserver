# Bridge Domain

## Filter by bridge domain's tenant name

```
# iserver get aci bd --apic apic21 --tenant k8s

Apic: apic21 (mode:online, cache:off)

Bridge Domain [#14]
-------------------

+--------+---------+-------------------+----------+----------+--------------------+-------+----------------+-------------------------+---------------------------+
| Health | Faults  | Bridge Domain     | Class ID | VNID     | Subnet             | Usage | EPG            | VRF                     | L3Out                     |
+--------+---------+-------------------+----------+----------+--------------------+-------+----------------+-------------------------+---------------------------+
| 100    | 0 0 0 0 | k8s/bmk8s_1_BD    | 49160    | 14680069 | 10.58.24.78/28     | 1/14  | k8s/bmk8s_1    | common/Infra_VRF        | common/Infra_L3out        | 
+--------+---------+-------------------+----------+----------+--------------------+-------+----------------+-------------------------+---------------------------+
| 100    | 0 0 0 0 | k8s/bmk8s_2_BD    | 16401    | 14680068 | 10.58.24.94/28     | 1/14  | k8s/bmk8s_2    | common/Infra_VRF        | common/Infra_L3out        | 
+--------+---------+-------------------+----------+----------+--------------------+-------+----------------+-------------------------+---------------------------+
| 100    | 0 0 0 0 | k8s/bmk8s_prov_BD | 49159    | 15106000 | 10.58.29.94/28     | 5/14  | k8s/bmk8s_prov | common/Infra_VRF        | common/Infra_L3out        | 
+--------+---------+-------------------+----------+----------+--------------------+-------+----------------+-------------------------+---------------------------+
| 100    | 0 0 0 0 | k8s/bml3outk8s_BD | 32770    | 14712830 | 10.58.24.126/28    | 1/14  |                | common/Infra_VRF        | k8s/bml3_k8s              | 
+--------+---------+-------------------+----------+----------+--------------------+-------+----------------+-------------------------+---------------------------+
| 100    | 0 0 0 0 | k8s/MGMT_BD       | 32771    | 15466407 | 10.58.25.174/28    | 1/14  | k8s/MGMT       | common/Infra_VRF        | common/Infra_L3out        | 
+--------+---------+-------------------+----------+----------+--------------------+-------+----------------+-------------------------+---------------------------+
| 100    | 0 0 0 0 | k8s/SRIoV_A_BD    | 16386    | 15433637 | 15.20.16.254/24    | 2/254 | k8s/SRIoV_A    | k8s/k8s_SRIoV_VRF       |                           | 
+--------+---------+-------------------+----------+----------+--------------------+-------+----------------+-------------------------+---------------------------+
| 100    | 0 0 0 0 | k8s/SRIoV_B_BD    | 49153    | 15597460 | 15.20.17.254/24    | 2/254 | k8s/SRIoV_B    | k8s/k8s_SRIoV_VRF       |                           | 
+--------+---------+-------------------+----------+----------+--------------------+-------+----------------+-------------------------+---------------------------+
| 100    | 0 0 0 0 | k8s/Test          | 49159    | 15695751 | 169.169.169.254/24 | 1/254 | k8s/Test       | common/Infra_privIP_VRF | common/Infra_L3out        | 
|        |         |                   |          |          | 169.169.170.254/24 | 1/254 |                |                         | common/Infra_privIP_L3out | 
+--------+---------+-------------------+----------+----------+--------------------+-------+----------------+-------------------------+---------------------------+
| 100    | 0 0 0 0 | k8s/vk8s_1_BD     | 16399    | 15007706 | 10.58.24.174/28    | 10/14 | k8s/vk8s_1     | common/Infra_VRF        | common/Infra_L3out        | 
+--------+---------+-------------------+----------+----------+--------------------+-------+----------------+-------------------------+---------------------------+
| 100    | 0 0 0 0 | k8s/vk8s_2_BD     | 32777    | 14745597 | 10.58.24.190/28    | 1/14  | k8s/vk8s_2     | common/Infra_VRF        | common/Infra_L3out        | 
+--------+---------+-------------------+----------+----------+--------------------+-------+----------------+-------------------------+---------------------------+
| 100    | 0 0 0 0 | k8s/vk8s_3_BD     | 16400    | 15335346 | 10.58.24.206/28    | 2/14  | k8s/vk8s_3     | common/Infra_VRF        | common/Infra_L3out        | 
+--------+---------+-------------------+----------+----------+--------------------+-------+----------------+-------------------------+---------------------------+
| 100    | 0 0 0 0 | k8s/vk8s_4_BD     | 32776    | 14843889 | 10.58.24.222/28    | 2/14  | k8s/vk8s_4     | common/Infra_VRF        | common/Infra_L3out        | 
+--------+---------+-------------------+----------+----------+--------------------+-------+----------------+-------------------------+---------------------------+
| 100    | 0 0 0 0 | k8s/vl3outk8s_BD  | 49161    | 14909416 | 10.58.24.110/28    | 1/14  |                | common/Infra_VRF        | k8s/vl3_k8s               | 
+--------+---------+-------------------+----------+----------+--------------------+-------+----------------+-------------------------+---------------------------+
| 100    | 0 0 0 0 | k8s/VM2VM_BD      | 16405    | 15499167 |                    |       | k8s/backbone1  | common/Infra_VRF        | common/Infra_L3out        | 
|        |         |                   |          |          |                    |       | k8s/csr1_lan   |                         |                           | 
|        |         |                   |          |          |                    |       | k8s/csr2_lan   |                         |                           | 
|        |         |                   |          |          |                    |       | k8s/csr_b2b    |                         |                           | 
|        |         |                   |          |          |                    |       | k8s/site1_lan  |                         |                           | 
|        |         |                   |          |          |                    |       | k8s/site1_pe   |                         |                           | 
|        |         |                   |          |          |                    |       | k8s/site2_lan  |                         |                           | 
|        |         |                   |          |          |                    |       | k8s/site2_pe   |                         |                           | 
+--------+---------+-------------------+----------+----------+--------------------+-------+----------------+-------------------------+---------------------------+
```

Developer

```
# iserver get aci bd --apic apic21 --tenant k8s

{
    "duration": 3244,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 459,
        "disconnect_time": 0,
        "mo_time": 1810,
        "total_time": 2269
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

True	459	-	connect apic21o.emea-sp.cisco.com:443
True	479	35	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	499	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	341	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	491	85	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
```

[[Back]](./BridgeDomain.md)