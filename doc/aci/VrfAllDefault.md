# Virtual Routing and Forwarding (VRF)

## Get all vrfs

Get all vrfs from selected APIC. Default output shows main properties of vrfs as well as associated objects.
- vrf name and tenant
- policy control enforcement preference and direction
- associated EPGs
- associated bridge domains and IP subnets
- associated L3 Outs

```
# iserver get aci vrf --apic apic21

Apic: apic21

+--------------------------+----------------+---------------+------------------------------------+---------------------------+--------------------+---------------------------+
| VRF                      | PCE Preference | PCE Direction | Associated EPG                     | Associated BD             | BD Subnets         | Associated L3Out          |
+--------------------------+----------------+---------------+------------------------------------+---------------------------+--------------------+---------------------------+
| common/copy              | enforced       | ingress       |                                    |                           |                    |                           | 
+--------------------------+----------------+---------------+------------------------------------+---------------------------+--------------------+---------------------------+
| common/default           | enforced       | ingress       |                                    |                           |                    | common/default            | 
+--------------------------+----------------+---------------+------------------------------------+---------------------------+--------------------+---------------------------+
| common/Infra_privIP_VRF  | enforced       | ingress       | common/privIP_TEST/privIP_TEST     | common/Infra_privIP_BD    | 15.254.254.254/28  | common/Infra_privIP_L3out | 
|                          |                |               | common/Test_ANP/Test_EPG           | common/Test_BD            | 169.169.170.254/24 |                           | 
|                          |                |               | k8s/k8s_ANP/Test                   | k8s/Test                  | 169.169.169.254/24 |                           | 
+--------------------------+----------------+---------------+------------------------------------+---------------------------+--------------------+---------------------------+
| common/Infra_VRF         | unenforced     | ingress       | k8s/k8s_ANP/bmk8s_1                | common/Infra_BD           | 10.58.24.78/28     | common/Infra_L3out        | 
|                          |                |               | k8s/k8s_ANP/bmk8s_2                | k8s/bmk8s_1_BD            | 10.58.24.94/28     |                           | 
|                          |                |               | k8s/k8s_ANP/bmk8s_prov             | k8s/bmk8s_2_BD            | 10.58.29.94/28     |                           | 
|                          |                |               | k8s/k8s_ANP/MGMT                   | k8s/bmk8s_prov_BD         | 10.58.24.126/28    |                           | 
|                          |                |               | k8s/k8s_ANP/vk8s_1                 | k8s/bml3outk8s_BD         | 10.58.25.174/28    |                           | 
|                          |                |               | k8s/k8s_ANP/vk8s_2                 | k8s/MGMT_BD               | 10.58.24.174/28    |                           | 
|                          |                |               | k8s/k8s_ANP/vk8s_3                 | k8s/vk8s_1_BD             | 10.58.24.190/28    |                           | 
|                          |                |               | k8s/k8s_ANP/vk8s_4                 | k8s/vk8s_2_BD             | 10.58.24.206/28    |                           | 
|                          |                |               | k8s/k8s_ANP/backbone1              | k8s/vk8s_3_BD             | 10.58.24.222/28    |                           | 
|                          |                |               | k8s/k8s_ANP/csr1_lan               | k8s/vk8s_4_BD             | 10.58.24.110/28    |                           | 
|                          |                |               | k8s/k8s_ANP/csr2_lan               | k8s/vl3outk8s_BD          | 10.58.25.158/27    |                           | 
|                          |                |               | k8s/k8s_ANP/csr_b2b                | k8s/VM2VM_BD              |                    |                           | 
|                          |                |               | k8s/k8s_ANP/site1_lan              | vEPC_demo/MGMT_BD         |                    |                           | 
|                          |                |               | k8s/k8s_ANP/site1_pe               |                           |                    |                           | 
|                          |                |               | k8s/k8s_ANP/site2_lan              |                           |                    |                           | 
|                          |                |               | k8s/k8s_ANP/site2_pe               |                           |                    |                           | 
|                          |                |               | vEPC_demo/vEPG_ANP/vEPG_MGMT       |                           |                    |                           | 
+--------------------------+----------------+---------------+------------------------------------+---------------------------+--------------------+---------------------------+
| common/Test_VRF1         | enforced       | ingress       |                                    |                           |                    |                           | 
+--------------------------+----------------+---------------+------------------------------------+---------------------------+--------------------+---------------------------+
| Ericsson_PACO/PDN        | enforced       | ingress       |                                    |                           |                    | Ericsson_PACO/PDN         | 
+--------------------------+----------------+---------------+------------------------------------+---------------------------+--------------------+---------------------------+
| Ericsson_PACO/RAN        | enforced       | ingress       |                                    |                           |                    | Ericsson_PACO/RAN         | 
+--------------------------+----------------+---------------+------------------------------------+---------------------------+--------------------+---------------------------+
| hefernan_ni-demo/ni-demo | enforced       | ingress       | hefernan_ni-demo/APP/EPG1          | hefernan_ni-demo/BD1      | 169.254.100.1/24   |                           | 
|                          |                |               | hefernan_ni-demo/APP/EPG2          | hefernan_ni-demo/BD2      | 169.254.101.1/24   |                           | 
+--------------------------+----------------+---------------+------------------------------------+---------------------------+--------------------+---------------------------+
| infra/ave-ctrl           | enforced       | ingress       | infra/ave-ctrl/ave-ctrl            | infra/ave-ctrl            |                    |                           | 
+--------------------------+----------------+---------------+------------------------------------+---------------------------+--------------------+---------------------------+
| infra/overlay-1          | enforced       | ingress       | infra/access/default               | infra/default             | 10.5.0.30/27       | infra/intersite           | 
|                          |                |               |                                    |                           |                    | infra/RL-L3Out            | 
+--------------------------+----------------+---------------+------------------------------------+---------------------------+--------------------+---------------------------+
| k8s/k8s_SRIoV_VRF        | enforced       | ingress       | k8s/k8s_ANP/SRIoV_A                | k8s/SRIoV_A_BD            | 15.20.16.254/24    |                           | 
|                          |                |               | k8s/k8s_ANP/SRIoV_B                | k8s/SRIoV_B_BD            | 15.20.17.254/24    |                           | 
+--------------------------+----------------+---------------+------------------------------------+---------------------------+--------------------+---------------------------+
| k8s/k8s_VRF              | enforced       | ingress       |                                    |                           |                    | k8s/bml3_k8s              | 
|                          |                |               |                                    |                           |                    | k8s/vl3_k8s               | 
+--------------------------+----------------+---------------+------------------------------------+---------------------------+--------------------+---------------------------+
| mgmt/EU-SPDC-ERSPAN-VRF  | enforced       | ingress       | common/privIP_TEST/privIP_TEST     | mgmt/EU-SPDC-ERSPAN_BD    | 99.100.100.254/24  |                           | 
|                          |                |               | common/Test_ANP/Test_EPG           |                           |                    |                           | 
|                          |                |               | hefernan_ni-demo/APP/EPG1          |                           |                    |                           | 
|                          |                |               | hefernan_ni-demo/APP/EPG2          |                           |                    |                           | 
|                          |                |               | infra/access/default               |                           |                    |                           | 
|                          |                |               | infra/ave-ctrl/ave-ctrl            |                           |                    |                           | 
|                          |                |               | k8s/k8s_ANP/backbone1              |                           |                    |                           | 
|                          |                |               | k8s/k8s_ANP/bmk8s_1                |                           |                    |                           | 
|                          |                |               | k8s/k8s_ANP/bmk8s_2                |                           |                    |                           | 
|                          |                |               | k8s/k8s_ANP/bmk8s_prov             |                           |                    |                           | 
|                          |                |               | k8s/k8s_ANP/csr1_lan               |                           |                    |                           | 
|                          |                |               | k8s/k8s_ANP/csr2_lan               |                           |                    |                           | 
|                          |                |               | k8s/k8s_ANP/csr_b2b                |                           |                    |                           | 
|                          |                |               | k8s/k8s_ANP/MGMT                   |                           |                    |                           | 
|                          |                |               | k8s/k8s_ANP/site1_lan              |                           |                    |                           | 
|                          |                |               | k8s/k8s_ANP/site1_pe               |                           |                    |                           | 
|                          |                |               | k8s/k8s_ANP/site2_lan              |                           |                    |                           | 
|                          |                |               | k8s/k8s_ANP/site2_pe               |                           |                    |                           | 
|                          |                |               | k8s/k8s_ANP/SRIoV_A                |                           |                    |                           | 
|                          |                |               | k8s/k8s_ANP/SRIoV_B                |                           |                    |                           | 
|                          |                |               | k8s/k8s_ANP/Test                   |                           |                    |                           | 
|                          |                |               | k8s/k8s_ANP/vk8s_1                 |                           |                    |                           | 
|                          |                |               | k8s/k8s_ANP/vk8s_2                 |                           |                    |                           | 
|                          |                |               | k8s/k8s_ANP/vk8s_3                 |                           |                    |                           | 
|                          |                |               | k8s/k8s_ANP/vk8s_4                 |                           |                    |                           | 
|                          |                |               | mgmt/EU-SPDC_ANP/EU-SPDC-ERSPAN    |                           |                    |                           | 
|                          |                |               | mgmt/EU-SPDC_ANP/EU-SPDC-MGMT      |                           |                    |                           | 
|                          |                |               | nidemo/streamz/appserver           |                           |                    |                           | 
|                          |                |               | nidemo/streamz/database            |                           |                    |                           | 
|                          |                |               | nidemo/streamz/frontend            |                           |                    |                           | 
|                          |                |               | nidemo/streamz/management          |                           |                    |                           | 
|                          |                |               | SPN_IntraLab/SPN_Connect_ANP/TEST2 |                           |                    |                           | 
|                          |                |               | vEPC/vSFO_ANP/WWW                  |                           |                    |                           | 
|                          |                |               | vEPC_demo/vEPG_ANP/vEPG_ACC        |                           |                    |                           | 
|                          |                |               | vEPC_demo/vEPG_ANP/vEPG_CTRL       |                           |                    |                           | 
|                          |                |               | vEPC_demo/vEPG_ANP/vEPG_INT        |                           |                    |                           | 
|                          |                |               | vEPC_demo/vEPG_ANP/vEPG_MGMT       |                           |                    |                           | 
+--------------------------+----------------+---------------+------------------------------------+---------------------------+--------------------+---------------------------+
| mgmt/EU-SPDC-MGMT-VRF1   | enforced       | ingress       | mgmt/EU-SPDC_ANP/EU-SPDC-MGMT      | mgmt/EU-SPDC-BD1          |                    |                           | 
+--------------------------+----------------+---------------+------------------------------------+---------------------------+--------------------+---------------------------+
| mgmt/inb                 | enforced       | ingress       |                                    | mgmt/inb                  | 10.58.50.190/27    | mgmt/INB_L3out            | 
+--------------------------+----------------+---------------+------------------------------------+---------------------------+--------------------+---------------------------+
| mgmt/oob                 | enforced       | ingress       |                                    |                           |                    |                           | 
+--------------------------+----------------+---------------+------------------------------------+---------------------------+--------------------+---------------------------+
| nidemo/streamz-vrf       | enforced       | ingress       | nidemo/streamz/appserver           | nidemo/appserver          | 10.0.2.1/24        |                           | 
|                          |                |               | nidemo/streamz/database            | nidemo/database           | 10.0.3.1/24        |                           | 
|                          |                |               | nidemo/streamz/frontend            | nidemo/frontend           | 10.0.1.1/24        |                           | 
|                          |                |               | nidemo/streamz/management          | nidemo/management         | 10.0.4.1/24        |                           | 
+--------------------------+----------------+---------------+------------------------------------+---------------------------+--------------------+---------------------------+
| SPN_IntraLab/SPN_VRF1    | enforced       | ingress       | SPN_IntraLab/SPN_Connect_ANP/TEST2 | SPN_IntraLab/SPN_BD1      | 192.168.1.254/24   |                           | 
+--------------------------+----------------+---------------+------------------------------------+---------------------------+--------------------+---------------------------+
| vEPC/Leaking_VRF         | enforced       | ingress       |                                    | vEPC/Leaking_BD           |                    |                           | 
+--------------------------+----------------+---------------+------------------------------------+---------------------------+--------------------+---------------------------+
| vEPC/VSFO                | enforced       | ingress       | vEPC/vSFO_ANP/WWW                  | vEPC/vSFO_BD              | 15.16.132.254/24   | vEPC/vSFO_L3out           | 
+--------------------------+----------------+---------------+------------------------------------+---------------------------+--------------------+---------------------------+
| vEPC_demo/ACC_VRF        | unenforced     | ingress       | vEPC_demo/vEPG_ANP/vEPG_ACC        | vEPC_demo/ACC_BD          | 15.20.0.254/24     | vEPC_demo/ACC_L3out       | 
|                          |                |               | vEPC_demo/vEPG_ANP/vEPG_CTRL       | vEPC_demo/vEPC-CTRL-SX_BD |                    | vEPC_demo/SX_L3out        | 
+--------------------------+----------------+---------------+------------------------------------+---------------------------+--------------------+---------------------------+
| vEPC_demo/INT_VRF        | enforced       | ingress       | vEPC_demo/vEPG_ANP/vEPG_INT        | vEPC_demo/INT_BD          | 15.20.3.254/24     | vEPC_demo/INT_L3out       | 
+--------------------------+----------------+---------------+------------------------------------+---------------------------+--------------------+---------------------------+
| vEPC_demo/MGMT_VRF       | enforced       | ingress       |                                    |                           |                    |                           | 
+--------------------------+----------------+---------------+------------------------------------+---------------------------+--------------------+---------------------------+
```

Developer

```
# iserver get aci vrf --apic apic21

{
    "duration": 4996,
    "apic": {
        "read": true,
        "success": 9,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 8,
        "connect_time": 405,
        "disconnect_time": 0,
        "mo_time": 3209,
        "total_time": 3614
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

True	405	-	connect apic21o.emea-sp.cisco.com
True	355	23	apic21o.emea-sp.cisco.com class fvCtx
True	505	36	apic21o.emea-sp.cisco.com class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	382	73	apic21o.emea-sp.cisco.com class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper
True	458	37	apic21o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	431	53	apic21o.emea-sp.cisco.com class fvAREpP query rsp-subtree=children&rsp-subtree-class=fvLocale
True	335	13	apic21o.emea-sp.cisco.com class fabricNode
True	383	14	apic21o.emea-sp.cisco.com class l3extOut query rsp-subtree=children&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	360	17	apic21o.emea-sp.cisco.com class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
```

[[Back]](./Vrf.md)