# Endpoint

## Filter by bridge domain

```
# iserver get aci ep --apic apic11 --bd *sPBR-ASA*

Apic: apic11 (mode:online, cache:off)

+----+-------------------+------------+--------+-------------------------+-------------------------+
| SF | MAC Address       | IP Address | Tenant | BD                      | VRF                     |
+----+-------------------+------------+--------+-------------------------+-------------------------+
| V  | 00:50:56:B2:03:17 |            | MPC    | MPC/sPBR-ASA-OUT_BD     | MPC/MPC-sPBR-IN_VRF     | 
+----+-------------------+------------+--------+-------------------------+-------------------------+
| V  | 00:50:56:B2:04:77 |            | MPC    | MPC/sPBR-ASA-OUT_BD     | MPC/MPC-sPBR-IN_VRF     | 
+----+-------------------+------------+--------+-------------------------+-------------------------+
| V  | 00:50:56:B2:07:12 |            | MPC    | MPC/sPBR-ASA-IN_BD      | MPC/MPC-sPBR-IN_VRF     | 
+----+-------------------+------------+--------+-------------------------+-------------------------+
| V  | 00:50:56:B2:2A:04 |            | MPC    | MPC/sPBR-ASA-OUT_BD     | MPC/MPC-sPBR-IN_VRF     | 
+----+-------------------+------------+--------+-------------------------+-------------------------+
| LV | 00:50:56:B2:40:96 | 15.2.6.5   | MPC    | MPC/sPBR-ASA-IN_BD      | MPC/MPC-sPBR-IN_VRF     | 
+----+-------------------+------------+--------+-------------------------+-------------------------+
| V  | 00:50:56:B2:5E:5B |            | MPC    | MPC/sPBR-ASA-IN_BD      | MPC/MPC-sPBR-IN_VRF     | 
+----+-------------------+------------+--------+-------------------------+-------------------------+
| LV | 00:50:56:B2:63:E4 | 15.3.61.1  | MPC-E  | MPC-E/E-sPBR-ASA-OUT_BD | MPC-E/MPC-E-sPBR-IN_VRF | 
+----+-------------------+------------+--------+-------------------------+-------------------------+
| LV | 00:50:56:B2:8D:52 | 15.3.6.2   | MPC-E  | MPC-E/E-sPBR-ASA-IN_BD  | MPC-E/MPC-E-sPBR-IN_VRF | 
+----+-------------------+------------+--------+-------------------------+-------------------------+
| LV | 00:50:56:B2:9E:04 | 15.3.6.1   | MPC-E  | MPC-E/E-sPBR-ASA-IN_BD  | MPC-E/MPC-E-sPBR-IN_VRF | 
+----+-------------------+------------+--------+-------------------------+-------------------------+
| LV | 00:50:56:B2:9F:56 | 15.3.61.3  | MPC-E  | MPC-E/E-sPBR-ASA-OUT_BD | MPC-E/MPC-E-sPBR-IN_VRF | 
+----+-------------------+------------+--------+-------------------------+-------------------------+
| V  | 00:50:56:B2:A1:06 |            | MPC    | MPC/sPBR-ASA-OUT_BD     | MPC/MPC-sPBR-IN_VRF     | 
+----+-------------------+------------+--------+-------------------------+-------------------------+
| V  | 00:50:56:B2:A2:F7 |            | MPC    | MPC/sPBR-ASA-IN_BD      | MPC/MPC-sPBR-IN_VRF     | 
+----+-------------------+------------+--------+-------------------------+-------------------------+
| LV | 00:50:56:B2:B4:4F | 15.2.61.5  | MPC    | MPC/sPBR-ASA-OUT_BD     | MPC/MPC-sPBR-IN_VRF     | 
+----+-------------------+------------+--------+-------------------------+-------------------------+
| V  | 00:50:56:B2:BC:84 |            | MPC    | MPC/sPBR-ASA-OUT_BD     | MPC/MPC-sPBR-IN_VRF     | 
+----+-------------------+------------+--------+-------------------------+-------------------------+
| LV | 00:50:56:B2:C5:63 | 15.3.61.2  | MPC-E  | MPC-E/E-sPBR-ASA-OUT_BD | MPC-E/MPC-E-sPBR-IN_VRF | 
+----+-------------------+------------+--------+-------------------------+-------------------------+
| LV | 00:50:56:B2:C7:DD | 15.3.6.3   | MPC-E  | MPC-E/E-sPBR-ASA-IN_BD  | MPC-E/MPC-E-sPBR-IN_VRF | 
+----+-------------------+------------+--------+-------------------------+-------------------------+
| V  | 00:50:56:B2:DB:49 |            | MPC    | MPC/sPBR-ASA-IN_BD      | MPC/MPC-sPBR-IN_VRF     | 
+----+-------------------+------------+--------+-------------------------+-------------------------+
| V  | 00:50:56:B2:EC:C0 |            | MPC    | MPC/sPBR-ASA-IN_BD      | MPC/MPC-sPBR-IN_VRF     | 
+----+-------------------+------------+--------+-------------------------+-------------------------+
```

Developer

```
# iserver get aci ep --apic apic11 --bd *sPBR-ASA*

{
    "duration": 1372,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 432,
        "disconnect_time": 0,
        "mo_time": 586,
        "total_time": 1018
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

True	432	-	connect apic11o.emea-sp.cisco.com
True	586	193	apic11o.emea-sp.cisco.com class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
```

[[Back]](./Endpoint.md)