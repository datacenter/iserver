# Phy Domain

## Filter by name

```
# iserver get aci domain phy --apic apic11 --name UCSB*

Apic: apic11

+--------------------+-----------------+---------------------+-----------------------+-----------+
| Domain Name        | AAEP            | VLAN Pool           | Encapsulation Block   | EPG Usage |
+--------------------+-----------------+---------------------+-----------------------+-----------+
| UCSB1-R3DC_PhysDom | UCSB1-R3DC_AAEP | UCSB1-R3DC_VlanPool | [2901-3000] (inherit) | 0/100     | 
+--------------------+-----------------+---------------------+-----------------------+-----------+
| UCSB1_PhysDom      | UCSB1_AAEP      | UCSB1_VlanPool      | [2-100] (static)      | 0/1999    | 
|                    |                 |                     | [101-1000] (inherit)  |           | 
|                    |                 |                     | [2001-2500] (inherit) |           | 
|                    |                 |                     | [3001-3500] (inherit) |           | 
+--------------------+-----------------+---------------------+-----------------------+-----------+
```

Developer

```
# iserver get aci domain phy --apic apic11 --name UCSB*

{
    "duration": 1582,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 398,
        "disconnect_time": 0,
        "mo_time": 1017,
        "total_time": 1415
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

True	398	-	connect apic11o.emea-sp.cisco.com
True	331	23	apic11o.emea-sp.cisco.com class physDomP query rsp-subtree=children&rsp-subtree-class=infraRsVlanNs,infraRtDomP,aaaDomain
True	376	25	apic11o.emea-sp.cisco.com class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	310	39	apic11o.emea-sp.cisco.com class vmmEpPD
```

[[Back]](./DomainPhy.md)