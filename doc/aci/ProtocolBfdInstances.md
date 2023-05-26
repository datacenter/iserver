# Node Protocol - BFD

## Get BFD instance summary from all nodes

```
# iserver get aci proto bfd --apic apic11 --node any -o instance

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc
- node: s101-eu-spdc
- node: s102-eu-spdc

+---------------------+---------+-------------+-----------------+-----------+-----------------+--------------------+
| Node                | Admin   | Echo Intf   | Session Summary | Interface | Interface State | Interface Sessions |
+---------------------+---------+-------------+-----------------+-----------+-----------------+--------------------+
| pod-1/bl205-eu-spdc | enabled | unspecified | 0/1             | lo3       | enabled         | 0/1                | 
| pod-1/bl206-eu-spdc | enabled | unspecified | 0/1             | lo3       | enabled         | 0/1                | 
| pod-1/cl201-eu-spdc | enabled | unspecified | 4/5             | vlan469   | enabled         | 2/2                | 
|                     |         |             |                 | vlan468   | enabled         | 0/1                | 
| pod-1/cl202-eu-spdc | enabled | unspecified | 4/4             | vlan491   | enabled         | 2/2                | 
| pod-1/rl301-eu-spdc | enabled | unspecified | 0/1             | lo4       | enabled         | 0/1                | 
| pod-1/rl302-eu-spdc | enabled | unspecified | 0/1             | lo4       | enabled         | 0/1                | 
| pod-1/s101-eu-spdc  | enabled | unspecified | 0/0             |           |                 |                    | 
| pod-1/s102-eu-spdc  | enabled | unspecified | 0/0             |           |                 |                    | 
+---------------------+---------+-------------+-----------------+-----------+-----------------+--------------------+
```

[[Back]](./ProtocolBfd.md)