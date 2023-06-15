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

+---------------+---------+---------+-------------+-----------------+----------------+
| Contract      | Scope   | Intent  | Target DSCP | Subject         | Filter         |
+---------------+---------+---------+-------------+-----------------+----------------+
| k8s/BT-Demo   | context | install | unspecified | k8s/Any         | k8s/alltraffic | 
+---------------+---------+---------+-------------+-----------------+----------------+
| k8s/k8s_tn_bm | global  | install | unspecified | common/k8s_prov | common/any     | 
+---------------+---------+---------+-------------+-----------------+----------------+
| k8s/k8s_tn_vm | global  | install | unspecified | common/k8s_prov | common/any     | 
+---------------+---------+---------+-------------+-----------------+----------------+

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
    "duration": 2543,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 437,
        "disconnect_time": 0,
        "mo_time": 1750,
        "total_time": 2187
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

True	437	-	connect apic21o.emea-sp.cisco.com
True	351	22	apic21o.emea-sp.cisco.com class vzBrCP query rsp-subtree=children&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	336	24	apic21o.emea-sp.cisco.com class vzSubj query rsp-subtree=children&rsp-subtree-class=vzRsSubjFiltAtt
True	345	30	apic21o.emea-sp.cisco.com class vzFilter query rsp-subtree=children&rsp-subtree-class=vzEntry
True	336	2	apic21o.emea-sp.cisco.com class vzTaboo query rsp-subtree=children&rsp-subtree-class=vzTSubj,vzRtProtBy
True	382	2	apic21o.emea-sp.cisco.com class vzTSubj query rsp-subtree=children&rsp-subtree-class=vzRsDenyRule
```

[[Back]](./Contract.md)