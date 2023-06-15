# Node Interface - Loopback

## Filter by interface id

```
# iserver get aci intf lb --apic apic11 --node any --id lo8

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

+---------------------+-----------+-------------+------------+--------------------+-------------+---------------------+
| Node                | Interface | Admin State | Oper State | IPv4 Address       | Last Errors | Current Error Index |
+---------------------+-----------+-------------+------------+--------------------+-------------+---------------------+
| pod-1/bl205-eu-spdc | lo8       | up          | up         | 205.205.205.205/32 | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo8       | up          | up         | 172.24.0.14/32     | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo8       | up          | up         | 15.254.101.0/32    | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo8       | up          | up         | 202.202.202.202/32 | 0           | 4294967295          | 
| pod-1/rl301-eu-spdc | lo8       | up          | up         | 131.131.131.131/32 | 0           | 4294967295          | 
| pod-1/rl302-eu-spdc | lo8       | up          | up         | 172.24.3.14/32     | 0           | 4294967295          | 
| pod-1/s101-eu-spdc  | lo8       | up          | up         | 172.16.10.1/32     | 0           | 4294967295          | 
| pod-1/s102-eu-spdc  | lo8       | up          | up         | 172.16.10.1/32     | 0           | 4294967295          | 
+---------------------+-----------+-------------+------------+--------------------+-------------+---------------------+
```

Developer

```
# iserver get aci intf lb --apic apic11 --node any --id lo8

{
    "duration": 7163,
    "apic": {
        "read": true,
        "success": 22,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 21,
        "connect_time": 389,
        "disconnect_time": 0,
        "mo_time": 6353,
        "total_time": 6742
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

True	389	-	connect apic11o.emea-sp.cisco.com
True	295	13	apic11o.emea-sp.cisco.com class fabricNode
True	282	12	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	312	61	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4Addr
True	302	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	295	63	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/ipv4Addr
True	285	15	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	302	91	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ipv4Addr
True	289	15	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	316	90	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ipv4Addr
True	293	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	309	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/ipv4Addr
True	319	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	324	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/ipv4Addr
True	299	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	312	46	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/ipv4Addr
True	314	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	297	46	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/ipv4Addr
True	293	21	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	295	23	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/ipv4Addr
True	310	20	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	310	22	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/ipv4Addr
```

[[Back]](./InterfaceLoopback.md)