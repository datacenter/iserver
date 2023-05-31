# Virtual Routing and Forwarding (VRF)

## Filter by vrf's associated EPG name

```
# iserver get aci vrf --apic apic21 --epg *vk8s_1*

Apic: apic21

+-------------------------+----------------+---------------+------------------------------------+------------------------+-------------------+--------------------+
| VRF                     | PCE Preference | PCE Direction | Associated EPG                     | Associated BD          | BD Subnets        | Associated L3Out   |
+-------------------------+----------------+---------------+------------------------------------+------------------------+-------------------+--------------------+
| common/Infra_VRF        | unenforced     | ingress       | k8s/k8s_ANP/bmk8s_1                | common/Infra_BD        | 10.58.24.78/28    | common/Infra_L3out | 
|                         |                |               | k8s/k8s_ANP/bmk8s_2                | k8s/bmk8s_1_BD         | 10.58.24.94/28    |                    | 
|                         |                |               | k8s/k8s_ANP/bmk8s_prov             | k8s/bmk8s_2_BD         | 10.58.29.94/28    |                    | 
|                         |                |               | k8s/k8s_ANP/MGMT                   | k8s/bmk8s_prov_BD      | 10.58.24.126/28   |                    | 
|                         |                |               | k8s/k8s_ANP/vk8s_1                 | k8s/bml3outk8s_BD      | 10.58.25.174/28   |                    | 
|                         |                |               | k8s/k8s_ANP/vk8s_2                 | k8s/MGMT_BD            | 10.58.24.174/28   |                    | 
|                         |                |               | k8s/k8s_ANP/vk8s_3                 | k8s/vk8s_1_BD          | 10.58.24.190/28   |                    | 
|                         |                |               | k8s/k8s_ANP/vk8s_4                 | k8s/vk8s_2_BD          | 10.58.24.206/28   |                    | 
|                         |                |               | k8s/k8s_ANP/backbone1              | k8s/vk8s_3_BD          | 10.58.24.222/28   |                    | 
|                         |                |               | k8s/k8s_ANP/csr1_lan               | k8s/vk8s_4_BD          | 10.58.24.110/28   |                    | 
|                         |                |               | k8s/k8s_ANP/csr2_lan               | k8s/vl3outk8s_BD       | 10.58.25.158/27   |                    | 
|                         |                |               | k8s/k8s_ANP/csr_b2b                | k8s/VM2VM_BD           |                   |                    | 
|                         |                |               | k8s/k8s_ANP/site1_lan              | vEPC_demo/MGMT_BD      |                   |                    | 
|                         |                |               | k8s/k8s_ANP/site1_pe               |                        |                   |                    | 
|                         |                |               | k8s/k8s_ANP/site2_lan              |                        |                   |                    | 
|                         |                |               | k8s/k8s_ANP/site2_pe               |                        |                   |                    | 
|                         |                |               | vEPC_demo/vEPG_ANP/vEPG_MGMT       |                        |                   |                    | 
+-------------------------+----------------+---------------+------------------------------------+------------------------+-------------------+--------------------+
| mgmt/EU-SPDC-ERSPAN-VRF | enforced       | ingress       | common/privIP_TEST/privIP_TEST     | mgmt/EU-SPDC-ERSPAN_BD | 99.100.100.254/24 |                    | 
|                         |                |               | common/Test_ANP/Test_EPG           |                        |                   |                    | 
|                         |                |               | hefernan_ni-demo/APP/EPG1          |                        |                   |                    | 
|                         |                |               | hefernan_ni-demo/APP/EPG2          |                        |                   |                    | 
|                         |                |               | infra/access/default               |                        |                   |                    | 
|                         |                |               | infra/ave-ctrl/ave-ctrl            |                        |                   |                    | 
|                         |                |               | k8s/k8s_ANP/backbone1              |                        |                   |                    | 
|                         |                |               | k8s/k8s_ANP/bmk8s_1                |                        |                   |                    | 
|                         |                |               | k8s/k8s_ANP/bmk8s_2                |                        |                   |                    | 
|                         |                |               | k8s/k8s_ANP/bmk8s_prov             |                        |                   |                    | 
|                         |                |               | k8s/k8s_ANP/csr1_lan               |                        |                   |                    | 
|                         |                |               | k8s/k8s_ANP/csr2_lan               |                        |                   |                    | 
|                         |                |               | k8s/k8s_ANP/csr_b2b                |                        |                   |                    | 
|                         |                |               | k8s/k8s_ANP/MGMT                   |                        |                   |                    | 
|                         |                |               | k8s/k8s_ANP/site1_lan              |                        |                   |                    | 
|                         |                |               | k8s/k8s_ANP/site1_pe               |                        |                   |                    | 
|                         |                |               | k8s/k8s_ANP/site2_lan              |                        |                   |                    | 
|                         |                |               | k8s/k8s_ANP/site2_pe               |                        |                   |                    | 
|                         |                |               | k8s/k8s_ANP/SRIoV_A                |                        |                   |                    | 
|                         |                |               | k8s/k8s_ANP/SRIoV_B                |                        |                   |                    | 
|                         |                |               | k8s/k8s_ANP/Test                   |                        |                   |                    | 
|                         |                |               | k8s/k8s_ANP/vk8s_1                 |                        |                   |                    | 
|                         |                |               | k8s/k8s_ANP/vk8s_2                 |                        |                   |                    | 
|                         |                |               | k8s/k8s_ANP/vk8s_3                 |                        |                   |                    | 
|                         |                |               | k8s/k8s_ANP/vk8s_4                 |                        |                   |                    | 
|                         |                |               | mgmt/EU-SPDC_ANP/EU-SPDC-ERSPAN    |                        |                   |                    | 
|                         |                |               | mgmt/EU-SPDC_ANP/EU-SPDC-MGMT      |                        |                   |                    | 
|                         |                |               | nidemo/streamz/appserver           |                        |                   |                    | 
|                         |                |               | nidemo/streamz/database            |                        |                   |                    | 
|                         |                |               | nidemo/streamz/frontend            |                        |                   |                    | 
|                         |                |               | nidemo/streamz/management          |                        |                   |                    | 
|                         |                |               | SPN_IntraLab/SPN_Connect_ANP/TEST2 |                        |                   |                    | 
|                         |                |               | vEPC/vSFO_ANP/WWW                  |                        |                   |                    | 
|                         |                |               | vEPC_demo/vEPG_ANP/vEPG_ACC        |                        |                   |                    | 
|                         |                |               | vEPC_demo/vEPG_ANP/vEPG_CTRL       |                        |                   |                    | 
|                         |                |               | vEPC_demo/vEPG_ANP/vEPG_INT        |                        |                   |                    | 
|                         |                |               | vEPC_demo/vEPG_ANP/vEPG_MGMT       |                        |                   |                    | 
+-------------------------+----------------+---------------+------------------------------------+------------------------+-------------------+--------------------+
```

Developer

```
# iserver get aci vrf --apic apic21 --epg *vk8s_1*

{
    "duration": 4986,
    "apic": {
        "read": true,
        "success": 9,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 8,
        "connect_time": 408,
        "disconnect_time": 0,
        "mo_time": 2899,
        "total_time": 3307
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

True	408	-	connect apic21o.emea-sp.cisco.com
True	319	23	apic21o.emea-sp.cisco.com class fvCtx
True	428	36	apic21o.emea-sp.cisco.com class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	378	72	apic21o.emea-sp.cisco.com class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper
True	386	37	apic21o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	381	53	apic21o.emea-sp.cisco.com class fvAREpP query rsp-subtree=children&rsp-subtree-class=fvLocale
True	353	13	apic21o.emea-sp.cisco.com class fabricNode
True	316	14	apic21o.emea-sp.cisco.com class l3extOut query rsp-subtree=children&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	338	17	apic21o.emea-sp.cisco.com class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
```

[[Back]](./Vrf.md)