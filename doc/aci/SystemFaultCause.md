# System Fault

## Filter by fault cause

```
# iserver get aci system fault --apic apic21 --cause *configuration*

Apic: apic21 (mode:online, cache:off)

System Faults Summary [#4]
--------------------------

+----------+--------+--------+-------+-------+----------------------+-----------------------------------------------------------------------------------------------------------------------+
| Severity | Domain | Type   | Code  | Count | Cause                | Explanation                                                                                                           |
+----------+--------+--------+-------+-------+----------------------+-----------------------------------------------------------------------------------------------------------------------+
| minor    | tenant | config | F1298 | 2     | configuration-failed | : This fault occurs when deliverying EPg policies to a node has failed                                                | 
+----------+--------+--------+-------+-------+----------------------+-----------------------------------------------------------------------------------------------------------------------+
| minor    | tenant | config | F0467 | 17    | configuration-failed | This fault occurs when an End Point Group is incompletely or incorrectly configured.                                  | 
+----------+--------+--------+-------+-------+----------------------+-----------------------------------------------------------------------------------------------------------------------+
| minor    | infra  | config | F0849 | 2     | configuration-failed | This fault occurs when a infra selector (port selector, card selector, node selector etc.) is incorrectly configured. | 
+----------+--------+--------+-------+-------+----------------------+-----------------------------------------------------------------------------------------------------------------------+
| minor    | infra  | config | F1295 | 2     | configuration-failed | This fault is raised when a Date and Time Policy (datetime:Pol) fails to apply due to configuration issues.           | 
+----------+--------+--------+-------+-------+----------------------+-----------------------------------------------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci system fault --apic apic21 --cause *configuration*

{
    "duration": 1914,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 493,
        "disconnect_time": 0,
        "mo_time": 1044,
        "total_time": 1537
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

True	493	-	connect apic21o.emea-sp.cisco.com:443
True	1044	164	apic21o.emea-sp.cisco.com:443 class faultInst
```

[[Back]](./SystemFault.md)