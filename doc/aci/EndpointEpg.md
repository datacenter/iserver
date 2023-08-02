# Endpoint

## Filter by epg

```
# iserver get aci ep --apic apic11 --epg *MX*

Apic: apic11 (mode:online, cache:off)

+----+-------------------+----------------+----------------------------------+-------+--------------------------+-------------------+
| SF | MAC Address       | IP Address     | EPG                              | Encap | BD                       | VRF               |
+----+-------------------+----------------+----------------------------------+-------+--------------------------+-------------------+
| L  | 26:CB:8E:E0:72:BD |                | cvim1a/cvim1a_ANP/cvim1a-MX-mgmt | 112   | cvim1a/cvim1a-MX-mgmt_BD | cvim1a/cvim1a_VRF | 
+----+-------------------+----------------+----------------------------------+-------+--------------------------+-------------------+
| L  | 3A:A6:D5:0D:28:94 |                | cvim1a/cvim1a_ANP/cvim1a-MX-mgmt | 112   | cvim1a/cvim1a-MX-mgmt_BD | cvim1a/cvim1a_VRF | 
+----+-------------------+----------------+----------------------------------+-------+--------------------------+-------------------+
| L  | 3C:FD:FE:CB:ED:70 |                | cvim1a/cvim1a_ANP/cvim1a-MX-mgmt | 112   | cvim1a/cvim1a-MX-mgmt_BD | cvim1a/cvim1a_VRF | 
+----+-------------------+----------------+----------------------------------+-------+--------------------------+-------------------+
| L  | 3C:FD:FE:CB:F5:18 | 192.168.152.14 | cvim4a/cvim4a_ANP/cvim4a-MX-mgmt | 152   | cvim4a/cvim4a-MX-mgmt_BD | cvim4a/cvim4a_VRF | 
+----+-------------------+----------------+----------------------------------+-------+--------------------------+-------------------+
| L  | 3C:FD:FE:CB:F5:B0 |                | cvim1a/cvim1a_ANP/cvim1a-MX-mgmt | 112   | cvim1a/cvim1a-MX-mgmt_BD | cvim1a/cvim1a_VRF | 
+----+-------------------+----------------+----------------------------------+-------+--------------------------+-------------------+
| L  | 3C:FD:FE:CE:0E:40 |                | cvim1a/cvim1a_ANP/cvim1a-MX-mgmt | 112   | cvim1a/cvim1a-MX-mgmt_BD | cvim1a/cvim1a_VRF | 
+----+-------------------+----------------+----------------------------------+-------+--------------------------+-------------------+
| L  | 3C:FD:FE:CE:13:A8 |                | cvim1a/cvim1a_ANP/cvim1a-MX-mgmt | 112   | cvim1a/cvim1a-MX-mgmt_BD | cvim1a/cvim1a_VRF | 
+----+-------------------+----------------+----------------------------------+-------+--------------------------+-------------------+
| L  | 3C:FD:FE:CE:16:40 |                | cvim1a/cvim1a_ANP/cvim1a-MX-mgmt | 112   | cvim1a/cvim1a-MX-mgmt_BD | cvim1a/cvim1a_VRF | 
+----+-------------------+----------------+----------------------------------+-------+--------------------------+-------------------+
| L  | 3C:FD:FE:CE:1A:60 |                | cvim1a/cvim1a_ANP/cvim1a-MX-mgmt | 112   | cvim1a/cvim1a-MX-mgmt_BD | cvim1a/cvim1a_VRF | 
+----+-------------------+----------------+----------------------------------+-------+--------------------------+-------------------+
| L  | 3C:FD:FE:CE:C4:28 | 192.168.152.15 | cvim4a/cvim4a_ANP/cvim4a-MX-mgmt | 152   | cvim4a/cvim4a-MX-mgmt_BD | cvim4a/cvim4a_VRF | 
+----+-------------------+----------------+----------------------------------+-------+--------------------------+-------------------+
| L  | 3C:FD:FE:EF:6F:48 | 192.168.152.1  | cvim4a/cvim4a_ANP/cvim4a-MX-mgmt | 152   | cvim4a/cvim4a-MX-mgmt_BD | cvim4a/cvim4a_VRF | 
+----+-------------------+----------------+----------------------------------+-------+--------------------------+-------------------+
| L  | 3C:FD:FE:F0:15:10 | 192.168.152.12 | cvim4a/cvim4a_ANP/cvim4a-MX-mgmt | 152   | cvim4a/cvim4a-MX-mgmt_BD | cvim4a/cvim4a_VRF | 
+----+-------------------+----------------+----------------------------------+-------+--------------------------+-------------------+
| L  | 3C:FD:FE:F0:15:68 | 192.168.152.10 | cvim4a/cvim4a_ANP/cvim4a-MX-mgmt | 152   | cvim4a/cvim4a-MX-mgmt_BD | cvim4a/cvim4a_VRF | 
+----+-------------------+----------------+----------------------------------+-------+--------------------------+-------------------+
| L  | 40:A6:B7:08:FC:20 | 192.168.152.13 | cvim4a/cvim4a_ANP/cvim4a-MX-mgmt | 152   | cvim4a/cvim4a-MX-mgmt_BD | cvim4a/cvim4a_VRF | 
+----+-------------------+----------------+----------------------------------+-------+--------------------------+-------------------+
| L  | 40:A6:B7:08:FC:28 | 192.168.152.11 | cvim4a/cvim4a_ANP/cvim4a-MX-mgmt | 152   | cvim4a/cvim4a-MX-mgmt_BD | cvim4a/cvim4a_VRF | 
+----+-------------------+----------------+----------------------------------+-------+--------------------------+-------------------+
| L  | 86:00:31:CE:C2:E6 |                | cvim4a/cvim4a_ANP/cvim4a-MX-mgmt | 152   | cvim4a/cvim4a-MX-mgmt_BD | cvim4a/cvim4a_VRF | 
+----+-------------------+----------------+----------------------------------+-------+--------------------------+-------------------+
| L  | A6:8F:A3:2F:34:BE |                | cvim1a/cvim1a_ANP/cvim1a-MX-mgmt | 112   | cvim1a/cvim1a-MX-mgmt_BD | cvim1a/cvim1a_VRF | 
+----+-------------------+----------------+----------------------------------+-------+--------------------------+-------------------+
| L  | D2:DC:38:24:D7:9A |                | cvim4a/cvim4a_ANP/cvim4a-MX-mgmt | 152   | cvim4a/cvim4a-MX-mgmt_BD | cvim4a/cvim4a_VRF | 
+----+-------------------+----------------+----------------------------------+-------+--------------------------+-------------------+
| L  | F2:81:48:54:03:85 | 192.168.152.2  | cvim4a/cvim4a_ANP/cvim4a-MX-mgmt | 152   | cvim4a/cvim4a-MX-mgmt_BD | cvim4a/cvim4a_VRF | 
+----+-------------------+----------------+----------------------------------+-------+--------------------------+-------------------+
| L  | F6:FA:93:3B:2C:06 |                | cvim1a/cvim1a_ANP/cvim1a-MX-mgmt | 112   | cvim1a/cvim1a-MX-mgmt_BD | cvim1a/cvim1a_VRF | 
+----+-------------------+----------------+----------------------------------+-------+--------------------------+-------------------+
```

Developer

```
# iserver get aci ep --apic apic11 --epg *MX*

{
    "duration": 1379,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 384,
        "disconnect_time": 0,
        "mo_time": 777,
        "total_time": 1161
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
True	777	360	apic11o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
```

[[Back]](./Endpoint.md)