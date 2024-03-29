# Attachable Access Entity Profile (AAEP)

## Epg view

```
# iserver get aci aaep --apic apic11 --view epg

Apic: apic11 (mode:online, cache:off)

Attachable Access Entity Profile (AAEP) - EPG Usage [#30]
---------------------------------------------------------

+---------+-----------------------------+------+-----------+------+-----+
| Faults  | Domain                      | AAEP | VLAN Pool | Vlan | EPG |
+---------+-----------------------------+------+-----------+------+-----+
| 0 0 0 0 | cvim-brAPI_AAEP             |      |           |      |     | 
+---------+-----------------------------+------+-----------+------+-----+
| 0 0 0 0 | cvim1-SRIOV_AAEP            |      |           |      |     | 
+---------+-----------------------------+------+-----------+------+-----+
| 0 0 0 0 | cvim4-SRIOV_AAEP            |      |           |      |     | 
+---------+-----------------------------+------+-----------+------+-----+
| 0 0 0 0 | DC-CFP                      |      |           |      |     | 
+---------+-----------------------------+------+-----------+------+-----+
| 0 0 0 1 | DC-CFP-AEP                  |      |           |      |     | 
+---------+-----------------------------+------+-----------+------+-----+
| 0 0 0 0 | default                     |      |           |      |     | 
+---------+-----------------------------+------+-----------+------+-----+
| 0 0 0 1 | ESX-CDC_AAEP                |      |           |      |     | 
+---------+-----------------------------+------+-----------+------+-----+
| 0 0 0 0 | ESX-R3DC_AAEP               |      |           |      |     | 
+---------+-----------------------------+------+-----------+------+-----+
| 0 0 0 1 | ESX_AAEP                    |      |           |      |     | 
+---------+-----------------------------+------+-----------+------+-----+
| 0 0 0 0 | F5-ADC_AAEP                 |      |           |      |     | 
+---------+-----------------------------+------+-----------+------+-----+
| 0 0 0 0 | HX1_AAEP                    |      |           |      |     | 
+---------+-----------------------------+------+-----------+------+-----+
| 0 0 0 0 | IKS1-mgmt_AAEP              |      |           |      |     | 
+---------+-----------------------------+------+-----------+------+-----+
| 0 0 0 0 | IKS2-mgmt_AAEP              |      |           |      |     | 
+---------+-----------------------------+------+-----------+------+-----+
| 0 0 0 0 | Infra-2_AAEP                |      |           |      |     | 
+---------+-----------------------------+------+-----------+------+-----+
| 0 0 0 0 | Infra_AAEP                  |      |           |      |     | 
+---------+-----------------------------+------+-----------+------+-----+
| 0 0 0 0 | Infra_L3_AAEP               |      |           |      |     | 
+---------+-----------------------------+------+-----------+------+-----+
| 0 0 0 0 | multipodL3Out_AAEP          |      |           |      |     | 
+---------+-----------------------------+------+-----------+------+-----+
| 0 0 0 0 | multipodL3Out_EntityProfile |      |           |      |     | 
+---------+-----------------------------+------+-----------+------+-----+
| 0 0 0 0 | nidemo-dummy                |      |           |      |     | 
+---------+-----------------------------+------+-----------+------+-----+
| 0 0 0 0 | pod1a_AAEP                  |      |           |      |     | 
+---------+-----------------------------+------+-----------+------+-----+
| 0 0 0 0 | pod4a_AAEP                  |      |           |      |     | 
+---------+-----------------------------+------+-----------+------+-----+
| 0 0 0 0 | Private5G_AAEP              |      |           |      |     | 
+---------+-----------------------------+------+-----------+------+-----+
| 0 0 0 0 | RL-L3Out_EntityProfile      |      |           |      |     | 
+---------+-----------------------------+------+-----------+------+-----+
| 0 0 0 0 | SPN_AAEP                    |      |           |      |     | 
+---------+-----------------------------+------+-----------+------+-----+
| 0 0 0 0 | SR-Infra-CDC-2_AAEP         |      |           |      |     | 
+---------+-----------------------------+------+-----------+------+-----+
| 0 0 0 0 | SR-Infra-RDC-3_AAEP         |      |           |      |     | 
+---------+-----------------------------+------+-----------+------+-----+
| 0 0 0 0 | SR-Infra-RDC-4_AAEP         |      |           |      |     | 
+---------+-----------------------------+------+-----------+------+-----+
| 0 0 0 1 | SR-Infra_AAEP               |      |           |      |     | 
+---------+-----------------------------+------+-----------+------+-----+
| 0 0 0 0 | UCSB1-R3DC_AAEP             |      |           |      |     | 
+---------+-----------------------------+------+-----------+------+-----+
| 0 0 0 0 | UCSB1_AAEP                  |      |           |      |     | 
+---------+-----------------------------+------+-----------+------+-----+
```

Developer

```
# iserver get aci aaep --apic apic11 --view epg

{
    "duration": 1276,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 384,
        "disconnect_time": 0,
        "mo_time": 726,
        "total_time": 1110
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

True	384	-	connect apic11o.emea-sp.cisco.com:443
True	394	30	apic11o.emea-sp.cisco.com:443 class infraAttEntityP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraProvAcc,infraRtAttEntP,infraRsDomP
True	332	31	apic11o.emea-sp.cisco.com:443 mo uni/infra query query-target=subtree&target-subtree-class=infraAttEntityP&target-subtree-class=infraRsFuncToEpg
```

[[Back]](./Aaep.md)