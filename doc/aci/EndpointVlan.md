# Endpoint

## Filter by encapsulation vlan

Supported vlan filtering options by example:
- --vlan 1234
- --vlan lt4000
- --vlan 3200-3300

```
# iserver get aci ep --apic apic11 --vlan 100-120

Apic: apic11 (mode:online, cache:off)

+----+-------------------+--------------+--------+------------+------------------+-------+----------------------------+----------------------+
| SF | MAC Address       | IP Address   | Tenant | AP         | EPG              | Encap | BD                         | VRF                  |
+----+-------------------+--------------+--------+------------+------------------+-------+----------------------------+----------------------+
| L  | 0E:C0:8C:71:9C:37 |              | cvim1a | cvim1a_ANP | cvim1a-MX-mgmt   | 112   | cvim1a/cvim1a-MX-mgmt_BD   | cvim1a/cvim1a_VRF    | 
+----+-------------------+--------------+--------+------------+------------------+-------+----------------------------+----------------------+
| L  | 16:F7:75:93:E4:25 |              | cvim1a | cvim1a_ANP | cvim1a-MX-mgmt   | 112   | cvim1a/cvim1a-MX-mgmt_BD   | cvim1a/cvim1a_VRF    | 
+----+-------------------+--------------+--------+------------+------------------+-------+----------------------------+----------------------+
| L  | 3A:18:2E:51:59:0E | 10.58.28.113 | cvim1a | cvim1a_ANP | cvim1a-OS-API    | 111   | cvim1a/cvim1a-A-OS-API_BD  | common/Infra_BGP_VRF | 
+----+-------------------+--------------+--------+------------+------------------+-------+----------------------------+----------------------+
| L  | 3C:FD:FE:CB:ED:70 |              | cvim1a | cvim1a_ANP | cvim1a-MX-mgmt   | 112   | cvim1a/cvim1a-MX-mgmt_BD   | cvim1a/cvim1a_VRF    | 
+----+-------------------+--------------+--------+------------+------------------+-------+----------------------------+----------------------+
| L  | 3C:FD:FE:CB:F5:B0 |              | cvim1a | cvim1a_ANP | cvim1a-MX-mgmt   | 112   | cvim1a/cvim1a-MX-mgmt_BD   | cvim1a/cvim1a_VRF    | 
+----+-------------------+--------------+--------+------------+------------------+-------+----------------------------+----------------------+
| L  | 3C:FD:FE:CB:F5:B0 |              | cvim1a | cvim1a_ANP | cvim1a-S-storage | 117   | cvim1a/cvim1a-S-storage_BD | cvim1a/cvim1a_VRF    | 
+----+-------------------+--------------+--------+------------+------------------+-------+----------------------------+----------------------+
| L  | 3C:FD:FE:CE:0E:40 |              | cvim1a | cvim1a_ANP | cvim1a-MX-mgmt   | 112   | cvim1a/cvim1a-MX-mgmt_BD   | cvim1a/cvim1a_VRF    | 
+----+-------------------+--------------+--------+------------+------------------+-------+----------------------------+----------------------+
| L  | 3C:FD:FE:CE:13:A8 |              | cvim1a | cvim1a_ANP | cvim1a-MX-mgmt   | 112   | cvim1a/cvim1a-MX-mgmt_BD   | cvim1a/cvim1a_VRF    | 
+----+-------------------+--------------+--------+------------+------------------+-------+----------------------------+----------------------+
| L  | 3C:FD:FE:CE:13:A8 |              | cvim1a | cvim1a_ANP | cvim1a-S-storage | 117   | cvim1a/cvim1a-S-storage_BD | cvim1a/cvim1a_VRF    | 
+----+-------------------+--------------+--------+------------+------------------+-------+----------------------------+----------------------+
| L  | 3C:FD:FE:CE:16:40 |              | cvim1a | cvim1a_ANP | cvim1a-MX-mgmt   | 112   | cvim1a/cvim1a-MX-mgmt_BD   | cvim1a/cvim1a_VRF    | 
+----+-------------------+--------------+--------+------------+------------------+-------+----------------------------+----------------------+
| L  | 3C:FD:FE:CE:16:40 |              | cvim1a | cvim1a_ANP | cvim1a-S-storage | 117   | cvim1a/cvim1a-S-storage_BD | cvim1a/cvim1a_VRF    | 
+----+-------------------+--------------+--------+------------+------------------+-------+----------------------------+----------------------+
| L  | 3C:FD:FE:CE:1A:60 |              | cvim1a | cvim1a_ANP | cvim1a-MX-mgmt   | 112   | cvim1a/cvim1a-MX-mgmt_BD   | cvim1a/cvim1a_VRF    | 
+----+-------------------+--------------+--------+------------+------------------+-------+----------------------------+----------------------+
| L  | BA:C0:2F:42:D2:FC |              | cvim1a | cvim1a_ANP | cvim1a-MX-mgmt   | 112   | cvim1a/cvim1a-MX-mgmt_BD   | cvim1a/cvim1a_VRF    | 
+----+-------------------+--------------+--------+------------+------------------+-------+----------------------------+----------------------+
| L  | CE:40:47:FF:F0:17 |              | cvim1a | cvim1a_ANP | cvim1a-MX-mgmt   | 112   | cvim1a/cvim1a-MX-mgmt_BD   | cvim1a/cvim1a_VRF    | 
+----+-------------------+--------------+--------+------------+------------------+-------+----------------------------+----------------------+
```

Developer

```
# iserver get aci ep --apic apic11 --vlan 100-120

{
    "duration": 1335,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 410,
        "disconnect_time": 0,
        "mo_time": 768,
        "total_time": 1178
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

True	410	-	connect apic11o.emea-sp.cisco.com:443
True	768	209	apic11o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
```

[[Back]](./Endpoint.md)