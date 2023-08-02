# Node Protocol - IS-IS

## Lsp view

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc --view lsp

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

Protocol ISIS - LSP [#8]
------------------------

+---------------------+---------+-------------------+--------+------+------+-------------------------------+--------+
| Node                | Domain  | Sys Id            | Lan Id | Frag | Type | Lifetime                      | Seqnum |
+---------------------+---------+-------------------+--------+------+------+-------------------------------+--------+
| pod-1/cl201-eu-spdc | overlay | 40:20:03:0A:00:00 | 0      | 0    | l1   | 2023-08-02T15:10:02.000+02:00 | 7982   | 
| pod-1/cl201-eu-spdc | overlay | 40:88:03:0A:00:00 | 0      | 0    | l1   | 2023-08-02T15:05:44.000+02:00 | 2181   | 
| pod-1/cl201-eu-spdc | overlay | 40:C0:03:0A:00:00 | 0      | 0    | l1   | 2023-08-02T15:11:44.000+02:00 | 7983   | 
| pod-1/cl201-eu-spdc | overlay | 41:20:03:0A:00:00 | 0      | 0    | l1   | 2023-08-02T15:05:11.000+02:00 | 8003   | 
| pod-1/cl201-eu-spdc | overlay | 41:88:03:0A:00:00 | 0      | 0    | l1   | 2023-08-02T15:06:00.000+02:00 | 2174   | 
| pod-1/cl201-eu-spdc | overlay | 41:C0:03:0A:00:00 | 0      | 0    | l1   | 2023-08-02T15:07:31.000+02:00 | 7999   | 
| pod-1/cl201-eu-spdc | overlay | 43:C0:03:0A:00:00 | 0      | 0    | l1   | 2023-08-02T14:59:52.000+02:00 | 7991   | 
| pod-1/cl201-eu-spdc | overlay | 44:C0:03:0A:00:00 | 0      | 0    | l1   | 2023-08-02T15:12:53.000+02:00 | 7981   | 
+---------------------+---------+-------------------+--------+------+------+-------------------------------+--------+
```

Developer

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc --view lsp

{
    "duration": 1987,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 415,
        "disconnect_time": 0,
        "mo_time": 1284,
        "total_time": 1699
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

True	415	-	connect apic11o.emea-sp.cisco.com:443
True	332	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	323	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/isis query query-target=children&rsp-subtree-include=health,fault-count
True	298	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	331	8	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1 query query-target=subtree&target-subtree-class=isisLspRec
```

[[Back]](./ProtocolIsis.md)