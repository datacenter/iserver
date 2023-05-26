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

[[Back]](./Contract.md)