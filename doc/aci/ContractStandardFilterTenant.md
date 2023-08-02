# Contract

## Filter by tenant

```
# iserver get aci contract standard --apic apic21 --tenant k8s

Apic: apic21 (mode:online, cache:off)

Standard Contract [#3]
----------------------

+---------+---------------+---------+---------+-------------+---------------+----------------+
| Faults  | Contract      | Scope   | Intent  | Target DSCP | Subject       | Filter         |
+---------+---------------+---------+---------+-------------+---------------+----------------+
| 0 0 0 0 | k8s/BT-Demo   | context | install | unspecified | k8s/Any       | k8s/alltraffic | 
+---------+---------------+---------+---------+-------------+---------------+----------------+
| 0 0 0 0 | k8s/k8s_tn_bm | global  | install | unspecified | k8s/k8s_tn_vm | common/any     | 
+---------+---------------+---------+---------+-------------+---------------+----------------+
| 0 0 0 0 | k8s/k8s_tn_vm | global  | install | unspecified | k8s/k8s_tn_vm | common/any     | 
+---------+---------------+---------+---------+-------------+---------------+----------------+

Contract Filter [#2]
--------------------

+---------+----------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| Faults  | Filter         | Entry      | Ether | ARP Flag | Proto | Fragments | Stateful | Source | Destination | Rules |
+---------+----------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| 0 0 0 0 | k8s/alltraffic | alltraffic |       |          |       | no        | no       |        |             |       | 
+---------+----------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| 0 0 0 0 | common/any     | any        | ipv4  |          |       | no        | no       |        |             |       | 
+---------+----------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+
```

Developer

```
# iserver get aci contract standard --apic apic21 --tenant k8s

{
    "duration": 2127,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 516,
        "disconnect_time": 0,
        "mo_time": 1297,
        "total_time": 1813
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

True	516	-	connect apic21o.emea-sp.cisco.com:443
True	457	22	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	426	24	apic21o.emea-sp.cisco.com:443 class vzSubj query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzRsSubjFiltAtt
True	414	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzEntry
```

[[Back]](./ContractStandard.md)