# Policy Group - Access Interface - Leaf Access Port

## Filter by name

```
# iserver get aci pg access intf port --apic apic11 --name P5G*

Apic: apic11

+-------------------------+-------------------------+------------+-----------+---------+---------+-------------+---------+---------------+
| Name                    | Attached Entity Profile | Link Level | Link Flap | CDP     | MCP     | LLDP        | STP     | Storm Control |
+-------------------------+-------------------------+------------+-----------+---------+---------+-------------+---------+---------------+
| P5G-ACI1-Napoli_PolGrp  | Private5G_AAEP          | Inherit    | default   | default | default | LLDP_enable | default | default       | 
| P5G-Core-MLOM-1_PolGrp  | Private5G_AAEP          | Inherit    | default   | default | default | LLDP_enable | default | default       | 
| P5G-Core-PCIe1-A_PolGrp | Private5G_AAEP          | Inherit    | default   | default | default | LLDP_enable | default | default       | 
| P5G-Core-PCIe2-A_PolGrp | Private5G_AAEP          | Inherit    | default   | default | default | LLDP_enable | default | default       | 
| P5G-CU-PCIe1-A_PolGrp   | Private5G_AAEP          | Inherit    | default   | default | default | LLDP_enable | default | default       | 
| P5G-CU-PCIe2-A_PolGrp   | Private5G_AAEP          | Inherit    | default   | default | default | LLDP_enable | default | default       | 
| P5G-LOM_PolGrp          | Private5G_AAEP          | Inherit    | default   | default | default | LLDP_enable | default | default       | 
+-------------------------+-------------------------+------------+-----------+---------+---------+-------------+---------+---------------+
```

[[Back]](./PgAccessInterfacePort.md)