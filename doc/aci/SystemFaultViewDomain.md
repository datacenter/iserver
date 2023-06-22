# System Fault

## Fault counts by domain view

```
# iserver get aci system fault --apic apic21 --view domain

Apic: apic21 (mode:online, cache:off)

System Fault Counts by Domain
-----------------------------

+------------+----------+-------+-------+---------+
| Domain     | Critical | Major | Minor | Warning |
+------------+----------+-------+-------+---------+
| Access     | 16       | 4     | 4     | 0       | 
+------------+----------+-------+-------+---------+
| Apps       | 0        | 0     | 0     | 0       | 
+------------+----------+-------+-------+---------+
| External   | 0        | 18    | 0     | 57      | 
+------------+----------+-------+-------+---------+
| Framework  | 0        | 1     | 0     | 0       | 
+------------+----------+-------+-------+---------+
| Infra      | 0        | 24    | 8     | 10      | 
+------------+----------+-------+-------+---------+
| Management | 0        | 0     | 0     | 0       | 
+------------+----------+-------+-------+---------+
| Security   | 0        | 0     | 0     | 0       | 
+------------+----------+-------+-------+---------+
| Tenant     | 0        | 0     | 19    | 0       | 
+------------+----------+-------+-------+---------+
| Total      | 16       | 47    | 31    | 67      | 
+------------+----------+-------+-------+---------+
```

Developer

```
# iserver get aci system fault --apic apic21 --view domain

{
    "duration": 1602,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 459,
        "disconnect_time": 0,
        "mo_time": 712,
        "total_time": 1171
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

True	459	-	connect apic21o.emea-sp.cisco.com:443
True	712	164	apic21o.emea-sp.cisco.com:443 class faultInst
```

[[Back]](./SystemFault.md)