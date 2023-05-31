# Node Protocol - BFD

## Get BFD instance summary from all nodes

```
# iserver get aci proto bfd --apic apic11 --node any --view instance

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

+---------------------+---------+-------------+-----------------+-----------+-----------------+--------------------+
| Node                | Admin   | Echo Intf   | Session Summary | Interface | Interface State | Interface Sessions |
+---------------------+---------+-------------+-----------------+-----------+-----------------+--------------------+
| pod-1/bl205-eu-spdc | enabled | unspecified | 0/1             | lo3       | enabled         | 0/1                | 
| pod-1/bl206-eu-spdc | enabled | unspecified | 0/1             | lo3       | enabled         | 0/1                | 
| pod-1/cl201-eu-spdc | enabled | unspecified | 4/5             | vlan469   | enabled         | 2/2                | 
|                     |         |             |                 | vlan468   | enabled         | 0/1                | 
| pod-1/cl202-eu-spdc | enabled | unspecified | 4/4             | vlan491   | enabled         | 2/2                | 
| pod-1/rl301-eu-spdc | enabled | unspecified | 0/1             | lo4       | enabled         | 0/1                | 
| pod-1/rl302-eu-spdc | enabled | unspecified | 0/1             | lo4       | enabled         | 0/1                | 
| pod-1/s101-eu-spdc  | enabled | unspecified | 0/0             |           |                 |                    | 
| pod-1/s102-eu-spdc  | enabled | unspecified | 0/0             |           |                 |                    | 
+---------------------+---------+-------------+-----------------+-----------+-----------------+--------------------+
```

Developer

```
# iserver get aci proto bfd --apic apic11 --node any --view instance

{
    "duration": 27056,
    "apic": {
        "read": true,
        "success": 26,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 25,
        "connect_time": 387,
        "disconnect_time": 0,
        "mo_time": 26398,
        "total_time": 26785
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

True	387	-	connect apic11o.emea-sp.cisco.com
True	284	11	apic11o.emea-sp.cisco.com class fabricNode
True	284	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bfd/inst
True	19335	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	327	8	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	312	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bfd/inst
True	271	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	284	12	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	334	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst
True	285	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	285	15	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	287	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/bfd/inst
True	300	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	286	15	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	284	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bfd/inst
True	277	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	280	7	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	282	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bfd/inst
True	278	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	294	7	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	384	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/bfd/inst
True	313	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	282	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	272	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/bfd/inst
True	291	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	287	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
```

[[Back]](./ProtocolBfd.md)