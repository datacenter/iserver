# Node Interface - Management

## Addr view

```
# iserver get aci intf mgmt --apic apic21 --node any --view addr

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

Interface Management - Address [#12]
------------------------------------

+----------------------+-----------+-------+-----------------+
| Node                 | Interface | Admin | IP Address      |
+----------------------+-----------+-------+-----------------+
| pod-1/bl2205-eu-spdc | mgmt0     | up    | 10.58.50.145/27 | 
| pod-1/bl2206-eu-spdc | mgmt0     | up    | 10.58.50.146/27 | 
| pod-1/cl2201-eu-spdc | mgmt0     | up    | 10.58.50.141/27 | 
| pod-1/cl2202-eu-spdc | mgmt0     | up    | 10.58.50.142/27 | 
| pod-1/cl2207-eu-spdc | mgmt0     | up    | 10.58.50.147/27 | 
| pod-1/cl2208-eu-spdc | mgmt0     | up    | 10.58.50.148/27 | 
| pod-1/cl2209-eu-spdc | mgmt0     | up    | 10.58.50.137/27 | 
| pod-1/cl2210-eu-spdc | mgmt0     | up    | 10.58.50.138/27 | 
| pod-1/rl2701-eu-spdc | mgmt0     | up    | 10.58.50.149/27 | 
| pod-1/rl2702-eu-spdc | mgmt0     | up    | 10.58.50.150/27 | 
| pod-1/s2101-eu-spdc  | mgmt0     | up    | 10.58.50.151/27 | 
| pod-1/s2102-eu-spdc  | mgmt0     | up    | 10.58.50.152/27 | 
+----------------------+-----------+-------+-----------------+
```

Developer

```
# iserver get aci intf mgmt --apic apic21 --node any --view addr

{
    "duration": 11047,
    "apic": {
        "read": true,
        "success": 38,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 37,
        "connect_time": 387,
        "disconnect_time": 0,
        "mo_time": 10274,
        "total_time": 10661
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

True	387	-	connect apic21o.emea-sp.cisco.com:443
True	269	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	269	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	279	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/mgmt-[mgmt0]/fltCnts
True	256	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	275	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	270	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2206/sys/mgmt-[mgmt0]/fltCnts
True	258	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2206/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	273	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	276	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/mgmt-[mgmt0]/fltCnts
True	264	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	279	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	279	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/mgmt-[mgmt0]/fltCnts
True	272	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	275	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	338	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/mgmt-[mgmt0]/fltCnts
True	270	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	281	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	269	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/mgmt-[mgmt0]/fltCnts
True	277	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	274	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	279	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2209/sys/mgmt-[mgmt0]/fltCnts
True	255	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2209/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	263	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	283	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2210/sys/mgmt-[mgmt0]/fltCnts
True	270	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2210/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	320	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	313	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/mgmt-[mgmt0]/fltCnts
True	294	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	270	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	272	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/mgmt-[mgmt0]/fltCnts
True	278	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	314	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	275	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2101/sys/mgmt-[mgmt0]/fltCnts
True	277	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2101/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	277	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	267	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2102/sys/mgmt-[mgmt0]/fltCnts
True	264	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2102/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
```

[[Back]](./InterfaceMgmt.md)