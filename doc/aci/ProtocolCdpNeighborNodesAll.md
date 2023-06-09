# Node Protocol - CDP

## Show CDP neighbors details for selected nodes

```
# iserver get aci proto cdp --apic apic11 --node any

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: cl209-eu-spdc
- node: cl210-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc
- node: s101-eu-spdc
- node: s102-eu-spdc

+---------------------+-----------------+------------------------+-----------------+-----------------+--------+------+-------------+---------------------------------------+
| Node                | Local Interface | Neighbor System Name   | Platform        | Port            | Duplex | MTU  | Native VLAN | Capabilities                          |
+---------------------+-----------------+------------------------+-----------------+-----------------+--------+------+-------------+---------------------------------------+
| pod-1/bl205-eu-spdc | eth1/1          | FI-ucsb1-eu-spdc-A     | UCS-FI-6454     | Ethernet1/51    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/bl205-eu-spdc | eth1/2          | FI-ucsb1-eu-spdc-B     | UCS-FI-6454     | Ethernet1/51    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/bl205-eu-spdc | eth1/11         | HX1-eu-spdc-A          | UCS-FI-6454     | Ethernet1/51    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/bl205-eu-spdc | eth1/12         | HX1-eu-spdc-B          | UCS-FI-6454     | Ethernet1/51    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/bl205-eu-spdc | eth1/28         | Lisboa-54              | cisco NCS-5500  | TenGigE0/0/0/45 | full   | 0    |             | router                                | 
| pod-1/bl205-eu-spdc | eth1/27         | Yavin-129              | N9K-C93180YC-EX | Ethernet1/21    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/bl205-eu-spdc | eth1/24         | ipn-eu-spdc            | N9K-C9504       | Ethernet3/25    | full   | 9216 |             | router,stp-dispute,switch             | 
| pod-1/bl205-eu-spdc | mgmt0           | r22-eu-spdc            | N9K-C92348GC-X  | Ethernet1/27    | full   | 1500 | 12          | igmp-filter,router,stp-dispute,switch | 
| pod-1/bl206-eu-spdc | eth1/1          | FI-ucsb1-eu-spdc-A     | UCS-FI-6454     | Ethernet1/52    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/bl206-eu-spdc | eth1/2          | FI-ucsb1-eu-spdc-B     | UCS-FI-6454     | Ethernet1/52    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/bl206-eu-spdc | eth1/11         | HX1-eu-spdc-A          | UCS-FI-6454     | Ethernet1/52    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/bl206-eu-spdc | eth1/12         | HX1-eu-spdc-B          | UCS-FI-6454     | Ethernet1/52    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/bl206-eu-spdc | eth1/28         | Lisboa-54              | cisco NCS-5500  | TenGigE0/0/0/44 | full   | 0    |             | router                                | 
| pod-1/bl206-eu-spdc | eth1/27         | Yavin-129              | N9K-C93180YC-EX | Ethernet1/20    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/bl206-eu-spdc | eth1/24         | ipn-eu-spdc            | N9K-C9504       | Ethernet2/25    | full   | 9216 |             | router,stp-dispute,switch             | 
| pod-1/bl206-eu-spdc | mgmt0           | r22-eu-spdc            | N9K-C92348GC-X  | Ethernet1/28    | full   | 1500 | 12          | igmp-filter,router,stp-dispute,switch | 
| pod-1/cl201-eu-spdc | eth1/41         | esx1-eu-spdc           | VMware ESXi     | vmnic4          | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/38         | esx10-eu-spdc          | VMware ESXi     | vmnic10         | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/37         | esx11-eu-spdc          | VMware ESXi     | vmnic10         | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/36         | esx12-eu-spdc          | VMware ESXi     | vmnic11         | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/36         | esx12-eu-spdc          | VMware ESXi     | vmnic10         | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/35         | esx13-eu-spdc          | VMware ESXi     | vmnic10         | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/34         | esx14-eu-spdc          | VMware ESXi     | vmnic5          | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/42         | esx2-eu-spdc           | VMware ESXi     | vmnic10         | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/43         | esx3-eu-spdc           | VMware ESXi     | vmnic10         | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/44         | esx4-eu-spdc           | VMware ESXi     | vmnic10         | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/45         | esx5-eu-spdc           | VMware ESXi     | vmnic10         | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/46         | esx6-eu-spdc.cisco.com | VMware ESXi     | vmnic10         | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/47         | esx7-eu-spdc.cisco.com | VMware ESXi     | vmnic10         | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/40         | esx8-eu-spdc.cisco.com | VMware ESXi     | vmnic10         | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/39         | esx9-eu-spdc           | VMware ESXi     | vmnic10         | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/96         | ipn21-eu-spdc          | N9K-C93180YC-EX | Ethernet1/48    | full   | 1500 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/cl201-eu-spdc | mgmt0           | r22-eu-spdc            | N9K-C92348GC-X  | Ethernet1/25    | full   | 1500 | 12          | igmp-filter,router,stp-dispute,switch | 
| pod-1/cl202-eu-spdc | eth1/41         | esx1-eu-spdc           | VMware ESXi     | vmnic5          | full   | 9000 |             | switch                                | 
| pod-1/cl202-eu-spdc | eth1/38         | esx10-eu-spdc          | VMware ESXi     | vmnic11         | full   | 9000 |             | switch                                | 
| pod-1/cl202-eu-spdc | eth1/37         | esx11-eu-spdc          | VMware ESXi     | vmnic11         | full   | 9000 |             | switch                                | 
| pod-1/cl202-eu-spdc | eth1/35         | esx13-eu-spdc          | VMware ESXi     | vmnic11         | full   | 9000 |             | switch                                | 
| pod-1/cl202-eu-spdc | eth1/34         | esx14-eu-spdc          | VMware ESXi     | vmnic4          | full   | 9000 |             | switch                                | 
| pod-1/cl202-eu-spdc | eth1/42         | esx2-eu-spdc           | VMware ESXi     | vmnic11         | full   | 9000 |             | switch                                | 
| pod-1/cl202-eu-spdc | eth1/43         | esx3-eu-spdc           | VMware ESXi     | vmnic11         | full   | 9000 |             | switch                                | 
| pod-1/cl202-eu-spdc | eth1/44         | esx4-eu-spdc           | VMware ESXi     | vmnic11         | full   | 9000 |             | switch                                | 
| pod-1/cl202-eu-spdc | eth1/45         | esx5-eu-spdc           | VMware ESXi     | vmnic11         | full   | 9000 |             | switch                                | 
| pod-1/cl202-eu-spdc | eth1/46         | esx6-eu-spdc.cisco.com | VMware ESXi     | vmnic11         | full   | 9000 |             | switch                                | 
| pod-1/cl202-eu-spdc | eth1/47         | esx7-eu-spdc.cisco.com | VMware ESXi     | vmnic11         | full   | 9000 |             | switch                                | 
| pod-1/cl202-eu-spdc | eth1/40         | esx8-eu-spdc.cisco.com | VMware ESXi     | vmnic11         | full   | 9000 |             | switch                                | 
| pod-1/cl202-eu-spdc | eth1/39         | esx9-eu-spdc           | VMware ESXi     | vmnic11         | full   | 9000 |             | switch                                | 
| pod-1/cl202-eu-spdc | eth1/96         | ipn22-eu-spdc          | N9K-C93180YC-EX | Ethernet1/48    | full   | 1500 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/cl202-eu-spdc | mgmt0           | r22-eu-spdc            | N9K-C92348GC-X  | Ethernet1/26    | full   | 1500 | 12          | igmp-filter,router,stp-dispute,switch | 
| pod-1/rl301-eu-spdc | eth1/29         | Berlin-35.cisco.com    | cisco NCS-5500  | TenGigE0/0/0/29 | full   | 0    |             | router                                | 
| pod-1/rl301-eu-spdc | eth1/4          | FI-ucsb1-eu-spdc-A     | UCS-FI-6454     | Ethernet1/46    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/rl301-eu-spdc | eth1/3          | FI-ucsb1-eu-spdc-B     | UCS-FI-6454     | Ethernet1/46    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/rl301-eu-spdc | mgmt0           | r23-eu-spdc            | N9K-C92348GC-X  | Ethernet1/41    | full   | 1500 | 12          | igmp-filter,router,stp-dispute,switch | 
| pod-1/rl302-eu-spdc | eth1/29         | Berlin-35.cisco.com    | cisco NCS-5500  | TenGigE0/0/0/28 | full   | 0    |             | router                                | 
| pod-1/rl302-eu-spdc | eth1/4          | FI-ucsb1-eu-spdc-A     | UCS-FI-6454     | Ethernet1/45    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/rl302-eu-spdc | eth1/3          | FI-ucsb1-eu-spdc-B     | UCS-FI-6454     | Ethernet1/45    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/rl302-eu-spdc | mgmt0           | r23-eu-spdc            | N9K-C92348GC-X  | Ethernet1/42    | full   | 1500 | 12          | igmp-filter,router,stp-dispute,switch | 
| pod-1/s101-eu-spdc  | mgmt0           | r23-eu-spdc            | N9K-C92348GC-X  | Ethernet1/39    | full   | 1500 | 12          | igmp-filter,router,stp-dispute,switch | 
| pod-1/s102-eu-spdc  | mgmt0           | r23-eu-spdc            | N9K-C92348GC-X  | Ethernet1/40    | full   | 1500 | 12          | igmp-filter,router,stp-dispute,switch | 
+---------------------+-----------------+------------------------+-----------------+-----------------+--------+------+-------------+---------------------------------------+
```

Developer

```
# iserver get aci proto cdp --apic apic11 --node any

{
    "duration": 12999,
    "apic": {
        "read": true,
        "success": 32,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 31,
        "connect_time": 516,
        "disconnect_time": 0,
        "mo_time": 10980,
        "total_time": 11496
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

True	516	-	connect apic11o.emea-sp.cisco.com
True	332	13	apic11o.emea-sp.cisco.com class fabricNode
True	310	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/cdp/inst
True	301	8	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	313	29	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	305	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/cdp/inst
True	332	8	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	364	29	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	331	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/cdp/inst
True	335	17	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	416	100	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	364	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/cdp/inst
True	373	15	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	374	100	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	342	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys/cdp/inst
True	342	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	360	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	326	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys/cdp/inst
True	339	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	340	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	362	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/cdp/inst
True	360	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	376	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	646	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/cdp/inst
True	465	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	371	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	333	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/cdp/inst
True	312	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	308	17	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	321	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/cdp/inst
True	316	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	311	17	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
```

[[Back]](./ProtocolCdp.md)