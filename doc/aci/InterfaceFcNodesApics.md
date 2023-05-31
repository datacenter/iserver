# Node Interface - FC

## Multi-APIC

```
# iserver get aci intf fc --apic dom:milan --node any --empty

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
Apic: apic21o.emea-sp.cisco.com
Pod: 1
- node: bl2205-eu-spdc
- node: bl2206-eu-spdc
- node: cl2201-eu-spdc
- node: cl2202-eu-spdc
- node: cl2207-eu-spdc
- node: cl2208-eu-spdc
- node: rl2701-eu-spdc
- node: rl2702-eu-spdc
- node: s2101-eu-spdc
- node: s2102-eu-spdc
```

Developer

```
# iserver get aci intf fc --apic dom:milan --node any --empty

{
    "duration": 7427,
    "apic": {
        "read": true,
        "success": 22,
        "failed": 0,
        "connect": 2,
        "disconnect": 0,
        "mo": 20,
        "connect_time": 808,
        "disconnect_time": 0,
        "mo_time": 6287,
        "total_time": 7095
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

True	408	-	connect apic11o.emea-sp.cisco.com
True	400	-	connect apic21o.emea-sp.cisco.com
True	302	11	apic11o.emea-sp.cisco.com class fabricNode
True	311	13	apic21o.emea-sp.cisco.com class fabricNode
True	288	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	306	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	301	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	295	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	348	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	316	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	327	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	409	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	295	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2205/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	298	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2206/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	374	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2201/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	293	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2202/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	299	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2207/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	305	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2208/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	331	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2701/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	298	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2702/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	294	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2101/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	297	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2102/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
```

[[Back]](./InterfaceFc.md)