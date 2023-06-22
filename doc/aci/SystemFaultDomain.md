# System Fault

## Filter by fault domain

Supported values
- any (default)
- access
- apps
- ext
- fw
- infra
- mgmt
- sec
- tenant

```
# iserver get aci system fault --apic apic21 --domain access

Apic: apic21 (mode:online, cache:off)

System Faults Summary [#4]
--------------------------

+----------+--------+----------------+-------+-------+-------------------------+---------------------------------------------------------------+
| Severity | Domain | Type           | Code  | Count | Cause                   | Explanation                                                   |
+----------+--------+----------------+-------+-------+-------------------------+---------------------------------------------------------------+
| critical | access | communications | F0532 | 16    | interface-physical-down | This fault occurs when a port is down and is in use for epg   | 
+----------+--------+----------------+-------+-------+-------------------------+---------------------------------------------------------------+
| major    | access | communications | F0475 | 2     | interface-tunnel-down   | This fault occurs when destination becomes unreachable.       | 
+----------+--------+----------------+-------+-------+-------------------------+---------------------------------------------------------------+
| major    | access | config         | F0600 | 2     | interface-pcmbr-down    | This fault occurs when port has been suspended.               | 
+----------+--------+----------------+-------+-------+-------------------------+---------------------------------------------------------------+
| minor    | access | communications | F0603 | 4     | interface-pcmbr-down    | This fault occurs when port becomes operationally individual. | 
+----------+--------+----------------+-------+-------+-------------------------+---------------------------------------------------------------+
```

Developer

```
# iserver get aci system fault --apic apic21 --domain access

{
    "duration": 1455,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 421,
        "disconnect_time": 0,
        "mo_time": 724,
        "total_time": 1145
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

True	421	-	connect apic21o.emea-sp.cisco.com:443
True	724	164	apic21o.emea-sp.cisco.com:443 class faultInst
```

[[Back]](./SystemFault.md)