# Node Protocol - CDP

## Filter CDP neighbors by neighbor's platform name

```
# iserver get aci proto cdp --apic apic11 --node rl --platform *fi*

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc
```

Developer

```
# iserver get aci proto cdp --apic apic11 --node rl --platform *fi*

{
    "duration": 2709,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 399,
        "disconnect_time": 0,
        "mo_time": 2172,
        "total_time": 2571
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

True	399	-	connect apic11o.emea-sp.cisco.com
True	319	11	apic11o.emea-sp.cisco.com class fabricNode
True	306	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/cdp/inst
True	301	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	307	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	337	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/cdp/inst
True	300	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	302	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
```

[[Back]](./ProtocolCdp.md)