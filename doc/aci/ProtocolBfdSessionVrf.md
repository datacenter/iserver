# Node Protocol - BFD

## Filter sessions by vrf name

```
# iserver get aci proto bfd --apic apic11 --node any --vrf *common*

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

+---------------------+----------------+-------+------------+----------------+-------+------------+-----------+-------------------------------+-----------+
| Node                | Local Address  | State | Session Id | Remote Address | State | Session Id | Type      | VRF                           | Interface |
+---------------------+----------------+-------+------------+----------------+-------+------------+-----------+-------------------------------+-----------+
| pod-1/cl201-eu-spdc | 15.254.101.4   | down  | 1090519041 | 15.100.7.41    | down  | 0          | singlehop | common:smi5Gc-cvim1-N3-N4_VRF | vlan468   | 
| pod-1/cl201-eu-spdc | 15.254.103.252 | up    | 1090519045 | 15.254.103.192 | up    | 3          | singlehop | common:smi5Gc-cvim1-N3-N4_VRF | vlan469   | 
| pod-1/cl201-eu-spdc | 15.254.103.252 | up    | 1090519047 | 15.254.103.191 | up    | 3          | singlehop | common:smi5Gc-cvim1-N3-N4_VRF | vlan469   | 
| pod-1/cl201-eu-spdc | 15.254.106.252 | up    | 1090519043 | 15.254.106.191 | up    | 1          | singlehop | common:smi5Gc-cvim1-N6_VRF    | vlan473   | 
| pod-1/cl201-eu-spdc | 15.254.106.252 | up    | 1090519049 | 15.254.106.192 | up    | 1          | singlehop | common:smi5Gc-cvim1-N6_VRF    | vlan473   | 
| pod-1/cl202-eu-spdc | 15.254.104.253 | up    | 1090519042 | 15.254.104.191 | up    | 4          | singlehop | common:smi5Gc-cvim1-N3-N4_VRF | vlan491   | 
| pod-1/cl202-eu-spdc | 15.254.104.253 | up    | 1090519045 | 15.254.104.192 | up    | 4          | singlehop | common:smi5Gc-cvim1-N3-N4_VRF | vlan491   | 
| pod-1/cl202-eu-spdc | 15.254.107.253 | up    | 1090519044 | 15.254.107.192 | up    | 2          | singlehop | common:smi5Gc-cvim1-N6_VRF    | vlan494   | 
| pod-1/cl202-eu-spdc | 15.254.107.253 | up    | 1090519046 | 15.254.107.191 | up    | 2          | singlehop | common:smi5Gc-cvim1-N6_VRF    | vlan494   | 
+---------------------+----------------+-------+------------+----------------+-------+------------+-----------+-------------------------------+-----------+
```

Developer

```
# iserver get aci proto bfd --apic apic11 --node any --vrf *common*

{
    "duration": 7936,
    "apic": {
        "read": true,
        "success": 26,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 25,
        "connect_time": 401,
        "disconnect_time": 0,
        "mo_time": 7249,
        "total_time": 7650
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

True	401	-	connect apic11o.emea-sp.cisco.com
True	297	11	apic11o.emea-sp.cisco.com class fabricNode
True	268	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bfd/inst
True	275	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	289	8	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	298	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bfd/inst
True	277	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	285	12	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	371	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst
True	290	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	285	15	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	277	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/bfd/inst
True	287	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	294	15	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	290	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bfd/inst
True	309	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	278	7	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	323	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bfd/inst
True	267	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	286	7	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	291	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/bfd/inst
True	276	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	282	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	286	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/bfd/inst
True	281	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	287	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
```

[[Back]](./ProtocolBfd.md)