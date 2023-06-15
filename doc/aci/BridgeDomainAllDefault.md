# Bridge Domain

## Get all bridge domains

Get all bridge domains from selected APIC. Default output shows properties of bridge domains as well as related objects.
- bridge domain name and tenant
- subnets with usage based on endpoints
- endpoint groups (EPG) associated with bridge domain
- Resolved VRF (tenant/name)
- associated L3 Outs (tenant/name)

```
# iserver get aci bd --apic apic21

Apic: apic21 (mode:online, cache:off)

+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| Bridge Domain             | Subnet             | Usage | EPG                   | VRF                      | L3Out                     |
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| common/default            |                    |       |                       | common/                  |                           | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| common/Infra_BD           |                    |       |                       | common/Infra_VRF         |                           | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| common/Infra_privIP_BD    | 15.254.254.254/28  | 1/14  | common/privIP_TEST    | common/Infra_privIP_VRF  | common/Infra_privIP_L3out | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| common/Test_BD            |                    |       | common/Test_EPG       | common/Infra_privIP_VRF  |                           | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| hefernan_ni-demo/BD1      | 169.254.100.1/24   | 1/254 | hefernan_ni-demo/EPG1 | hefernan_ni-demo/ni-demo |                           | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| hefernan_ni-demo/BD2      | 169.254.101.1/24   | 1/254 | hefernan_ni-demo/EPG2 | hefernan_ni-demo/ni-demo |                           | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| infra/ave-ctrl            |                    |       | infra/ave-ctrl        | infra/ave-ctrl           |                           | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| infra/default             | 10.5.0.30/27       | 1/30  | common/privIP_TEST    | infra/overlay-1          |                           | 
|                           |                    |       | common/Test_EPG       |                          |                           | 
|                           |                    |       | hefernan_ni-demo/EPG1 |                          |                           | 
|                           |                    |       | hefernan_ni-demo/EPG2 |                          |                           | 
|                           |                    |       | infra/default         |                          |                           | 
|                           |                    |       | infra/ave-ctrl        |                          |                           | 
|                           |                    |       | k8s/backbone1         |                          |                           | 
|                           |                    |       | k8s/bmk8s_1           |                          |                           | 
|                           |                    |       | k8s/bmk8s_2           |                          |                           | 
|                           |                    |       | k8s/bmk8s_prov        |                          |                           | 
|                           |                    |       | k8s/csr1_lan          |                          |                           | 
|                           |                    |       | k8s/csr2_lan          |                          |                           | 
|                           |                    |       | k8s/csr_b2b           |                          |                           | 
|                           |                    |       | k8s/MGMT              |                          |                           | 
|                           |                    |       | k8s/site1_lan         |                          |                           | 
|                           |                    |       | k8s/site1_pe          |                          |                           | 
|                           |                    |       | k8s/site2_lan         |                          |                           | 
|                           |                    |       | k8s/site2_pe          |                          |                           | 
|                           |                    |       | k8s/SRIoV_A           |                          |                           | 
|                           |                    |       | k8s/SRIoV_B           |                          |                           | 
|                           |                    |       | k8s/Test              |                          |                           | 
|                           |                    |       | k8s/vk8s_1            |                          |                           | 
|                           |                    |       | k8s/vk8s_2            |                          |                           | 
|                           |                    |       | k8s/vk8s_3            |                          |                           | 
|                           |                    |       | k8s/vk8s_4            |                          |                           | 
|                           |                    |       | mgmt/EU-SPDC-ERSPAN   |                          |                           | 
|                           |                    |       | mgmt/EU-SPDC-MGMT     |                          |                           | 
|                           |                    |       | nidemo/appserver      |                          |                           | 
|                           |                    |       | nidemo/database       |                          |                           | 
|                           |                    |       | nidemo/frontend       |                          |                           | 
|                           |                    |       | nidemo/management     |                          |                           | 
|                           |                    |       | SPN_IntraLab/TEST2    |                          |                           | 
|                           |                    |       | vEPC/WWW              |                          |                           | 
|                           |                    |       | vEPC_demo/vEPG_ACC    |                          |                           | 
|                           |                    |       | vEPC_demo/vEPG_CTRL   |                          |                           | 
|                           |                    |       | vEPC_demo/vEPG_INT    |                          |                           | 
|                           |                    |       | vEPC_demo/vEPG_MGMT   |                          |                           | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| k8s/bmk8s_1_BD            | 10.58.24.78/28     | 1/14  | k8s/bmk8s_1           | common/Infra_VRF         | common/Infra_L3out        | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| k8s/bmk8s_2_BD            | 10.58.24.94/28     | 1/14  | k8s/bmk8s_2           | common/Infra_VRF         | common/Infra_L3out        | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| k8s/bmk8s_prov_BD         | 10.58.29.94/28     | 5/14  | k8s/bmk8s_prov        | common/Infra_VRF         | common/Infra_L3out        | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| k8s/bml3outk8s_BD         | 10.58.24.126/28    | 1/14  |                       | common/Infra_VRF         | k8s/bml3_k8s              | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| k8s/MGMT_BD               | 10.58.25.174/28    | 1/14  | k8s/MGMT              | common/Infra_VRF         | common/Infra_L3out        | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| k8s/SRIoV_A_BD            | 15.20.16.254/24    | 2/254 | k8s/SRIoV_A           | k8s/k8s_SRIoV_VRF        |                           | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| k8s/SRIoV_B_BD            | 15.20.17.254/24    | 2/254 | k8s/SRIoV_B           | k8s/k8s_SRIoV_VRF        |                           | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| k8s/Test                  | 169.169.169.254/24 | 1/254 | k8s/Test              | common/Infra_privIP_VRF  | common/Infra_L3out        | 
|                           | 169.169.170.254/24 | 1/254 |                       |                          | common/Infra_privIP_L3out | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| k8s/vk8s_1_BD             | 10.58.24.174/28    | 1/14  | k8s/vk8s_1            | common/Infra_VRF         | common/Infra_L3out        | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| k8s/vk8s_2_BD             | 10.58.24.190/28    | 1/14  | k8s/vk8s_2            | common/Infra_VRF         | common/Infra_L3out        | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| k8s/vk8s_3_BD             | 10.58.24.206/28    | 1/14  | k8s/vk8s_3            | common/Infra_VRF         | common/Infra_L3out        | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| k8s/vk8s_4_BD             | 10.58.24.222/28    | 1/14  | k8s/vk8s_4            | common/Infra_VRF         | common/Infra_L3out        | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| k8s/vl3outk8s_BD          | 10.58.24.110/28    | 1/14  |                       | common/Infra_VRF         | k8s/vl3_k8s               | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| k8s/VM2VM_BD              |                    |       | k8s/backbone1         | common/Infra_VRF         | common/Infra_L3out        | 
|                           |                    |       | k8s/csr1_lan          |                          |                           | 
|                           |                    |       | k8s/csr2_lan          |                          |                           | 
|                           |                    |       | k8s/csr_b2b           |                          |                           | 
|                           |                    |       | k8s/site1_lan         |                          |                           | 
|                           |                    |       | k8s/site1_pe          |                          |                           | 
|                           |                    |       | k8s/site2_lan         |                          |                           | 
|                           |                    |       | k8s/site2_pe          |                          |                           | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| mgmt/EU-SPDC-BD1          |                    |       | mgmt/EU-SPDC-MGMT     | mgmt/EU-SPDC-MGMT-VRF1   |                           | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| mgmt/EU-SPDC-ERSPAN_BD    | 99.100.100.254/24  | 1/254 | mgmt/EU-SPDC-ERSPAN   | mgmt/EU-SPDC-ERSPAN-VRF  |                           | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| mgmt/inb                  | 10.58.50.190/27    | 1/30  |                       | mgmt/inb                 | mgmt/INB_L3out            | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| nidemo/appserver          | 10.0.2.1/24        | 1/254 | nidemo/appserver      | nidemo/streamz-vrf       |                           | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| nidemo/database           | 10.0.3.1/24        | 1/254 | nidemo/database       | nidemo/streamz-vrf       |                           | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| nidemo/frontend           | 10.0.1.1/24        | 1/254 | nidemo/frontend       | nidemo/streamz-vrf       |                           | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| nidemo/management         | 10.0.4.1/24        | 1/254 | nidemo/management     | nidemo/streamz-vrf       |                           | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| SPN_IntraLab/SPN_BD1      | 192.168.1.254/24   | 1/254 | SPN_IntraLab/TEST2    | SPN_IntraLab/SPN_VRF1    |                           | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| vEPC/Leaking_BD           |                    |       |                       | vEPC/Leaking_VRF         |                           | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| vEPC/vSFO_BD              | 15.16.132.254/24   | 1/254 | vEPC/WWW              | vEPC/VSFO                | vEPC/vSFO_L3out           | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| vEPC_demo/ACC_BD          | 15.20.0.254/24     | 1/254 | vEPC_demo/vEPG_ACC    | vEPC_demo/ACC_VRF        | vEPC_demo/ACC_L3out       | 
|                           |                    |       |                       |                          | vEPC_demo/SX_L3out        | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| vEPC_demo/INT_BD          | 15.20.3.254/24     | 1/254 | vEPC_demo/vEPG_INT    | vEPC_demo/INT_VRF        | vEPC_demo/INT_L3out       | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| vEPC_demo/MGMT_BD         | 10.58.25.158/27    | 1/30  | vEPC_demo/vEPG_MGMT   | common/Infra_VRF         | common/Infra_L3out        | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| vEPC_demo/vEPC-CTRL-SX_BD |                    |       | vEPC_demo/vEPG_CTRL   | vEPC_demo/ACC_VRF        | vEPC_demo/SX_L3out        | 
+---------------------------+--------------------+-------+-----------------------+--------------------------+---------------------------+
```

Developer

```
# iserver get aci bd --apic apic21

{
    "duration": 2904,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 443,
        "disconnect_time": 0,
        "mo_time": 1213,
        "total_time": 1656
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

True	443	-	connect apic21o.emea-sp.cisco.com
True	411	36	apic21o.emea-sp.cisco.com class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	367	37	apic21o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	435	93	apic21o.emea-sp.cisco.com class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
```

[[Back]](./BridgeDomain.md)