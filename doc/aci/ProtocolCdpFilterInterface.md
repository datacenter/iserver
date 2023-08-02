# Node Protocol - CDP

## Filter by interface

```
# iserver get aci proto cdp
    --apic apic11
    --node cl201-eu-spdc
    --intf eth1/4*
    --view nei

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

Protocol CDP - Neighbor [#8]
----------------------------

+---------------------+-----------------+------------------------+-------------+---------+--------+------+--------------+
| Node                | Local Interface | Neighbor System Name   | Platform    | Port    | Duplex | MTU  | Capabilities |
+---------------------+-----------------+------------------------+-------------+---------+--------+------+--------------+
| pod-1/cl201-eu-spdc | eth1/41         | esx1-eu-spdc           | VMware ESXi | vmnic4  | full   | 9000 | switch       | 
| pod-1/cl201-eu-spdc | eth1/42         | esx2-eu-spdc           | VMware ESXi | vmnic10 | full   | 9000 | switch       | 
| pod-1/cl201-eu-spdc | eth1/43         | esx3-eu-spdc           | VMware ESXi | vmnic10 | full   | 9000 | switch       | 
| pod-1/cl201-eu-spdc | eth1/44         | esx4-eu-spdc           | VMware ESXi | vmnic10 | full   | 9000 | switch       | 
| pod-1/cl201-eu-spdc | eth1/45         | esx5-eu-spdc           | VMware ESXi | vmnic10 | full   | 9000 | switch       | 
| pod-1/cl201-eu-spdc | eth1/46         | esx6-eu-spdc.cisco.com | VMware ESXi | vmnic10 | full   | 9000 | switch       | 
| pod-1/cl201-eu-spdc | eth1/47         | esx7-eu-spdc.cisco.com | VMware ESXi | vmnic10 | full   | 9000 | switch       | 
| pod-1/cl201-eu-spdc | eth1/40         | esx8-eu-spdc.cisco.com | VMware ESXi | vmnic10 | full   | 9000 | switch       | 
+---------------------+-----------------+------------------------+-------------+---------+--------+------+--------------+
```

Developer

```
# iserver get aci proto cdp
    --apic apic11
    --node cl201-eu-spdc
    --intf eth1/4*
    --view nei

{
    "duration": 1091,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 393,
        "disconnect_time": 0,
        "mo_time": 576,
        "total_time": 969
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

True	393	-	connect apic11o.emea-sp.cisco.com:443
True	292	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	284	19	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
```

[[Back]](./ProtocolCdp.md)