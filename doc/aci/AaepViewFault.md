# Attachable Access Entity Profile (AAEP)

## Fault view

```
# iserver get aci aaep --apic apic11 --view fault

Apic: apic11 (mode:online, cache:off)

Attachable Access Entity Profile (AAEP) - Faults [#4]
-----------------------------------------------------

+---------------+------+-------+-------------------+-------------------------------+-----------+---------------------------------------------------------------------------------+
| Name          | Sev  | Code  | Cause             | Created Time                  | Lifecycle | Description                                                                     |
+---------------+------+-------+-------------------+-------------------------------+-----------+---------------------------------------------------------------------------------+
| DC-CFP-AEP    | Warn | F1003 | resolution-failed | 2023-06-12T10:35:06.292+02:00 | raised    | Failed to form relation to MO uni/l3dom-DC-CFP-EXT-DOMAIN of class l3extDomP    | 
| ESX-CDC_AAEP  | Warn | F1003 | resolution-failed | 2023-06-12T10:35:06.308+02:00 | raised    | Failed to form relation to MO uni/l3dom-smi5Gc-ExtR_L3Dom of class l3extDomP    | 
| ESX_AAEP      | Warn | F1003 | resolution-failed | 2023-06-12T10:35:06.312+02:00 | raised    | Failed to form relation to MO uni/phys-ESX_PhysDom of class physDomP            | 
| SR-Infra_AAEP | Warn | F1003 | resolution-failed | 2023-06-12T10:35:06.324+02:00 | raised    | Failed to form relation to MO uni/l3dom-SR-Infra-CDC-3_L3Dom of class l3extDomP | 
+---------------+------+-------+-------------------+-------------------------------+-----------+---------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci aaep --apic apic11 --view fault

{
    "duration": 1568,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 386,
        "disconnect_time": 0,
        "mo_time": 1036,
        "total_time": 1422
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

True	386	-	connect apic11o.emea-sp.cisco.com:443
True	408	30	apic11o.emea-sp.cisco.com:443 class infraAttEntityP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraProvAcc,infraRtAttEntP,infraRsDomP
True	305	31	apic11o.emea-sp.cisco.com:443 mo uni/infra query query-target=subtree&target-subtree-class=infraAttEntityP&target-subtree-class=infraRsFuncToEpg
True	323	4	apic11o.emea-sp.cisco.com:443 class infraAttEntityP query rsp-subtree-include=faults,no-scoped,subtree
```

[[Back]](./Aaep.md)