# Policy Group - Access Interface - Leaf Access Port

## AAEP specific output

```
# iserver get aci pg access intf port --apic apic11 --name P5G* -o aaep

Apic: apic11

+-------------------------+-------------------------+-------------+-------------------+
| Name                    | Attached Entity Profile | Domain Type | Domain Name       |
+-------------------------+-------------------------+-------------+-------------------+
| P5G-ACI1-Napoli_PolGrp  | Private5G_AAEP          | Physical    | Private5G_PhysDom | 
+-------------------------+-------------------------+-------------+-------------------+
| P5G-Core-MLOM-1_PolGrp  | Private5G_AAEP          | Physical    | Private5G_PhysDom | 
+-------------------------+-------------------------+-------------+-------------------+
| P5G-Core-PCIe1-A_PolGrp | Private5G_AAEP          | Physical    | Private5G_PhysDom | 
+-------------------------+-------------------------+-------------+-------------------+
| P5G-Core-PCIe2-A_PolGrp | Private5G_AAEP          | Physical    | Private5G_PhysDom | 
+-------------------------+-------------------------+-------------+-------------------+
| P5G-CU-PCIe1-A_PolGrp   | Private5G_AAEP          | Physical    | Private5G_PhysDom | 
+-------------------------+-------------------------+-------------+-------------------+
| P5G-CU-PCIe2-A_PolGrp   | Private5G_AAEP          | Physical    | Private5G_PhysDom | 
+-------------------------+-------------------------+-------------+-------------------+
| P5G-LOM_PolGrp          | Private5G_AAEP          | Physical    | Private5G_PhysDom | 
+-------------------------+-------------------------+-------------+-------------------+
```

[[Back]](./PgAccessInterfacePort.md)