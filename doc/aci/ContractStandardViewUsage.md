# Standard Contract

## Usage view

```
# iserver get aci contract standard
    --apic apic21
    --name k8s/k8s_tn_bm
    --view usage

Apic: apic21 (mode:online, cache:off)

Standard Contract - Usage [#1]
------------------------------

+---------+---------------+--------------+------------------------------+
| Faults  | Contract      | Consumer EPG | Provider EPG                 |
+---------+---------------+--------------+------------------------------+
| 0 0 0 0 | k8s/k8s_tn_bm |              | k8s/bml3_k8s/bml3_k8s_ExtEPG | 
+---------+---------------+--------------+------------------------------+
```

Developer

```
# iserver get aci contract standard
    --apic apic21
    --name k8s/k8s_tn_bm
    --view usage

{
    "duration": 2099,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 476,
        "disconnect_time": 0,
        "mo_time": 1318,
        "total_time": 1794
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
True	482	22	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	405	24	apic21o.emea-sp.cisco.com:443 class vzSubj query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzRsSubjFiltAtt
True	431	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzEntry
```

[[Back]](./ContractStandard.md)