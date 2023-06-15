# Node Interface - Loopback

## Verbose output

```
# iserver get aci intf lb --apic apic11 --node any --id lo8 --view verbose

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
- IPv4 Address        : 172.24.0.14/32
- Last Errors         : 0
- Current Error Index : 4294967295


Interface Loopback
------------------
- Interface           : lo8
- Admin State         : up
- Oper State          : up
- Reason              : 
- IPv4 Address        : 15.254.101.0/32
- Last Errors         : 0
- Current Error Index : 4294967295


Interface Loopback
------------------
- Interface           : lo8
- Admin State         : up
- Oper State          : up
- Reason              : 
- IPv4 Address        : 202.202.202.202/32
- Last Errors         : 0
- Current Error Index : 4294967295


Interface Loopback
------------------
- Interface           : lo8
- Admin State         : up
- Oper State          : up
- Reason              : 
- IPv4 Address        : 131.131.131.131/32
- Last Errors         : 0
- Current Error Index : 4294967295


Interface Loopback
------------------
- Interface           : lo8
- Admin State         : up
- Oper State          : up
- Reason              : 
- IPv4 Address        : 172.24.3.14/32
- Last Errors         : 0
- Current Error Index : 4294967295


Interface Loopback
------------------
- Interface           : lo8
- Admin State         : up
- Oper State          : up
- Reason              : 
- IPv4 Address        : 172.16.10.1/32
- Last Errors         : 0
- Current Error Index : 4294967295


Interface Loopback
------------------
- Interface           : lo8
- Admin State         : up
- Oper State          : up
- Reason              : 
- IPv4 Address        : 172.16.10.1/32
- Last Errors         : 0
- Current Error Index : 4294967295
```

Developer

```
# iserver get aci intf lb --apic apic11 --node any --id lo8 --view verbose

{
    "duration": 7202,
    "apic": {
        "read": true,
        "success": 22,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 21,
        "connect_time": 388,
        "disconnect_time": 0,
        "mo_time": 6393,
        "total_time": 6781
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

True	388	-	connect apic11o.emea-sp.cisco.com
True	296	13	apic11o.emea-sp.cisco.com class fabricNode
True	324	12	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	302	61	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4Addr
True	294	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	310	63	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/ipv4Addr
True	296	15	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	307	91	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ipv4Addr
True	311	15	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	302	90	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ipv4Addr
True	271	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	302	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/ipv4Addr
True	333	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	337	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/ipv4Addr
True	289	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	299	46	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/ipv4Addr
True	300	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	315	46	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/ipv4Addr
True	326	21	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	285	23	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/ipv4Addr
True	290	20	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	304	22	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/ipv4Addr
```

[[Back]](./InterfaceLoopback.md)