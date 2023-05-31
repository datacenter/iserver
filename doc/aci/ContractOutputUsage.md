# Contract

## Contract usage view

```
# iserver get aci contract
    --apic apic21
    --type filter
    --name alltraffic
    --view usage

Apic: apic21

Contract Filters Usage
----------------------

+----------------------+-----------------------------+-------+
| Filter               | Contract                    | Taboo |
+----------------------+-----------------------------+-------+
| common/alltraffic    | common/IKSHS-alltraffic     |       | 
|                      | common/vEPG-MGMT_alltraffic |       | 
+----------------------+-----------------------------+-------+
| vEPC_demo/alltraffic | vEPC_demo/vEPG_ACC          |       | 
|                      | vEPC_demo/vEPG_INT          |       | 
|                      | vEPC_demo/vEPG_SX           |       | 
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
    "duration": 3373,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 419,
        "disconnect_time": 0,
        "mo_time": 2829,
        "total_time": 3248
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

True	419	-	connect apic21o.emea-sp.cisco.com
True	1128	30	apic21o.emea-sp.cisco.com class vzFilter query rsp-subtree=children&rsp-subtree-class=vzEntry
True	321	2	apic21o.emea-sp.cisco.com class vzTaboo query rsp-subtree=children&rsp-subtree-class=vzTSubj,vzRtProtBy
True	685	2	apic21o.emea-sp.cisco.com class vzTSubj query rsp-subtree=children&rsp-subtree-class=vzRsDenyRule
True	374	22	apic21o.emea-sp.cisco.com class vzBrCP query rsp-subtree=children&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	321	24	apic21o.emea-sp.cisco.com class vzSubj query rsp-subtree=children&rsp-subtree-class=vzRsSubjFiltAtt
```

[[Back]](./Contract.md)