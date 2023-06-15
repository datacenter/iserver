# Node Protocol - IS-IS

## Show LSP records details for selected nodes

```
# iserver get aci proto isis --apic apic11 --node rl --view lsp

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+---------+-------------------+--------+------+------+-------------------------------+--------+
| Node                | Domain  | Sys Id            | Lan Id | Frag | Type | Lifetime                      | Seqnum |
+---------------------+---------+-------------------+--------+------+------+-------------------------------+--------+
| pod-1/rl301-eu-spdc | overlay | 78:1E:10:AC:00:00 | 0      | 0    | l1   | 2023-06-14T08:54:45.000+02:00 | 318    | 
| pod-1/rl301-eu-spdc | overlay | A0:1E:10:AC:00:00 | 0      | 0    | l1   | 2023-06-14T08:43:43.000+02:00 | 321    | 
| pod-1/rl302-eu-spdc | overlay | 78:1E:10:AC:00:00 | 0      | 0    | l1   | 2023-06-14T08:44:21.000+02:00 | 318    | 
| pod-1/rl302-eu-spdc | overlay | A0:1E:10:AC:00:00 | 0      | 0    | l1   | 2023-06-14T08:55:06.000+02:00 | 321    | 
+---------------------+---------+-------------------+--------+------+------+-------------------------------+--------+
```

Developer

```
# iserver get aci proto isis --apic apic11 --node rl --view lsp

{
    "duration": 2864,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 427,
        "disconnect_time": 0,
        "mo_time": 2192,
        "total_time": 2619
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

True	427	-	connect apic11o.emea-sp.cisco.com
True	315	13	apic11o.emea-sp.cisco.com class fabricNode
True	314	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/isis
True	315	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	314	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/isis/inst-default/dom-overlay-1 query query-target=subtree&target-subtree-class=isisLspRec
True	316	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/isis
True	332	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	286	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/isis/inst-default/dom-overlay-1 query query-target=subtree&target-subtree-class=isisLspRec
```

[[Back]](./ProtocolIsis.md)