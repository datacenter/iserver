# Node Protocol - CDP

## Default output

```
# iserver get aci proto cdp --apic apic11 --node cl201-eu-spdc --view nei

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

Protocol CDP - Neighbor [#19]
-----------------------------

+---------------------+-----------------+------------------------+-----------------+--------------+--------+------+-------------+---------------------------------------+
| Node                | Local Interface | Neighbor System Name   | Platform        | Port         | Duplex | MTU  | Native VLAN | Capabilities                          |
+---------------------+-----------------+------------------------+-----------------+--------------+--------+------+-------------+---------------------------------------+
| pod-1/cl201-eu-spdc | eth1/32         | esx00-eu-spdc          | VMware ESXi     | vmnic4       | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/31         | esx01-eu-spdc          | VMware ESXi     | vmnic6       | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/41         | esx1-eu-spdc           | VMware ESXi     | vmnic4       | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/38         | esx10-eu-spdc          | VMware ESXi     | vmnic10      | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/37         | esx11-eu-spdc          | VMware ESXi     | vmnic10      | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/36         | esx12-eu-spdc          | VMware ESXi     | vmnic11      | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/36         | esx12-eu-spdc          | VMware ESXi     | vmnic10      | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/35         | esx13-eu-spdc          | VMware ESXi     | vmnic10      | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/34         | esx14-eu-spdc          | VMware ESXi     | vmnic5       | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/42         | esx2-eu-spdc           | VMware ESXi     | vmnic10      | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/43         | esx3-eu-spdc           | VMware ESXi     | vmnic10      | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/44         | esx4-eu-spdc           | VMware ESXi     | vmnic10      | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/45         | esx5-eu-spdc           | VMware ESXi     | vmnic10      | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/46         | esx6-eu-spdc.cisco.com | VMware ESXi     | vmnic10      | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/47         | esx7-eu-spdc.cisco.com | VMware ESXi     | vmnic10      | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/40         | esx8-eu-spdc.cisco.com | VMware ESXi     | vmnic10      | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/39         | esx9-eu-spdc           | VMware ESXi     | vmnic10      | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/96         | ipn21-eu-spdc          | N9K-C93180YC-EX | Ethernet1/48 | full   | 1500 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/cl201-eu-spdc | mgmt0           | r22-eu-spdc            | N9K-C92348GC-X  | Ethernet1/25 | full   | 1500 | 12          | igmp-filter,router,stp-dispute,switch | 
+---------------------+-----------------+------------------------+-----------------+--------------+--------+------+-------------+---------------------------------------+
```

Developer

```
# iserver get aci proto cdp --apic apic11 --node cl201-eu-spdc --view nei

{
    "duration": 1242,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 406,
        "disconnect_time": 0,
        "mo_time": 614,
        "total_time": 1020
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

True	406	-	connect apic11o.emea-sp.cisco.com:443
True	308	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	306	19	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
```

[[Back]](./ProtocolBgp.md)