# Node Protocol - LACP

## Show instance summary for selected node

```
# iserver get aci proto lacp --apic apic11 --node bl205-eu-spdc

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-------------+-------------------+----------------+---------------+-------------------------+
| Node                | Admin State | System MAC        | Admin Priority | Oper Priority | Port Channel Interfaces |
+---------------------+-------------+-------------------+----------------+---------------+-------------------------+
| pod-1/bl205-eu-spdc | enabled     | 4C:71:0D:7E:84:C0 | 32768          | 32768         | 5/0/5                   | 
+---------------------+-------------+-------------------+----------------+---------------+-------------------------+
```

[[Back]](./ProtocolLacp.md)