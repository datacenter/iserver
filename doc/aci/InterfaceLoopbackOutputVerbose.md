# Node Interface - Loopback

## Verbose output

```
# iserver get aci intf lb --apic apic11 --node any --id lo8 --view verbose

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

Interface Loopback
------------------
- Interface           : lo8
- Admin State         : up
- Oper State          : up
- Reason              : 
- IPv4 Address        : 205.205.205.205/32
- Last Errors         : 0
- Current Error Index : 4294967295


Interface Loopback
------------------
- Interface           : lo8
- Admin State         : up
- Oper State          : up
- Reason              : 
- IPv4 Address        : 122.122.122.122/32
- Last Errors         : 0
- Current Error Index : 4294967295


Interface Loopback
------------------
- Interface           : lo8
- Admin State         : up
- Oper State          : up
- Reason              : 
- IPv4 Address        : 15.254.101.6/32
- Last Errors         : 0
- Current Error Index : 4294967295


Interface Loopback
------------------
- Interface           : lo8
- Admin State         : up
- Oper State          : up
- Reason              : 
- IPv4 Address        : 15.254.101.9/32
- Last Errors         : 0
- Current Error Index : 4294967295


Interface Loopback
------------------
- Interface           : lo8
- Admin State         : up
- Oper State          : up
- Reason              : 
- IPv4 Address        : 172.24.3.15/32
- Last Errors         : 0
- Current Error Index : 4294967295


Interface Loopback
------------------
- Interface           : lo8
- Admin State         : up
- Oper State          : up
- Reason              : 
- IPv4 Address        : 132.132.132.132/32
- Last Errors         : 0
- Current Error Index : 4294967295


Interface Loopback
------------------
- Interface           : lo8
- Admin State         : up
- Oper State          : up
- Reason              : 
- IPv4 Address        : 10.3.0.33/32
- Last Errors         : 0
- Current Error Index : 4294967295


Interface Loopback
------------------
- Interface           : lo8
- Admin State         : up
- Oper State          : up
- Reason              : 
- IPv4 Address        : 10.3.0.33/32
- Last Errors         : 0
- Current Error Index : 4294967295
```

Developer

```
# iserver get aci intf lb --apic apic11 --node any --id lo8 --view verbose

{
    "duration": 6241,
    "apic": {
        "read": true,
        "success": 18,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 17,
        "connect_time": 405,
        "disconnect_time": 0,
        "mo_time": 5401,
        "total_time": 5806
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

True	405	-	connect apic11o.emea-sp.cisco.com
True	313	11	apic11o.emea-sp.cisco.com class fabricNode
True	293	12	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	298	61	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4Addr
True	291	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	338	63	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/ipv4Addr
True	289	15	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	316	91	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ipv4Addr
True	290	15	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	302	90	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ipv4Addr
True	291	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	298	46	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/ipv4Addr
True	318	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	303	46	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/ipv4Addr
True	508	21	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	355	23	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/ipv4Addr
True	303	20	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	295	22	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/ipv4Addr
```

[[Back]](./InterfaceLoopback.md)