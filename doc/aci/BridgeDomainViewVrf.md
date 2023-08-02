# Bridge Domain

## VRF view

Use '--view vrf' to get configured VRF related properties of selected bridge domains
- resolved VRF tenant and name
- data plane learning
- policy control enforcement preference
- policy control enforcement direction
- bridge domain enforcement

```
# iserver get aci bd --apic apic21 --view vrf

Apic: apic21 (mode:online, cache:off)

Bridge Domain - VRF Properties [#35]
------------------------------------

+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| Bridge Domain             | VRF                      | Learning | PCE Direction | PCE Preference | BD Enforcement |
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| common/default            | common/default           | V        | ingress       | enforced       | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| common/Infra_BD           | common/Infra_VRF         | V        | ingress       | unenforced     | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| common/Infra_privIP_BD    | common/Infra_privIP_VRF  | V        | ingress       | enforced       | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| common/Test_BD            | common/Infra_privIP_VRF  | V        | ingress       | enforced       | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| hefernan_ni-demo/BD1      | hefernan_ni-demo/ni-demo | V        | ingress       | enforced       | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| hefernan_ni-demo/BD2      | hefernan_ni-demo/ni-demo | V        | ingress       | enforced       | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| infra/ave-ctrl            | infra/ave-ctrl           | V        | ingress       | enforced       | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| infra/default             | infra/overlay-1          | V        | ingress       | enforced       | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| k8s/bmk8s_1_BD            | common/Infra_VRF         | V        | ingress       | unenforced     | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| k8s/bmk8s_2_BD            | common/Infra_VRF         | V        | ingress       | unenforced     | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| k8s/bmk8s_prov_BD         | common/Infra_VRF         | V        | ingress       | unenforced     | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| k8s/bml3outk8s_BD         | common/Infra_VRF         | V        | ingress       | unenforced     | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| k8s/MGMT_BD               | common/Infra_VRF         | V        | ingress       | unenforced     | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| k8s/SRIoV_A_BD            | k8s/k8s_SRIoV_VRF        | V        | ingress       | enforced       | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| k8s/SRIoV_B_BD            | k8s/k8s_SRIoV_VRF        | V        | ingress       | enforced       | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| k8s/Test                  | common/Infra_privIP_VRF  | V        | ingress       | enforced       | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| k8s/vk8s_1_BD             | common/Infra_VRF         | V        | ingress       | unenforced     | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| k8s/vk8s_2_BD             | common/Infra_VRF         | V        | ingress       | unenforced     | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| k8s/vk8s_3_BD             | common/Infra_VRF         | V        | ingress       | unenforced     | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| k8s/vk8s_4_BD             | common/Infra_VRF         | V        | ingress       | unenforced     | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| k8s/vl3outk8s_BD          | common/Infra_VRF         | V        | ingress       | unenforced     | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| k8s/VM2VM_BD              | common/Infra_VRF         | V        | ingress       | unenforced     | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| mgmt/EU-SPDC-ERSPAN_BD    | mgmt/EU-SPDC-ERSPAN-VRF  | V        | ingress       | enforced       | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| mgmt/inb                  | mgmt/inb                 | V        | ingress       | enforced       | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| nidemo/appserver          | nidemo/streamz-vrf       | V        | ingress       | enforced       | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| nidemo/database           | nidemo/streamz-vrf       | V        | ingress       | enforced       | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| nidemo/frontend           | nidemo/streamz-vrf       | V        | ingress       | enforced       | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| nidemo/management         | nidemo/streamz-vrf       | V        | ingress       | enforced       | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| SPN_IntraLab/SPN_BD1      | SPN_IntraLab/SPN_VRF1    | V        | ingress       | enforced       | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| vEPC/Leaking_BD           | vEPC/Leaking_VRF         | V        | ingress       | enforced       | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| vEPC/vSFO_BD              | vEPC/VSFO                | V        | ingress       | enforced       | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| vEPC_demo/ACC_BD          | vEPC_demo/ACC_VRF        | V        | ingress       | unenforced     | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| vEPC_demo/INT_BD          | vEPC_demo/INT_VRF        | V        | ingress       | enforced       | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| vEPC_demo/MGMT_BD         | common/Infra_VRF         | V        | ingress       | unenforced     | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| vEPC_demo/vEPC-CTRL-SX_BD | vEPC_demo/ACC_VRF        | V        | ingress       | unenforced     | X              | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
```

Developer

```
# iserver get aci bd --apic apic21 --view vrf

{
    "duration": 5097,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 540,
        "disconnect_time": 0,
        "mo_time": 3406,
        "total_time": 3946
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

True	540	-	connect apic21o.emea-sp.cisco.com:443
True	1487	35	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	545	23	apic21o.emea-sp.cisco.com:443 class fvCtx query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	530	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	379	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	465	87	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
```

[[Back]](./BridgeDomain.md)