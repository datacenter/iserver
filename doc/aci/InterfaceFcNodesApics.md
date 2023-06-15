# Node Interface - FC

## Multi-APIC

```
# iserver get aci intf fc --apic dom:milan --node any --empty

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
# iserver get aci intf fc --apic dom:milan --node any --empty

{
    "duration": 8382,
    "apic": {
        "read": true,
        "success": 26,
        "failed": 0,
        "connect": 2,
        "disconnect": 0,
        "mo": 24,
        "connect_time": 789,
        "disconnect_time": 0,
        "mo_time": 7168,
        "total_time": 7957
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

True	400	-	connect apic11o.emea-sp.cisco.com
True	305	13	apic11o.emea-sp.cisco.com class fabricNode
True	389	-	connect apic21o.emea-sp.cisco.com
True	319	15	apic21o.emea-sp.cisco.com class fabricNode
True	290	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	287	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	310	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	300	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	288	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	293	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	271	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	285	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	299	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	297	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	279	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2205/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	306	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2206/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	358	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2201/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	285	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2202/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	280	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2207/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	298	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2208/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	303	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2209/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	318	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2210/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	308	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2701/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	308	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2702/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	281	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2101/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
True	300	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2102/l1FcPhysIf query query-target=subtree&target-subtree-class=l1RtFcBrConf
```

[[Back]](./InterfaceFc.md)