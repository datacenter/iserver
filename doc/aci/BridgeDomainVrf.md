# Bridge Domain

## Filter by bridge domain's vrf name

```
# iserver get aci bd --apic apic21 --vrf *mgmt*

Apic: apic21

+------------------+-------------------+------------------------+
| Bridge Domain    | EPG               | VRF                    |
+------------------+-------------------+------------------------+
| mgmt/EU-SPDC-BD1 | mgmt/EU-SPDC-MGMT | mgmt/EU-SPDC-MGMT-VRF1 | 
+------------------+-------------------+------------------------+
```

[[Back]](./BridgeDomain.md)