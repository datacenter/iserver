# Node Protocol - CDP

## Show CDP state summary for selected node

```
# iserver get aci proto cdp --apic apic11 --node cl201-eu-spdc -o instance

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: cl201-eu-spdc

+---------------+-------------+-------------+--------------------+---------------+---------------+-------------------+
| System Name   | Admin State | CDP Version | Transmit Frequency | Hold Interval | CDP Neighbors | Active Interfaces |
+---------------+-------------+-------------+--------------------+---------------+---------------+-------------------+
| cl201-eu-spdc | enabled     | v2          | 60                 | 180           | 17            | 16                | 
+---------------+-------------+-------------+--------------------+---------------+---------------+-------------------+
```

[[Back]](./ProtocolCdp.md)