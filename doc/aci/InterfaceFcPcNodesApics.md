# Node Interface - FCPC

## Multi-APIC

```
# iserver get aci intf fcpc --apic dom:milan --node any --empty

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
# iserver get aci intf fcpc --apic dom:milan --node any --empty

{
    "duration": 7286,
    "apic": {
        "read": true,
        "success": 22,
        "failed": 0,
        "connect": 2,
        "disconnect": 0,
        "mo": 20,
        "connect_time": 789,
        "disconnect_time": 0,
        "mo_time": 6156,
        "total_time": 6945
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

True	412	-	connect apic11o.emea-sp.cisco.com
True	377	-	connect apic21o.emea-sp.cisco.com
True	309	11	apic11o.emea-sp.cisco.com class fabricNode
True	298	13	apic21o.emea-sp.cisco.com class fabricNode
True	314	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/pcFcAggrIf
True	295	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/pcFcAggrIf
True	300	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/pcFcAggrIf
True	309	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/pcFcAggrIf
True	338	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/pcFcAggrIf
True	297	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/pcFcAggrIf
True	301	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/pcFcAggrIf
True	294	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/pcFcAggrIf
True	292	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2205/pcFcAggrIf
True	335	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2206/pcFcAggrIf
True	297	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2201/pcFcAggrIf
True	303	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2202/pcFcAggrIf
True	371	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2207/pcFcAggrIf
True	304	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2208/pcFcAggrIf
True	300	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2701/pcFcAggrIf
True	308	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2702/pcFcAggrIf
True	291	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2101/pcFcAggrIf
True	300	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2102/pcFcAggrIf
```

[[Back]](./InterfaceFcPc.md)