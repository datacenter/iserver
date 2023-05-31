# Policy Group - Access Interface - Leaf Access Port

## AAEP specific output

```
# iserver get aci pg access intf port --apic apic11 --name P5G* --view aaep

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

Developer

```
# iserver get aci pg access intf port --apic apic11 --name P5G* --view aaep

{
    "duration": 1556,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 405,
        "disconnect_time": 0,
        "mo_time": 949,
        "total_time": 1354
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
    }
}

Log: apic
----------

True	405	-	connect apic11o.emea-sp.cisco.com
True	603	46	apic11o.emea-sp.cisco.com mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccPortGrp&rsp-subtree=children&rsp-subtree-class=infraRsAttEntP,infraRsCdpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsMonIfInfraPol,infraRsStpIfPol,infraRsMcpIfPol,infraRsStormctrlIfPol
True	346	30	apic11o.emea-sp.cisco.com class infraAttEntityP query rsp-subtree=children&rsp-subtree-class=infraProvAcc,infraRtAttEntP,infraRsDomP
```

[[Back]](./PgAccessInterfacePort.md)