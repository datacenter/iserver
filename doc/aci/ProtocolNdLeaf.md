# Node Protocol - ND

## Leaf nodes adjacencies

```
# iserver get aci proto nd --apic apic11 --role leaf

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+-------------+----------------+----------------+------------------------+
| Node                | Admin State | Aging Interval | Neighbor Count | Active Interface Count |
+---------------------+-------------+----------------+----------------+------------------------+
| pod-1/bl205-eu-spdc | enabled     | 1380           | 0              | 0                      | 
| pod-1/bl206-eu-spdc | enabled     | 1380           | 0              | 0                      | 
| pod-1/cl201-eu-spdc | enabled     | 1380           | 0              | 0                      | 
| pod-1/cl202-eu-spdc | enabled     | 1380           | 0              | 0                      | 
| pod-1/rl301-eu-spdc | enabled     | 1380           | 0              | 0                      | 
| pod-1/rl302-eu-spdc | enabled     | 1380           | 0              | 0                      | 
+---------------------+-------------+----------------+----------------+------------------------+
```

[[Back]](./ProtocolNd.md)