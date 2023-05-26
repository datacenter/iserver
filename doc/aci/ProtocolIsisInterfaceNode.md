# Node Protocol - IS-IS

## Show interface details for selected node

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc -o intf

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: cl201-eu-spdc

+---------------------+---------+--------------+-------------+--------------+--------------------+----------------+
| Node                | Domain  | Id           | Admin State | Circuit Type | Control            | Protocol State |
+---------------------+---------+--------------+-------------+--------------+--------------------+----------------+
| pod-1/cl201-eu-spdc | overlay | eth1/107.7   | enabled     | l1           |                    | Ready          | 
| pod-1/cl201-eu-spdc | overlay | eth1/108.504 | enabled     | l1           |                    | Ready          | 
| pod-1/cl201-eu-spdc | overlay | lo0          | enabled     | l1           | advert-tep,passive | Ready          | 
| pod-1/cl201-eu-spdc | overlay | lo1          | enabled     | l1           | advert-tep,passive | Ready          | 
| pod-1/cl201-eu-spdc | overlay | lo2          | enabled     | l1           | passive            | Ready          | 
+---------------------+---------+--------------+-------------+--------------+--------------------+----------------+
```

[[Back]](./ProtocolIsis.md)