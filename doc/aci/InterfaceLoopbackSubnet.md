# Node Interface - Loopback

## Filter by ip subnet

```
# iserver get aci intf lb --apic apic11 --node any --subnet 15.0.0.0/8

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

+---------------------+-----------+-------------+------------+-------------------+-------------+---------------------+
| Node                | Interface | Admin State | Oper State | IPv4 Address      | Last Errors | Current Error Index |
+---------------------+-----------+-------------+------------+-------------------+-------------+---------------------+
| pod-1/cl201-eu-spdc | lo6       | up          | up         | 15.254.101.8/32   | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo7       | up          | up         | 15.254.101.6/32   | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo8       | up          | up         | 15.254.101.0/32   | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo9       | up          | up         | 15.254.101.4/32   | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo10      | up          | up         | 15.254.101.99/32  | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo12      | up          | up         | 15.254.101.2/32   | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo4       | up          | up         | 15.254.101.9/32   | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo5       | up          | up         | 15.254.101.5/32   | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo6       | up          | up         | 15.254.101.100/32 | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo7       | up          | up         | 15.254.101.1/32   | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo11      | up          | up         | 15.254.101.7/32   | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo12      | up          | up         | 15.254.101.3/32   | 0           | 4294967295          | 
+---------------------+-----------+-------------+------------+-------------------+-------------+---------------------+
```

Developer

```
# iserver get aci intf lb --apic apic11 --node any --subnet 15.0.0.0/8

{
    "duration": 7232,
    "apic": {
        "read": true,
        "success": 22,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 21,
        "connect_time": 421,
        "disconnect_time": 0,
        "mo_time": 6407,
        "total_time": 6828
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

True	421	-	connect apic11o.emea-sp.cisco.com
True	318	13	apic11o.emea-sp.cisco.com class fabricNode
True	315	12	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	289	61	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4Addr
True	304	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	288	63	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/ipv4Addr
True	297	15	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	292	91	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ipv4Addr
True	293	15	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	297	90	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ipv4Addr
True	281	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	313	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/ipv4Addr
True	311	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	299	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/ipv4Addr
True	338	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	331	46	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/ipv4Addr
True	341	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	303	46	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/ipv4Addr
True	298	21	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	288	23	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/ipv4Addr
True	307	20	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	304	22	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/ipv4Addr
```

[[Back]](./InterfaceLoopback.md)