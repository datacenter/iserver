# Intersight Workload Optimizer

## List of storage devices

```
# iserver get iwo storage

Summary
-------
- Active   : 68/72
- Severity : 1/1/37/33
- Current  : 72/72


+---------+-------------+-----------+---------------------------------------------------------------------------------------+----------+---------+
| State   | Severity    | Staleness | Storage Device Name                                                                   | Location | Type    |
+---------+-------------+-----------+---------------------------------------------------------------------------------------+----------+---------+
| ACTIVE  | Normal      | CURRENT   | disk (berlin-esxi)                                                                    | ONPREM   | vCenter | 
| UNKNOWN | Normal      | CURRENT   | disk (berlin-esxi-242)                                                                | ONPREM   | vCenter | 
| ACTIVE  | Normal      | CURRENT   | disk (berlin-esxi-246)                                                                | ONPREM   | vCenter | 
| ACTIVE  | Minor (1)   | CURRENT   | ESX00-Datastore-Host-vCenter-RESERVED                                                 | ONPREM   | vCenter | 
| ACTIVE  | Normal      | CURRENT   | ESX01-Datastore-Host-RESERVED                                                         | ONPREM   | vCenter | 
| ACTIVE  | Normal      | CURRENT   | ESX1-Datastore-host                                                                   | ONPREM   | vCenter | 
| ACTIVE  | Minor (4)   | CURRENT   | ESX10-Datastore-host                                                                  | ONPREM   | vCenter | 
| ACTIVE  | Minor (2)   | CURRENT   | ESX11-Datastore-host                                                                  | ONPREM   | vCenter | 
| ACTIVE  | Minor (2)   | CURRENT   | ESX12-Datastore-host                                                                  | ONPREM   | vCenter | 
| ACTIVE  | Minor (3)   | CURRENT   | ESX13-Datastore-host                                                                  | ONPREM   | vCenter | 
| ACTIVE  | Normal      | CURRENT   | ESX14-Datastore-host                                                                  | ONPREM   | vCenter | 
| ACTIVE  | Minor (2)   | CURRENT   | ESX2-Datastore-host                                                                   | ONPREM   | vCenter | 
| ACTIVE  | Minor (2)   | CURRENT   | ESX20-Datastore-host                                                                  | ONPREM   | vCenter | 
| ACTIVE  | Minor (3)   | CURRENT   | ESX21-Datastore-host                                                                  | ONPREM   | vCenter | 
| UNKNOWN | Normal      | CURRENT   | ESX22-Datastore-host                                                                  | ONPREM   | vCenter | 
| ACTIVE  | Minor (2)   | CURRENT   | ESX3-Datastore-host                                                                   | ONPREM   | vCenter | 
| ACTIVE  | Normal      | CURRENT   | ESX31-Datastore-host                                                                  | ONPREM   | vCenter | 
| ACTIVE  | Normal      | CURRENT   | ESX32-Datastore-host                                                                  | ONPREM   | vCenter | 
| ACTIVE  | Normal      | CURRENT   | ESX33-Datastore-host                                                                  | ONPREM   | vCenter | 
| ACTIVE  | Minor (1)   | CURRENT   | ESX34-Datastore-host                                                                  | ONPREM   | vCenter | 
| ACTIVE  | Minor (1)   | CURRENT   | ESX35-Datastore-host                                                                  | ONPREM   | vCenter | 
| ACTIVE  | Minor (1)   | CURRENT   | ESX36-Datastore-host                                                                  | ONPREM   | vCenter | 
| ACTIVE  | Minor (1)   | CURRENT   | ESX37-Datastore-host                                                                  | ONPREM   | vCenter | 
| ACTIVE  | Minor (2)   | CURRENT   | ESX4-Datastore-host                                                                   | ONPREM   | vCenter | 
| ACTIVE  | Minor (2)   | CURRENT   | ESX41-Datastore-host                                                                  | ONPREM   | vCenter | 
| ACTIVE  | Minor (2)   | CURRENT   | ESX42-Datastore-host                                                                  | ONPREM   | vCenter | 
| ACTIVE  | Minor (2)   | CURRENT   | ESX43-Datastore-host                                                                  | ONPREM   | vCenter | 
| ACTIVE  | Minor (4)   | CURRENT   | ESX44-Datastore-host                                                                  | ONPREM   | vCenter | 
| ACTIVE  | Minor (1)   | CURRENT   | ESX5-Datastore-host                                                                   | ONPREM   | vCenter | 
| ACTIVE  | Minor (2)   | CURRENT   | ESX51-Datastore-host                                                                  | ONPREM   | vCenter | 
| ACTIVE  | Minor (2)   | CURRENT   | ESX52-Datastore-host                                                                  | ONPREM   | vCenter | 
| ACTIVE  | Minor (2)   | CURRENT   | ESX53-Datastore-host                                                                  | ONPREM   | vCenter | 
| ACTIVE  | Minor (2)   | CURRENT   | ESX54-Datastore-host                                                                  | ONPREM   | vCenter | 
| ACTIVE  | Minor (2)   | CURRENT   | ESX6-Datastore-host                                                                   | ONPREM   | vCenter | 
| ACTIVE  | Minor (2)   | CURRENT   | ESX7-Datastore-host                                                                   | ONPREM   | vCenter | 
| ACTIVE  | Minor (2)   | CURRENT   | ESX8-Datastore-host                                                                   | ONPREM   | vCenter | 
| ACTIVE  | Minor (2)   | CURRENT   | ESX9-Datastore-host                                                                   | ONPREM   | vCenter | 
| ACTIVE  | Minor (20)  | CURRENT   | ESX91-VC_data_reserved                                                                | ONPREM   | vCenter | 
| ACTIVE  | Minor (3)   | CURRENT   | ESX92-Datastore-host                                                                  | ONPREM   | vCenter | 
| ACTIVE  | Minor (3)   | CURRENT   | ESX93-Datastore-host                                                                  | ONPREM   | vCenter | 
| UNKNOWN | Normal      | CURRENT   | ESX94-Datastore-host                                                                  | ONPREM   | vCenter | 
| UNKNOWN | Normal      | CURRENT   | ESX95-Datastore-host                                                                  | ONPREM   | vCenter | 
| ACTIVE  | Normal      | CURRENT   | ESXUnknown-Datastore-host                                                             | ONPREM   | vCenter | 
| ACTIVE  | Minor (9)   | CURRENT   | EU-SPDC-Datastore-SNAS                                                                | ONPREM   | vCenter | 
| ACTIVE  | Normal      | CURRENT   | EU-SPDC-Datastore-TNAS-DO-NOT-USE                                                     | ONPREM   | vCenter | 
| ACTIVE  | Minor (97)  | CURRENT   | EU-SPDC-Datastore-WNAS                                                                | ONPREM   | vCenter | 
| ACTIVE  | Minor (5)   | CURRENT   | EU-SPDC-Datastore-YNAS                                                                | ONPREM   | vCenter | 
| ACTIVE  | Minor (56)  | CURRENT   | EU-SPDC-Datastore-ZNAS                                                                | ONPREM   | vCenter | 
| ACTIVE  | Minor (13)  | CURRENT   | EU-SPDC-DMZ-Datastore1                                                                | ONPREM   | vCenter | 
| ACTIVE  | Minor (100) | CURRENT   | EU-SPDC-DMZ-TNAS                                                                      | ONPREM   | vCenter | 
| ACTIVE  | Minor (3)   | CURRENT   | EU-SPDC-ESX4-Datastore                                                                | ONPREM   | vCenter | 
| ACTIVE  | Minor (4)   | CURRENT   | EU-SPDC-ESX5-Datastore                                                                | ONPREM   | vCenter | 
| ACTIVE  | Minor (21)  | CURRENT   | EU-SPDC-FlashArray-Blades-Vol01                                                       | ONPREM   | vCenter | 
| ACTIVE  | Normal      | CURRENT   | EU-SPDC-FlashArray-Racks-Vol01                                                        | ONPREM   | vCenter | 
| ACTIVE  | Normal      | CURRENT   | SPDC-DMZ-NAS-Critical-VM : [ESX91-VC_data_reserved] SPDC-DMZ-NAS/SPDC-DMZ-NAS_1.vmdk  | ONPREM   | vCenter | 
| ACTIVE  | Normal      | CURRENT   | SPDC-DMZ-NAS-Critical-VM : [ESX91-VC_data_reserved] SPDC-DMZ-NAS/SPDC-DMZ-NAS_10.vmdk | ONPREM   | vCenter | 
| ACTIVE  | Normal      | CURRENT   | SPDC-DMZ-NAS-Critical-VM : [ESX91-VC_data_reserved] SPDC-DMZ-NAS/SPDC-DMZ-NAS_11.vmdk | ONPREM   | vCenter | 
| ACTIVE  | Normal      | CURRENT   | SPDC-DMZ-NAS-Critical-VM : [ESX91-VC_data_reserved] SPDC-DMZ-NAS/SPDC-DMZ-NAS_12.vmdk | ONPREM   | vCenter | 
| ACTIVE  | Normal      | CURRENT   | SPDC-DMZ-NAS-Critical-VM : [ESX91-VC_data_reserved] SPDC-DMZ-NAS/SPDC-DMZ-NAS_13.vmdk | ONPREM   | vCenter | 
| ACTIVE  | Normal      | CURRENT   | SPDC-DMZ-NAS-Critical-VM : [ESX91-VC_data_reserved] SPDC-DMZ-NAS/SPDC-DMZ-NAS_14.vmdk | ONPREM   | vCenter | 
| ACTIVE  | Normal      | CURRENT   | SPDC-DMZ-NAS-Critical-VM : [ESX91-VC_data_reserved] SPDC-DMZ-NAS/SPDC-DMZ-NAS_15.vmdk | ONPREM   | vCenter | 
| ACTIVE  | Normal      | CURRENT   | SPDC-DMZ-NAS-Critical-VM : [ESX91-VC_data_reserved] SPDC-DMZ-NAS/SPDC-DMZ-NAS_16.vmdk | ONPREM   | vCenter | 
| ACTIVE  | Normal      | CURRENT   | SPDC-DMZ-NAS-Critical-VM : [ESX91-VC_data_reserved] SPDC-DMZ-NAS/SPDC-DMZ-NAS_17.vmdk | ONPREM   | vCenter | 
| ACTIVE  | Normal      | CURRENT   | SPDC-DMZ-NAS-Critical-VM : [ESX91-VC_data_reserved] SPDC-DMZ-NAS/SPDC-DMZ-NAS_18.vmdk | ONPREM   | vCenter | 
| ACTIVE  | Normal      | CURRENT   | SPDC-DMZ-NAS-Critical-VM : [ESX91-VC_data_reserved] SPDC-DMZ-NAS/SPDC-DMZ-NAS_2.vmdk  | ONPREM   | vCenter | 
| ACTIVE  | Normal      | CURRENT   | SPDC-DMZ-NAS-Critical-VM : [ESX91-VC_data_reserved] SPDC-DMZ-NAS/SPDC-DMZ-NAS_3.vmdk  | ONPREM   | vCenter | 
| ACTIVE  | Normal      | CURRENT   | SPDC-DMZ-NAS-Critical-VM : [ESX91-VC_data_reserved] SPDC-DMZ-NAS/SPDC-DMZ-NAS_4.vmdk  | ONPREM   | vCenter | 
| ACTIVE  | Normal      | CURRENT   | SPDC-DMZ-NAS-Critical-VM : [ESX91-VC_data_reserved] SPDC-DMZ-NAS/SPDC-DMZ-NAS_5.vmdk  | ONPREM   | vCenter | 
| ACTIVE  | Normal      | CURRENT   | SPDC-DMZ-NAS-Critical-VM : [ESX91-VC_data_reserved] SPDC-DMZ-NAS/SPDC-DMZ-NAS_6.vmdk  | ONPREM   | vCenter | 
| ACTIVE  | Normal      | CURRENT   | SPDC-DMZ-NAS-Critical-VM : [ESX91-VC_data_reserved] SPDC-DMZ-NAS/SPDC-DMZ-NAS_7.vmdk  | ONPREM   | vCenter | 
| ACTIVE  | Normal      | CURRENT   | SPDC-DMZ-NAS-Critical-VM : [ESX91-VC_data_reserved] SPDC-DMZ-NAS/SPDC-DMZ-NAS_8.vmdk  | ONPREM   | vCenter | 
| ACTIVE  | Normal      | CURRENT   | SPDC-DMZ-NAS-Critical-VM : [ESX91-VC_data_reserved] SPDC-DMZ-NAS/SPDC-DMZ-NAS_9.vmdk  | ONPREM   | vCenter | 
+---------+-------------+-----------+---------------------------------------------------------------------------------------+----------+---------+
```