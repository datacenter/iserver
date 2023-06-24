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
| common/alltraffic    | common/IKSHS-alltraffic     |       | 
|                      | common/vEPG-MGMT_alltraffic |       | 
+----------------------+-----------------------------+-------+
| k8s/alltraffic       | k8s/BT-Demo                 |       | 
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
    "duration": 2543,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 431,
        "disconnect_time": 0,
        "mo_time": 1789,
        "total_time": 2220
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

True	431	-	connect apic21o.emea-sp.cisco.com:443
True	365	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-class=vzEntry
True	354	2	apic21o.emea-sp.cisco.com:443 class vzTaboo query rsp-subtree=children&rsp-subtree-class=vzTSubj,vzRtProtBy
True	336	2	apic21o.emea-sp.cisco.com:443 class vzTSubj query rsp-subtree=children&rsp-subtree-class=vzRsDenyRule
True	371	22	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree=children&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	363	24	apic21o.emea-sp.cisco.com:443 class vzSubj query rsp-subtree=children&rsp-subtree-class=vzRsSubjFiltAtt
```

[[Back]](./Contract.md)