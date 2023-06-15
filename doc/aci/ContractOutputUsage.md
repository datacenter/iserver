# Contract

## Contract usage view

```
# iserver get aci contract
    --apic apic21
    --type filter
    --name alltraffic
    --view usage

Apic: apic21 (mode:online, cache:off)

Contract Filters Usage
----------------------

+----------------------+-----------------------------+-------+
| Filter               | Contract                    | Taboo |
+----------------------+-----------------------------+-------+
| vEPC_demo/alltraffic | vEPC_demo/vEPG_ACC          |       | 
|                      | vEPC_demo/vEPG_INT          |       | 
|                      | vEPC_demo/vEPG_SX           |       | 
+----------------------+-----------------------------+-------+
| k8s/alltraffic       | k8s/BT-Demo                 |       | 
+----------------------+-----------------------------+-------+
| common/alltraffic    | common/IKSHS-alltraffic     |       | 
|                      | common/vEPG-MGMT_alltraffic |       | 
+----------------------+-----------------------------+-------+
```

Developer

```
# iserver get aci contract
    --apic apic21
    --type filter
    --name alltraffic
    --view usage

{
    "duration": 2451,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 415,
        "disconnect_time": 0,
        "mo_time": 1720,
        "total_time": 2135
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

True	415	-	connect apic21o.emea-sp.cisco.com
True	352	30	apic21o.emea-sp.cisco.com class vzFilter query rsp-subtree=children&rsp-subtree-class=vzEntry
True	330	2	apic21o.emea-sp.cisco.com class vzTaboo query rsp-subtree=children&rsp-subtree-class=vzTSubj,vzRtProtBy
True	326	2	apic21o.emea-sp.cisco.com class vzTSubj query rsp-subtree=children&rsp-subtree-class=vzRsDenyRule
True	355	22	apic21o.emea-sp.cisco.com class vzBrCP query rsp-subtree=children&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	357	24	apic21o.emea-sp.cisco.com class vzSubj query rsp-subtree=children&rsp-subtree-class=vzRsSubjFiltAtt
```

[[Back]](./Contract.md)