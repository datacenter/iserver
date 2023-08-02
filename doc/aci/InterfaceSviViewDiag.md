# Node Interface - SVI

## Diag view

```
# iserver get aci intf svi
    --apic apic21
    --when 180d
    --node cl2208-eu-spdc
    --name vlan30
    --view diag

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: cl2208-eu-spdc

Interface SVI - Faults [#0]
---------------------------
None

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

Interface SVI - Event Logs last 180d [#8]
-----------------------------------------

+----------------------+------+----------+-----------------+-------------------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------+
| Node                 | Sev  | Code     | Cause           | Created Time                  | Description                                               | Change Set                                                                      |
+----------------------+------+----------+-----------------+-------------------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------+
| pod-1/cl2208-eu-spdc | Info | E4208074 | if-state-change | 2023-05-31T22:20:45.659+02:00 | Line Protocol on Interface, changed state to up connected | operSt (New: up), operStQual (New: none), vlanT (New: bd-external)              | 
+----------------------+------+----------+-----------------+-------------------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------+
| pod-1/cl2208-eu-spdc | Info | E4208074 | if-state-change | 2023-05-31T22:20:45.131+02:00 | Line Protocol on Interface, changed state to up connected | iod (New: 109), operSt (New: up), operStQual (New: none), osSum (New: failed),  | 
|                      |      |          |                 |                               |                                                           | vlanT (New: bd-external), vmacChgQual (New: )                                   | 
+----------------------+------+----------+-----------------+-------------------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------+
| pod-1/cl2208-eu-spdc | Info | E4208074 | if-state-change | 2023-05-31T22:20:46.437+02:00 | Line Protocol on Interface, changed state to up connected | operSt (New: up), operStQual (New: none)                                        | 
+----------------------+------+----------+-----------------+-------------------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------+
| pod-1/cl2208-eu-spdc | Info | E4208074 | if-state-change | 2023-05-31T22:20:46.522+02:00 | Line Protocol on Interface, changed state to up connected | operSt (New: up), operStQual (New: none)                                        | 
+----------------------+------+----------+-----------------+-------------------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------+
| pod-1/cl2208-eu-spdc | Info | E4208074 | if-state-change | 2023-06-18T09:15:12.412+02:00 | Line Protocol on Interface, changed state to up connected | iod (New: 100), operSt (New: up), operStQual (New: none), osSum (New: failed),  | 
|                      |      |          |                 |                               |                                                           | vlanT (New: bd-external), vmacChgQual (New: )                                   | 
+----------------------+------+----------+-----------------+-------------------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------+
| pod-1/cl2208-eu-spdc | Info | E4208074 | if-state-change | 2023-06-18T09:15:13.648+02:00 | Line Protocol on Interface, changed state to up connected | operSt (New: up), operStQual (New: none), vlanT (New: bd-external)              | 
+----------------------+------+----------+-----------------+-------------------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------+
| pod-1/cl2208-eu-spdc | Info | E4208074 | if-state-change | 2023-06-18T09:15:13.850+02:00 | Line Protocol on Interface, changed state to up connected | operSt (New: up), operStQual (New: none)                                        | 
+----------------------+------+----------+-----------------+-------------------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------+
| pod-1/cl2208-eu-spdc | Info | E4208074 | if-state-change | 2023-06-18T09:15:13.914+02:00 | Line Protocol on Interface, changed state to up connected | operSt (New: up), operStQual (New: none)                                        | 
+----------------------+------+----------+-----------------+-------------------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------+

Interface SVI - Audit Logs last 180d [#0]
-----------------------------------------
None
```

Developer

```
# iserver get aci intf svi
    --apic apic21
    --when 180d
    --node cl2208-eu-spdc
    --name vlan30
    --view diag

{
    "duration": 5344,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 383,
        "disconnect_time": 0,
        "mo_time": 4444,
        "total_time": 4827
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

True	383	-	connect apic21o.emea-sp.cisco.com:443
True	287	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	379	19	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	270	29	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/ipv4Addr
True	415	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l2BD query rsp-subtree-include=faults,no-scoped,subtree
True	1312	262	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	1233	1547	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=event-logs,no-scoped,subtree
True	548	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/sviIf query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./InterfaceSvi.md)