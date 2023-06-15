# Node Protocol - IS-IS

## Show neighbor details for selected nodes

```
# iserver get aci proto isis --apic apic11 --node rl --view neighbor

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+---------+-----------+-------------------+-------+--------------+---------------+-------+
| Node                | Domain  | Interface | System Id         | Level | Circuit Type | Peer IP       | State |
+---------------------+---------+-----------+-------------------+-------+--------------+---------------+-------+
| pod-1/rl301-eu-spdc | overlay | eth1/33.7 | 78:1E:10:AC:00:00 | l1    | bcast        | 172.16.30.120 | up    | 
| pod-1/rl301-eu-spdc | overlay | eth1/34.8 | 78:1E:10:AC:00:00 | l1    | bcast        | 172.16.30.120 | up    | 
| pod-1/rl302-eu-spdc | overlay | eth1/33.7 | A0:1E:10:AC:00:00 | l1    | bcast        | 172.16.30.160 | up    | 
| pod-1/rl302-eu-spdc | overlay | eth1/34.8 | A0:1E:10:AC:00:00 | l1    | bcast        | 172.16.30.160 | up    | 
+---------------------+---------+-----------+-------------------+-------+--------------+---------------+-------+
```

Developer

```
# iserver get aci proto isis --apic apic11 --node rl --view neighbor

{
    "duration": 2999,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 433,
        "disconnect_time": 0,
        "mo_time": 2335,
        "total_time": 2768
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

True	433	-	connect apic11o.emea-sp.cisco.com
True	357	13	apic11o.emea-sp.cisco.com class fabricNode
True	345	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/isis
True	325	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	335	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/isis/inst-default/dom-overlay-1 query query-target=subtree&target-subtree-class=isisAdjEp&rsp-subtree=children&rsp-subtree-class=isisPeerIpAddr
True	283	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/isis
True	345	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	345	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/isis/inst-default/dom-overlay-1 query query-target=subtree&target-subtree-class=isisAdjEp&rsp-subtree=children&rsp-subtree-class=isisPeerIpAddr
```

[[Back]](./ProtocolIsis.md)