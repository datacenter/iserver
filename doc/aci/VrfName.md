# Virtual Routing and Forwarding (VRF)

## Filter by vrf's name

Example: name

```
# iserver get aci vrf --apic apic21 --name *infra*

Apic: apic21 (mode:online, cache:off)

+-------------------------+----------------+---------------+--------------------------------+------------------------+--------------------+---------------------------+
| VRF                     | PCE Preference | PCE Direction | Associated EPG                 | Associated BD          | BD Subnets         | Associated L3Out          |
+-------------------------+----------------+---------------+--------------------------------+------------------------+--------------------+---------------------------+
| common/Infra_privIP_VRF | enforced       | ingress       | common/privIP_TEST/privIP_TEST | common/Infra_privIP_BD | 15.254.254.254/28  | common/Infra_privIP_L3out | 
|                         |                |               | common/Test_ANP/Test_EPG       | common/Test_BD         | 169.169.169.254/24 |                           | 
|                         |                |               | k8s/k8s_ANP/Test               | k8s/Test               | 169.169.170.254/24 |                           | 
+-------------------------+----------------+---------------+--------------------------------+------------------------+--------------------+---------------------------+
| common/Infra_VRF        | unenforced     | ingress       | k8s/k8s_ANP/bmk8s_1            | common/Infra_BD        | 10.58.24.78/28     | common/Infra_L3out        | 
|                         |                |               | k8s/k8s_ANP/bmk8s_2            | k8s/bmk8s_1_BD         | 10.58.24.94/28     |                           | 
|                         |                |               | k8s/k8s_ANP/bmk8s_prov         | k8s/bmk8s_2_BD         | 10.58.29.94/28     |                           | 
|                         |                |               | k8s/k8s_ANP/MGMT               | k8s/bmk8s_prov_BD      | 10.58.24.126/28    |                           | 
|                         |                |               | k8s/k8s_ANP/vk8s_1             | k8s/bml3outk8s_BD      | 10.58.25.174/28    |                           | 
|                         |                |               | k8s/k8s_ANP/vk8s_2             | k8s/MGMT_BD            | 10.58.24.174/28    |                           | 
|                         |                |               | k8s/k8s_ANP/vk8s_3             | k8s/vk8s_1_BD          | 10.58.24.190/28    |                           | 
|                         |                |               | k8s/k8s_ANP/vk8s_4             | k8s/vk8s_2_BD          | 10.58.24.206/28    |                           | 
|                         |                |               | k8s/k8s_ANP/backbone1          | k8s/vk8s_3_BD          | 10.58.24.222/28    |                           | 
|                         |                |               | k8s/k8s_ANP/csr1_lan           | k8s/vk8s_4_BD          | 10.58.24.110/28    |                           | 
|                         |                |               | k8s/k8s_ANP/csr2_lan           | k8s/vl3outk8s_BD       | 10.58.25.158/27    |                           | 
|                         |                |               | k8s/k8s_ANP/csr_b2b            | k8s/VM2VM_BD           |                    |                           | 
|                         |                |               | k8s/k8s_ANP/site1_lan          | vEPC_demo/MGMT_BD      |                    |                           | 
|                         |                |               | k8s/k8s_ANP/site1_pe           |                        |                    |                           | 
|                         |                |               | k8s/k8s_ANP/site2_lan          |                        |                    |                           | 
|                         |                |               | k8s/k8s_ANP/site2_pe           |                        |                    |                           | 
|                         |                |               | vEPC_demo/vEPG_ANP/vEPG_MGMT   |                        |                    |                           | 
+-------------------------+----------------+---------------+--------------------------------+------------------------+--------------------+---------------------------+
```

Example: tenant and name

```
# iserver get aci vrf --apic apic21 --name k8s/*sriov*

Apic: apic21 (mode:online, cache:off)

+-------------------+----------------+---------------+---------------------+----------------+-----------------+------------------+
| VRF               | PCE Preference | PCE Direction | Associated EPG      | Associated BD  | BD Subnets      | Associated L3Out |
+-------------------+----------------+---------------+---------------------+----------------+-----------------+------------------+
| k8s/k8s_SRIoV_VRF | enforced       | ingress       | k8s/k8s_ANP/SRIoV_A | k8s/SRIoV_A_BD | 15.20.16.254/24 |                  | 
|                   |                |               | k8s/k8s_ANP/SRIoV_B | k8s/SRIoV_B_BD | 15.20.17.254/24 |                  | 
+-------------------+----------------+---------------+---------------------+----------------+-----------------+------------------+
```

Developer

```
# iserver get aci vrf --apic apic21 --name *infra*

{
    "duration": 3984,
    "apic": {
        "read": true,
        "success": 9,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 8,
        "connect_time": 405,
        "disconnect_time": 0,
        "mo_time": 2988,
        "total_time": 3393
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

True	405	-	connect apic21o.emea-sp.cisco.com:443
True	336	23	apic21o.emea-sp.cisco.com:443 class fvCtx
True	429	36	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	412	94	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	339	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	359	54	apic21o.emea-sp.cisco.com:443 class fvAREpP query rsp-subtree=children&rsp-subtree-class=fvLocale
True	364	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	410	15	apic21o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree=children&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	339	18	apic21o.emea-sp.cisco.com:443 class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
```

[[Back]](./Vrf.md)