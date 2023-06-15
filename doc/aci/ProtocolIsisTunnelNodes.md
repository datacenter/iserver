# Node Protocol - IS-IS

## Show tunnel endpoints for selected nodes

```
# iserver get aci proto isis --apic apic11 --node rl --view tunnel

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

Discovered Tunnel Endpoints
---------------------------

+---------------------+---------+---------------+---------------------+------+----------+
| Node                | Domain  | Id            | Destination         | Role | Type     |
+---------------------+---------+---------------+---------------------+------+----------+
| pod-1/rl301-eu-spdc | overlay | 172.16.30.120 | pod-1/rl302-eu-spdc | leaf | physical | 
| pod-1/rl301-eu-spdc | overlay | 172.16.30.88  |                     | leaf | physical | 
| pod-1/rl302-eu-spdc | overlay | 172.16.30.160 | pod-1/rl301-eu-spdc | leaf | physical | 
| pod-1/rl302-eu-spdc | overlay | 172.16.30.88  |                     | leaf | physical | 
+---------------------+---------+---------------+---------------------+------+----------+
```

Developer

```
# iserver get aci proto isis --apic apic11 --node rl --view tunnel

{
    "duration": 3054,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 426,
        "disconnect_time": 0,
        "mo_time": 2370,
        "total_time": 2796
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

True	426	-	connect apic11o.emea-sp.cisco.com
True	333	13	apic11o.emea-sp.cisco.com class fabricNode
True	394	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/isis
True	321	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	337	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/isis/inst-default/dom-overlay-1 query query-target=subtree&target-subtree-class=isisDTEp
True	312	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/isis
True	349	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	324	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/isis/inst-default/dom-overlay-1 query query-target=subtree&target-subtree-class=isisDTEp
```

[[Back]](./ProtocolIsis.md)