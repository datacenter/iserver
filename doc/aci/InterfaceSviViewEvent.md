# Node Interface - SVI

## Event focused output

```
# iserver get aci intf svi
    --apic apic21
    --node cl2208-eu-spdc
    --name vlan30
    --view event
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
```

Developer

```
# iserver get aci intf svi
    --apic apic21
    --node cl2208-eu-spdc
    --name vlan30
    --view event
    --when 180d

{
    "duration": 3493,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 404,
        "disconnect_time": 0,
        "mo_time": 2431,
        "total_time": 2835
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
True	396	20	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	297	29	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/ipv4Addr
True	1426	1586	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=event-logs,no-scoped,subtree
```

[[Back]](./InterfaceSvi.md)