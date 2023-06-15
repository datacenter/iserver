# Node Protocol - BFD

## Filter sessions by IP address

```
# iserver get aci proto bfd --apic apic11 --node any --ip 15.254.104.192

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
# iserver get aci proto bfd --apic apic11 --node any --ip 15.254.104.192

{
    "duration": 12051,
    "apic": {
        "read": true,
        "success": 32,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 31,
        "connect_time": 422,
        "disconnect_time": 0,
        "mo_time": 11006,
        "total_time": 11428
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

True	422	-	connect apic11o.emea-sp.cisco.com
True	322	13	apic11o.emea-sp.cisco.com class fabricNode
True	290	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bfd/inst
True	292	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	318	8	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	291	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bfd/inst
True	306	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	301	12	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	308	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst
True	330	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	283	15	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	368	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/bfd/inst
True	297	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	356	15	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	304	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys/bfd/inst
True	356	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	1337	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	339	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys/bfd/inst
True	327	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	299	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	344	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bfd/inst
True	357	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	359	7	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	327	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bfd/inst
True	327	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	369	7	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	332	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/bfd/inst
True	303	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	309	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	329	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/bfd/inst
True	302	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	324	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
```

[[Back]](./ProtocolBfd.md)