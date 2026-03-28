# UDN - Get State

[[Back]](./README.md)

```
# iserver get k8s udn --cluster bm1
Cluster: bm1 (type: ocp)

+----+----------+---+---+---+----------+--------------+--------------------------------------------+-------------------------+
| ID | UDN      | C | A | P | Topology | Subnet       | Net Attach Def                             | Workload                |
+----+----------+---+---+---+----------+--------------+--------------------------------------------+-------------------------+
| 1  | island-p | V | V | V | Layer2   | 66.66.0.0/24 | {                                          | [POD] nginx3 (ovn-udn1) |
|    | pl2      |   |   |   |          |              |   "cniVersion": "1.0.0",                   | [POD] p1-1 (ovn-udn1)   |
|    |          |   |   |   |          |              |   "joinSubnet": "100.65.0.0/16,fd99::/64", | [POD] p1-2 (ovn-udn1)   |
|    |          |   |   |   |          |              |   "name": "island-p_pl2",                  | [VM] c8kv1 (default)    |
|    |          |   |   |   |          |              |   "netAttachDefName": "island-p/pl2",      | [VM] c8kv2 (default)    |
|    |          |   |   |   |          |              |   "role": "primary",                       |                         |
|    |          |   |   |   |          |              |   "subnets": "66.66.0.0/24",               |                         |
|    |          |   |   |   |          |              |   "topology": "layer2",                    |                         |
|    |          |   |   |   |          |              |   "transitSubnet": "100.88.0.0/16",        |                         |
|    |          |   |   |   |          |              |   "type": "ovn-k8s-cni-overlay"            |                         |
|    |          |   |   |   |          |              | }                                          |                         |
+----+----------+---+---+---+----------+--------------+--------------------------------------------+-------------------------+
| 2  | island-p | V | V |   | Layer2   | 66.66.1.0/24 | {                                          | [POD] p1-1 (net1)       |
|    | sl2      |   |   |   |          |              |   "cniVersion": "1.0.0",                   | [POD] p1-2 (net1)       |
|    |          |   |   |   |          |              |   "name": "island-p_sl2",                  | [VM] c8kv1 (net1)       |
|    |          |   |   |   |          |              |   "netAttachDefName": "island-p/sl2",      | [VM] c8kv2 (net1)       | 
|    |          |   |   |   |          |              |   "role": "secondary",                     |                         |
|    |          |   |   |   |          |              |   "subnets": "66.66.1.0/24",               |                         |
|    |          |   |   |   |          |              |   "topology": "layer2",                    |                         |
|    |          |   |   |   |          |              |   "type": "ovn-k8s-cni-overlay"            |                         |
|    |          |   |   |   |          |              | }                                          |                         |
+----+----------+---+---+---+----------+--------------+--------------------------------------------+-------------------------+
| 3  | island-q | V | V | V | Layer3   | 66.66.0.0/24 | {                                          | [POD] nginx3 (ovn-udn1) |
|    | pl3      |   |   |   |          | host /28     |   "cniVersion": "1.0.0",                   | [POD] p1-1 (ovn-udn1)   |
|    |          |   |   |   |          |              |   "joinSubnet": "100.65.0.0/16,fd99::/64", | [POD] p1-2 (ovn-udn1)   |
|    |          |   |   |   |          |              |   "name": "island-q_pl3",                  | [VM] c8kv1 (default)    |
|    |          |   |   |   |          |              |   "netAttachDefName": "island-q/pl3",      | [VM] c8kv2 (default)    |
|    |          |   |   |   |          |              |   "role": "primary",                       |                         |
|    |          |   |   |   |          |              |   "subnets": "66.66.0.0/24/28",            |                         |
|    |          |   |   |   |          |              |   "topology": "layer3",                    |                         |
|    |          |   |   |   |          |              |   "type": "ovn-k8s-cni-overlay"            |                         |
|    |          |   |   |   |          |              | }                                          |                         |
+----+----------+---+---+---+----------+--------------+--------------------------------------------+-------------------------+
| 4  | island-q | V | V |   | Layer3   | 66.66.1.0/24 | {                                          | [POD] p1-1 (net1)       |
|    | sl3      |   |   |   |          | host /28     |   "cniVersion": "1.0.0",                   | [POD] p1-2 (net1)       |
|    |          |   |   |   |          |              |   "name": "island-q_sl3",                  | [VM] c8kv1 (net1)       |
|    |          |   |   |   |          |              |   "netAttachDefName": "island-q/sl3",      | [VM] c8kv2 (net1)       |
|    |          |   |   |   |          |              |   "role": "secondary",                     |                         |
|    |          |   |   |   |          |              |   "subnets": "66.66.1.0/24/28",            |                         |
|    |          |   |   |   |          |              |   "topology": "layer3",                    |                         |
|    |          |   |   |   |          |              |   "type": "ovn-k8s-cni-overlay"            |                         |
|    |          |   |   |   |          |              | }                                          |                         |
+----+----------+---+---+---+----------+--------------+--------------------------------------------+-------------------------+

Legend: (C)reated, (A)llocated, (P)rimary
Filter: namespace, name, topology
View:   state
```

[[Back]](./README.md)