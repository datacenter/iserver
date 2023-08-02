# Node Interface - Management

## Default output

```
# iserver get aci intf mgmt --apic apic21 --node any

Apic: apic21 (mode:online, cache:off)
Pod: 1
- node: bl2205-eu-spdc
- node: bl2206-eu-spdc
- node: cl2201-eu-spdc
- node: cl2202-eu-spdc
- node: cl2207-eu-spdc
- node: cl2208-eu-spdc
- node: cl2209-eu-spdc
- node: cl2210-eu-spdc
- node: rl2701-eu-spdc
- node: rl2702-eu-spdc
- node: s2101-eu-spdc
- node: s2102-eu-spdc

Interface Management - State [#12]
----------------------------------

+----------------------+--------+---------+-----------+-------+-----------+------+------------------+--------+------+-------+-------------------------------+
| Node                 | Health | Faults  | Interface | Admin | Switching | Oper | Auto Negotiation | Duplex | MTU  | Speed | Last Link State Change        |
+----------------------+--------+---------+-----------+-------+-----------+------+------------------+--------+------+-------+-------------------------------+
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | mgmt0     | up    | disabled  | up   | on               | full   | 1500 | 1G    | 2023-06-18T09:38:34.501+02:00 | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | mgmt0     | up    | disabled  | up   | on               | full   | 1500 | 1G    | 2023-06-18T09:11:38.326+02:00 | 
| pod-1/cl2201-eu-spdc | 100    | 0 0 0 0 | mgmt0     | up    | disabled  | up   | on               | full   | 1500 | 1G    | 2023-06-18T09:36:45.595+02:00 | 
| pod-1/cl2202-eu-spdc | 100    | 0 0 0 0 | mgmt0     | up    | disabled  | up   | on               | full   | 1500 | 1G    | 2023-06-18T09:09:45.446+02:00 | 
| pod-1/cl2207-eu-spdc | 100    | 0 0 0 0 | mgmt0     | up    | disabled  | up   | on               | full   | 1500 | 1G    | 2023-06-18T09:36:23.019+02:00 | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | mgmt0     | up    | disabled  | up   | on               | full   | 1500 | 1G    | 2023-06-18T09:09:27.621+02:00 | 
| pod-1/cl2209-eu-spdc | 100    | 0 0 0 0 | mgmt0     | up    | disabled  | up   | on               | full   | 1500 | 1G    | 2023-07-21T16:50:37.464+02:00 | 
| pod-1/cl2210-eu-spdc | 100    | 0 0 0 0 | mgmt0     | up    | disabled  | up   | on               | full   | 1500 | 1G    | 2023-07-21T16:51:07.112+02:00 | 
| pod-1/rl2701-eu-spdc | 100    | 0 0 0 0 | mgmt0     | up    | disabled  | up   | on               | full   | 1500 | 1G    | 2023-06-18T09:37:20.467+02:00 | 
| pod-1/rl2702-eu-spdc | 100    | 0 0 0 0 | mgmt0     | up    | disabled  | up   | on               | full   | 1500 | 1G    | 2023-06-18T09:10:40.655+02:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | mgmt0     | up    | disabled  | up   | on               | full   | 1500 | 1G    | 2023-06-18T09:32:11.790+02:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | mgmt0     | up    | disabled  | up   | on               | full   | 1500 | 1G    | 2023-06-18T09:05:21.524+02:00 | 
+----------------------+--------+---------+-----------+-------+-----------+------+------------------+--------+------+-------+-------------------------------+
```

Developer

```
# iserver get aci intf mgmt --apic apic21 --node any

{
    "duration": 7720,
    "apic": {
        "read": true,
        "success": 26,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 25,
        "connect_time": 382,
        "disconnect_time": 0,
        "mo_time": 7000,
        "total_time": 7382
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

True	382	-	connect apic21o.emea-sp.cisco.com:443
True	305	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	290	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	265	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	306	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	279	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2206/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	278	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	273	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	290	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	270	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	273	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	278	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	282	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	270	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	275	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	268	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2209/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	311	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	297	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2210/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	274	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	262	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	298	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	259	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	268	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	269	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2101/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	292	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	268	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2102/sys query query-target=subtree&target-subtree-class=imMgmtIf
```

[[Back]](./InterfaceMgmt.md)