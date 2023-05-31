# Node Protocol - IS-IS

## Show tunnel endpoints for selected nodes

```
# iserver get aci proto isis --apic apic11 --node rl --view tunnel

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+---------+---------------+------+----------+
| Node                | Domain  | Id            | Role | Type     |
+---------------------+---------+---------------+------+----------+
| pod-1/rl301-eu-spdc | overlay | 172.16.30.120 | leaf | physical | 
| pod-1/rl301-eu-spdc | overlay | 172.16.30.88  | leaf | physical | 
| pod-1/rl302-eu-spdc | overlay | 172.16.30.160 | leaf | physical | 
| pod-1/rl302-eu-spdc | overlay | 172.16.30.88  | leaf | physical | 
+---------------------+---------+---------------+------+----------+
```

Developer

```
# iserver get aci proto isis --apic apic11 --node rl --view tunnel

{
    "duration": 2746,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 411,
        "disconnect_time": 0,
        "mo_time": 2192,
        "total_time": 2603
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

True	411	-	connect apic11o.emea-sp.cisco.com
True	315	11	apic11o.emea-sp.cisco.com class fabricNode
True	282	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/isis
True	296	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	316	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/isis/inst-default/dom-overlay-1 query query-target=subtree&target-subtree-class=isisDTEp
True	330	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/isis
True	337	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	316	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/isis/inst-default/dom-overlay-1 query query-target=subtree&target-subtree-class=isisDTEp
```

[[Back]](./ProtocolIsis.md)