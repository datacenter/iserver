# Bridge Domain

## Get VRF properties of bridge domains

Use '-o vrf' to get configured VRF related properties of selected bridge domains
- resolved VRF tenant and name
- data plane learning
- policy control enforcement preference
- policy control enforcement direction
- bridge domain enforcement

```
# iserver get aci bd --apic apic21 -o vrf

Apic: apic21

+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| Bridge Domain             | VRF                      | Learning | PCE Direction | PCE Preference | BD Enforcement |
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| common/default            | common/default           | enabled  | ingress       | enforced       | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| common/Infra_BD           | common/Infra_VRF         | enabled  | ingress       | unenforced     | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| common/Infra_privIP_BD    | common/Infra_privIP_VRF  | enabled  | ingress       | enforced       | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| common/Test_BD            | common/Infra_privIP_VRF  | enabled  | ingress       | enforced       | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| hefernan_ni-demo/BD1      | hefernan_ni-demo/ni-demo | enabled  | ingress       | enforced       | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| hefernan_ni-demo/BD2      | hefernan_ni-demo/ni-demo | enabled  | ingress       | enforced       | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| infra/ave-ctrl            | infra/ave-ctrl           | enabled  | ingress       | enforced       | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| infra/default             | infra/overlay-1          | enabled  | ingress       | enforced       | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| k8s/bmk8s_1_BD            | common/Infra_VRF         | enabled  | ingress       | unenforced     | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| k8s/bmk8s_2_BD            | common/Infra_VRF         | enabled  | ingress       | unenforced     | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| k8s/bmk8s_prov_BD         | common/Infra_VRF         | enabled  | ingress       | unenforced     | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| k8s/bml3outk8s_BD         | common/Infra_VRF         | enabled  | ingress       | unenforced     | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| k8s/MGMT_BD               | common/Infra_VRF         | enabled  | ingress       | unenforced     | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| k8s/SRIoV_A_BD            | k8s/k8s_SRIoV_VRF        | enabled  | ingress       | enforced       | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| k8s/SRIoV_B_BD            | k8s/k8s_SRIoV_VRF        | enabled  | ingress       | enforced       | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| k8s/Test                  | common/Infra_privIP_VRF  | enabled  | ingress       | enforced       | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| k8s/vk8s_1_BD             | common/Infra_VRF         | enabled  | ingress       | unenforced     | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| k8s/vk8s_2_BD             | common/Infra_VRF         | enabled  | ingress       | unenforced     | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| k8s/vk8s_3_BD             | common/Infra_VRF         | enabled  | ingress       | unenforced     | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| k8s/vk8s_4_BD             | common/Infra_VRF         | enabled  | ingress       | unenforced     | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| k8s/vl3outk8s_BD          | common/Infra_VRF         | enabled  | ingress       | unenforced     | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| k8s/VM2VM_BD              | common/Infra_VRF         | enabled  | ingress       | unenforced     | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| mgmt/EU-SPDC-BD1          | mgmt/EU-SPDC-MGMT-VRF1   | enabled  | ingress       | enforced       | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| mgmt/EU-SPDC-ERSPAN_BD    | mgmt/EU-SPDC-ERSPAN-VRF  | enabled  | ingress       | enforced       | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| mgmt/inb                  | mgmt/inb                 | enabled  | ingress       | enforced       | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| nidemo/appserver          | nidemo/streamz-vrf       | enabled  | ingress       | enforced       | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| nidemo/database           | nidemo/streamz-vrf       | enabled  | ingress       | enforced       | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| nidemo/frontend           | nidemo/streamz-vrf       | enabled  | ingress       | enforced       | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| nidemo/management         | nidemo/streamz-vrf       | enabled  | ingress       | enforced       | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| SPN_IntraLab/SPN_BD1      | SPN_IntraLab/SPN_VRF1    | enabled  | ingress       | enforced       | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| TESTING_BRUNO/BD2         | TESTING_BRUNO/default    | enabled  | ingress       | enforced       | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| TESTING_BRUNO/BDSITE2     | TESTING_BRUNO/default    | enabled  | ingress       | enforced       | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| vEPC/Leaking_BD           | vEPC/Leaking_VRF         | enabled  | ingress       | enforced       | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| vEPC/vSFO_BD              | vEPC/VSFO                | enabled  | ingress       | enforced       | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| vEPC_demo/ACC_BD          | vEPC_demo/ACC_VRF        | enabled  | ingress       | unenforced     | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| vEPC_demo/INT_BD          | vEPC_demo/INT_VRF        | enabled  | ingress       | enforced       | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| vEPC_demo/MGMT_BD         | common/Infra_VRF         | enabled  | ingress       | unenforced     | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
| vEPC_demo/vEPC-CTRL-SX_BD | vEPC_demo/ACC_VRF        | enabled  | ingress       | unenforced     | no             | 
+---------------------------+--------------------------+----------+---------------+----------------+----------------+
```

[[Back]](./BridgeDomain.md)