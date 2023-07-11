# Node Interface - SVI

## Fault focused output

```
# iserver get aci intf svi
    --apic apic21
    --node cl2208-eu-spdc
    --name vlan30
    --view fault
    --when 180d

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: cl2208-eu-spdc

Interface SVI Faults [#1]
-------------------------

+----------------------+-----------+------+---------+-------------------+-------------------------------+-----------+--------------------------------------------------------------------------------+
| Node                 | Interface | Sev  | Code    | Cause             | Created Time                  | Lifecycle | Description                                                                    |
+----------------------+-----------+------+---------+-------------------+-------------------------------+-----------+--------------------------------------------------------------------------------+
| pod-1/cl2208-eu-spdc | vlan30    | Warn | F112128 | threshold-crossed | 2023-06-18T09:18:08.755+02:00 | raised    | TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 10 raised above  | 
|                      |           |      |         |                   |                               |           | threshold 10                                                                   | 
+----------------------+-----------+------+---------+-------------------+-------------------------------+-----------+--------------------------------------------------------------------------------+

Interface SVI Fault Records last 180d [#6]
------------------------------------------

+----------------------+-----------+------+---------+-------------------+-------------------------------+-----------+--------------------------------------------------------------------------------+
| Node                 | Interface | Sev  | Code    | Cause             | Created Time                  | Lifecycle | Description                                                                    |
+----------------------+-----------+------+---------+-------------------+-------------------------------+-----------+--------------------------------------------------------------------------------+
| pod-1/cl2208-eu-spdc | vlan30    | Warn | F112128 | threshold-crossed | 2023-05-31T22:25:19.050+02:00 | raised    | TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 16 raised above  | 
|                      |           |      |         |                   |                               |           | threshold 10                                                                   | 
| pod-1/cl2208-eu-spdc | vlan30    | --   | F112128 | threshold-crossed | 2023-05-31T23:42:20.812+02:00 | retaining | TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 8 fell below     | 
|                      |           |      |         |                   |                               |           | threshold 10                                                                   | 
| pod-1/cl2208-eu-spdc | vlan30    | Warn | F112128 | threshold-crossed | 2023-05-31T23:56:23.944+02:00 | raised    | TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 10 raised above  | 
|                      |           |      |         |                   |                               |           | threshold 10                                                                   | 
| pod-1/cl2208-eu-spdc | vlan30    | --   | F112128 | threshold-crossed | 2023-06-07T13:40:41.216+02:00 | retaining | TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 0 fell below     | 
|                      |           |      |         |                   |                               |           | threshold 10                                                                   | 
| pod-1/cl2208-eu-spdc | vlan30    | --   | F112128 | threshold-crossed | 2023-06-07T14:40:55.223+02:00 |           | TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 0 fell below     | 
|                      |           |      |         |                   |                               |           | threshold 10                                                                   | 
| pod-1/cl2208-eu-spdc | vlan30    | Warn | F112128 | threshold-crossed | 2023-06-18T09:18:08.756+02:00 | raised    | TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 10 raised above  | 
|                      |           |      |         |                   |                               |           | threshold 10                                                                   | 
+----------------------+-----------+------+---------+-------------------+-------------------------------+-----------+--------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci intf svi
    --apic apic21
    --node cl2208-eu-spdc
    --name vlan30
    --view fault
    --when 180d

{
    "duration": 3780,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 455,
        "disconnect_time": 0,
        "mo_time": 2788,
        "total_time": 3243
    },
    "error": {
        "read": false,
        "lines": 0
    },
    "info": {
        "read": false,
        "lines": 0
    },
    "debug": {
        "read": false,
        "lines": 0
    },
    "cache_hits": 0
}

Log: apic
----------

True	455	-	connect apic21o.emea-sp.cisco.com:443
True	301	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	490	20	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	308	29	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/ipv4Addr
True	1689	248	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=faults,fault-records,no-scoped,subtree
```

[[Back]](./InterfaceSvi.md)