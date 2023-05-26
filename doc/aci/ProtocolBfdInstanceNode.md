# Node Protocol - BFD

## Get BFD instance summary from selected node

```
# iserver get aci proto bfd --apic apic11 --node cl201-eu-spdc -o instance

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: cl201-eu-spdc

+---------------------+---------+-------------+-----------------+-----------+-----------------+--------------------+
| Node                | Admin   | Echo Intf   | Session Summary | Interface | Interface State | Interface Sessions |
+---------------------+---------+-------------+-----------------+-----------+-----------------+--------------------+
| pod-1/cl201-eu-spdc | enabled | unspecified | 4/5             | vlan469   | enabled         | 2/2                | 
|                     |         |             |                 | vlan468   | enabled         | 0/1                | 
+---------------------+---------+-------------+-----------------+-----------+-----------------+--------------------+
```

[[Back]](./ProtocolBfd.md)