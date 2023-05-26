# Virtual Routing and Forwarding (VRF)

## Get VRF properties

Use '-o props' to get properties of selected vrfs
- vrf name and tenant
- data plane learning
- policy control enforcement preference and direction
- multicast
- bridge domain enforcement

```
# iserver get aci vrf --apic apic21 -o props

Apic: apic21

+--------------------------+-------------+--------+----------------+---------------+-------------+
| VRF                      | DP Learning | Mcast  | PCE Preference | PCE Direction | BD Enforced |
+--------------------------+-------------+--------+----------------+---------------+-------------+
| vEPC_demo/ACC_VRF        | enabled     | permit | unenforced     | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| infra/ave-ctrl           | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| common/copy              | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| common/default           | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| TESTING_BRUNO/default    | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| mgmt/EU-SPDC-ERSPAN-VRF  | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| mgmt/EU-SPDC-MGMT-VRF1   | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| mgmt/inb                 | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| common/Infra_privIP_VRF  | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| common/Infra_VRF         | enabled     | permit | unenforced     | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| vEPC_demo/INT_VRF        | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| k8s/k8s_SRIoV_VRF        | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| k8s/k8s_VRF              | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| vEPC/Leaking_VRF         | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| vEPC_demo/MGMT_VRF       | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| hefernan_ni-demo/ni-demo | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| mgmt/oob                 | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| infra/overlay-1          | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| SPN_IntraLab/SPN_VRF1    | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| nidemo/streamz-vrf       | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| common/Test_VRF1         | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
| vEPC/VSFO                | enabled     | permit | enforced       | ingress       | no          | 
+--------------------------+-------------+--------+----------------+---------------+-------------+
```

[[Back]](./Vrf.md)