# System Fault

## Filter by fault code

Supported values
- integer-based: gt, ge, lt, le, start-end
- string-based: strich match or any substring

Example: range of values

```
# iserver get aci system fault --apic apic21 --code 250-1000

Apic: apic21 (mode:online, cache:off)

System Faults Summary [#8]
--------------------------

+----------+----------+----------------+-------+-------+-----------------------------+-----------------------------------------------------------------------------------------------------------------------+
| Severity | Domain   | Type           | Code  | Count | Cause                       | Explanation                                                                                                           |
+----------+----------+----------------+-------+-------+-----------------------------+-----------------------------------------------------------------------------------------------------------------------+
| critical | access   | communications | F0532 | 16    | interface-physical-down     | This fault occurs when a port is down and is in use for epg                                                           | 
+----------+----------+----------------+-------+-------+-----------------------------+-----------------------------------------------------------------------------------------------------------------------+
| major    | access   | communications | F0475 | 2     | interface-tunnel-down       | This fault occurs when destination becomes unreachable.                                                               | 
+----------+----------+----------------+-------+-------+-----------------------------+-----------------------------------------------------------------------------------------------------------------------+
| major    | access   | config         | F0600 | 2     | interface-pcmbr-down        | This fault occurs when port has been suspended.                                                                       | 
+----------+----------+----------------+-------+-------+-----------------------------+-----------------------------------------------------------------------------------------------------------------------+
| minor    | access   | communications | F0603 | 4     | interface-pcmbr-down        | This fault occurs when port becomes operationally individual.                                                         | 
+----------+----------+----------------+-------+-------+-----------------------------+-----------------------------------------------------------------------------------------------------------------------+
| minor    | tenant   | config         | F0467 | 17    | configuration-failed        | This fault occurs when an End Point Group is incompletely or incorrectly configured.                                  | 
+----------+----------+----------------+-------+-------+-----------------------------+-----------------------------------------------------------------------------------------------------------------------+
| minor    | infra    | config         | F0849 | 2     | configuration-failed        | This fault occurs when a infra selector (port selector, card selector, node selector etc.) is incorrectly configured. | 
+----------+----------+----------------+-------+-------+-----------------------------+-----------------------------------------------------------------------------------------------------------------------+
| warning  | external | operational    | F0299 | 56    | protocol-bgp-adjacency-down | This fault occurs when the peer state is not established                                                              | 
+----------+----------+----------------+-------+-------+-----------------------------+-----------------------------------------------------------------------------------------------------------------------+
| warning  | infra    | config         | F0882 | 1     | resolution-failed           | The object refers to an object that was not found.                                                                    | 
+----------+----------+----------------+-------+-------+-----------------------------+-----------------------------------------------------------------------------------------------------------------------+
```

Example: string match

```
# iserver get aci system fault --apic apic21 --code f029*

Apic: apic21 (mode:online, cache:off)

System Faults Summary [#1]
--------------------------

+----------+----------+-------------+-------+-------+-----------------------------+----------------------------------------------------------+
| Severity | Domain   | Type        | Code  | Count | Cause                       | Explanation                                              |
+----------+----------+-------------+-------+-------+-----------------------------+----------------------------------------------------------+
| warning  | external | operational | F0299 | 56    | protocol-bgp-adjacency-down | This fault occurs when the peer state is not established | 
+----------+----------+-------------+-------+-------+-----------------------------+----------------------------------------------------------+
```

Developer

```
# iserver get aci system fault --apic apic21 --code 250-1000

{
    "duration": 1613,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 399,
        "disconnect_time": 0,
        "mo_time": 967,
        "total_time": 1366
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

True	399	-	connect apic21o.emea-sp.cisco.com:443
True	967	164	apic21o.emea-sp.cisco.com:443 class faultInst
```

[[Back]](./SystemFault.md)