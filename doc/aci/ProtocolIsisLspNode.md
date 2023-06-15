# Node Protocol - IS-IS

## Show LSP records details for selected node

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc --view lsp

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

+---------------------+---------+-------------------+--------+------+------+-------------------------------+--------+
| Node                | Domain  | Sys Id            | Lan Id | Frag | Type | Lifetime                      | Seqnum |
+---------------------+---------+-------------------+--------+------+------+-------------------------------+--------+
| pod-1/cl201-eu-spdc | overlay | 40:20:03:0A:00:00 | 0      | 0    | l1   | 2023-06-14T08:48:12.000+02:00 | 310    | 
| pod-1/cl201-eu-spdc | overlay | 40:88:03:0A:00:00 | 0      | 0    | l1   | 2023-06-14T08:52:12.000+02:00 | 264    | 
| pod-1/cl201-eu-spdc | overlay | 40:C0:03:0A:00:00 | 0      | 0    | l1   | 2023-06-14T08:55:13.000+02:00 | 309    | 
| pod-1/cl201-eu-spdc | overlay | 41:20:03:0A:00:00 | 0      | 0    | l1   | 2023-06-14T08:50:48.000+02:00 | 327    | 
| pod-1/cl201-eu-spdc | overlay | 41:88:03:0A:00:00 | 0      | 0    | l1   | 2023-06-14T08:51:01.000+02:00 | 262    | 
| pod-1/cl201-eu-spdc | overlay | 41:C0:03:0A:00:00 | 0      | 0    | l1   | 2023-06-14T08:49:10.000+02:00 | 324    | 
| pod-1/cl201-eu-spdc | overlay | 43:C0:03:0A:00:00 | 0      | 0    | l1   | 2023-06-14T08:42:50.000+02:00 | 315    | 
| pod-1/cl201-eu-spdc | overlay | 44:C0:03:0A:00:00 | 0      | 0    | l1   | 2023-06-14T08:56:03.000+02:00 | 311    | 
+---------------------+---------+-------------------+--------+------+------+-------------------------------+--------+
```

Developer

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc --view lsp

{
    "duration": 2333,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 776,
        "disconnect_time": 0,
        "mo_time": 1355,
        "total_time": 2131
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

True	776	-	connect apic11o.emea-sp.cisco.com
True	352	13	apic11o.emea-sp.cisco.com class fabricNode
True	332	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis
True	341	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	330	8	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1 query query-target=subtree&target-subtree-class=isisLspRec
```

[[Back]](./ProtocolIsis.md)