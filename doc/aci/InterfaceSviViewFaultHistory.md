# Node Interface - SVI

## Fault history view

```
# iserver get aci intf svi
    --apic apic21
    --when 180d
    --node cl2208-eu-spdc
    --name vlan30
    --view hfault

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: cl2208-eu-spdc

Interface SVI - Fault Records last 180d [#10]
---------------------------------------------

+----------------------+------+---------+-------------------+-------------------------------+-----------+--------------------------------------------------------------------------------+
| Node                 | Sev  | Code    | Cause             | Created Time                  | Lifecycle | Description                                                                    |
+----------------------+------+---------+-------------------+-------------------------------+-----------+--------------------------------------------------------------------------------+
| pod-1/cl2208-eu-spdc | Warn | F112128 | threshold-crossed | 2023-05-31T22:25:19.050+02:00 | raised    | TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 16 raised above  | 
|                      |      |         |                   |                               |           | threshold 10                                                                   | 
| pod-1/cl2208-eu-spdc | --   | F112128 | threshold-crossed | 2023-05-31T23:42:20.812+02:00 | retaining | TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 8 fell below     | 
|                      |      |         |                   |                               |           | threshold 10                                                                   | 
| pod-1/cl2208-eu-spdc | Warn | F112128 | threshold-crossed | 2023-05-31T23:56:23.944+02:00 | raised    | TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 10 raised above  | 
|                      |      |         |                   |                               |           | threshold 10                                                                   | 
| pod-1/cl2208-eu-spdc | --   | F112128 | threshold-crossed | 2023-06-07T13:40:41.216+02:00 | retaining | TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 0 fell below     | 
|                      |      |         |                   |                               |           | threshold 10                                                                   | 
| pod-1/cl2208-eu-spdc | --   | F112128 | threshold-crossed | 2023-06-07T14:40:55.223+02:00 |           | TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 0 fell below     | 
|                      |      |         |                   |                               |           | threshold 10                                                                   | 
| pod-1/cl2208-eu-spdc | Warn | F112128 | threshold-crossed | 2023-06-18T09:18:08.756+02:00 | raised    | TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 10 raised above  | 
|                      |      |         |                   |                               |           | threshold 10                                                                   | 
| pod-1/cl2208-eu-spdc | --   | F112128 | threshold-crossed | 2023-07-27T07:20:19.228+02:00 | retaining | TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 0 fell below     | 
|                      |      |         |                   |                               |           | threshold 10                                                                   | 
| pod-1/cl2208-eu-spdc | Warn | F112128 | threshold-crossed | 2023-07-27T07:40:22.309+02:00 | raised    | TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 12 raised above  | 
|                      |      |         |                   |                               |           | threshold 10                                                                   | 
| pod-1/cl2208-eu-spdc | --   | F112128 | threshold-crossed | 2023-07-27T08:00:28.485+02:00 | retaining | TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 4 fell below     | 
|                      |      |         |                   |                               |           | threshold 10                                                                   | 
| pod-1/cl2208-eu-spdc | --   | F112128 | threshold-crossed | 2023-07-27T09:00:43.994+02:00 |           | TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 4 fell below     | 
|                      |      |         |                   |                               |           | threshold 10                                                                   | 
+----------------------+------+---------+-------------------+-------------------------------+-----------+--------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci intf svi
    --apic apic21
    --when 180d
    --node cl2208-eu-spdc
    --name vlan30
    --view hfault

{
    "duration": 2856,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 366,
        "disconnect_time": 0,
        "mo_time": 2275,
        "total_time": 2641
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

True	366	-	connect apic21o.emea-sp.cisco.com:443
True	289	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	376	19	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	259	29	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/ipv4Addr
True	1351	262	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
```

[[Back]](./InterfaceSvi.md)