# Node Interface - Loopback

## Filter by interface id

```
# iserver get aci intf lb --apic apic11 --node any --id lo8

Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc
- node: s101-eu-spdc
- node: s102-eu-spdc

+---------------------+-----------+-------------+------------+--------------------+-------------+---------------------+
| Node                | Interface | Admin State | Oper State | IPv4 Address       | Last Errors | Current Error Index |
+---------------------+-----------+-------------+------------+--------------------+-------------+---------------------+
| pod-1/bl205-eu-spdc | lo8       | up          | up         | 205.205.205.205/32 | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo8       | up          | up         | 122.122.122.122/32 | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo8       | up          | up         | 15.254.101.6/32    | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo8       | up          | up         | 15.254.101.9/32    | 0           | 4294967295          | 
| pod-1/rl301-eu-spdc | lo8       | up          | up         | 172.24.3.15/32     | 0           | 4294967295          | 
| pod-1/rl302-eu-spdc | lo8       | up          | up         | 132.132.132.132/32 | 0           | 4294967295          | 
| pod-1/s101-eu-spdc  | lo8       | up          | up         | 10.3.0.33/32       | 0           | 4294967295          | 
| pod-1/s102-eu-spdc  | lo8       | up          | up         | 10.3.0.33/32       | 0           | 4294967295          | 
+---------------------+-----------+-------------+------------+--------------------+-------------+---------------------+
```

Developer

```
# iserver get aci intf lb --apic apic11 --node any --id lo8

{
    "duration": 6481,
    "apic": {
        "read": true,
        "success": 18,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 17,
        "connect_time": 532,
        "disconnect_time": 0,
        "mo_time": 5462,
        "total_time": 5994
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

True	532	-	connect apic11o.emea-sp.cisco.com
True	311	11	apic11o.emea-sp.cisco.com class fabricNode
True	301	12	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	302	61	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4Addr
True	322	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	383	63	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/ipv4Addr
True	312	15	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	345	91	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ipv4Addr
True	297	15	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	335	90	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ipv4Addr
True	312	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	317	46	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/ipv4Addr
True	300	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	375	46	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/ipv4Addr
True	324	21	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	310	23	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/ipv4Addr
True	312	20	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	304	22	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/ipv4Addr
```

[[Back]](./InterfaceLoopback.md)