# Node Interface - VFC

## Multi-APIC

```
# iserver get aci intf vfc --apic dom:milan --node any --empty

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
# iserver get aci intf vfc --apic dom:milan --node any --empty

{
    "duration": 8123,
    "apic": {
        "read": true,
        "success": 22,
        "failed": 0,
        "connect": 2,
        "disconnect": 0,
        "mo": 20,
        "connect_time": 861,
        "disconnect_time": 0,
        "mo_time": 6886,
        "total_time": 7747
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

True	424	-	connect apic11o.emea-sp.cisco.com
True	437	-	connect apic21o.emea-sp.cisco.com
True	685	11	apic11o.emea-sp.cisco.com class fabricNode
True	300	13	apic21o.emea-sp.cisco.com class fabricNode
True	324	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l2VfcIf
True	291	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/l2VfcIf
True	290	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l2VfcIf
True	311	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l2VfcIf
True	357	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/l2VfcIf
True	291	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/l2VfcIf
True	275	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/l2VfcIf
True	298	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/l2VfcIf
True	301	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2205/l2VfcIf
True	431	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2206/l2VfcIf
True	306	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2201/l2VfcIf
True	307	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2202/l2VfcIf
True	316	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2207/l2VfcIf
True	337	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2208/l2VfcIf
True	401	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2701/l2VfcIf
True	413	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2702/l2VfcIf
True	332	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2101/l2VfcIf
True	320	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2102/l2VfcIf
```

[[Back]](./InterfaceVfc.md)