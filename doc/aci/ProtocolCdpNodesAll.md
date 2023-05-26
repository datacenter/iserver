# Node Protocol - CDP

## Show CDP state summary for all nodes

```
# iserver get aci proto cdp --apic apic11 --node any -o instance

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

+---------------+-------------+-------------+--------------------+---------------+---------------+-------------------+
| System Name   | Admin State | CDP Version | Transmit Frequency | Hold Interval | CDP Neighbors | Active Interfaces |
+---------------+-------------+-------------+--------------------+---------------+---------------+-------------------+
| bl205-eu-spdc | enabled     | v2          | 60                 | 180           | 8             | 8                 | 
| bl206-eu-spdc | enabled     | v2          | 60                 | 180           | 8             | 8                 | 
| cl201-eu-spdc | enabled     | v2          | 60                 | 180           | 17            | 16                | 
| cl202-eu-spdc | enabled     | v2          | 60                 | 180           | 15            | 15                | 
| rl301-eu-spdc | enabled     | v2          | 60                 | 180           | 4             | 4                 | 
| rl302-eu-spdc | enabled     | v2          | 60                 | 180           | 4             | 4                 | 
| s101-eu-spdc  | enabled     | v2          | 60                 | 180           | 1             | 1                 | 
| s102-eu-spdc  | enabled     | v2          | 60                 | 180           | 1             | 1                 | 
+---------------+-------------+-------------+--------------------+---------------+---------------+-------------------+
```

[[Back]](./ProtocolCdp.md)