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

Bridge Domain Summary
---------------------

+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| Bridge Domain             | Class ID | VNID     | Subnet             | Usage | EPG                   | VRF                      | L3Out                     |
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| common/default            | 49153    | 15728622 |                    |       |                       | common/                  |                           | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| common/Infra_BD           | 16386    | 15662984 |                    |       |                       | common/Infra_VRF         |                           | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| common/Infra_privIP_BD    | 16386    | 15302580 | 15.254.254.254/28  | 1/14  | common/privIP_TEST    | common/Infra_privIP_VRF  | common/Infra_privIP_L3out | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| common/Test_BD            | 49155    | 16514958 |                    |       | common/Test_EPG       | common/Infra_privIP_VRF  |                           | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| hefernan_ni-demo/BD1      | 16386    | 16646014 | 169.254.100.1/24   | 1/254 | hefernan_ni-demo/EPG1 | hefernan_ni-demo/ni-demo |                           | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| hefernan_ni-demo/BD2      | 16387    | 16089029 | 169.254.101.1/24   | 1/254 | hefernan_ni-demo/EPG2 | hefernan_ni-demo/ni-demo |                           | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| infra/ave-ctrl            | 49153    | 15957970 |                    |       | infra/ave-ctrl        | infra/ave-ctrl           |                           | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| infra/default             | 16386    | 16777209 | 10.5.0.30/27       | 1/30  | infra/default         | infra/overlay-1          |                           | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| k8s/bmk8s_1_BD            | 49160    | 14680069 | 10.58.24.78/28     | 1/14  | k8s/bmk8s_1           | common/Infra_VRF         | common/Infra_L3out        | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| k8s/bmk8s_2_BD            | 16401    | 14680068 | 10.58.24.94/28     | 1/14  | k8s/bmk8s_2           | common/Infra_VRF         | common/Infra_L3out        | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| k8s/bmk8s_prov_BD         | 49159    | 15106000 | 10.58.29.94/28     | 5/14  | k8s/bmk8s_prov        | common/Infra_VRF         | common/Infra_L3out        | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| k8s/bml3outk8s_BD         | 32770    | 14712830 | 10.58.24.126/28    | 1/14  |                       | common/Infra_VRF         | k8s/bml3_k8s              | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| k8s/MGMT_BD               | 32771    | 15466407 | 10.58.25.174/28    | 1/14  | k8s/MGMT              | common/Infra_VRF         | common/Infra_L3out        | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| k8s/SRIoV_A_BD            | 16386    | 15433637 | 15.20.16.254/24    | 2/254 | k8s/SRIoV_A           | k8s/k8s_SRIoV_VRF        |                           | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| k8s/SRIoV_B_BD            | 49153    | 15597460 | 15.20.17.254/24    | 2/254 | k8s/SRIoV_B           | k8s/k8s_SRIoV_VRF        |                           | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| k8s/Test                  | 49159    | 16744309 | 169.169.169.254/24 | 1/254 | k8s/Test              | common/Infra_privIP_VRF  | common/Infra_L3out        | 
|                           |          |          | 169.169.170.254/24 | 1/254 |                       |                          | common/Infra_privIP_L3out | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| k8s/vk8s_1_BD             | 16399    | 15007706 | 10.58.24.174/28    | 2/14  | k8s/vk8s_1            | common/Infra_VRF         | common/Infra_L3out        | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| k8s/vk8s_2_BD             | 32777    | 14745597 | 10.58.24.190/28    | 1/14  | k8s/vk8s_2            | common/Infra_VRF         | common/Infra_L3out        | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| k8s/vk8s_3_BD             | 16400    | 15335346 | 10.58.24.206/28    | 2/14  | k8s/vk8s_3            | common/Infra_VRF         | common/Infra_L3out        | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| k8s/vk8s_4_BD             | 32776    | 14843889 | 10.58.24.222/28    | 2/14  | k8s/vk8s_4            | common/Infra_VRF         | common/Infra_L3out        | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| k8s/vl3outk8s_BD          | 49161    | 14909416 | 10.58.24.110/28    | 1/14  |                       | common/Infra_VRF         | k8s/vl3_k8s               | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| k8s/VM2VM_BD              | 16405    | 15499167 |                    |       | k8s/backbone1         | common/Infra_VRF         | common/Infra_L3out        | 
|                           |          |          |                    |       | k8s/csr1_lan          |                          |                           | 
|                           |          |          |                    |       | k8s/csr2_lan          |                          |                           | 
|                           |          |          |                    |       | k8s/csr_b2b           |                          |                           | 
|                           |          |          |                    |       | k8s/site1_lan         |                          |                           | 
|                           |          |          |                    |       | k8s/site1_pe          |                          |                           | 
|                           |          |          |                    |       | k8s/site2_lan         |                          |                           | 
|                           |          |          |                    |       | k8s/site2_pe          |                          |                           | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| mgmt/EU-SPDC-BD1          | 49153    | 16514959 |                    |       | mgmt/EU-SPDC-MGMT     | mgmt/EU-SPDC-MGMT-VRF1   |                           | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| mgmt/EU-SPDC-ERSPAN_BD    | 16386    | 16416666 | 99.100.100.254/24  | 2/254 | mgmt/EU-SPDC-ERSPAN   | mgmt/EU-SPDC-ERSPAN-VRF  |                           | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| mgmt/inb                  | 16387    | 16187318 | 10.58.50.190/27    | 1/30  |                       | mgmt/inb                 | mgmt/INB_L3out            | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| nidemo/appserver          | 49154    | 15892444 | 10.0.2.1/24        | 1/254 | nidemo/appserver      | nidemo/streamz-vrf       |                           | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| nidemo/database           | 16387    | 16285613 | 10.0.3.1/24        | 1/254 | nidemo/database       | nidemo/streamz-vrf       |                           | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| nidemo/frontend           | 49153    | 16285610 | 10.0.1.1/24        | 1/254 | nidemo/frontend       | nidemo/streamz-vrf       |                           | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| nidemo/management         | 16388    | 16154555 | 10.0.4.1/24        | 1/254 | nidemo/management     | nidemo/streamz-vrf       |                           | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| SPN_IntraLab/SPN_BD1      | 16387    | 15335344 | 192.168.1.254/24   | 1/254 | SPN_IntraLab/TEST2    | SPN_IntraLab/SPN_VRF1    |                           | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| vEPC/Leaking_BD           | 49153    | 15826914 |                    |       |                       | vEPC/Leaking_VRF         |                           | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| vEPC/vSFO_BD              | 32770    | 16613251 | 15.16.132.254/24   | 1/254 | vEPC/WWW              | vEPC/VSFO                | vEPC/vSFO_L3out           | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| vEPC_demo/ACC_BD          | 49153    | 15794150 | 15.20.0.254/24     | 1/254 | vEPC_demo/vEPG_ACC    | vEPC_demo/ACC_VRF        | vEPC_demo/ACC_L3out       | 
|                           |          |          |                    |       |                       |                          | vEPC_demo/SX_L3out        | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| vEPC_demo/INT_BD          | 32770    | 15892442 | 15.20.3.254/24     | 1/254 | vEPC_demo/vEPG_INT    | vEPC_demo/INT_VRF        | vEPC_demo/INT_L3out       | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| vEPC_demo/MGMT_BD         | 16391    | 16449430 | 10.58.25.158/27    | 1/30  | vEPC_demo/vEPG_MGMT   | common/Infra_VRF         | common/Infra_L3out        | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
| vEPC_demo/vEPC-CTRL-SX_BD | 16387    | 15728623 |                    |       | vEPC_demo/vEPG_CTRL   | vEPC_demo/ACC_VRF        | vEPC_demo/SX_L3out        | 
+---------------------------+----------+----------+--------------------+-------+-----------------------+--------------------------+---------------------------+
```

Developer

```
# iserver get aci bd --apic apic21

{
    "duration": 2860,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 436,
        "disconnect_time": 0,
        "mo_time": 1451,
        "total_time": 1887
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

True	436	-	connect apic21o.emea-sp.cisco.com:443
True	398	36	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	374	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	292	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	387	93	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
```

[[Back]](./BridgeDomain.md)