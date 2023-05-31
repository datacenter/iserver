# Node

## Physical interface summary output

```
# iserver get aci node --apic apic11 --view intf

Apic: apic11

+---------------------+-----------------------+---------+-----------+-------+-------+---------+---------+--------+---------+---------+
| Node Name           | Ports (Up/Down/Total) | Uplink  | Downlink  | 100M  | 1G    | 10G     | 25G     | 40G    | 100G    | 400G    |
+---------------------+-----------------------+---------+-----------+-------+-------+---------+---------+--------+---------+---------+
| pod-1/bl205-eu-spdc | 10/26/36              | 2/6/8   | 8/20/28   | 0/0/0 | 0/0/0 | 2/0/2   | 0/0/0   | 5/6/11 | 1/14/15 | 2/6/8   | 
| pod-1/bl206-eu-spdc | 7/29/36               | 2/6/8   | 5/23/28   | 0/0/0 | 0/0/0 | 2/0/2   | 0/0/0   | 2/4/6  | 1/19/20 | 2/6/8   | 
| pod-1/cl201-eu-spdc | 61/47/108             | 2/4/6   | 59/43/102 | 0/0/0 | 5/0/5 | 54/1/55 | 0/34/34 | 0/0/0  | 2/10/12 | 0/0/0   | 
| pod-1/cl202-eu-spdc | 57/51/108             | 2/4/6   | 55/47/102 | 0/0/0 | 2/0/2 | 53/1/54 | 0/38/38 | 0/0/0  | 2/9/11  | 0/0/0   | 
| pod-1/rl301-eu-spdc | 20/32/52              | 3/3/6   | 17/29/46  | 0/0/0 | 0/0/0 | 18/2/20 | 0/0/0   | 2/0/2  | 0/25/25 | 0/0/0   | 
| pod-1/rl302-eu-spdc | 20/32/52              | 3/3/6   | 17/29/46  | 0/0/0 | 0/0/0 | 18/2/20 | 0/0/0   | 2/0/2  | 0/25/25 | 0/0/0   | 
| pod-1/s101-eu-spdc  | 5/11/16               | 5/11/16 | 0/0/0     | 0/0/0 | 0/0/0 | 0/0/0   | 0/0/0   | 0/0/0  | 3/0/3   | 2/11/13 | 
| pod-1/s102-eu-spdc  | 5/11/16               | 5/11/16 | 0/0/0     | 0/0/0 | 0/0/0 | 0/0/0   | 0/0/0   | 0/0/0  | 3/0/3   | 2/11/13 | 
+---------------------+-----------------------+---------+-----------+-------+-------+---------+---------+--------+---------+---------+
```

Developer

```
# iserver get aci node --apic apic11 --view intf

{
    "duration": 7019,
    "apic": {
        "read": true,
        "success": 18,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 17,
        "connect_time": 437,
        "disconnect_time": 0,
        "mo_time": 5753,
        "total_time": 6190
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

True	437	-	connect apic11o.emea-sp.cisco.com
True	307	11	apic11o.emea-sp.cisco.com class fabricNode
True	315	52	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/l1PhysIf
True	322	48	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/ethpmPhysIf
True	402	108	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l1PhysIf
True	409	108	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ethpmPhysIf
True	316	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/l1PhysIf
True	304	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/ethpmPhysIf
True	323	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/l1PhysIf
True	328	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/ethpmPhysIf
True	313	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/l1PhysIf
True	325	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/ethpmPhysIf
True	355	52	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/l1PhysIf
True	345	48	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/ethpmPhysIf
True	350	108	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l1PhysIf
True	392	108	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ethpmPhysIf
True	322	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	325	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
```

[[Back]](./Node.md)