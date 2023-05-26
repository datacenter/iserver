# Node Protocol - IS-IS

## Show tunnel endpoints for selected node

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc -o tunnel

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: cl201-eu-spdc

+---------------------+---------+-------------+-------+--------------------------+
| Node                | Domain  | Id          | Role  | Type                     |
+---------------------+---------+-------------+-------+--------------------------+
| pod-1/cl201-eu-spdc | overlay | 10.3.192.64 | leaf  | physical                 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.192.65 | spine | physical                 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.192.68 | leaf  | physical                 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.32.64  | leaf  | physical                 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.32.65  | spine | physical                 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.40.64  | spine | physical,proxy-acast-v4  | 
| pod-1/cl201-eu-spdc | overlay | 10.3.40.65  | spine | physical,proxy-acast-mac | 
| pod-1/cl201-eu-spdc | overlay | 10.3.40.66  | spine | physical,proxy-acast-v6  | 
| pod-1/cl201-eu-spdc | overlay | 10.3.40.67  | leaf  | physical                 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.48.64  | leaf  | physical                 | 
+---------------------+---------+-------------+-------+--------------------------+
```

[[Back]](./ProtocolIsis.md)