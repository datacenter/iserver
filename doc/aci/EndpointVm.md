# Endpoint

## Filter by vm name

```
# iserver get aci ep --apic apic11 --vm *cnc* --view vm

Apic: apic11 (mode:online, cache:off)

+----+-------------------+--------------+-------------+-------------------------+----------------+------------+-------------------+------------+
| SF | MAC Address       | IP Address   | VMM         | Hypervisor              | VM Name        | VM State   | vNIC Name         | vNIC State |
+----+-------------------+--------------+-------------+-------------------------+----------------+------------+-------------------+------------+
| LV | 00:50:56:B2:12:35 | 10.58.239.61 | EU-SPDC-CDC | esx5-eu-spdc.cisco.com  | sr-cnc5-1vm    | poweredOn  | Network adapter 1 | up         | 
|    |                   | 10.58.239.60 |             |                         |                |            |                   |            | 
+----+-------------------+--------------+-------------+-------------------------+----------------+------------+-------------------+------------+
| LV | 00:50:56:B2:1E:01 | 10.58.239.53 | EU-SPDC-CDC | esx10-eu-spdc.cisco.com | cnc50-hybrid-3 | poweredOn  | Network adapter 1 | up         | 
+----+-------------------+--------------+-------------+-------------------------+----------------+------------+-------------------+------------+
| LV | 00:50:56:B2:1E:4D | 10.58.239.41 | EU-SPDC-CDC | esx8-eu-spdc.cisco.com  | cnc41-hybrid-1 | poweredOn  | Network adapter 1 | up         | 
|    |                   | 10.58.239.40 |             |                         |                |            |                   |            | 
+----+-------------------+--------------+-------------+-------------------------+----------------+------------+-------------------+------------+
| V  | 00:50:56:B2:21:5F |              | EU-SPDC-CDC | esx9-eu-spdc.cisco.com  | sr-cnc5-cdg    | poweredOn  | Network adapter 4 | up         | 
+----+-------------------+--------------+-------------+-------------------------+----------------+------------+-------------------+------------+
| V  | 00:50:56:B2:25:E7 |              | EU-SPDC-CDC | esx4-eu-spdc.cisco.com  | cnc50-dg-1     | poweredOn  | Network adapter 2 | up         | 
+----+-------------------+--------------+-------------+-------------------------+----------------+------------+-------------------+------------+
| LV | 00:50:56:B2:58:B3 | 10.58.239.62 | EU-SPDC-CDC | esx9-eu-spdc.cisco.com  | sr-cnc5-cdg    | poweredOn  | Network adapter 1 | up         | 
|    |                   | 10.58.239.63 |             |                         |                |            |                   |            | 
+----+-------------------+--------------+-------------+-------------------------+----------------+------------+-------------------+------------+
| V  | 00:50:56:B2:6F:76 |              | EU-SPDC-CDC | esx14-eu-spdc.cisco.com | CNC-installer  | poweredOff | Network adapter 1 | down       | 
+----+-------------------+--------------+-------------+-------------------------+----------------+------------+-------------------+------------+
| V  | 00:50:56:B2:6F:9E |              | EU-SPDC-CDC | esx9-eu-spdc.cisco.com  | sr-cnc5-cdg    | poweredOn  | Network adapter 2 | up         | 
+----+-------------------+--------------+-------------+-------------------------+----------------+------------+-------------------+------------+
| LV | 00:50:56:B2:92:87 | 10.58.239.45 | EU-SPDC-CDC | esx3-eu-spdc.cisco.com  | cnc41-worker-2 | poweredOn  | Network adapter 1 | up         | 
+----+-------------------+--------------+-------------+-------------------------+----------------+------------+-------------------+------------+
| LV | 00:50:56:B2:9D:19 | 10.58.239.54 | EU-SPDC-CDC | esx4-eu-spdc.cisco.com  | cnc50-worker-1 | poweredOn  | Network adapter 1 | up         | 
+----+-------------------+--------------+-------------+-------------------------+----------------+------------+-------------------+------------+
| V  | 00:50:56:B2:AC:65 |              | EU-SPDC-CDC | esx9-eu-spdc.cisco.com  | sr-cnc5-cdg    | poweredOn  | Network adapter 3 | up         | 
+----+-------------------+--------------+-------------+-------------------------+----------------+------------+-------------------+------------+
| LV | 00:50:56:B2:B0:B2 | 10.58.239.46 | EU-SPDC-CDC | esx5-eu-spdc.cisco.com  | cnc41-dg-2     | poweredOn  | Network adapter 1 | up         | 
|    |                   | 10.58.239.48 |             |                         |                |            |                   |            | 
+----+-------------------+--------------+-------------+-------------------------+----------------+------------+-------------------+------------+
| V  | 00:50:56:B2:B1:1D |              | EU-SPDC-CDC | esx5-eu-spdc.cisco.com  | cnc41-dg-2     | poweredOn  | Network adapter 2 | up         | 
+----+-------------------+--------------+-------------+-------------------------+----------------+------------+-------------------+------------+
| LV | 00:50:56:B2:B8:26 | 10.58.239.57 | EU-SPDC-CDC | esx4-eu-spdc.cisco.com  | cnc50-dg-1     | poweredOn  | Network adapter 1 | up         | 
|    |                   | 10.58.239.56 |             |                         |                |            |                   |            | 
+----+-------------------+--------------+-------------+-------------------------+----------------+------------+-------------------+------------+
| V  | 00:50:56:B2:BE:A0 |              | EU-SPDC-CDC | esx5-eu-spdc.cisco.com  | cnc41-dg-2     | poweredOn  | Network adapter 3 | up         | 
+----+-------------------+--------------+-------------+-------------------------+----------------+------------+-------------------+------------+
| LV | 00:50:56:B2:C3:17 | 10.58.239.51 | EU-SPDC-CDC | esx12-eu-spdc.cisco.com | cnc50-hybrid-1 | poweredOn  | Network adapter 1 | up         | 
|    |                   | 10.58.239.50 |             |                         |                |            |                   |            | 
+----+-------------------+--------------+-------------+-------------------------+----------------+------------+-------------------+------------+
| LV | 00:50:56:B2:CD:84 | 10.58.239.43 | EU-SPDC-CDC | esx10-eu-spdc.cisco.com | cnc41-hybrid-3 | poweredOn  | Network adapter 1 | up         | 
+----+-------------------+--------------+-------------+-------------------------+----------------+------------+-------------------+------------+
| V  | 00:50:56:B2:D1:41 |              | EU-SPDC-CDC | esx4-eu-spdc.cisco.com  | cnc50-dg-1     | poweredOn  | Network adapter 3 | up         | 
+----+-------------------+--------------+-------------+-------------------------+----------------+------------+-------------------+------------+
| LV | 00:50:56:B2:DB:D9 | 10.58.239.55 | EU-SPDC-CDC | esx7-eu-spdc.cisco.com  | cnc50-worker-2 | poweredOn  | Network adapter 1 | up         | 
+----+-------------------+--------------+-------------+-------------------------+----------------+------------+-------------------+------------+
| LV | 00:50:56:B2:DD:ED | 10.58.239.42 | EU-SPDC-CDC | esx6-eu-spdc.cisco.com  | cnc41-hybrid-2 | poweredOn  | Network adapter 1 | up         | 
+----+-------------------+--------------+-------------+-------------------------+----------------+------------+-------------------+------------+
| LV | 00:50:56:B2:F1:E8 | 10.58.239.44 | EU-SPDC-CDC | esx14-eu-spdc.cisco.com | cnc41-worker-1 | poweredOn  | Network adapter 1 | up         | 
+----+-------------------+--------------+-------------+-------------------------+----------------+------------+-------------------+------------+
| LV | 00:50:56:B2:F7:A1 | 10.58.239.52 | EU-SPDC-CDC | esx1-eu-spdc.cisco.com  | cnc50-hybrid-2 | poweredOn  | Network adapter 1 | up         | 
+----+-------------------+--------------+-------------+-------------------------+----------------+------------+-------------------+------------+
| V  | 00:50:56:B2:FA:79 |              | EU-SPDC-CDC | esx4-eu-spdc.cisco.com  | cnc50-dg-1     | poweredOn  | Network adapter 4 | up         | 
+----+-------------------+--------------+-------------+-------------------------+----------------+------------+-------------------+------------+
```

Developer

```
# iserver get aci ep --apic apic11 --vm *cnc* --view vm

{
    "duration": 3551,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 399,
        "disconnect_time": 0,
        "mo_time": 2163,
        "total_time": 2562
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

True	399	-	connect apic11o.emea-sp.cisco.com:443
True	684	360	apic11o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	523	666	apic11o.emea-sp.cisco.com:443 class compVm
True	655	1888	apic11o.emea-sp.cisco.com:443 class compVNic
True	301	68	apic11o.emea-sp.cisco.com:443 class compHv
```

[[Back]](./Endpoint.md)