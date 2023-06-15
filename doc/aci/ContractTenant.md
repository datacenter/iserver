# Contract

## Filter by tenant

Depending on '--type [all|standard|taboo|filter]', filtering applies to either all contract related object, standard contract, taboo contract or filter.

```
# iserver get aci contract --apic apic21 --view usage --tenant k8s

Apic: apic21 (mode:online, cache:off)

Standard Contracts Usage
------------------------

+---------------+---------------------+------------------------------+
| Contract      | Consumer EPG        | Provider EPG                 |
+---------------+---------------------+------------------------------+
| k8s/BT-Demo   | k8s/k8s_ANP/SRIoV_A | k8s/k8s_ANP/SRIoV_A          | 
+---------------+---------------------+------------------------------+
| k8s/k8s_tn_bm |                     | k8s/bml3_k8s/bml3_k8s_ExtEPG | 
+---------------+---------------------+------------------------------+
| k8s/k8s_tn_vm |                     | k8s/vl3_k8s/vl3_k8s_ExtEPG   | 
+---------------+---------------------+------------------------------+

Taboo Contracts Usage
---------------------

+---------------------+---------------------+
| Taboo               | Protected EPG       |
+---------------------+---------------------+
| k8s/MyTabooContract | k8s/k8s_ANP/SRIoV_A | 
+---------------------+---------------------+

Contract Filters Usage
----------------------

+----------------+-------------+---------------------+
| Filter         | Contract    | Taboo               |
+----------------+-------------+---------------------+
| k8s/alltraffic | k8s/BT-Demo |                     | 
+----------------+-------------+---------------------+
| k8s/http       |             |                     | 
+----------------+-------------+---------------------+
| k8s/https      |             |                     | 
+----------------+-------------+---------------------+
| k8s/icmp       |             | k8s/MyTabooContract | 
+----------------+-------------+---------------------+
| k8s/ssh        |             |                     | 
+----------------+-------------+---------------------+
```

Developer

```
# iserver get aci contract --apic apic21 --view usage --tenant k8s

{
    "duration": 2613,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 446,
        "disconnect_time": 0,
        "mo_time": 1824,
        "total_time": 2270
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

True	446	-	connect apic21o.emea-sp.cisco.com
True	379	22	apic21o.emea-sp.cisco.com class vzBrCP query rsp-subtree=children&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	356	24	apic21o.emea-sp.cisco.com class vzSubj query rsp-subtree=children&rsp-subtree-class=vzRsSubjFiltAtt
True	358	30	apic21o.emea-sp.cisco.com class vzFilter query rsp-subtree=children&rsp-subtree-class=vzEntry
True	370	2	apic21o.emea-sp.cisco.com class vzTaboo query rsp-subtree=children&rsp-subtree-class=vzTSubj,vzRtProtBy
True	361	2	apic21o.emea-sp.cisco.com class vzTSubj query rsp-subtree=children&rsp-subtree-class=vzRsDenyRule
```

[[Back]](./Contract.md)