# Node Protocol - LACP

## Show instance summary for all leaf nodes

```
# iserver get aci proto lacp --apic apic11 --role leaf

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+-------------+-------------------+----------------+---------------+-------------------------+
| Node                | Admin State | System MAC        | Admin Priority | Oper Priority | Port Channel Interfaces |
+---------------------+-------------+-------------------+----------------+---------------+-------------------------+
| pod-1/bl205-eu-spdc | enabled     | 4C:71:0D:7E:84:C0 | 32768          | 32768         | 5/0/5                   | 
| pod-1/bl206-eu-spdc | enabled     | 3C:13:CC:C9:ED:80 | 32768          | 32768         | 5/0/5                   | 
| pod-1/cl201-eu-spdc | enabled     | 4C:71:0D:23:FA:E3 | 32768          | 32768         | 27/1/28                 | 
| pod-1/cl202-eu-spdc | enabled     | 10:B3:D5:B5:62:C7 | 32768          | 32768         | 25/3/28                 | 
| pod-1/rl301-eu-spdc | enabled     | A0:B4:39:4A:2B:DF | 32768          | 32768         | 2/0/2                   | 
| pod-1/rl302-eu-spdc | enabled     | A0:B4:39:4A:2D:B3 | 32768          | 32768         | 2/0/2                   | 
+---------------------+-------------+-------------------+----------------+---------------+-------------------------+
```

[[Back]](./ProtocolLacp.md)