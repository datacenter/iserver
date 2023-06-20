# Node

## Physical interface summary output

```
# iserver get aci node --apic apic11 --view intf

Apic: apic11 (mode:online, cache:off)

+---------------------+-----------------------+---------+-----------+-------+-------+---------+---------+--------+---------+---------+
| Node Name           | Ports (Up/Down/Total) | Uplink  | Downlink  | 100M  | 1G    | 10G     | 25G     | 40G    | 100G    | 400G    |
+---------------------+-----------------------+---------+-----------+-------+-------+---------+---------+--------+---------+---------+
| pod-1/bl205-eu-spdc | 10/26/36              | 2/6/8   | 8/20/28   | 0/0/0 | 0/0/0 | 2/0/2   | 0/0/0   | 5/6/11 | 1/14/15 | 2/6/8   | 
| pod-1/bl206-eu-spdc | 7/29/36               | 2/6/8   | 5/23/28   | 0/0/0 | 0/0/0 | 2/0/2   | 0/0/0   | 2/4/6  | 1/19/20 | 2/6/8   | 
| pod-1/cl201-eu-spdc | 61/47/108             | 2/4/6   | 59/43/102 | 0/0/0 | 5/0/5 | 54/1/55 | 0/36/36 | 0/0/0  | 2/10/12 | 0/0/0   | 
| pod-1/cl202-eu-spdc | 57/51/108             | 2/4/6   | 55/47/102 | 0/0/0 | 2/0/2 | 53/1/54 | 0/40/40 | 0/0/0  | 2/10/12 | 0/0/0   | 
| pod-1/cl209-eu-spdc | 1/35/36               | 1/7/8   | 0/28/28   | 0/0/0 | 0/0/0 | 0/0/0   | 0/0/0   | 0/2/2  | 1/26/27 | 0/7/7   | 
| pod-1/cl210-eu-spdc | 1/35/36               | 1/7/8   | 0/28/28   | 0/0/0 | 0/0/0 | 0/0/0   | 0/0/0   | 0/2/2  | 1/26/27 | 0/7/7   | 
| pod-1/rl301-eu-spdc | 20/32/52              | 3/3/6   | 17/29/46  | 0/0/0 | 0/0/0 | 18/2/20 | 0/0/0   | 2/0/2  | 0/25/25 | 0/0/0   | 
| pod-1/rl302-eu-spdc | 20/32/52              | 3/3/6   | 17/29/46  | 0/0/0 | 0/0/0 | 18/2/20 | 0/0/0   | 2/0/2  | 0/25/25 | 0/0/0   | 
| pod-1/s101-eu-spdc  | 6/10/16               | 6/10/16 | 0/0/0     | 0/0/0 | 0/0/0 | 0/0/0   | 0/0/0   | 0/0/0  | 4/0/4   | 2/10/12 | 
| pod-1/s102-eu-spdc  | 6/10/16               | 6/10/16 | 0/0/0     | 0/0/0 | 0/0/0 | 0/0/0   | 0/0/0   | 0/0/0  | 4/0/4   | 2/10/12 | 
+---------------------+-----------------------+---------+-----------+-------+-------+---------+---------+--------+---------+---------+
```

Developer

```
# iserver get aci node --apic apic11 --view intf

{
    "duration": 9985,
    "apic": {
        "read": true,
        "success": 22,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 21,
        "connect_time": 475,
        "disconnect_time": 0,
        "mo_time": 7866,
        "total_time": 8341
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

True	475	-	connect apic11o.emea-sp.cisco.com:443
True	324	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	343	52	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-302/l1PhysIf
True	357	48	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-302/ethpmPhysIf
True	351	36	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-209/l1PhysIf
True	412	36	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-209/ethpmPhysIf
True	345	36	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-210/l1PhysIf
True	356	36	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-210/ethpmPhysIf
True	346	108	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-201/l1PhysIf
True	427	108	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-201/ethpmPhysIf
True	384	36	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-206/l1PhysIf
True	343	36	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-206/ethpmPhysIf
True	322	16	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-102/l1PhysIf
True	378	16	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-102/ethpmPhysIf
True	362	16	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-101/l1PhysIf
True	378	16	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-101/ethpmPhysIf
True	386	52	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-301/l1PhysIf
True	392	48	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-301/ethpmPhysIf
True	472	108	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-202/l1PhysIf
True	383	108	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-202/ethpmPhysIf
True	404	36	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-205/l1PhysIf
True	401	36	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-205/ethpmPhysIf
```

[[Back]](./Node.md)