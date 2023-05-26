# Contract

## Taboo Contract

Use '--type taboo' to get taboo contracts details
- contract name and tenant
- subject and filters
- details of all filters used by selected taboo contracts
- taboo contracts usage (protected EPG)

```
# iserver get aci contract --apic apic21 --type taboo --tenant k8s

Apic: apic21

Taboo Contracts
---------------

+---------------------+--------------------+----------+
| Taboo               | Subject            | Filter   |
+---------------------+--------------------+----------+
| k8s/MyTabooContract | k8s/MyTabooSubject | k8s/icmp | 
+---------------------+--------------------+----------+

Contract Filters
----------------

+----------+-------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| Filter   | Entry | Ether | ARP Flag | Proto | Fragments | Stateful | Source | Destination | Rules |
+----------+-------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| k8s/icmp | icmp  | ipv4  |          | icmp  | no        | no       |        |             |       | 
+----------+-------+-------+----------+-------+-----------+----------+--------+-------------+-------+

Taboo Contracts Usage
---------------------

+---------------------+---------------------+
| Taboo               | Protected EPG       |
+---------------------+---------------------+
| k8s/MyTabooContract | k8s/k8s_ANP/SRIoV_A | 
+---------------------+---------------------+
```

[[Back]](./Contract.md)