# Node Protocol - IS-IS

## Show instance summary for all nodes

```
# iserver get aci proto isis --apic apic11 --node any

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

+---------------------+-------------+------------+-------------+------------+-------------------+------+----------+--------+----------+--------------+------+
| Node                | Admin State | Oper State | Domain Name | Oper State | System ID         | Area | Protocol | Mode   | Max ECMP | Metric Style | MTU  |
+---------------------+-------------+------------+-------------+------------+-------------------+------+----------+--------+----------+--------------+------+
| pod-1/bl205-eu-spdc | enabled     | enabled    | overlay-1   | ok         | 40:C0:03:0A:00:00 | 1    | ip       | fabric | 18       | narrow       | 1492 | 
| pod-1/bl206-eu-spdc | enabled     | enabled    | overlay-1   | ok         | 40:20:03:0A:00:00 | 1    | ip       | fabric | 18       | narrow       | 1492 | 
| pod-1/cl201-eu-spdc | enabled     | enabled    | overlay-1   | ok         | 43:C0:03:0A:00:00 | 1    | ip       | fabric | 18       | narrow       | 1492 | 
| pod-1/cl202-eu-spdc | enabled     | enabled    | overlay-1   | ok         | 44:C0:03:0A:00:00 | 1    | ip       | fabric | 18       | narrow       | 1492 | 
| pod-1/rl301-eu-spdc | enabled     | enabled    | overlay-1   | ok         | A0:1E:10:AC:00:00 | 1    | ip       | fabric | 18       | wide         | 1492 | 
| pod-1/rl302-eu-spdc | enabled     | enabled    | overlay-1   | ok         | 78:1E:10:AC:00:00 | 1    | ip       | fabric | 18       | wide         | 1492 | 
| pod-1/s101-eu-spdc  | enabled     | enabled    | overlay-1   | ok         | 41:C0:03:0A:00:00 | 1    | ip       | fabric | 18       | narrow       | 1492 | 
| pod-1/s102-eu-spdc  | enabled     | enabled    | overlay-1   | ok         | 41:20:03:0A:00:00 | 1    | ip       | fabric | 18       | narrow       | 1492 | 
+---------------------+-------------+------------+-------------+------------+-------------------+------+----------+--------+----------+--------------+------+
```

[[Back]](./ProtocolIsis.md)