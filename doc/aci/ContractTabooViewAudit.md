# Taboo Contract

## Audit view

```
# iserver get aci contract taboo
    --apic apic21
    --name k8s/my*
    --when any
    --view audit

Apic: apic21 (mode:online, cache:off)

Taboo Contract - Audit Logs last 10y [#3]
-----------------------------------------

+---------------------+------+----------+------------+-------------------------------+-------------------------------+--------------------------------------------+
| Taboo Contract      | Sev  | Code     | Cause      | Created Time                  | Description                   | Change Set                                 |
+---------------------+------+----------+------------+-------------------------------+-------------------------------+--------------------------------------------+
| k8s/MyTabooContract | Info | E4213703 | transition | 2023-05-02T16:12:41.616+02:00 | TSubj MyTabooSubject created  | name:MyTabooSubject, userdom::all:common:  | 
+---------------------+------+----------+------------+-------------------------------+-------------------------------+--------------------------------------------+
| k8s/MyTabooContract | Info | E4213679 | transition | 2023-05-02T16:12:41.616+02:00 | RsDenyRule icmp created       | tnVzFilterName:icmp, userdom::all:common:  | 
+---------------------+------+----------+------------+-------------------------------+-------------------------------+--------------------------------------------+
| k8s/MyTabooContract | Info | E4213706 | transition | 2023-05-02T16:12:41.616+02:00 | Taboo MyTabooContract created | name:MyTabooContract, userdom::all:common: | 
+---------------------+------+----------+------------+-------------------------------+-------------------------------+--------------------------------------------+
```

Developer

```
# iserver get aci contract taboo
    --apic apic21
    --name k8s/my*
    --when any
    --view audit

{
    "duration": 2195,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 476,
        "disconnect_time": 0,
        "mo_time": 1526,
        "total_time": 2002
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

True	476	-	connect apic21o.emea-sp.cisco.com:443
True	352	2	apic21o.emea-sp.cisco.com:443 class vzTaboo query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzTSubj,vzRtProtBy
True	347	2	apic21o.emea-sp.cisco.com:443 class vzTSubj query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzRsDenyRule
True	380	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzEntry
True	447	3	apic21o.emea-sp.cisco.com:443 class vzTaboo query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./ContractTaboo.md)