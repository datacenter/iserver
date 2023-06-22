# System Fault

## Filter by fault type

Supported values
- any (default)
- env
- comm
- config
- oper

```
# iserver get aci system fault --apic apic21 --type config

Apic: apic21 (mode:online, cache:off)

System Faults Summary [#11]
---------------------------

+----------+----------+--------+---------+-------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| Severity | Domain   | Type   | Code    | Count | Cause                           | Explanation                                                                                                           |
+----------+----------+--------+---------+-------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| major    | external | config | F4222   | 1     | rum-ack-not-received            | F4222                                                                                                                 | 
+----------+----------+--------+---------+-------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| major    | infra    | config | F610395 | 3     | fsm-failed                      | F610395                                                                                                               | 
+----------+----------+--------+---------+-------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| major    | infra    | config | F609423 | 1     | fsm-failed                      | None set.                                                                                                             | 
+----------+----------+--------+---------+-------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| major    | access   | config | F0600   | 2     | interface-pcmbr-down            | This fault occurs when port has been suspended.                                                                       | 
+----------+----------+--------+---------+-------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| minor    | tenant   | config | F1298   | 2     | configuration-failed            | : This fault occurs when deliverying EPg policies to a node has failed                                                | 
+----------+----------+--------+---------+-------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| minor    | tenant   | config | F0467   | 17    | configuration-failed            | This fault occurs when an End Point Group is incompletely or incorrectly configured.                                  | 
+----------+----------+--------+---------+-------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| minor    | infra    | config | F0849   | 2     | configuration-failed            | This fault occurs when a infra selector (port selector, card selector, node selector etc.) is incorrectly configured. | 
+----------+----------+--------+---------+-------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| minor    | infra    | config | F1295   | 2     | configuration-failed            | This fault is raised when a Date and Time Policy (datetime:Pol) fails to apply due to configuration issues.           | 
+----------+----------+--------+---------+-------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| warning  | external | config | F3057   | 1     | network-settings-not-configured | This fault is raised when APIC Controller product is not registered with Cisco Smart Software Manager (CSSM).         | 
+----------+----------+--------+---------+-------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| warning  | infra    | config | F0882   | 1     | resolution-failed               | The object refers to an object that was not found.                                                                    | 
+----------+----------+--------+---------+-------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| warning  | infra    | config | F1665   | 1     | resolution-failed               | The object refers to an object that was not found.                                                                    | 
+----------+----------+--------+---------+-------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci system fault --apic apic21 --type config

{
    "duration": 1850,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 496,
        "disconnect_time": 0,
        "mo_time": 833,
        "total_time": 1329
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

True	496	-	connect apic21o.emea-sp.cisco.com:443
True	833	164	apic21o.emea-sp.cisco.com:443 class faultInst
```

[[Back]](./SystemFault.md)