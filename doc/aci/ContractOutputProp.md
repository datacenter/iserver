# Contract

## Contract properties view

```
# iserver get aci contract
    --apic apic21
    --type filter
    --name alltraffic
    --view prop

Apic: apic21 (mode:online, cache:off)

Contract Filters
----------------

+----------------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| Filter               | Entry      | Ether | ARP Flag | Proto | Fragments | Stateful | Source | Destination | Rules |
+----------------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| vEPC_demo/alltraffic | alltraffic |       |          |       | no        | no       |        |             |       | 
+----------------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| common/alltraffic    | alltraffic |       |          |       | no        | no       |        |             |       | 
+----------------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| k8s/alltraffic       | alltraffic |       |          |       | no        | no       |        |             |       | 
+----------------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+
```

Developer

```
# iserver get aci contract
    --apic apic21
    --type filter
    --name alltraffic
    --view prop

{
    "duration": 2936,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 444,
        "disconnect_time": 0,
        "mo_time": 1878,
        "total_time": 2322
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

True	444	-	connect apic21o.emea-sp.cisco.com:443
True	380	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-class=vzEntry
True	383	2	apic21o.emea-sp.cisco.com:443 class vzTaboo query rsp-subtree=children&rsp-subtree-class=vzTSubj,vzRtProtBy
True	330	2	apic21o.emea-sp.cisco.com:443 class vzTSubj query rsp-subtree=children&rsp-subtree-class=vzRsDenyRule
True	387	22	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree=children&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	398	24	apic21o.emea-sp.cisco.com:443 class vzSubj query rsp-subtree=children&rsp-subtree-class=vzRsSubjFiltAtt
```

[[Back]](./Contract.md)