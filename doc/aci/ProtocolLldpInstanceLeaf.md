# Node Protocol - LLDP

## Show instance summary for all leaf nodes

```
# iserver get aci proto lldp --apic apic11 --role leaf --view summary

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

+---------------------+-------------+-----------+-----------------+------------------------+-----------+--------+
| Node                | Admin State | Hold Time | Init Delay Time | Transmission Frequency | Neighbors | Errors |
+---------------------+-------------+-----------+-----------------+------------------------+-----------+--------+
| pod-1/bl205-eu-spdc | enabled     | 120       | 2               | 30                     | 13        | X      | 
| pod-1/bl206-eu-spdc | enabled     | 120       | 2               | 30                     | 10        | X      | 
| pod-1/cl201-eu-spdc | enabled     | 120       | 2               | 30                     | 45        | V      | 
| pod-1/cl202-eu-spdc | enabled     | 120       | 2               | 30                     | 45        | X      | 
| pod-1/cl209-eu-spdc | enabled     | 120       | 2               | 30                     | 1         | X      | 
| pod-1/cl210-eu-spdc | enabled     | 120       | 2               | 30                     | 1         | X      | 
| pod-1/rl301-eu-spdc | enabled     | 120       | 2               | 30                     | 21        | V      | 
| pod-1/rl302-eu-spdc | enabled     | 120       | 2               | 30                     | 21        | V      | 
+---------------------+-------------+-----------+-----------------+------------------------+-----------+--------+
Interface context: lldp
```

Developer

```
# iserver get aci proto lldp --apic apic11 --role leaf --view summary

{
    "duration": 9667,
    "apic": {
        "read": true,
        "success": 26,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 25,
        "connect_time": 397,
        "disconnect_time": 0,
        "mo_time": 8974,
        "total_time": 9371
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

True	397	-	connect apic11o.emea-sp.cisco.com:443
True	404	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	389	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/lldp/inst
True	284	1	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-205/lldpInstStats
True	286	13	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	278	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-206/sys/lldp/inst
True	297	1	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-206/lldpInstStats
True	285	10	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-206/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	292	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/lldp/inst
True	285	1	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-201/lldpInstStats
True	304	45	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	282	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-202/sys/lldp/inst
True	281	1	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-202/lldpInstStats
True	296	45	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-202/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	470	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-209/sys/lldp/inst
True	506	1	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-209/lldpInstStats
True	622	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-209/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	557	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-210/sys/lldp/inst
True	289	1	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-210/lldpInstStats
True	293	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-210/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	281	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/lldp/inst
True	418	1	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-301/lldpInstStats
True	282	21	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	439	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-302/sys/lldp/inst
True	561	1	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-302/lldpInstStats
True	293	21	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-302/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
```

[[Back]](./ProtocolLldp.md)