# Node Interface - SVI

## Diagnostics focused output i.e. faults and events

```
# iserver get aci intf svi
    --apic apic21
    --node cl2208-eu-spdc
    --name vlan30
    --view diag
    --when 180d

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: cl2208-eu-spdc

Interface SVI Event Logs last 180d [#8]
---------------------------------------

+----------------------+-----------+------+----------+-----------------+-------------------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------+
| Node                 | Interface | Sev  | Code     | Cause           | Created Time                  | Description                                               | Change Set                                                                      |
+----------------------+-----------+------+----------+-----------------+-------------------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------+
| pod-1/cl2208-eu-spdc | vlan30    | Info | E4208074 | if-state-change | 2023-05-31T22:20:45.659+02:00 | Line Protocol on Interface, changed state to up connected | operSt (New: up), operStQual (New: none), vlanT (New: bd-external)              | 
+----------------------+-----------+------+----------+-----------------+-------------------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------+
| pod-1/cl2208-eu-spdc | vlan30    | Info | E4208074 | if-state-change | 2023-05-31T22:20:45.131+02:00 | Line Protocol on Interface, changed state to up connected | iod (New: 109), operSt (New: up), operStQual (New: none), osSum (New: failed),  | 
|                      |           |      |          |                 |                               |                                                           | vlanT (New: bd-external), vmacChgQual (New: )                                   | 
+----------------------+-----------+------+----------+-----------------+-------------------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------+
| pod-1/cl2208-eu-spdc | vlan30    | Info | E4208074 | if-state-change | 2023-05-31T22:20:46.437+02:00 | Line Protocol on Interface, changed state to up connected | operSt (New: up), operStQual (New: none)                                        | 
+----------------------+-----------+------+----------+-----------------+-------------------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------+
| pod-1/cl2208-eu-spdc | vlan30    | Info | E4208074 | if-state-change | 2023-05-31T22:20:46.522+02:00 | Line Protocol on Interface, changed state to up connected | operSt (New: up), operStQual (New: none)                                        | 
+----------------------+-----------+------+----------+-----------------+-------------------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------+
| pod-1/cl2208-eu-spdc | vlan30    | Info | E4208074 | if-state-change | 2023-06-18T09:15:12.412+02:00 | Line Protocol on Interface, changed state to up connected | iod (New: 100), operSt (New: up), operStQual (New: none), osSum (New: failed),  | 
|                      |           |      |          |                 |                               |                                                           | vlanT (New: bd-external), vmacChgQual (New: )                                   | 
+----------------------+-----------+------+----------+-----------------+-------------------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------+
| pod-1/cl2208-eu-spdc | vlan30    | Info | E4208074 | if-state-change | 2023-06-18T09:15:13.648+02:00 | Line Protocol on Interface, changed state to up connected | operSt (New: up), operStQual (New: none), vlanT (New: bd-external)              | 
+----------------------+-----------+------+----------+-----------------+-------------------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------+
| pod-1/cl2208-eu-spdc | vlan30    | Info | E4208074 | if-state-change | 2023-06-18T09:15:13.850+02:00 | Line Protocol on Interface, changed state to up connected | operSt (New: up), operStQual (New: none)                                        | 
+----------------------+-----------+------+----------+-----------------+-------------------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------+
| pod-1/cl2208-eu-spdc | vlan30    | Info | E4208074 | if-state-change | 2023-06-18T09:15:13.914+02:00 | Line Protocol on Interface, changed state to up connected | operSt (New: up), operStQual (New: none)                                        | 
+----------------------+-----------+------+----------+-----------------+-------------------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------+

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
    --view diag
    --when 180d

{
    "duration": 5874,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 404,
        "disconnect_time": 0,
        "mo_time": 4289,
        "total_time": 4693
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

True	404	-	connect apic21o.emea-sp.cisco.com:443
True	312	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	407	20	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	328	29	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/ipv4Addr
True	1729	248	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=faults,fault-records,no-scoped,subtree
True	1513	1586	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=event-logs,no-scoped,subtree
```

[[Back]](./InterfaceSvi.md)