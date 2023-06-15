# Node Interface - VFC

## Multi-APIC

```
# iserver get aci intf vfc --apic dom:milan --node any

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
```

Developer

```
# iserver get aci intf vfc --apic dom:milan --node any

{
    "duration": 9430,
    "apic": {
        "read": true,
        "success": 26,
        "failed": 0,
        "connect": 2,
        "disconnect": 0,
        "mo": 24,
        "connect_time": 863,
        "disconnect_time": 0,
        "mo_time": 7947,
        "total_time": 8810
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

True	415	-	connect apic11o.emea-sp.cisco.com
True	319	13	apic11o.emea-sp.cisco.com class fabricNode
True	448	-	connect apic21o.emea-sp.cisco.com
True	332	15	apic21o.emea-sp.cisco.com class fabricNode
True	309	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l2VfcIf
True	320	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/l2VfcIf
True	323	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l2VfcIf
True	303	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l2VfcIf
True	318	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/l2VfcIf
True	321	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/l2VfcIf
True	322	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/l2VfcIf
True	439	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/l2VfcIf
True	351	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/l2VfcIf
True	343	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/l2VfcIf
True	376	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2205/l2VfcIf
True	315	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2206/l2VfcIf
True	318	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2201/l2VfcIf
True	324	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2202/l2VfcIf
True	331	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2207/l2VfcIf
True	340	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2208/l2VfcIf
True	339	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2209/l2VfcIf
True	363	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2210/l2VfcIf
True	300	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2701/l2VfcIf
True	298	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2702/l2VfcIf
True	307	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2101/l2VfcIf
True	336	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2102/l2VfcIf
```

[[Back]](./InterfaceVfc.md)