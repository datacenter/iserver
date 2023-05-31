# Node Interface - Loopback

## Filter by ip address

```
# iserver get aci intf lb --apic apic11 --node any --ip 10.3.0.32

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

+---------------------+-----------+-------------+------------+--------------+-------------+---------------------+
| Node                | Interface | Admin State | Oper State | IPv4 Address | Last Errors | Current Error Index |
+---------------------+-----------+-------------+------------+--------------+-------------+---------------------+
| pod-1/bl205-eu-spdc | lo1023    | up          | up         | 10.3.0.32/32 | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo1023    | up          | up         | 10.3.0.32/32 | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo1023    | up          | up         | 10.3.0.32/32 | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo1023    | up          | up         | 10.3.0.32/32 | 0           | 4294967295          | 
+---------------------+-----------+-------------+------------+--------------+-------------+---------------------+
```

Developer

```
# iserver get aci intf lb --apic apic11 --node any --ip 10.3.0.32

{
    "duration": 6440,
    "apic": {
        "read": true,
        "success": 18,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 17,
        "connect_time": 411,
        "disconnect_time": 0,
        "mo_time": 5565,
        "total_time": 5976
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

True	411	-	connect apic11o.emea-sp.cisco.com
True	316	11	apic11o.emea-sp.cisco.com class fabricNode
True	310	12	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	329	61	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4Addr
True	312	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	377	63	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/ipv4Addr
True	312	15	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	317	91	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ipv4Addr
True	306	15	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	338	90	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ipv4Addr
True	309	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	317	46	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/ipv4Addr
True	317	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	307	46	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/ipv4Addr
True	305	21	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	386	23	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/ipv4Addr
True	362	20	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	345	22	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/ipv4Addr
```

[[Back]](./InterfaceLoopback.md)