# L3 Domain

## All domains

```
# iserver get aci domain l3 --apic apic11

Apic: apic11 (mode:online, cache:off)

+-------------------------------+-----------------------------+-----------------------------------+-----------------------+-----------+
| Domain Name                   | AAEP                        | VLAN Pool                         | Encapsulation Block   | EPG Usage |
+-------------------------------+-----------------------------+-----------------------------------+-----------------------+-----------+
| cvim1_TEST_L3dom              |                             | cvim1_VlanPool                    |                       |           | 
+-------------------------------+-----------------------------+-----------------------------------+-----------------------+-----------+
| cvim2_L3dom                   |                             | pod2A_VlanPool                    |                       |           | 
+-------------------------------+-----------------------------+-----------------------------------+-----------------------+-----------+
| cvim3_L3dom                   |                             | pod3A_VlanPool                    |                       |           | 
+-------------------------------+-----------------------------+-----------------------------------+-----------------------+-----------+
| DC-CFP                        | DC-CFP                      | L3OUT-DCCFP-VLAN                  | [2371-2371] (static)  | 0/4       | 
|                               |                             |                                   | [2372-2372] (static)  |           | 
|                               |                             |                                   | [2373-2373] (static)  |           | 
|                               |                             |                                   | [2374-2374] (static)  |           | 
+-------------------------------+-----------------------------+-----------------------------------+-----------------------+-----------+
| Infra-2_L3Dom                 |                             | Infra_VlanPool                    | [1-1000] (inherit)    | 0/1001    | 
|                               |                             |                                   | [2000-2000] (inherit) |           | 
+-------------------------------+-----------------------------+-----------------------------------+-----------------------+-----------+
| Infra-BGP_L3Dom               | Infra_L3_AAEP               | Infra_VlanPool                    | [1-1000] (inherit)    | 0/1001    | 
|                               |                             |                                   | [2000-2000] (inherit) |           | 
+-------------------------------+-----------------------------+-----------------------------------+-----------------------+-----------+
| Infra_L3Dom                   | UCSB1-R3DC_AAEP             | Infra_VlanPool                    | [1-1000] (inherit)    | 0/1001    | 
|                               | Infra_L3_AAEP               |                                   | [2000-2000] (inherit) |           | 
|                               | UCSB1_AAEP                  |                                   |                       |           | 
|                               | Infra_AAEP                  |                                   |                       |           | 
|                               | SPN_AAEP                    |                                   |                       |           | 
+-------------------------------+-----------------------------+-----------------------------------+-----------------------+-----------+
| multipodL3Out_L3Dom           | multipodL3Out_AAEP          | multipodL3Out_VlanPool            | [4-4] (inherit)       | 0/1       | 
+-------------------------------+-----------------------------+-----------------------------------+-----------------------+-----------+
| multipodL3Out_RoutedDomain    | multipodL3Out_EntityProfile | multipodL3Out_VlanPool            | [4-4] (inherit)       | 0/1       | 
+-------------------------------+-----------------------------+-----------------------------------+-----------------------+-----------+
| RL-L3Out_RoutedDomain         | RL-L3Out_EntityProfile      | RL-L3Out_VlanPool                 | [4-4] (inherit)       | 0/1       | 
+-------------------------------+-----------------------------+-----------------------------------+-----------------------+-----------+
| smi5Gc-cvim1-SRIOV_L3Dom      | pod1a_AAEP                  | smi5Gc-cvim1-SRIOV-L3Out_VlanPool | [1191-1192] (static)  | 0/7       | 
|                               | cvim1-SRIOV_AAEP            |                                   | [1193-1193] (inherit) |           | 
|                               |                             |                                   | [1503-1504] (static)  |           | 
|                               |                             |                                   | [1506-1507] (static)  |           | 
+-------------------------------+-----------------------------+-----------------------------------+-----------------------+-----------+
| smi5Gc-cvim4-SRIOV_L3Dom      | pod4a_AAEP                  | smi5Gc-cvim4-SRIOV-L3Out_VlanPool | [1803-1804] (static)  | 0/7       | 
|                               | cvim4-SRIOV_AAEP            |                                   | [1806-1807] (static)  |           | 
|                               |                             |                                   | [2791-2792] (inherit) |           | 
|                               |                             |                                   | [2799-2799] (inherit) |           | 
+-------------------------------+-----------------------------+-----------------------------------+-----------------------+-----------+
| SPIN_InnoLab_Calico_L3Dom     | ESX-CDC_AAEP                | ESX-CDC_VlanPool                  | [418-419] (static)    | 20/524    | 
|                               |                             |                                   | [500-519] (static)    |           | 
|                               |                             |                                   | [520-520] (static)    |           | 
|                               |                             |                                   | [1108-1108] (static)  |           | 
|                               |                             |                                   | [2001-2500] (dynamic) |           | 
+-------------------------------+-----------------------------+-----------------------------------+-----------------------+-----------+
| SPIN_InnoLab_Calico_RDC_L3Dom | ESX-R3DC_AAEP               | ESX-R3DC_VlanPool                 | [2300-2309] (static)  | 5/410     | 
|                               |                             |                                   | [2310-2310] (static)  |           | 
|                               |                             |                                   | [3001-3399] (inherit) |           | 
+-------------------------------+-----------------------------+-----------------------------------+-----------------------+-----------+
| SR-Infra-CDC-2_L3dom          | SR-Infra-CDC-2_AAEP         | SR-Infra_VlanPool                 | [1-1] (static)        | 0/10      | 
|                               |                             |                                   | [101-109] (static)    |           | 
+-------------------------------+-----------------------------+-----------------------------------+-----------------------+-----------+
| SR-Infra-RDC-3_L3Dom          | SR-Infra-RDC-3_AAEP         | SR-Infra_VlanPool                 | [1-1] (static)        | 0/10      | 
|                               |                             |                                   | [101-109] (static)    |           | 
+-------------------------------+-----------------------------+-----------------------------------+-----------------------+-----------+
| SR-Infra-RDC-4_L3dom          | SR-Infra-RDC-4_AAEP         | SR-Infra_VlanPool                 | [1-1] (static)        | 0/10      | 
|                               |                             |                                   | [101-109] (static)    |           | 
+-------------------------------+-----------------------------+-----------------------------------+-----------------------+-----------+
| UCSB1_L3Dom                   | UCSB1_AAEP                  | UCSB1_VlanPool                    | [2-100] (static)      | 0/1999    | 
|                               |                             |                                   | [101-1000] (inherit)  |           | 
|                               |                             |                                   | [2001-2500] (inherit) |           | 
|                               |                             |                                   | [3001-3500] (inherit) |           | 
+-------------------------------+-----------------------------+-----------------------------------+-----------------------+-----------+
```

Developer

```
# iserver get aci domain l3 --apic apic11

{
    "duration": 1611,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 422,
        "disconnect_time": 0,
        "mo_time": 979,
        "total_time": 1401
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

True	422	-	connect apic11o.emea-sp.cisco.com
True	313	18	apic11o.emea-sp.cisco.com class l3extDomP query rsp-subtree=children&rsp-subtree-class=infraRsVlanNs,infraRtDomP,aaaDomain
True	342	25	apic11o.emea-sp.cisco.com class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	324	39	apic11o.emea-sp.cisco.com class vmmEpPD
```

[[Back]](./DomainL3.md)