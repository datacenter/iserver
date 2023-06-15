# Node Protocol - IS-IS

## Show interface details for selected nodes

```
# iserver get aci proto isis --apic apic11 --node rl --view intf

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+---------+-----------+-------------+--------------+--------------------+----------------+
| Node                | Domain  | Id        | Admin State | Circuit Type | Control            | Protocol State |
+---------------------+---------+-----------+-------------+--------------+--------------------+----------------+
| pod-1/rl301-eu-spdc | overlay | eth1/33.7 | enabled     | l1           |                    | Ready          | 
| pod-1/rl301-eu-spdc | overlay | eth1/34.8 | enabled     | l1           |                    | Ready          | 
| pod-1/rl301-eu-spdc | overlay | lo0       | enabled     | l1           | advert-tep,passive | Ready          | 
| pod-1/rl301-eu-spdc | overlay | lo1       | enabled     | l1           | passive            | Ready          | 
| pod-1/rl301-eu-spdc | overlay | lo2       | enabled     | l1           | passive            | Ready          | 
| pod-1/rl301-eu-spdc | overlay | lo4       | enabled     | l1           | advert-tep,passive | Ready          | 
| pod-1/rl302-eu-spdc | overlay | eth1/33.7 | enabled     | l1           |                    | Ready          | 
| pod-1/rl302-eu-spdc | overlay | eth1/34.8 | enabled     | l1           |                    | Ready          | 
| pod-1/rl302-eu-spdc | overlay | lo0       | enabled     | l1           | advert-tep,passive | Ready          | 
| pod-1/rl302-eu-spdc | overlay | lo1       | enabled     | l1           | passive            | Ready          | 
| pod-1/rl302-eu-spdc | overlay | lo2       | enabled     | l1           | passive            | Ready          | 
| pod-1/rl302-eu-spdc | overlay | lo4       | enabled     | l1           | advert-tep,passive | Ready          | 
+---------------------+---------+-----------+-------------+--------------+--------------------+----------------+
```

Developer

```
# iserver get aci proto isis --apic apic11 --node rl --view intf

{
    "duration": 2906,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 416,
        "disconnect_time": 0,
        "mo_time": 2250,
        "total_time": 2666
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

True	416	-	connect apic11o.emea-sp.cisco.com
True	324	13	apic11o.emea-sp.cisco.com class fabricNode
True	319	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/isis
True	305	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	312	6	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/isis/inst-default/dom-overlay-1 query query-target=subtree&target-subtree-class=isisIf
True	352	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/isis
True	334	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	304	6	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/isis/inst-default/dom-overlay-1 query query-target=subtree&target-subtree-class=isisIf
```

[[Back]](./ProtocolIsis.md)