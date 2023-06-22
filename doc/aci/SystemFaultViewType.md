# System Fault

## Fault counts by type view

```
# iserver get aci system fault --apic apic21 --view type

Apic: apic21 (mode:online, cache:off)

System Fault Counts by Type
---------------------------

+----------------+----------+-------+-------+---------+
| Type           | Critical | Major | Minor | Warning |
+----------------+----------+-------+-------+---------+
| Environmental  | 0        | 0     | 0     | 0       | 
+----------------+----------+-------+-------+---------+
| Communications | 16       | 19    | 4     | 0       | 
+----------------+----------+-------+-------+---------+
| Config         | 0        | 7     | 23    | 3       | 
+----------------+----------+-------+-------+---------+
| Operational    | 0        | 21    | 4     | 64      | 
+----------------+----------+-------+-------+---------+
| Total          | 16       | 47    | 31    | 67      | 
+----------------+----------+-------+-------+---------+
```

Developer

```
# iserver get aci system fault --apic apic21 --view type

{
    "duration": 1568,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 448,
        "disconnect_time": 0,
        "mo_time": 828,
        "total_time": 1276
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

True	448	-	connect apic21o.emea-sp.cisco.com:443
True	828	163	apic21o.emea-sp.cisco.com:443 class faultInst
```

[[Back]](./SystemFault.md)