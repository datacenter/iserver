# Contract

## Standard and Taboo Contracts with Contract Filter

Use '--type all' (default) to get all contracts related details
- [standard](./ContractStandard.md)
- [taboo](./ContractTaboo.md)
- [filter](./ContractFilter.md)

```
# iserver get aci contract --apic apic21 --tenant k8s

Apic: apic21 (mode:online, cache:off)

Standard Contracts
------------------

+---------------+---------+---------+-------------+---------------+----------------+
| Contract      | Scope   | Intent  | Target DSCP | Subject       | Filter         |
+---------------+---------+---------+-------------+---------------+----------------+
| k8s/BT-Demo   | context | install | unspecified | k8s/Any       | k8s/alltraffic | 
+---------------+---------+---------+-------------+---------------+----------------+
| k8s/k8s_tn_bm | global  | install | unspecified | k8s/k8s_tn_vm | common/any     | 
+---------------+---------+---------+-------------+---------------+----------------+
| k8s/k8s_tn_vm | global  | install | unspecified | k8s/k8s_tn_vm | common/any     | 
+---------------+---------+---------+-------------+---------------+----------------+

Taboo Contracts
---------------

+---------------------+--------------------+----------+
| Taboo               | Subject            | Filter   |
+---------------------+--------------------+----------+
| k8s/MyTabooContract | k8s/MyTabooSubject | k8s/icmp | 
+---------------------+--------------------+----------+

Contract Filters
----------------

+----------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| Filter         | Entry      | Ether | ARP Flag | Proto | Fragments | Stateful | Source | Destination   | Rules |
+----------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| k8s/alltraffic | alltraffic |       |          |       | no        | no       |        |               |       | 
+----------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| k8s/http       | http       | ipv4  |          | tcp   | no        | no       |        | http - http   |       | 
+----------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| k8s/https      | https      | ipv4  |          | tcp   | no        | no       |        | https - https |       | 
+----------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| k8s/icmp       | icmp       | ipv4  |          | icmp  | no        | no       |        |               |       | 
+----------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| k8s/ssh        | ssh        | ipv4  |          | tcp   | no        | no       |        | ssh - ssh     |       | 
+----------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+

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
# iserver get aci contract --apic apic21 --tenant k8s

{
    "duration": 4695,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 1560,
        "disconnect_time": 0,
        "mo_time": 2768,
        "total_time": 4328
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

True	1560	-	connect apic21o.emea-sp.cisco.com:443
True	348	22	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree=children&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	1367	24	apic21o.emea-sp.cisco.com:443 class vzSubj query rsp-subtree=children&rsp-subtree-class=vzRsSubjFiltAtt
True	358	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-class=vzEntry
True	352	2	apic21o.emea-sp.cisco.com:443 class vzTaboo query rsp-subtree=children&rsp-subtree-class=vzTSubj,vzRtProtBy
True	343	2	apic21o.emea-sp.cisco.com:443 class vzTSubj query rsp-subtree=children&rsp-subtree-class=vzRsDenyRule
```

[[Back]](./Contract.md)