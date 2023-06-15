# Policy Group - Access Interface - Leaf Access Port

## AAEP specific output

```
# iserver get aci pg access intf port --apic apic11 --name P5G* --view aaep

Apic: apic11 (mode:online, cache:off)

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
    "duration": 1837,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 439,
        "disconnect_time": 0,
        "mo_time": 1109,
        "total_time": 1548
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

True	439	-	connect apic11o.emea-sp.cisco.com
True	462	46	apic11o.emea-sp.cisco.com mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccPortGrp&rsp-subtree=children&rsp-subtree-class=infraRsAttEntP,infraRsCdpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsMonIfInfraPol,infraRsStpIfPol,infraRsMcpIfPol,infraRsStormctrlIfPol
True	647	30	apic11o.emea-sp.cisco.com class infraAttEntityP query rsp-subtree=children&rsp-subtree-class=infraProvAcc,infraRtAttEntP,infraRsDomP
```

[[Back]](./PgAccessInterfacePort.md)