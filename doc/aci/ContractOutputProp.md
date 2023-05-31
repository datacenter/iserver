# Contract

## Contract properties view

```
# iserver get aci contract
    --apic apic21
    --type filter
    --name alltraffic
    --view prop

Apic: apic21

Contract Filters
----------------

+----------------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| Filter               | Entry      | Ether | ARP Flag | Proto | Fragments | Stateful | Source | Destination | Rules |
+----------------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| common/alltraffic    | alltraffic |       |          |       | no        | no       |        |             |       | 
+----------------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| vEPC_demo/alltraffic | alltraffic |       |          |       | no        | no       |        |             |       | 
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
    "duration": 2267,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 408,
        "disconnect_time": 0,
        "mo_time": 1674,
        "total_time": 2082
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
    }
}

Log: apic
----------

True	408	-	connect apic21o.emea-sp.cisco.com
True	338	30	apic21o.emea-sp.cisco.com class vzFilter query rsp-subtree=children&rsp-subtree-class=vzEntry
True	301	2	apic21o.emea-sp.cisco.com class vzTaboo query rsp-subtree=children&rsp-subtree-class=vzTSubj,vzRtProtBy
True	301	2	apic21o.emea-sp.cisco.com class vzTSubj query rsp-subtree=children&rsp-subtree-class=vzRsDenyRule
True	396	22	apic21o.emea-sp.cisco.com class vzBrCP query rsp-subtree=children&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	338	24	apic21o.emea-sp.cisco.com class vzSubj query rsp-subtree=children&rsp-subtree-class=vzRsSubjFiltAtt
```

[[Back]](./Contract.md)