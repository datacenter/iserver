# Bridge Domain

## Filter by bridge domain's IP address

Bridge domain with IP subnet that contains provided IP address will be shown.

```
# iserver get aci bd --apic apic21 --ip 10.58.24.209

Apic: apic21

+---------------+-----------------+-------+------------+------------------+--------------------+
| Bridge Domain | Subnet          | Usage | EPG        | VRF              | L3Out              |
+---------------+-----------------+-------+------------+------------------+--------------------+
| k8s/vk8s_4_BD | 10.58.24.222/28 | 10/14 | k8s/vk8s_4 | common/Infra_VRF | common/Infra_L3out | 
+---------------+-----------------+-------+------------+------------------+--------------------+
```

[[Back]](./BridgeDomain.md)