# Node Protocol - BFD

## Filter sessions by state

State 'up'

```
# iserver get aci proto bfd --apic apic11 --node any --state up

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: cl209-eu-spdc
- node: cl210-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc
- node: s101-eu-spdc
- node: s102-eu-spdc
```

State 'down'

```
# iserver get aci proto bfd --apic apic11 --node any --state down

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: cl209-eu-spdc
- node: cl210-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc
- node: s101-eu-spdc
- node: s102-eu-spdc

+---------------------+---------------+-------+------------+----------------+-------+------------+----------+-----------+-----------+
| Node                | Local Address | State | Session Id | Remote Address | State | Session Id | Type     | VRF       | Interface |
+---------------------+---------------+-------+------------+----------------+-------+------------+----------+-----------+-----------+
| pod-1/bl205-eu-spdc | 172.31.2.25   | down  | 1090519041 | 172.31.2.54    | down  | 0          | multihop | overlay-1 | lo3       | 
| pod-1/bl206-eu-spdc | 172.31.2.26   | down  | 1090519041 | 172.31.2.54    | down  | 0          | multihop | overlay-1 | lo2       | 
| pod-1/rl301-eu-spdc | 172.31.3.31   | down  | 1090519041 | 172.31.3.35    | down  | 0          | multihop | overlay-1 | lo3       | 
| pod-1/rl302-eu-spdc | 172.31.3.32   | down  | 1090519041 | 172.31.3.35    | down  | 0          | multihop | overlay-1 | lo3       | 
+---------------------+---------------+-------+------------+----------------+-------+------------+----------+-----------+-----------+
```

Developer

```
# iserver get aci proto bfd --apic apic11 --node any --state up

{
    "duration": 11200,
    "apic": {
        "read": true,
        "success": 32,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 31,
        "connect_time": 453,
        "disconnect_time": 0,
        "mo_time": 10086,
        "total_time": 10539
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

True	453	-	connect apic11o.emea-sp.cisco.com
True	320	13	apic11o.emea-sp.cisco.com class fabricNode
True	309	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bfd/inst
True	358	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	340	8	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	334	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bfd/inst
True	349	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	333	12	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	314	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst
True	341	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	337	15	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	352	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/bfd/inst
True	356	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	380	15	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	321	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys/bfd/inst
True	288	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	327	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	334	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys/bfd/inst
True	348	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	325	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	295	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bfd/inst
True	332	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	330	7	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	374	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bfd/inst
True	294	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	307	7	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	299	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/bfd/inst
True	273	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	349	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	298	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/bfd/inst
True	278	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	291	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
```


[[Back]](./ProtocolBfd.md)