# Node Interface - Loopback

## Filter by ip subnet

```
# iserver get aci intf lb --apic apic11 --node any --subnet 15.0.0.0/8

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

+---------------------+-----------+-------------+------------+-------------------+-------------+---------------------+
| Node                | Interface | Admin State | Oper State | IPv4 Address      | Last Errors | Current Error Index |
+---------------------+-----------+-------------+------------+-------------------+-------------+---------------------+
| pod-1/cl201-eu-spdc | lo6       | up          | up         | 15.254.101.8/32   | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo7       | up          | up         | 15.254.101.2/32   | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo8       | up          | up         | 15.254.101.6/32   | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo10      | up          | up         | 15.254.101.99/32  | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo11      | up          | up         | 15.254.101.4/32   | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo13      | up          | up         | 15.254.101.0/32   | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo6       | up          | up         | 15.254.101.3/32   | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo7       | up          | up         | 15.254.101.1/32   | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo8       | up          | up         | 15.254.101.9/32   | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo11      | up          | up         | 15.254.101.7/32   | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo12      | up          | up         | 15.254.101.5/32   | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo13      | up          | up         | 15.254.101.100/32 | 0           | 4294967295          | 
+---------------------+-----------+-------------+------------+-------------------+-------------+---------------------+
```

Developer

```
# iserver get aci intf lb --apic apic11 --node any --subnet 15.0.0.0/8

{
    "duration": 6378,
    "apic": {
        "read": true,
        "success": 18,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 17,
        "connect_time": 416,
        "disconnect_time": 0,
        "mo_time": 5501,
        "total_time": 5917
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

True	416	-	connect apic11o.emea-sp.cisco.com
True	306	11	apic11o.emea-sp.cisco.com class fabricNode
True	287	12	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	342	61	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4Addr
True	314	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	436	63	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/ipv4Addr
True	292	15	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	306	91	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ipv4Addr
True	314	15	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	345	90	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ipv4Addr
True	332	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	318	46	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/ipv4Addr
True	354	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	351	46	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/ipv4Addr
True	304	21	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	292	23	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/ipv4Addr
True	314	20	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	294	22	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/ipv4Addr
```

[[Back]](./InterfaceLoopback.md)