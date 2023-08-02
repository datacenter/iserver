# Attachable Access Entity Profile (AAEP)

## Audit view

```
# iserver get aci aaep --apic apic11 --when 60d --view audit

Apic: apic11 (mode:online, cache:off)

Attachable Access Entity Profile (AAEP) - Audit Logs last 60d [#0]
------------------------------------------------------------------
None
```

Developer

```
# iserver get aci aaep --apic apic11 --when 60d --view audit

{
    "duration": 3145,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 395,
        "disconnect_time": 0,
        "mo_time": 2615,
        "total_time": 3010
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

True	395	-	connect apic11o.emea-sp.cisco.com:443
True	396	30	apic11o.emea-sp.cisco.com:443 class infraAttEntityP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraProvAcc,infraRtAttEntP,infraRsDomP
True	306	31	apic11o.emea-sp.cisco.com:443 mo uni/infra query query-target=subtree&target-subtree-class=infraAttEntityP&target-subtree-class=infraRsFuncToEpg
True	1913	70	apic11o.emea-sp.cisco.com:443 class infraAttEntityP query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./Aaep.md)