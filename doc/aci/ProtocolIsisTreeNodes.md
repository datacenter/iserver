# Node Protocol - IS-IS

## Show multicast tree for selected nodes

```
# iserver get aci proto isis --apic apic11 --node rl -o tree

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+---------+----+--------------+-------------+----------+--------+----------------+------------+
| Node                | Domain  | Id | Root Address | Root Port   | Diameter | Origin | Diameter Alert | Oper State |
+---------------------+---------+----+--------------+-------------+----------+--------+----------------+------------+
| pod-1/rl301-eu-spdc | overlay | 0  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl301-eu-spdc | overlay | 1  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl301-eu-spdc | overlay | 2  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl301-eu-spdc | overlay | 3  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl301-eu-spdc | overlay | 4  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl301-eu-spdc | overlay | 5  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl301-eu-spdc | overlay | 6  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl301-eu-spdc | overlay | 7  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl301-eu-spdc | overlay | 8  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl301-eu-spdc | overlay | 9  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl301-eu-spdc | overlay | 10 | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl301-eu-spdc | overlay | 11 | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl301-eu-spdc | overlay | 12 | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl301-eu-spdc | overlay | 13 | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl301-eu-spdc | overlay | 14 | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl301-eu-spdc | overlay | 15 | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl302-eu-spdc | overlay | 0  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl302-eu-spdc | overlay | 1  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl302-eu-spdc | overlay | 2  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl302-eu-spdc | overlay | 3  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl302-eu-spdc | overlay | 4  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl302-eu-spdc | overlay | 5  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl302-eu-spdc | overlay | 6  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl302-eu-spdc | overlay | 7  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl302-eu-spdc | overlay | 8  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl302-eu-spdc | overlay | 9  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl302-eu-spdc | overlay | 10 | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl302-eu-spdc | overlay | 11 | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl302-eu-spdc | overlay | 12 | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl302-eu-spdc | overlay | 13 | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl302-eu-spdc | overlay | 14 | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl302-eu-spdc | overlay | 15 | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
+---------------------+---------+----+--------------+-------------+----------+--------+----------------+------------+
```

[[Back]](./ProtocolIsis.md)