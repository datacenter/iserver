# Virtual Routing and Forwarding (VRF)

## Filter by vrf's associated bridge domain IP address

VRFs associated with bridge domain with IP subnet that contains provided IP address will be shown.

```
# iserver get aci vrf --apic apic21 --ip 10.58.24.209

Apic: apic21 (mode:online, cache:off)

+--------------------------+----------------+---------------+----------+----------+---------------------------+---------------------------+--------------------+---------------------------+
| VRF                      | PCE Preference | PCE Direction | Class ID | VNID     | Associated EPG            | Associated BD             | BD Subnets         | Associated L3Out          |
+--------------------------+----------------+---------------+----------+----------+---------------------------+---------------------------+--------------------+---------------------------+
| common/copy              | enforced       | ingress       | 49153    | 2555904  |                           |                           |                    |                           | 
+--------------------------+----------------+---------------+----------+----------+---------------------------+---------------------------+--------------------+---------------------------+
| common/default           | enforced       | ingress       | 16386    | 3014656  |                           |                           |                    | common/default            | 
+--------------------------+----------------+---------------+----------+----------+---------------------------+---------------------------+--------------------+---------------------------+
| common/Infra_privIP_VRF  | enforced       | ingress       | 49153    | 2326529  | k8s/k8s_ANP/Test          | common/Infra_privIP_BD    | 15.254.254.254/28  | common/Infra_privIP_L3out | 
|                          |                |               |          |          |                           | common/Test_BD            | 169.169.169.254/24 |                           | 
|                          |                |               |          |          |                           | k8s/Test                  | 169.169.170.254/24 |                           | 
+--------------------------+----------------+---------------+----------+----------+---------------------------+---------------------------+--------------------+---------------------------+
| common/Infra_VRF         | unenforced     | ingress       | 49153    | 2818048  |                           | common/Infra_BD           | 10.58.24.78/28     | common/Infra_L3out        | 
|                          |                |               |          |          |                           | k8s/bmk8s_1_BD            | 10.58.24.94/28     |                           | 
|                          |                |               |          |          |                           | k8s/bmk8s_2_BD            | 10.58.29.94/28     |                           | 
|                          |                |               |          |          |                           | k8s/bmk8s_prov_BD         | 10.58.24.126/28    |                           | 
|                          |                |               |          |          |                           | k8s/bml3outk8s_BD         | 10.58.25.174/28    |                           | 
|                          |                |               |          |          |                           | k8s/MGMT_BD               | 10.58.24.174/28    |                           | 
|                          |                |               |          |          |                           | k8s/vk8s_1_BD             | 10.58.24.190/28    |                           | 
|                          |                |               |          |          |                           | k8s/vk8s_2_BD             | 10.58.24.206/28    |                           | 
|                          |                |               |          |          |                           | k8s/vk8s_3_BD             | 10.58.24.222/28    |                           | 
|                          |                |               |          |          |                           | k8s/vk8s_4_BD             | 10.58.24.110/28    |                           | 
|                          |                |               |          |          |                           | k8s/vl3outk8s_BD          | 10.58.25.158/27    |                           | 
|                          |                |               |          |          |                           | k8s/VM2VM_BD              |                    |                           | 
|                          |                |               |          |          |                           | vEPC_demo/MGMT_BD         |                    |                           | 
+--------------------------+----------------+---------------+----------+----------+---------------------------+---------------------------+--------------------+---------------------------+
| common/Test_VRF1         | enforced       | ingress       | 32770    | 2490368  |                           |                           |                    |                           | 
+--------------------------+----------------+---------------+----------+----------+---------------------------+---------------------------+--------------------+---------------------------+
| Ericsson_PACO/PDN        | enforced       | ingress       | 49153    | 3112962  |                           |                           |                    | Ericsson_PACO/DUMMY       | 
|                          |                |               |          |          |                           |                           |                    | Ericsson_PACO/PDN         | 
+--------------------------+----------------+---------------+----------+----------+---------------------------+---------------------------+--------------------+---------------------------+
| Ericsson_PACO/RAN        | enforced       | ingress       | 16386    | 2293761  |                           |                           |                    | Ericsson_PACO/RAN         | 
+--------------------------+----------------+---------------+----------+----------+---------------------------+---------------------------+--------------------+---------------------------+
| hefernan_ni-demo/ni-demo | enforced       | ingress       | 32770    | 2916353  |                           | hefernan_ni-demo/BD1      | 169.254.100.1/24   |                           | 
|                          |                |               |          |          |                           | hefernan_ni-demo/BD2      | 169.254.101.1/24   |                           | 
+--------------------------+----------------+---------------+----------+----------+---------------------------+---------------------------+--------------------+---------------------------+
| infra/ave-ctrl           | enforced       | ingress       | 32770    | 2686976  | infra/ave-ctrl/ave-ctrl   | infra/ave-ctrl            |                    |                           | 
+--------------------------+----------------+---------------+----------+----------+---------------------------+---------------------------+--------------------+---------------------------+
| infra/overlay-1          | enforced       | ingress       | 32770    | 16777199 | infra/access/default      | infra/default             | 10.5.0.30/27       | infra/intersite           | 
|                          |                |               |          |          |                           |                           |                    | infra/RL-L3Out            | 
+--------------------------+----------------+---------------+----------+----------+---------------------------+---------------------------+--------------------+---------------------------+
| k8s/k8s_SRIoV_VRF        | enforced       | ingress       | 32770    | 2228224  |                           | k8s/SRIoV_A_BD            | 15.20.16.254/24    |                           | 
|                          |                |               |          |          |                           | k8s/SRIoV_B_BD            | 15.20.17.254/24    |                           | 
+--------------------------+----------------+---------------+----------+----------+---------------------------+---------------------------+--------------------+---------------------------+
| k8s/k8s_VRF              | enforced       | ingress       | 32770    | 2916354  |                           |                           |                    | k8s/bml3_k8s              | 
|                          |                |               |          |          |                           |                           |                    | k8s/vl3_k8s               | 
+--------------------------+----------------+---------------+----------+----------+---------------------------+---------------------------+--------------------+---------------------------+
| mgmt/EU-SPDC-ERSPAN-VRF  | enforced       | ingress       | 32770    | 2883584  |                           | mgmt/EU-SPDC-ERSPAN_BD    | 99.100.100.254/24  |                           | 
+--------------------------+----------------+---------------+----------+----------+---------------------------+---------------------------+--------------------+---------------------------+
| mgmt/EU-SPDC-MGMT-VRF1   | enforced       | ingress       | 16386    | 2916352  |                           | mgmt/EU-SPDC-BD1          |                    |                           | 
+--------------------------+----------------+---------------+----------+----------+---------------------------+---------------------------+--------------------+---------------------------+
| mgmt/inb                 | enforced       | ingress       | 16386    | 3080192  |                           | mgmt/inb                  | 10.58.50.190/27    | mgmt/INB_L3out            | 
+--------------------------+----------------+---------------+----------+----------+---------------------------+---------------------------+--------------------+---------------------------+
| mgmt/oob                 | enforced       | ingress       | 49153    | 2195456  |                           |                           |                    |                           | 
+--------------------------+----------------+---------------+----------+----------+---------------------------+---------------------------+--------------------+---------------------------+
| nidemo/streamz-vrf       | enforced       | ingress       | 16386    | 2424834  | nidemo/streamz/appserver  | nidemo/appserver          | 10.0.2.1/24        |                           | 
|                          |                |               |          |          | nidemo/streamz/database   | nidemo/database           | 10.0.3.1/24        |                           | 
|                          |                |               |          |          | nidemo/streamz/frontend   | nidemo/frontend           | 10.0.1.1/24        |                           | 
|                          |                |               |          |          | nidemo/streamz/management | nidemo/management         | 10.0.4.1/24        |                           | 
+--------------------------+----------------+---------------+----------+----------+---------------------------+---------------------------+--------------------+---------------------------+
| SPN_IntraLab/SPN_VRF1    | enforced       | ingress       | 16386    | 3080193  |                           | SPN_IntraLab/SPN_BD1      | 192.168.1.254/24   |                           | 
+--------------------------+----------------+---------------+----------+----------+---------------------------+---------------------------+--------------------+---------------------------+
| vEPC/Leaking_VRF         | enforced       | ingress       | 32770    | 2457600  |                           | vEPC/Leaking_BD           |                    |                           | 
+--------------------------+----------------+---------------+----------+----------+---------------------------+---------------------------+--------------------+---------------------------+
| vEPC/VSFO                | enforced       | ingress       | 49153    | 3112960  |                           | vEPC/vSFO_BD              | 15.16.132.254/24   | vEPC/vSFO_L3out           | 
+--------------------------+----------------+---------------+----------+----------+---------------------------+---------------------------+--------------------+---------------------------+
| vEPC_demo/ACC_VRF        | unenforced     | ingress       | 32770    | 2785280  |                           | vEPC_demo/ACC_BD          | 15.20.0.254/24     | vEPC_demo/ACC_L3out       | 
|                          |                |               |          |          |                           | vEPC_demo/vEPC-CTRL-SX_BD |                    | vEPC_demo/SX_L3out        | 
+--------------------------+----------------+---------------+----------+----------+---------------------------+---------------------------+--------------------+---------------------------+
| vEPC_demo/INT_VRF        | enforced       | ingress       | 49153    | 2424833  |                           | vEPC_demo/INT_BD          | 15.20.3.254/24     | vEPC_demo/INT_L3out       | 
+--------------------------+----------------+---------------+----------+----------+---------------------------+---------------------------+--------------------+---------------------------+
| vEPC_demo/MGMT_VRF       | enforced       | ingress       | 16386    | 2588672  |                           |                           |                    |                           | 
+--------------------------+----------------+---------------+----------+----------+---------------------------+---------------------------+--------------------+---------------------------+
```

Developer

```
# iserver get aci vrf --apic apic21 --ip 10.58.24.209

{
    "duration": 4802,
    "apic": {
        "read": true,
        "success": 9,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 8,
        "connect_time": 394,
        "disconnect_time": 0,
        "mo_time": 3371,
        "total_time": 3765
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

True	394	-	connect apic21o.emea-sp.cisco.com:443
True	292	23	apic21o.emea-sp.cisco.com:443 class fvCtx
True	381	36	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	340	15	apic21o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree=children&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	369	18	apic21o.emea-sp.cisco.com:443 class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
True	490	93	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	587	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	565	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	347	152	apic21o.emea-sp.cisco.com:443 class fvLocale
```

[[Back]](./Vrf.md)