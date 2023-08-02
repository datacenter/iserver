# Node Interface - Management

## Nei view

```
# iserver get aci intf mgmt --apic apic21 --node any --view nei

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

Interface Management - CDP/LLDP Neighbor [#12]
----------------------------------------------

+----------------------+-----------+-------+------+----------------+-------------------+--------------+-------------------------------+--------------+
| Node                 | Interface | Admin | Oper | CDP - Platform | CDP - System Name | CDP - Port   | LLDP - System Name            | LLDP - Port  |
+----------------------+-----------+-------+------+----------------+-------------------+--------------+-------------------------------+--------------+
| pod-1/bl2205-eu-spdc | mgmt0     | up    |      | N9K-C92348GC-X | r25-eu-spdc       | Ethernet1/41 | r25-eu-spdc.emea-sp.cisco.com | Ethernet1/41 | 
| pod-1/bl2206-eu-spdc | mgmt0     | up    |      | N9K-C92348GC-X | r25-eu-spdc       | Ethernet1/42 | r25-eu-spdc.emea-sp.cisco.com | Ethernet1/42 | 
| pod-1/cl2201-eu-spdc | mgmt0     | up    |      | N9K-C92348GC-X | r25-eu-spdc       | Ethernet1/37 | r25-eu-spdc.emea-sp.cisco.com | Ethernet1/37 | 
| pod-1/cl2202-eu-spdc | mgmt0     | up    |      | N9K-C92348GC-X | r25-eu-spdc       | Ethernet1/38 | r25-eu-spdc.emea-sp.cisco.com | Ethernet1/38 | 
| pod-1/cl2207-eu-spdc | mgmt0     | up    |      | N9K-C92348GC-X | r24-eu-spdc       | Ethernet1/41 | r24-eu-spdc.emea-sp.cisco.com | Ethernet1/41 | 
| pod-1/cl2208-eu-spdc | mgmt0     | up    |      | N9K-C92348GC-X | r24-eu-spdc       | Ethernet1/42 | r24-eu-spdc.emea-sp.cisco.com | Ethernet1/42 | 
| pod-1/cl2209-eu-spdc | mgmt0     | up    |      |                |                   |              |                               |              | 
| pod-1/cl2210-eu-spdc | mgmt0     | up    |      |                |                   |              |                               |              | 
| pod-1/rl2701-eu-spdc | mgmt0     | up    |      |                |                   |              |                               |              | 
| pod-1/rl2702-eu-spdc | mgmt0     | up    |      |                |                   |              |                               |              | 
| pod-1/s2101-eu-spdc  | mgmt0     | up    |      | N9K-C92348GC-X | r26-eu-spdc       | Ethernet1/37 | r26-eu-spdc.emea-sp.cisco.com | Ethernet1/37 | 
| pod-1/s2102-eu-spdc  | mgmt0     | up    |      | N9K-C92348GC-X | r26-eu-spdc       | Ethernet1/38 | r26-eu-spdc.emea-sp.cisco.com | Ethernet1/38 | 
+----------------------+-----------+-------+------+----------------+-------------------+--------------+-------------------------------+--------------+
```

Developer

```
# iserver get aci intf mgmt --apic apic21 --node any --view nei

{
    "duration": 11101,
    "apic": {
        "read": true,
        "success": 38,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 37,
        "connect_time": 383,
        "disconnect_time": 0,
        "mo_time": 10292,
        "total_time": 10675
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
True	303	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	281	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	269	7	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp&rsp-subtree-include=fault-count
True	274	10	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
True	279	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	285	7	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2206/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp&rsp-subtree-include=fault-count
True	274	10	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2206/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
True	273	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	265	2	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp&rsp-subtree-include=fault-count
True	280	26	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
True	275	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	265	2	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp&rsp-subtree-include=fault-count
True	302	26	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
True	283	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	307	3	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp&rsp-subtree-include=fault-count
True	276	18	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
True	302	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	280	3	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp&rsp-subtree-include=fault-count
True	289	17	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
True	267	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	260	0	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2209/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp&rsp-subtree-include=fault-count
True	256	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2209/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
True	269	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	264	0	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2210/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp&rsp-subtree-include=fault-count
True	265	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2210/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
True	267	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	272	2	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp&rsp-subtree-include=fault-count
True	289	16	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
True	298	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	286	2	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp&rsp-subtree-include=fault-count
True	280	16	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
True	313	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	268	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2101/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp&rsp-subtree-include=fault-count
True	260	9	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2101/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
True	271	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	267	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2102/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp&rsp-subtree-include=fault-count
True	278	9	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2102/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
```

[[Back]](./InterfaceMgmt.md)