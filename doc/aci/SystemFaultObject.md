# System Fault

## Filter by fault affected object

```
# iserver get aci system fault
    --apic apic21
    --object *pod-1/node-2209*
    --view verbose

Apic: apic21 (mode:online, cache:off)

System Faults Details [#2]
--------------------------

+----------+--------+-------------+-------+--------------------------+------------------------------------+--------------------------------------------------------------+
| Severity | Domain | Type        | Code  | Cause                    | Object                             | Description                                                  |
+----------+--------+-------------+-------+--------------------------+------------------------------------+--------------------------------------------------------------+
| minor    | infra  | operational | F1700 | protocol-ntp-sync-failed | topology/pod-1/node-2209/sys/time/ | Ntp configuration on leaf cl2209-eu-spdc is Not Synchronized | 
|          |        |             |       |                          | fault-F1700                        |                                                              | 
+----------+--------+-------------+-------+--------------------------+------------------------------------+--------------------------------------------------------------+
| minor    | infra  | config      | F1295 | configuration-failed     | topology/pod-1/node-2209/local/    | Datetime Policy Configuration for default failed due to :    | 
|          |        |             |       |                          | svc-policyelem-id-0/uni/fabric/    | access-epp-is-not-available                                  | 
|          |        |             |       |                          | time-default/issues/fault-F1295    |                                                              | 
+----------+--------+-------------+-------+--------------------------+------------------------------------+--------------------------------------------------------------+
```

Developer

```
# iserver get aci system fault
    --apic apic21
    --object *pod-1/node-2209*
    --view verbose

{
    "duration": 1525,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 427,
        "disconnect_time": 0,
        "mo_time": 746,
        "total_time": 1173
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

True	427	-	connect apic21o.emea-sp.cisco.com:443
True	746	164	apic21o.emea-sp.cisco.com:443 class faultInst
```

[[Back]](./SystemFault.md)