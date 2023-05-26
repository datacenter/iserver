# Node Protocol - IS-IS

## Show interface details for selected nodes

```
# iserver get aci proto isis --apic apic11 --node rl -o intf

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+---------+------------+-------------+--------------+--------------------+----------------+
| Node                | Domain  | Id         | Admin State | Circuit Type | Control            | Protocol State |
+---------------------+---------+------------+-------------+--------------+--------------------+----------------+
| pod-1/rl301-eu-spdc | overlay | eth1/33.47 | enabled     | l1           |                    | Ready          | 
| pod-1/rl301-eu-spdc | overlay | eth1/34.48 | enabled     | l1           |                    | Ready          | 
| pod-1/rl301-eu-spdc | overlay | lo0        | enabled     | l1           | advert-tep,passive | Ready          | 
| pod-1/rl301-eu-spdc | overlay | lo1        | enabled     | l1           | passive            | Ready          | 
| pod-1/rl301-eu-spdc | overlay | lo2        | enabled     | l1           | passive            | Ready          | 
| pod-1/rl301-eu-spdc | overlay | lo3        | enabled     | l1           | advert-tep,passive | Ready          | 
| pod-1/rl302-eu-spdc | overlay | eth1/33.7  | enabled     | l1           |                    | Ready          | 
| pod-1/rl302-eu-spdc | overlay | eth1/34.8  | enabled     | l1           |                    | Ready          | 
| pod-1/rl302-eu-spdc | overlay | lo0        | enabled     | l1           | advert-tep,passive | Ready          | 
| pod-1/rl302-eu-spdc | overlay | lo1        | enabled     | l1           | passive            | Ready          | 
| pod-1/rl302-eu-spdc | overlay | lo2        | enabled     | l1           | passive            | Ready          | 
| pod-1/rl302-eu-spdc | overlay | lo3        | enabled     | l1           | advert-tep,passive | Ready          | 
+---------------------+---------+------------+-------------+--------------+--------------------+----------------+
```

[[Back]](./ProtocolIsis.md)