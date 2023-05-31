# Attachable Access Entity Profile (AAEP)

## Filter by name

```
# iserver get aci aaep --apic apic11 --name UCSB*

Apic: apic11

+----------------------------------+------------+--------------------+-------------+--------------+------------------------+-----------------------------+
| Attachable Access Entity Profile | Infra VLAN | Domain Name        | Domain Type | Domain State | Policy Group Name      | Policy Group Interface Type |
+----------------------------------+------------+--------------------+-------------+--------------+------------------------+-----------------------------+
| UCSB1-R3DC_AAEP                  | X          | EU-SPDC-R3DC       | VMM         | formed       | UCSB1-R3DC-FI-A_PolGrp | PC/VPC Interface            | 
|                                  |            | Infra_L3Dom        | L3          | formed       | UCSB1-R3DC-FI-B_PolGrp | PC/VPC Interface            | 
|                                  |            | UCSB1-R3DC_PhysDom | Physical    | formed       |                        |                             | 
+----------------------------------+------------+--------------------+-------------+--------------+------------------------+-----------------------------+
| UCSB1_AAEP                       | X          | EU-SPDC-CDC        | VMM         | formed       | UCSB1-FI-A_PolGrp      | PC/VPC Interface            | 
|                                  |            | Infra_L3Dom        | L3          | formed       | UCSB1-FI-B_PolGrp      | PC/VPC Interface            | 
|                                  |            | UCSB1_L3Dom        | L3          | formed       |                        |                             | 
|                                  |            | UCSB1_PhysDom      | Physical    | formed       |                        |                             | 
+----------------------------------+------------+--------------------+-------------+--------------+------------------------+-----------------------------+
```

Developer

```
# iserver get aci aaep --apic apic11 --name UCSB*

{
    "duration": 870,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 378,
        "disconnect_time": 0,
        "mo_time": 359,
        "total_time": 737
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

True	378	-	connect apic11o.emea-sp.cisco.com
True	359	30	apic11o.emea-sp.cisco.com class infraAttEntityP query rsp-subtree=children&rsp-subtree-class=infraProvAcc,infraRtAttEntP,infraRsDomP
```

[[Back]](./Aaep.md)