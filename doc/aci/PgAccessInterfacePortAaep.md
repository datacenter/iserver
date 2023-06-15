# Policy Group - Access Interface - Leaf Access Port

## Filter by aaep

```
# iserver get aci pg access intf port --apic apic11 --aaep ESX --view aaep

Apic: apic11 (mode:online, cache:off)

+---------------------+-------------------------+-------------+-------------+
| Name                | Attached Entity Profile | Domain Type | Domain Name |
+---------------------+-------------------------+-------------+-------------+
| ESX-CDC-DVS_PolGrp  | ESX                     |             |             | 
+---------------------+-------------------------+-------------+-------------+
| ESX-CDC_PolGrp      | ESX                     |             |             | 
+---------------------+-------------------------+-------------+-------------+
| ESX-R3DC-DVS_PolGrp | ESX                     |             |             | 
+---------------------+-------------------------+-------------+-------------+
```

Developer

```
# iserver get aci pg access intf port --apic apic11 --aaep ESX --view aaep

{
    "duration": 1664,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 424,
        "disconnect_time": 0,
        "mo_time": 950,
        "total_time": 1374
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

True	424	-	connect apic11o.emea-sp.cisco.com
True	592	46	apic11o.emea-sp.cisco.com mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccPortGrp&rsp-subtree=children&rsp-subtree-class=infraRsAttEntP,infraRsCdpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsMonIfInfraPol,infraRsStpIfPol,infraRsMcpIfPol,infraRsStormctrlIfPol
True	358	30	apic11o.emea-sp.cisco.com class infraAttEntityP query rsp-subtree=children&rsp-subtree-class=infraProvAcc,infraRtAttEntP,infraRsDomP
```

[[Back]](./PgAccessInterfacePort.md)