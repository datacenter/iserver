# Virtual Routing and Forwarding (VRF)

## Filter by vrf's name

Example: name

```
# iserver get aci vrf --apic apic21 --name *infra*

Apic: apic21

+-------------------------+----------------+---------------+----------------+---------------+------------+---------------------------+
| VRF                     | PCE Preference | PCE Direction | Associated EPG | Associated BD | BD Subnets | Associated L3Out          |
+-------------------------+----------------+---------------+----------------+---------------+------------+---------------------------+
| common/Infra_privIP_VRF | enforced       | ingress       |                |               |            | common/Infra_privIP_L3out | 
+-------------------------+----------------+---------------+----------------+---------------+------------+---------------------------+
| common/Infra_VRF        | unenforced     | ingress       |                |               |            | common/Infra_L3out        | 
+-------------------------+----------------+---------------+----------------+---------------+------------+---------------------------+
```

Example: tenant and name

```
# iserver get aci vrf --apic apic21 --name k8s/*sriov*

Apic: apic21

+-------------------+----------------+---------------+----------------+---------------+------------+------------------+
| VRF               | PCE Preference | PCE Direction | Associated EPG | Associated BD | BD Subnets | Associated L3Out |
+-------------------+----------------+---------------+----------------+---------------+------------+------------------+
| k8s/k8s_SRIoV_VRF | enforced       | ingress       |                |               |            |                  | 
+-------------------+----------------+---------------+----------------+---------------+------------+------------------+
```

[[Back]](./Vrf.md)