# Standard Contract

## Filter by name

```
# iserver get aci contract standard --apic apic21 --name k8s/k8s_tn_bm

Apic: apic21 (mode:online, cache:off)

Standard Contract [#1]
----------------------

+---------+---------------+--------+---------+-------------+---------------+------------+
| Faults  | Contract      | Scope  | Intent  | Target DSCP | Subject       | Filter     |
+---------+---------------+--------+---------+-------------+---------------+------------+
| 0 0 0 0 | k8s/k8s_tn_bm | global | install | unspecified | k8s/k8s_tn_vm | common/any | 
+---------+---------------+--------+---------+-------------+---------------+------------+

Contract Filter [#1]
--------------------

+---------+------------+-------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| Faults  | Filter     | Entry | Ether | ARP Flag | Proto | Fragments | Stateful | Source | Destination | Rules |
+---------+------------+-------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| 0 0 0 0 | common/any | any   | ipv4  |          |       | no        | no       |        |             |       | 
+---------+------------+-------+-------+----------+-------+-----------+----------+--------+-------------+-------+
```

Developer

```
# iserver get aci contract standard --apic apic21 --name k8s/k8s_tn_bm

{
    "duration": 2026,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 489,
        "disconnect_time": 0,
        "mo_time": 1200,
        "total_time": 1689
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

True	489	-	connect apic21o.emea-sp.cisco.com:443
True	399	22	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	408	24	apic21o.emea-sp.cisco.com:443 class vzSubj query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzRsSubjFiltAtt
True	393	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzEntry
```

[[Back]](./ContractStandard.md)