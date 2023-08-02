# Taboo Contract

## Filter by tenant

```
# iserver get aci contract taboo --apic apic21 --tenant k8s

Apic: apic21 (mode:online, cache:off)

Taboo Contract [#1]
-------------------

+---------+---------------------+--------------------+----------+
| Faults  | Taboo               | Subject            | Filter   |
+---------+---------------------+--------------------+----------+
| 0 0 0 0 | k8s/MyTabooContract | k8s/MyTabooSubject | k8s/icmp | 
+---------+---------------------+--------------------+----------+

Contract Filter [#1]
--------------------

+---------+----------+-------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| Faults  | Filter   | Entry | Ether | ARP Flag | Proto | Fragments | Stateful | Source | Destination | Rules |
+---------+----------+-------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| 0 0 0 0 | k8s/icmp | icmp  | ipv4  |          | icmp  | no        | no       |        |             |       | 
+---------+----------+-------+-------+----------+-------+-----------+----------+--------+-------------+-------+
```

Developer

```
# iserver get aci contract taboo --apic apic21 --tenant k8s

{
    "duration": 1618,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 459,
        "disconnect_time": 0,
        "mo_time": 1046,
        "total_time": 1505
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

True	459	-	connect apic21o.emea-sp.cisco.com:443
True	342	2	apic21o.emea-sp.cisco.com:443 class vzTaboo query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzTSubj,vzRtProtBy
True	341	2	apic21o.emea-sp.cisco.com:443 class vzTSubj query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzRsDenyRule
True	363	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzEntry
```

[[Back]](./ContractTaboo.md)