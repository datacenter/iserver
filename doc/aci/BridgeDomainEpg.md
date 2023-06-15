# Bridge Domain

## Filter by bridge domain's associated EPG name

```
# iserver get aci bd --apic apic21 --epg *vEPG_MGMT*

Apic: apic21 (mode:online, cache:off)

+-------------------+-----------------+-------+-----------------------+------------------+--------------------+
| Bridge Domain     | Subnet          | Usage | EPG                   | VRF              | L3Out              |
+-------------------+-----------------+-------+-----------------------+------------------+--------------------+
| infra/default     | 10.5.0.30/27    | 1/30  | common/privIP_TEST    | infra/overlay-1  |                    | 
|                   |                 |       | common/Test_EPG       |                  |                    | 
|                   |                 |       | hefernan_ni-demo/EPG1 |                  |                    | 
|                   |                 |       | hefernan_ni-demo/EPG2 |                  |                    | 
|                   |                 |       | infra/default         |                  |                    | 
|                   |                 |       | infra/ave-ctrl        |                  |                    | 
|                   |                 |       | k8s/backbone1         |                  |                    | 
|                   |                 |       | k8s/bmk8s_1           |                  |                    | 
|                   |                 |       | k8s/bmk8s_2           |                  |                    | 
|                   |                 |       | k8s/bmk8s_prov        |                  |                    | 
|                   |                 |       | k8s/csr1_lan          |                  |                    | 
|                   |                 |       | k8s/csr2_lan          |                  |                    | 
|                   |                 |       | k8s/csr_b2b           |                  |                    | 
|                   |                 |       | k8s/MGMT              |                  |                    | 
|                   |                 |       | k8s/site1_lan         |                  |                    | 
|                   |                 |       | k8s/site1_pe          |                  |                    | 
|                   |                 |       | k8s/site2_lan         |                  |                    | 
|                   |                 |       | k8s/site2_pe          |                  |                    | 
|                   |                 |       | k8s/SRIoV_A           |                  |                    | 
|                   |                 |       | k8s/SRIoV_B           |                  |                    | 
|                   |                 |       | k8s/Test              |                  |                    | 
|                   |                 |       | k8s/vk8s_1            |                  |                    | 
|                   |                 |       | k8s/vk8s_2            |                  |                    | 
|                   |                 |       | k8s/vk8s_3            |                  |                    | 
|                   |                 |       | k8s/vk8s_4            |                  |                    | 
|                   |                 |       | mgmt/EU-SPDC-ERSPAN   |                  |                    | 
|                   |                 |       | mgmt/EU-SPDC-MGMT     |                  |                    | 
|                   |                 |       | nidemo/appserver      |                  |                    | 
|                   |                 |       | nidemo/database       |                  |                    | 
|                   |                 |       | nidemo/frontend       |                  |                    | 
|                   |                 |       | nidemo/management     |                  |                    | 
|                   |                 |       | SPN_IntraLab/TEST2    |                  |                    | 
|                   |                 |       | vEPC/WWW              |                  |                    | 
|                   |                 |       | vEPC_demo/vEPG_ACC    |                  |                    | 
|                   |                 |       | vEPC_demo/vEPG_CTRL   |                  |                    | 
|                   |                 |       | vEPC_demo/vEPG_INT    |                  |                    | 
|                   |                 |       | vEPC_demo/vEPG_MGMT   |                  |                    | 
+-------------------+-----------------+-------+-----------------------+------------------+--------------------+
| vEPC_demo/MGMT_BD | 10.58.25.158/27 | 1/30  | vEPC_demo/vEPG_MGMT   | common/Infra_VRF | common/Infra_L3out | 
+-------------------+-----------------+-------+-----------------------+------------------+--------------------+
```

Developer

```
# iserver get aci bd --apic apic21 --epg *vEPG_MGMT*

{
    "duration": 2976,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 477,
        "disconnect_time": 0,
        "mo_time": 1266,
        "total_time": 1743
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

True	477	-	connect apic21o.emea-sp.cisco.com
True	461	36	apic21o.emea-sp.cisco.com class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	379	37	apic21o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	426	93	apic21o.emea-sp.cisco.com class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
```

[[Back]](./BridgeDomain.md)