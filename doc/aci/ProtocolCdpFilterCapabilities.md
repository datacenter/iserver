# Node Protocol - CDP

## Filter CDP neighbors by neighbor's advertised capabilities

```
# iserver get aci proto cdp
    --apic apic11
    --node cl201-eu-spdc
    --cap *switch*
    --view nei

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
# iserver get aci proto cdp
    --apic apic11
    --node cl201-eu-spdc
    --cap *switch*
    --view nei

{
    "duration": 1107,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 388,
        "disconnect_time": 0,
        "mo_time": 569,
        "total_time": 957
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

True	388	-	connect apic11o.emea-sp.cisco.com:443
True	292	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	277	19	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
```

[[Back]](./ProtocolCdp.md)