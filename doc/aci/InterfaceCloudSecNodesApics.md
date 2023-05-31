# Node Interface - FC

## Multi-APIC

```
# iserver get aci intf cloudsec --apic dom:milan --node any --empty

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
# iserver get aci intf cloudsec --apic dom:milan --node any --empty

{
    "duration": 7372,
    "apic": {
        "read": true,
        "success": 22,
        "failed": 0,
        "connect": 2,
        "disconnect": 0,
        "mo": 20,
        "connect_time": 841,
        "disconnect_time": 0,
        "mo_time": 6245,
        "total_time": 7086
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

True	420	-	connect apic11o.emea-sp.cisco.com
True	421	-	connect apic21o.emea-sp.cisco.com
True	305	11	apic11o.emea-sp.cisco.com class fabricNode
True	312	13	apic21o.emea-sp.cisco.com class fabricNode
True	304	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205 query query-target=subtree&target-subtree-class=cloudsecIf
True	305	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206 query query-target=subtree&target-subtree-class=cloudsecIf
True	299	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201 query query-target=subtree&target-subtree-class=cloudsecIf
True	314	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202 query query-target=subtree&target-subtree-class=cloudsecIf
True	384	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301 query query-target=subtree&target-subtree-class=cloudsecIf
True	299	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302 query query-target=subtree&target-subtree-class=cloudsecIf
True	295	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101 query query-target=subtree&target-subtree-class=cloudsecIf
True	303	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102 query query-target=subtree&target-subtree-class=cloudsecIf
True	308	0	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2205 query query-target=subtree&target-subtree-class=cloudsecIf
True	312	0	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2206 query query-target=subtree&target-subtree-class=cloudsecIf
True	301	0	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2201 query query-target=subtree&target-subtree-class=cloudsecIf
True	309	0	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2202 query query-target=subtree&target-subtree-class=cloudsecIf
True	342	0	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2207 query query-target=subtree&target-subtree-class=cloudsecIf
True	303	0	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2208 query query-target=subtree&target-subtree-class=cloudsecIf
True	307	0	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2701 query query-target=subtree&target-subtree-class=cloudsecIf
True	304	0	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2702 query query-target=subtree&target-subtree-class=cloudsecIf
True	327	0	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2101 query query-target=subtree&target-subtree-class=cloudsecIf
True	312	0	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2102 query query-target=subtree&target-subtree-class=cloudsecIf
```

[[Back]](./InterfaceCloudSec.md)