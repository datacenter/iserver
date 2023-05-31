# Node Protocol - BFD

## Filter sessions by interface name

```
# iserver get aci proto bfd --apic apic11 --node any --intf lo*

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc
- node: s101-eu-spdc
- node: s102-eu-spdc

+---------------------+---------------+-------+------------+----------------+-------+------------+----------+-----------+-----------+
| Node                | Local Address | State | Session Id | Remote Address | State | Session Id | Type     | VRF       | Interface |
+---------------------+---------------+-------+------------+----------------+-------+------------+----------+-----------+-----------+
| pod-1/bl205-eu-spdc | 172.31.2.25   | down  | 1090519041 | 172.31.2.54    | down  | 0          | multihop | overlay-1 | lo3       | 
| pod-1/bl206-eu-spdc | 172.31.2.26   | down  | 1090519041 | 172.31.2.54    | down  | 0          | multihop | overlay-1 | lo3       | 
| pod-1/rl301-eu-spdc | 172.31.3.31   | down  | 1090519041 | 172.31.3.35    | down  | 0          | multihop | overlay-1 | lo4       | 
| pod-1/rl302-eu-spdc | 172.31.3.32   | down  | 1090519041 | 172.31.3.35    | down  | 0          | multihop | overlay-1 | lo4       | 
+---------------------+---------------+-------+------------+----------------+-------+------------+----------+-----------+-----------+
```

Developer

```
# iserver get aci proto bfd --apic apic11 --node any --intf lo*

{
    "duration": 7951,
    "apic": {
        "read": true,
        "success": 26,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 25,
        "connect_time": 391,
        "disconnect_time": 0,
        "mo_time": 7315,
        "total_time": 7706
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

True	391	-	connect apic11o.emea-sp.cisco.com
True	300	11	apic11o.emea-sp.cisco.com class fabricNode
True	283	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bfd/inst
True	278	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	282	8	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	284	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bfd/inst
True	281	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	281	12	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	343	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst
True	290	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	310	15	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	296	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/bfd/inst
True	303	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	276	15	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	306	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bfd/inst
True	289	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	337	7	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	279	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bfd/inst
True	287	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	292	7	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	294	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/bfd/inst
True	285	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	290	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	277	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/bfd/inst
True	288	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	284	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
```

[[Back]](./ProtocolBfd.md)