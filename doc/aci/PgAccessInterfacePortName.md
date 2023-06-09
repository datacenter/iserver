# Policy Group - Access Interface - Leaf Access Port

## Filter by name

```
# iserver get aci pg access intf port --apic apic11 --name P5G*

Apic: apic11 (mode:online, cache:off)

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

Developer

```
# iserver get aci pg access intf port --apic apic11 --name P5G*

{
    "duration": 1229,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 446,
        "disconnect_time": 0,
        "mo_time": 521,
        "total_time": 967
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

True	446	-	connect apic11o.emea-sp.cisco.com
True	521	46	apic11o.emea-sp.cisco.com mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccPortGrp&rsp-subtree=children&rsp-subtree-class=infraRsAttEntP,infraRsCdpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsMonIfInfraPol,infraRsStpIfPol,infraRsMcpIfPol,infraRsStormctrlIfPol
```

[[Back]](./PgAccessInterfacePort.md)