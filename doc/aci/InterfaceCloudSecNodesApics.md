# Node Interface - FC

## Multi-APIC

```
# iserver get aci intf cloudsec --apic dom:milan --node any --empty

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
# iserver get aci intf cloudsec --apic dom:milan --node any --empty

{
    "duration": 8315,
    "apic": {
        "read": true,
        "success": 26,
        "failed": 0,
        "connect": 2,
        "disconnect": 0,
        "mo": 24,
        "connect_time": 808,
        "disconnect_time": 0,
        "mo_time": 7138,
        "total_time": 7946
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

True	409	-	connect apic11o.emea-sp.cisco.com
True	314	13	apic11o.emea-sp.cisco.com class fabricNode
True	399	-	connect apic21o.emea-sp.cisco.com
True	311	15	apic21o.emea-sp.cisco.com class fabricNode
True	309	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205 query query-target=subtree&target-subtree-class=cloudsecIf
True	283	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206 query query-target=subtree&target-subtree-class=cloudsecIf
True	281	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201 query query-target=subtree&target-subtree-class=cloudsecIf
True	292	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202 query query-target=subtree&target-subtree-class=cloudsecIf
True	298	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209 query query-target=subtree&target-subtree-class=cloudsecIf
True	288	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210 query query-target=subtree&target-subtree-class=cloudsecIf
True	301	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301 query query-target=subtree&target-subtree-class=cloudsecIf
True	286	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302 query query-target=subtree&target-subtree-class=cloudsecIf
True	286	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101 query query-target=subtree&target-subtree-class=cloudsecIf
True	302	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102 query query-target=subtree&target-subtree-class=cloudsecIf
True	293	0	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2205 query query-target=subtree&target-subtree-class=cloudsecIf
True	292	0	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2206 query query-target=subtree&target-subtree-class=cloudsecIf
True	277	0	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2201 query query-target=subtree&target-subtree-class=cloudsecIf
True	308	0	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2202 query query-target=subtree&target-subtree-class=cloudsecIf
True	340	0	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2207 query query-target=subtree&target-subtree-class=cloudsecIf
True	289	0	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2208 query query-target=subtree&target-subtree-class=cloudsecIf
True	307	0	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2209 query query-target=subtree&target-subtree-class=cloudsecIf
True	294	0	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2210 query query-target=subtree&target-subtree-class=cloudsecIf
True	306	0	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2701 query query-target=subtree&target-subtree-class=cloudsecIf
True	289	0	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2702 query query-target=subtree&target-subtree-class=cloudsecIf
True	304	0	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2101 query query-target=subtree&target-subtree-class=cloudsecIf
True	288	0	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2102 query query-target=subtree&target-subtree-class=cloudsecIf
```

[[Back]](./InterfaceCloudSec.md)