# Node Interface - FCPC

## Multi-APIC

```
# iserver get aci intf fcpc --apic dom:milan --node any --empty

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
# iserver get aci intf fcpc --apic dom:milan --node any --empty

{
    "duration": 8087,
    "apic": {
        "read": true,
        "success": 26,
        "failed": 0,
        "connect": 2,
        "disconnect": 0,
        "mo": 24,
        "connect_time": 799,
        "disconnect_time": 0,
        "mo_time": 6968,
        "total_time": 7767
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

True	410	-	connect apic11o.emea-sp.cisco.com
True	303	13	apic11o.emea-sp.cisco.com class fabricNode
True	389	-	connect apic21o.emea-sp.cisco.com
True	303	15	apic21o.emea-sp.cisco.com class fabricNode
True	289	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/pcFcAggrIf
True	285	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/pcFcAggrIf
True	286	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/pcFcAggrIf
True	295	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/pcFcAggrIf
True	280	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/pcFcAggrIf
True	288	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/pcFcAggrIf
True	281	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/pcFcAggrIf
True	289	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/pcFcAggrIf
True	288	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/pcFcAggrIf
True	280	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/pcFcAggrIf
True	287	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2205/pcFcAggrIf
True	287	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2206/pcFcAggrIf
True	281	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2201/pcFcAggrIf
True	302	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2202/pcFcAggrIf
True	283	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2207/pcFcAggrIf
True	333	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2208/pcFcAggrIf
True	285	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2209/pcFcAggrIf
True	278	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2210/pcFcAggrIf
True	285	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2701/pcFcAggrIf
True	289	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2702/pcFcAggrIf
True	279	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2101/pcFcAggrIf
True	312	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2102/pcFcAggrIf
```

[[Back]](./InterfaceFcPc.md)