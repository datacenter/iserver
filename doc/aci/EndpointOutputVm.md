# Endpoint

## VM specific output

```
# iserver get aci ep --apic apic11 --subnet 10.58.239.0/26 --view vm

Apic: apic11 (mode:online, cache:off)

+----+-------------------+--------------+-------------+-------------------------+----------------+-----------+-------------------+------------+
| SF | MAC Address       | IP Address   | VMM         | Hypervisor              | VM Name        | VM State  | vNIC Name         | vNIC State |
+----+-------------------+--------------+-------------+-------------------------+----------------+-----------+-------------------+------------+
| LV | 00:50:56:B2:1E:01 | 10.58.239.53 | EU-SPDC-CDC | esx10-eu-spdc.cisco.com | cnc50-hybrid-3 | poweredOn | Network adapter 1 | up         | 
+----+-------------------+--------------+-------------+-------------------------+----------------+-----------+-------------------+------------+
| LV | 00:50:56:B2:1E:4D | 10.58.239.41 | EU-SPDC-CDC | esx8-eu-spdc.cisco.com  | cnc41-hybrid-1 | poweredOn | Network adapter 1 | up         | 
|    |                   | 10.58.239.40 |             |                         |                |           |                   |            | 
+----+-------------------+--------------+-------------+-------------------------+----------------+-----------+-------------------+------------+
| LV | 00:50:56:B2:92:87 | 10.58.239.45 | EU-SPDC-CDC | esx3-eu-spdc.cisco.com  | cnc41-worker-2 | poweredOn | Network adapter 1 | up         | 
+----+-------------------+--------------+-------------+-------------------------+----------------+-----------+-------------------+------------+
| LV | 00:50:56:B2:9D:19 | 10.58.239.54 | EU-SPDC-CDC | esx4-eu-spdc.cisco.com  | cnc50-worker-1 | poweredOn | Network adapter 1 | up         | 
+----+-------------------+--------------+-------------+-------------------------+----------------+-----------+-------------------+------------+
| LV | 00:50:56:B2:B0:B2 | 10.58.239.46 | EU-SPDC-CDC | esx5-eu-spdc.cisco.com  | cnc41-dg-2     | poweredOn | Network adapter 1 | up         | 
|    |                   | 10.58.239.48 |             |                         |                |           |                   |            | 
+----+-------------------+--------------+-------------+-------------------------+----------------+-----------+-------------------+------------+
| LV | 00:50:56:B2:B8:26 | 10.58.239.57 | EU-SPDC-CDC | esx4-eu-spdc.cisco.com  | cnc50-dg-1     | poweredOn | Network adapter 1 | up         | 
|    |                   | 10.58.239.56 |             |                         |                |           |                   |            | 
+----+-------------------+--------------+-------------+-------------------------+----------------+-----------+-------------------+------------+
| LV | 00:50:56:B2:C3:17 | 10.58.239.51 | EU-SPDC-CDC | esx12-eu-spdc.cisco.com | cnc50-hybrid-1 | poweredOn | Network adapter 1 | up         | 
|    |                   | 10.58.239.50 |             |                         |                |           |                   |            | 
+----+-------------------+--------------+-------------+-------------------------+----------------+-----------+-------------------+------------+
| LV | 00:50:56:B2:CD:84 | 10.58.239.43 | EU-SPDC-CDC | esx10-eu-spdc.cisco.com | cnc41-hybrid-3 | poweredOn | Network adapter 1 | up         | 
+----+-------------------+--------------+-------------+-------------------------+----------------+-----------+-------------------+------------+
| LV | 00:50:56:B2:DB:D9 | 10.58.239.55 | EU-SPDC-CDC | esx7-eu-spdc.cisco.com  | cnc50-worker-2 | poweredOn | Network adapter 1 | up         | 
+----+-------------------+--------------+-------------+-------------------------+----------------+-----------+-------------------+------------+
| LV | 00:50:56:B2:DD:ED | 10.58.239.42 | EU-SPDC-CDC | esx6-eu-spdc.cisco.com  | cnc41-hybrid-2 | poweredOn | Network adapter 1 | up         | 
+----+-------------------+--------------+-------------+-------------------------+----------------+-----------+-------------------+------------+
| LV | 00:50:56:B2:F1:E8 | 10.58.239.44 | EU-SPDC-CDC | esx14-eu-spdc.cisco.com | cnc41-worker-1 | poweredOn | Network adapter 1 | up         | 
+----+-------------------+--------------+-------------+-------------------------+----------------+-----------+-------------------+------------+
| LV | 00:50:56:B2:F5:CE | 10.58.239.1  | EU-SPDC-CDC | esx2-eu-spdc.cisco.com  | 239-master     | poweredOn | Network adapter 1 | up         | 
+----+-------------------+--------------+-------------+-------------------------+----------------+-----------+-------------------+------------+
| LV | 00:50:56:B2:F7:A1 | 10.58.239.52 | EU-SPDC-CDC | esx1-eu-spdc.cisco.com  | cnc50-hybrid-2 | poweredOn | Network adapter 1 | up         | 
+----+-------------------+--------------+-------------+-------------------------+----------------+-----------+-------------------+------------+
```

Developer

```
# iserver get aci ep --apic apic11 --subnet 10.58.239.0/26 --view vm

{
    "duration": 4742,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 418,
        "disconnect_time": 0,
        "mo_time": 3320,
        "total_time": 3738
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

True	418	-	connect apic11o.emea-sp.cisco.com:443
True	813	209	apic11o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	1107	654	apic11o.emea-sp.cisco.com:443 class compVm
True	1080	1870	apic11o.emea-sp.cisco.com:443 class compVNic
True	320	68	apic11o.emea-sp.cisco.com:443 class compHv
```

[[Back]](./Endpoint.md)