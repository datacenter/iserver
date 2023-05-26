# Bridge Domain

## Filter by bridge domain's associated EPG name

```
# iserver get aci bd --apic apic21 --epg *vEPG_MGMT*

Apic: apic21

+-------------------+-----------------+-------+---------------------+------------------+--------------------+
| Bridge Domain     | Subnet          | Usage | EPG                 | VRF              | L3Out              |
+-------------------+-----------------+-------+---------------------+------------------+--------------------+
| vEPC_demo/MGMT_BD | 10.58.25.158/27 | 1/30  | vEPC_demo/vEPG_MGMT | common/Infra_VRF | common/Infra_L3out | 
+-------------------+-----------------+-------+---------------------+------------------+--------------------+
```

[[Back]](./BridgeDomain.md)