# Node Interface - Virtual Port Channel (VPC)

## Address focused output

```
# iserver get aci intf vpc --apic dom:milan --node any --view address

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

+--------+----------------------+---------------+-----------+---------------------------------+------------+------------------+-------------------+-------------------+------------+------------------+-------------------+-----------+
| Apic   | Node                 | VPC Domain Id | Oper Role | Oper State                      | Peer State | VPC IP           | VPC MAC           | Local MAC         | Local Prio | Peer IP          | Peer MAC          | Peer Prio |
+--------+----------------------+---------------+-----------+---------------------------------+------------+------------------+-------------------+-------------------+------------+------------------+-------------------+-----------+
| apic11 | pod-1/bl205-eu-spdc  | 105           | master    | configured-master,vpcs-reinited | up         | 10.3.48.64/32    | 00:23:04:EE:BE:69 | 4C:71:0D:7E:84:C0 | 205        | 10.3.32.64/32    | 3C:13:CC:C9:ED:80 | 206       | 
| apic11 | pod-1/bl206-eu-spdc  | 105           | slave     | vpcs-reinited                   | up         | 10.3.48.64/32    | 00:23:04:EE:BE:69 | 3C:13:CC:C9:ED:80 | 206        | 10.3.192.64/32   | 4C:71:0D:7E:84:C0 | 205       | 
| apic11 | pod-1/cl201-eu-spdc  | 100           | master    | configured-master,vpcs-reinited | up         | 10.3.40.67/32    | 00:23:04:EE:BE:64 | 4C:71:0D:23:FA:E3 | 201        | 10.3.192.68/32   | 10:B3:D5:B5:62:C7 | 202       | 
| apic11 | pod-1/cl202-eu-spdc  | 100           | slave     | vpcs-reinited                   | up         | 10.3.40.67/32    | 00:23:04:EE:BE:64 | 10:B3:D5:B5:62:C7 | 202        | 10.3.192.67/32   | 4C:71:0D:23:FA:E3 | 201       | 
| apic11 | pod-1/rl301-eu-spdc  | 300           | master    | configured-master,vpcs-reinited | up         | 172.16.30.88/32  | 00:23:04:EE:BF:2C | A0:B4:39:4A:2B:DF | 301        | 172.16.30.121/32 | A0:B4:39:4A:2D:B3 | 302       | 
| apic11 | pod-1/rl302-eu-spdc  | 300           | slave     | vpcs-reinited                   | up         | 172.16.30.88/32  | 00:23:04:EE:BF:2C | A0:B4:39:4A:2D:B3 | 302        | 172.16.30.161/32 | A0:B4:39:4A:2B:DF | 301       | 
| apic21 | pod-1/bl2205-eu-spdc | 256           | master    | configured-master,vpcs-reinited | up         | 10.5.192.65/32   | 00:23:04:EE:BF:00 | 3C:13:CC:B9:EE:80 | 2205       | 10.5.216.64/32   | 64:3A:EA:DA:B2:10 | 2206      | 
| apic21 | pod-1/bl2206-eu-spdc | 256           | slave     | vpcs-reinited                   | up         | 10.5.192.65/32   | 00:23:04:EE:BF:00 | 64:3A:EA:DA:B2:10 | 2206       | 10.5.216.66/32   | 3C:13:CC:B9:EE:80 | 2205      | 
| apic21 | pod-1/cl2201-eu-spdc | 212           | master    | configured-master,vpcs-reinited | up         | 10.5.192.64/32   | 00:23:04:EE:BE:D4 | 68:9E:0B:13:63:40 | 2201       | 10.5.216.67/32   | E4:1F:7B:F4:87:70 | 2202      | 
| apic21 | pod-1/cl2202-eu-spdc | 212           | slave     | vpcs-reinited                   | up         | 10.5.192.64/32   | 00:23:04:EE:BE:D4 | E4:1F:7B:F4:87:70 | 2202       | 10.5.80.96/32    | 68:9E:0B:13:63:40 | 2201      | 
| apic21 | pod-1/cl2207-eu-spdc | 278           | master    | configured-master,vpcs-reinited | up         | 10.5.192.66/32   | 00:23:04:EE:BF:16 | A0:B4:39:71:F8:9F | 2207       | 10.5.240.35/32   | A0:B4:39:71:A8:30 | 2208      | 
| apic21 | pod-1/cl2208-eu-spdc | 278           | slave     | vpcs-reinited                   | up         | 10.5.192.66/32   | 00:23:04:EE:BF:16 | A0:B4:39:71:A8:30 | 2208       | 10.5.240.34/32   | A0:B4:39:71:F8:9F | 2207      | 
| apic21 | pod-1/cl2209-eu-spdc | 291           | master    | configured-master,vpcs-reinited | up         | 10.5.192.67/32   | 00:23:04:EE:BF:23 | 24:2A:04:E4:43:A0 | 2209       | 10.5.216.68/32   | 24:2A:04:99:C2:30 | 2210      | 
| apic21 | pod-1/cl2210-eu-spdc | 291           | slave     | vpcs-reinited                   | up         | 10.5.192.67/32   | 00:23:04:EE:BF:23 | 24:2A:04:99:C2:30 | 2210       | 10.5.216.65/32   | 24:2A:04:E4:43:A0 | 2209      | 
| apic21 | pod-1/rl2701-eu-spdc | 227           | master    | configured-master,vpcs-reinited | up         | 172.16.70.232/32 | 00:23:04:EE:BE:E3 | 00:2C:C8:9E:58:7D | 2701       | 172.16.70.25/32  | 2C:33:11:39:FC:AF | 2702      | 
| apic21 | pod-1/rl2702-eu-spdc | 227           | slave     | vpcs-reinited                   | up         | 172.16.70.232/32 | 00:23:04:EE:BE:E3 | 2C:33:11:39:FC:AF | 2702       | 172.16.70.209/32 | 00:2C:C8:9E:58:7D | 2701      | 
+--------+----------------------+---------------+-----------+---------------------------------+------------+------------------+-------------------+-------------------+------------+------------------+-------------------+-----------+
```

Developer

```
# iserver get aci intf vpc --apic dom:milan --node any --view address

{
    "duration": 8192,
    "apic": {
        "read": true,
        "success": 26,
        "failed": 0,
        "connect": 2,
        "disconnect": 0,
        "mo": 24,
        "connect_time": 761,
        "disconnect_time": 0,
        "mo_time": 7035,
        "total_time": 7796
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

True	392	-	connect apic11o.emea-sp.cisco.com
True	306	13	apic11o.emea-sp.cisco.com class fabricNode
True	369	-	connect apic21o.emea-sp.cisco.com
True	306	15	apic21o.emea-sp.cisco.com class fabricNode
True	291	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/vpcDom
True	291	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/vpcDom
True	340	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/vpcDom
True	287	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/vpcDom
True	288	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/vpcDom
True	277	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/vpcDom
True	279	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/vpcDom
True	286	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/vpcDom
True	280	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/vpcDom
True	285	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/vpcDom
True	291	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2205/vpcDom
True	293	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2206/vpcDom
True	326	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2201/vpcDom
True	281	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2202/vpcDom
True	296	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2207/vpcDom
True	297	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2208/vpcDom
True	294	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2209/vpcDom
True	291	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2210/vpcDom
True	299	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2701/vpcDom
True	285	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2702/vpcDom
True	283	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2101/vpcDom
True	283	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2102/vpcDom
```

[[Back]](./InterfaceVpc.md)