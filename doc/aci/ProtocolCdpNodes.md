# Node Protocol - CDP

## Show CDP state summary for selected nodes

```
# iserver get aci proto cdp --apic apic11 --node rl -o instance

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------+-------------+-------------+--------------------+---------------+---------------+-------------------+
| System Name   | Admin State | CDP Version | Transmit Frequency | Hold Interval | CDP Neighbors | Active Interfaces |
+---------------+-------------+-------------+--------------------+---------------+---------------+-------------------+
| rl301-eu-spdc | enabled     | v2          | 60                 | 180           | 4             | 4                 | 
| rl302-eu-spdc | enabled     | v2          | 60                 | 180           | 4             | 4                 | 
+---------------+-------------+-------------+--------------------+---------------+---------------+-------------------+
```

[[Back]](./ProtocolCdp.md)