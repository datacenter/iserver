# Node Protocol - CDP

## Filter by system

```
# iserver get aci proto cdp
    --apic apic11
    --node cl201-eu-spdc
    --sys esx4*
    --view nei

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

Protocol CDP - Neighbor [#1]
----------------------------

+---------------------+-----------------+----------------------+-------------+---------+--------+------+--------------+
| Node                | Local Interface | Neighbor System Name | Platform    | Port    | Duplex | MTU  | Capabilities |
+---------------------+-----------------+----------------------+-------------+---------+--------+------+--------------+
| pod-1/cl201-eu-spdc | eth1/44         | esx4-eu-spdc         | VMware ESXi | vmnic10 | full   | 9000 | switch       | 
+---------------------+-----------------+----------------------+-------------+---------+--------+------+--------------+
```

Developer

```
# iserver get aci proto cdp
    --apic apic11
    --node cl201-eu-spdc
    --sys esx4*
    --view nei

{
    "duration": 1096,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 382,
        "disconnect_time": 0,
        "mo_time": 596,
        "total_time": 978
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

True	382	-	connect apic11o.emea-sp.cisco.com:443
True	301	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	295	19	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
```

[[Back]](./ProtocolCdp.md)