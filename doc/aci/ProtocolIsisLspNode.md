# Node Protocol - IS-IS

## Show LSP records details for selected node

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc --view lsp

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: cl201-eu-spdc

+---------------------+---------+-------------------+--------+------+------+-------------------------------+--------+
| Node                | Domain  | Sys Id            | Lan Id | Frag | Type | Lifetime                      | Seqnum |
+---------------------+---------+-------------------+--------+------+------+-------------------------------+--------+
| pod-1/cl201-eu-spdc | overlay | 40:20:03:0A:00:00 | 0      | 0    | l1   | 2023-05-30T20:20:33.000+02:00 | 54739  | 
| pod-1/cl201-eu-spdc | overlay | 40:C0:03:0A:00:00 | 0      | 0    | l1   | 2023-05-30T20:16:39.000+02:00 | 54714  | 
| pod-1/cl201-eu-spdc | overlay | 41:20:03:0A:00:00 | 0      | 0    | l1   | 2023-05-30T20:18:08.000+02:00 | 54793  | 
| pod-1/cl201-eu-spdc | overlay | 41:C0:03:0A:00:00 | 0      | 0    | l1   | 2023-05-30T20:15:51.000+02:00 | 54785  | 
| pod-1/cl201-eu-spdc | overlay | 43:C0:03:0A:00:00 | 0      | 0    | l1   | 2023-05-30T20:08:40.000+02:00 | 54733  | 
| pod-1/cl201-eu-spdc | overlay | 44:C0:03:0A:00:00 | 0      | 0    | l1   | 2023-05-30T20:20:33.000+02:00 | 54757  | 
+---------------------+---------+-------------------+--------+------+------+-------------------------------+--------+
```

Developer

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc --view lsp

{
    "duration": 1828,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 457,
        "disconnect_time": 0,
        "mo_time": 1252,
        "total_time": 1709
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

True	457	-	connect apic11o.emea-sp.cisco.com
True	319	11	apic11o.emea-sp.cisco.com class fabricNode
True	305	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis
True	293	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	335	6	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1 query query-target=subtree&target-subtree-class=isisLspRec
```

[[Back]](./ProtocolIsis.md)