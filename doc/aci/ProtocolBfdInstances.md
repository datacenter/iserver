# Node Protocol - BFD

## Get BFD instance summary from all nodes

```
# iserver get aci proto bfd --apic apic11 --node any --view instance

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

+---------------------+---------+-------------+-----------------+-----------+-----------------+--------------------+
| Node                | Admin   | Echo Intf   | Session Summary | Interface | Interface State | Interface Sessions |
+---------------------+---------+-------------+-----------------+-----------+-----------------+--------------------+
| pod-1/bl205-eu-spdc | enabled | unspecified | 0/1             | lo3       | enabled         | 0/1                | 
| pod-1/bl206-eu-spdc | enabled | unspecified | 0/1             | lo2       | enabled         | 0/1                | 
| pod-1/cl201-eu-spdc | enabled | unspecified | 0/0             |           |                 |                    | 
| pod-1/cl202-eu-spdc | enabled | unspecified | 0/0             |           |                 |                    | 
| pod-1/cl209-eu-spdc | enabled | unspecified | 0/0             |           |                 |                    | 
| pod-1/cl210-eu-spdc | enabled | unspecified | 0/0             |           |                 |                    | 
| pod-1/rl301-eu-spdc | enabled | unspecified | 0/1             | lo3       | enabled         | 0/1                | 
| pod-1/rl302-eu-spdc | enabled | unspecified | 0/1             | lo3       | enabled         | 0/1                | 
| pod-1/s101-eu-spdc  | enabled | unspecified | 0/0             |           |                 |                    | 
| pod-1/s102-eu-spdc  | enabled | unspecified | 0/0             |           |                 |                    | 
+---------------------+---------+-------------+-----------------+-----------+-----------------+--------------------+
```

Developer

```
# iserver get aci proto bfd --apic apic11 --node any --view instance

{
    "duration": 10679,
    "apic": {
        "read": true,
        "success": 32,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 31,
        "connect_time": 429,
        "disconnect_time": 0,
        "mo_time": 9668,
        "total_time": 10097
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

True	429	-	connect apic11o.emea-sp.cisco.com
True	308	13	apic11o.emea-sp.cisco.com class fabricNode
True	296	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bfd/inst
True	295	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	302	8	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	300	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bfd/inst
True	297	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	280	12	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	302	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst
True	277	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	300	15	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	292	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/bfd/inst
True	292	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	300	15	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	304	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys/bfd/inst
True	343	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	303	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	345	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys/bfd/inst
True	306	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	348	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	300	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bfd/inst
True	305	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	309	7	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	352	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bfd/inst
True	306	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	307	7	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	319	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/bfd/inst
True	351	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	300	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	337	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/bfd/inst
True	362	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	330	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
```

[[Back]](./ProtocolBfd.md)