# Node Protocol - LLDP

## Interface stats output

```
# iserver get aci proto lldp --apic apic11 --node bl205-eu-spdc -o stats

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-------------+--------------+------------------+-------------------+---------------+-------------------+---------------------+--------------+
| Node                | Admin State | Packets Sent | Packets Received | Packets Discarded | Error Packets | Adjacencies Added | Adjacencies Removed | Entries Aged |
+---------------------+-------------+--------------+------------------+-------------------+---------------+-------------------+---------------------+--------------+
| pod-1/bl205-eu-spdc | enabled     | 3032779      | 3036182          | 0                 | 0             | 26                | 0                   | 0            | 
+---------------------+-------------+--------------+------------------+-------------------+---------------+-------------------+---------------------+--------------+
```

[[Back]](./ProtocolLldp.md)