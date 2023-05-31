# Node Protocol - IS-IS

## Show LSP records details for selected nodes

```
# iserver get aci proto isis --apic apic11 --node rl --view lsp

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+---------+-------------------+--------+------+------+-------------------------------+--------+
| Node                | Domain  | Sys Id            | Lan Id | Frag | Type | Lifetime                      | Seqnum |
+---------------------+---------+-------------------+--------+------+------+-------------------------------+--------+
| pod-1/rl301-eu-spdc | overlay | 78:1E:10:AC:00:00 | 0      | 1    | l1   | 2023-05-30T20:19:08.000+02:00 | 13767  | 
| pod-1/rl301-eu-spdc | overlay | 78:1E:10:AC:00:00 | 0      | 0    | l1   | 2023-05-30T20:16:23.000+02:00 | 13776  | 
| pod-1/rl301-eu-spdc | overlay | A0:1E:10:AC:00:00 | 0      | 0    | l1   | 2023-05-30T20:05:25.000+02:00 | 13843  | 
| pod-1/rl301-eu-spdc | overlay | A0:1E:10:AC:00:00 | 0      | 1    | l1   | 2023-05-30T20:08:23.000+02:00 | 13786  | 
| pod-1/rl302-eu-spdc | overlay | 78:1E:10:AC:00:00 | 0      | 0    | l1   | 2023-05-30T20:05:50.000+02:00 | 13776  | 
| pod-1/rl302-eu-spdc | overlay | 78:1E:10:AC:00:00 | 0      | 1    | l1   | 2023-05-30T20:08:48.000+02:00 | 13767  | 
| pod-1/rl302-eu-spdc | overlay | A0:1E:10:AC:00:00 | 0      | 1    | l1   | 2023-05-30T20:19:38.000+02:00 | 13786  | 
| pod-1/rl302-eu-spdc | overlay | A0:1E:10:AC:00:00 | 0      | 0    | l1   | 2023-05-30T20:16:23.000+02:00 | 13843  | 
+---------------------+---------+-------------------+--------+------+------+-------------------------------+--------+
```

Developer

```
# iserver get aci proto isis --apic apic11 --node rl --view lsp

{
    "duration": 3043,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 475,
        "disconnect_time": 0,
        "mo_time": 2306,
        "total_time": 2781
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

True	475	-	connect apic11o.emea-sp.cisco.com
True	356	11	apic11o.emea-sp.cisco.com class fabricNode
True	298	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/isis
True	321	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	311	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/isis/inst-default/dom-overlay-1 query query-target=subtree&target-subtree-class=isisLspRec
True	361	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/isis
True	329	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	330	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/isis/inst-default/dom-overlay-1 query query-target=subtree&target-subtree-class=isisLspRec
```

[[Back]](./ProtocolIsis.md)