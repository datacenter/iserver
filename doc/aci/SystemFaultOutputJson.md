# System Fault

## JSON output

```
# iserver get aci system fault --apic apic21 --desc *datetime* --view verbose

[
    {
        "__Output": {
            "severity": "Yellow"
        },
        "ack": "no",
        "alert": "no",
        "cause": "configuration-failed",
        "changeSet": "configQual:access-epp-is-not-available, configSt:failed-to-apply",
        "childAction": "",
        "code": "F1295",
        "created": "2023-06-18T09:45:32.177+02:00",
        "delegated": "yes",
        "descr": "Datetime Policy Configuration for default  failed due to : access-epp-is-not-available",
        "dn": "topology/pod-1/node-2209/local/svc-policyelem-id-0/uni/fabric/time-default/issues/fault-F1295",
        "domain": "infra",
        "highestSeverity": "minor",
        "lastTransition": "2023-06-18T09:47:47.778+02:00",
        "lc": "raised",
        "occur": "1",
        "origSeverity": "minor",
        "prevSeverity": "minor",
        "rule": "datetime-conf-issues-config-failed",
        "severity": "minor",
        "status": "",
        "subject": "management",
        "title": "",
        "type": "config",
        "codeInt": 1295,
        "codeT": "This fault is raised when a Date and Time Policy (datetime:Pol) fails to apply due to configuration issues.",
        "count": 1,
        "severityT": "Min",
        "descrT": [
            "Datetime Policy Configuration for default failed due to : ",
            "access-epp-is-not-available"
        ],
        "dnT": [
            "topology/pod-1/node-2209/local/",
            "svc-policyelem-id-0/uni/fabric/",
            "time-default/issues/fault-F1295"
        ]
    },
    {
        "__Output": {
            "severity": "Yellow"
        },
        "ack": "no",
        "alert": "no",
        "cause": "configuration-failed",
        "changeSet": "configQual:access-epp-is-not-available, configSt:failed-to-apply",
        "childAction": "",
        "code": "F1295",
        "created": "2023-06-18T09:19:04.553+02:00",
        "delegated": "yes",
        "descr": "Datetime Policy Configuration for default  failed due to : access-epp-is-not-available",
        "dn": "topology/pod-1/node-2210/local/svc-policyelem-id-0/uni/fabric/time-default/issues/fault-F1295",
        "domain": "infra",
        "highestSeverity": "minor",
        "lastTransition": "2023-06-18T09:21:08.257+02:00",
        "lc": "raised",
        "occur": "1",
        "origSeverity": "minor",
        "prevSeverity": "minor",
        "rule": "datetime-conf-issues-config-failed",
        "severity": "minor",
        "status": "",
        "subject": "management",
        "title": "",
        "type": "config",
        "codeInt": 1295,
        "codeT": "This fault is raised when a Date and Time Policy (datetime:Pol) fails to apply due to configuration issues.",
        "count": 1,
        "severityT": "Min",
        "descrT": [
            "Datetime Policy Configuration for default failed due to : ",
            "access-epp-is-not-available"
        ],
        "dnT": [
            "topology/pod-1/node-2210/local/",
            "svc-policyelem-id-0/uni/fabric/",
            "time-default/issues/fault-F1295"
        ]
    }
]
```

Developer

```
# iserver get aci system fault --apic apic21 --desc *datetime* --view verbose

{
    "duration": 1638,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 486,
        "disconnect_time": 0,
        "mo_time": 768,
        "total_time": 1254
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

True	486	-	connect apic21o.emea-sp.cisco.com:443
True	768	164	apic21o.emea-sp.cisco.com:443 class faultInst
```

[[Back]](./SystemFault.md)