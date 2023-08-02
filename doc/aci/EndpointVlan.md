# Endpoint

## Filter by encapsulation vlan

Supported vlan filtering options by example:
- --vlan 1234
- --vlan lt4000
- --vlan 3200-3300

```
# iserver get aci ep --apic apic11 --vlan 100-120

Apic: apic11 (mode:online, cache:off)

+----+-------------------+--------------+------------------------------------+-------+----------------------------+----------------------+
| SF | MAC Address       | IP Address   | EPG                                | Encap | BD                         | VRF                  |
+----+-------------------+--------------+------------------------------------+-------+----------------------------+----------------------+
| L  | 26:CB:8E:E0:72:BD |              | cvim1a/cvim1a_ANP/cvim1a-MX-mgmt   | 112   | cvim1a/cvim1a-MX-mgmt_BD   | cvim1a/cvim1a_VRF    | 
+----+-------------------+--------------+------------------------------------+-------+----------------------------+----------------------+
| L  | 3A:A6:D5:0D:28:94 |              | cvim1a/cvim1a_ANP/cvim1a-MX-mgmt   | 112   | cvim1a/cvim1a-MX-mgmt_BD   | cvim1a/cvim1a_VRF    | 
+----+-------------------+--------------+------------------------------------+-------+----------------------------+----------------------+
| L  | 3C:FD:FE:CB:ED:70 |              | cvim1a/cvim1a_ANP/cvim1a-MX-mgmt   | 112   | cvim1a/cvim1a-MX-mgmt_BD   | cvim1a/cvim1a_VRF    | 
+----+-------------------+--------------+------------------------------------+-------+----------------------------+----------------------+
| L  | 3C:FD:FE:CB:F5:B0 |              | cvim1a/cvim1a_ANP/cvim1a-S-storage | 117   | cvim1a/cvim1a-S-storage_BD | cvim1a/cvim1a_VRF    | 
+----+-------------------+--------------+------------------------------------+-------+----------------------------+----------------------+
| L  | 3C:FD:FE:CB:F5:B0 |              | cvim1a/cvim1a_ANP/cvim1a-MX-mgmt   | 112   | cvim1a/cvim1a-MX-mgmt_BD   | cvim1a/cvim1a_VRF    | 
+----+-------------------+--------------+------------------------------------+-------+----------------------------+----------------------+
| L  | 3C:FD:FE:CE:0E:40 |              | cvim1a/cvim1a_ANP/cvim1a-MX-mgmt   | 112   | cvim1a/cvim1a-MX-mgmt_BD   | cvim1a/cvim1a_VRF    | 
+----+-------------------+--------------+------------------------------------+-------+----------------------------+----------------------+
| L  | 3C:FD:FE:CE:13:A8 |              | cvim1a/cvim1a_ANP/cvim1a-MX-mgmt   | 112   | cvim1a/cvim1a-MX-mgmt_BD   | cvim1a/cvim1a_VRF    | 
+----+-------------------+--------------+------------------------------------+-------+----------------------------+----------------------+
| L  | 3C:FD:FE:CE:13:A8 |              | cvim1a/cvim1a_ANP/cvim1a-S-storage | 117   | cvim1a/cvim1a-S-storage_BD | cvim1a/cvim1a_VRF    | 
+----+-------------------+--------------+------------------------------------+-------+----------------------------+----------------------+
| L  | 3C:FD:FE:CE:16:40 |              | cvim1a/cvim1a_ANP/cvim1a-MX-mgmt   | 112   | cvim1a/cvim1a-MX-mgmt_BD   | cvim1a/cvim1a_VRF    | 
+----+-------------------+--------------+------------------------------------+-------+----------------------------+----------------------+
| L  | 3C:FD:FE:CE:16:40 |              | cvim1a/cvim1a_ANP/cvim1a-S-storage | 117   | cvim1a/cvim1a-S-storage_BD | cvim1a/cvim1a_VRF    | 
+----+-------------------+--------------+------------------------------------+-------+----------------------------+----------------------+
| L  | 3C:FD:FE:CE:1A:60 |              | cvim1a/cvim1a_ANP/cvim1a-MX-mgmt   | 112   | cvim1a/cvim1a-MX-mgmt_BD   | cvim1a/cvim1a_VRF    | 
+----+-------------------+--------------+------------------------------------+-------+----------------------------+----------------------+
| L  | A6:8F:A3:2F:34:BE |              | cvim1a/cvim1a_ANP/cvim1a-MX-mgmt   | 112   | cvim1a/cvim1a-MX-mgmt_BD   | cvim1a/cvim1a_VRF    | 
+----+-------------------+--------------+------------------------------------+-------+----------------------------+----------------------+
| L  | DA:70:BA:22:DC:72 | 10.58.28.113 | cvim1a/cvim1a_ANP/cvim1a-OS-API    | 111   | cvim1a/cvim1a-A-OS-API_BD  | common/Infra_BGP_VRF | 
+----+-------------------+--------------+------------------------------------+-------+----------------------------+----------------------+
| L  | F6:FA:93:3B:2C:06 |              | cvim1a/cvim1a_ANP/cvim1a-MX-mgmt   | 112   | cvim1a/cvim1a-MX-mgmt_BD   | cvim1a/cvim1a_VRF    | 
+----+-------------------+--------------+------------------------------------+-------+----------------------------+----------------------+
| L  | FA:16:3E:C1:37:01 | 10.58.28.81  | cvim1a/cvim1a_ANP/cvim1a-ExtIP     | 113   | cvim1a/cvim1a-ExtIP_BD     | common/Infra_BGP_VRF | 
|    |                   | 10.58.28.85  |                                    |       |                            |                      | 
|    |                   | 10.58.28.84  |                                    |       |                            |                      | 
|    |                   | 10.58.28.83  |                                    |       |                            |                      | 
|    |                   | 10.58.28.82  |                                    |       |                            |                      | 
+----+-------------------+--------------+------------------------------------+-------+----------------------------+----------------------+
```

Developer

```
# iserver get aci ep --apic apic11 --vlan 100-120

{
    "duration": 1364,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 399,
        "disconnect_time": 0,
        "mo_time": 716,
        "total_time": 1115
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
True	716	360	apic11o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
```

[[Back]](./Endpoint.md)