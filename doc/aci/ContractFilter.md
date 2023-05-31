# Contract

## Contract Filter

Use '--type filter' to get contract filters details
- filter name and tenant
- properties
    - Ethernet Type
    - IP Protocol
    - match only fragments
    - stateful
    - source range
    - destination range
    - TCP rules
- filter usage (standard and taboo contracts)

```
# iserver get aci contract --apic apic21 --type filter --tenant k8s/*

Apic: apic21

Contract Filters
----------------

+--------+-------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| Filter | Entry | Ether | ARP Flag | Proto | Fragments | Stateful | Source | Destination | Rules |
+--------+-------+-------+----------+-------+-----------+----------+--------+-------------+-------+

Contract Filters Usage
----------------------

+--------+----------+-------+
| Filter | Contract | Taboo |
+--------+----------+-------+
```

Developer

```
# iserver get aci contract --apic apic21 --type filter --tenant k8s/*

{
    "duration": 1001,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 570,
        "disconnect_time": 0,
        "mo_time": 349,
        "total_time": 919
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

True	570	-	connect apic21o.emea-sp.cisco.com
True	349	30	apic21o.emea-sp.cisco.com class vzFilter query rsp-subtree=children&rsp-subtree-class=vzEntry
```

[[Back]](./Contract.md)