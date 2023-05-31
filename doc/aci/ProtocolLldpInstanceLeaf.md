# Node Protocol - LLDP

## Show instance summary for all leaf nodes

```
# iserver get aci proto lldp --apic apic11 --role leaf

Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+-------------+-----------+-----------------+------------------------+-----------+
| Node                | Admin State | Hold Time | Init Delay Time | Transmission Frequency | Neighbors |
+---------------------+-------------+-----------+-----------------+------------------------+-----------+
| pod-1/bl205-eu-spdc | enabled     | 120       | 2               | 30                     | 13        | 
| pod-1/bl206-eu-spdc | enabled     | 120       | 2               | 30                     | 10        | 
| pod-1/cl201-eu-spdc | enabled     | 120       | 2               | 30                     | 43        | 
| pod-1/cl202-eu-spdc | enabled     | 120       | 2               | 30                     | 43        | 
| pod-1/rl301-eu-spdc | enabled     | 120       | 2               | 30                     | 21        | 
| pod-1/rl302-eu-spdc | enabled     | 120       | 2               | 30                     | 21        | 
+---------------------+-------------+-----------+-----------------+------------------------+-----------+
```

Developer

```
# iserver get aci proto lldp --apic apic11 --role leaf

{
    "duration": 8298,
    "apic": {
        "read": true,
        "success": 20,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 19,
        "connect_time": 409,
        "disconnect_time": 0,
        "mo_time": 7533,
        "total_time": 7942
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
    }
}

Log: apic
----------

True	409	-	connect apic11o.emea-sp.cisco.com
True	1531	11	apic11o.emea-sp.cisco.com class fabricNode
True	314	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lldp/inst
True	312	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/lldpInstStats
True	318	13	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	304	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/lldp/inst
True	318	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/lldpInstStats
True	309	10	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	309	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lldp/inst
True	304	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/lldpInstStats
True	361	43	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	352	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lldp/inst
True	284	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/lldpInstStats
True	329	43	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	309	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/lldp/inst
True	349	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/lldpInstStats
True	338	21	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	335	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/lldp/inst
True	389	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/lldpInstStats
True	468	21	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
```

[[Back]](./ProtocolLldp.md)