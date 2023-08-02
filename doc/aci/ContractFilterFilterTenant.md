# Contract Filter

## Filter by tenant

```
# iserver get aci contract filter --apic apic21 --tenant k8s

Apic: apic21 (mode:online, cache:off)

Contract Filter [#5]
--------------------

+---------+----------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| Faults  | Filter         | Entry      | Ether | ARP Flag | Proto | Fragments | Stateful | Source | Destination   | Rules |
+---------+----------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| 0 0 0 0 | k8s/alltraffic | alltraffic |       |          |       | no        | no       |        |               |       | 
+---------+----------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| 0 0 0 0 | k8s/http       | http       | ipv4  |          | tcp   | no        | no       |        | http - http   |       | 
+---------+----------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| 0 0 0 0 | k8s/https      | https      | ipv4  |          | tcp   | no        | no       |        | https - https |       | 
+---------+----------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| 0 0 0 0 | k8s/icmp       | icmp       | ipv4  |          | icmp  | no        | no       |        |               |       | 
+---------+----------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
| 0 0 0 0 | k8s/ssh        | ssh        | ipv4  |          | tcp   | no        | no       |        | ssh - ssh     |       | 
+---------+----------------+------------+-------+----------+-------+-----------+----------+--------+---------------+-------+
```

Developer

```
# iserver get aci contract filter --apic apic21 --tenant k8s

{
    "duration": 896,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 425,
        "disconnect_time": 0,
        "mo_time": 362,
        "total_time": 787
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

True	425	-	connect apic21o.emea-sp.cisco.com:443
True	362	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzEntry
```

[[Back]](./ContractFilter.md)