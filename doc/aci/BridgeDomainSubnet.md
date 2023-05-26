# Bridge Domain

## Filter by bridge domain's subnet

Bridge domain with IP subnet that contains provided IP subnet will be shown.

```
# iserver get aci bd --apic apic21 --subnet 10.58.24.206/28

Apic: apic21

+---------------+-----------------+-------+------------+------------------+--------------------+
| Bridge Domain | Subnet          | Usage | EPG        | VRF              | L3Out              |
+---------------+-----------------+-------+------------+------------------+--------------------+
| k8s/vk8s_3_BD | 10.58.24.206/28 | 10/14 | k8s/vk8s_3 | common/Infra_VRF | common/Infra_L3out | 
+---------------+-----------------+-------+------------+------------------+--------------------+
```

[[Back]](./BridgeDomain.md)