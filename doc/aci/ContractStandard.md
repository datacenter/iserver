# Contract

## Standard Contract

Use '--type standard' to get standard contracts details
- contract name and tenant
- properties (scope, intent and target DSCP)
- subject and filters
- details of all filters used by selected contracts
- standard contracts usage (consumer and provider EPG)

```
# iserver get aci contract --apic apic21 --type standard --tenant k8s

Apic: apic21

Standard Contracts
------------------

+---------------+---------+---------+-------------+---------------+----------------+
| Contract      | Scope   | Intent  | Target DSCP | Subject       | Filter         |
+---------------+---------+---------+-------------+---------------+----------------+
| k8s/BT-Demo   | context | install | unspecified | k8s/Any       | k8s/alltraffic | 
+---------------+---------+---------+-------------+---------------+----------------+
| k8s/k8s_tn_bm | global  | install | unspecified | k8s/k8s_tn_bm | common/any     | 
+---------------+---------+---------+-------------+---------------+----------------+
| k8s/k8s_tn_vm | global  | install | unspecified | k8s/k8s_tn_bm | common/any     | 
+---------------+---------+---------+-------------+---------------+----------------+

Contract Filters
----------------

+----------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| Filter         | Entry      | Ether | ARP Flag | Proto | Fragments | Stateful | Source | Destination | Rules |
+----------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| k8s/alltraffic | alltraffic |       |          |       | no        | no       |        |             |       | 
+----------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| common/any     | any        | ipv4  |          |       | no        | no       |        |             |       | 
+----------------+------------+-------+----------+-------+-----------+----------+--------+-------------+-------+

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
```

[[Back]](./Contract.md)