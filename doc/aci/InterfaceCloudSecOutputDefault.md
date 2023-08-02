# Node Interface - CloudSec

## Default output

```
# iserver get aci intf cloudsec --apic apic21 --node any

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

Interface CloudSec State [#0]
-----------------------------
None
```

Developer

```
# iserver get aci intf cloudsec --apic apic21 --node any

{
    "duration": 6270,
    "apic": {
        "read": true,
        "success": 14,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 13,
        "connect_time": 545,
        "disconnect_time": 0,
        "mo_time": 5317,
        "total_time": 5862
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

True	545	-	connect apic21o.emea-sp.cisco.com:443
True	401	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	399	0	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205 query query-target=children&target-subtree-class=cloudsecIf&rsp-subtree-include=health,fault-count,required
True	411	0	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2206 query query-target=children&target-subtree-class=cloudsecIf&rsp-subtree-include=health,fault-count,required
True	398	0	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201 query query-target=children&target-subtree-class=cloudsecIf&rsp-subtree-include=health,fault-count,required
True	492	0	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202 query query-target=children&target-subtree-class=cloudsecIf&rsp-subtree-include=health,fault-count,required
True	408	0	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207 query query-target=children&target-subtree-class=cloudsecIf&rsp-subtree-include=health,fault-count,required
True	395	0	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208 query query-target=children&target-subtree-class=cloudsecIf&rsp-subtree-include=health,fault-count,required
True	384	0	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2209 query query-target=children&target-subtree-class=cloudsecIf&rsp-subtree-include=health,fault-count,required
True	393	0	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2210 query query-target=children&target-subtree-class=cloudsecIf&rsp-subtree-include=health,fault-count,required
True	400	0	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701 query query-target=children&target-subtree-class=cloudsecIf&rsp-subtree-include=health,fault-count,required
True	459	0	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702 query query-target=children&target-subtree-class=cloudsecIf&rsp-subtree-include=health,fault-count,required
True	388	0	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2101 query query-target=children&target-subtree-class=cloudsecIf&rsp-subtree-include=health,fault-count,required
True	389	0	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2102 query query-target=children&target-subtree-class=cloudsecIf&rsp-subtree-include=health,fault-count,required
```

[[Back]](./InterfaceCloudSec.md)