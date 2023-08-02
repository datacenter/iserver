# Contract Filter

## Filter by name

```
# iserver get aci contract filter --apic apic21 --name k8s/icmp

Apic: apic21 (mode:online, cache:off)

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
# iserver get aci contract filter --apic apic21 --name k8s/icmp

{
    "duration": 891,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 445,
        "disconnect_time": 0,
        "mo_time": 356,
        "total_time": 801
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

True	445	-	connect apic21o.emea-sp.cisco.com:443
True	356	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzEntry
```

[[Back]](./ContractFilter.md)