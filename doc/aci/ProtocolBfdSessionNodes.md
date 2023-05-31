# Node Protocol - BFD

## Get BFD sessions from selected nodes

```
# iserver get aci proto bfd --apic apic11 --node cl201-eu-spdc --node bl

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc

+---------------------+----------------+-------+------------+----------------+-------+------------+-----------+-------------------------------+-----------+
| Node                | Local Address  | State | Session Id | Remote Address | State | Session Id | Type      | VRF                           | Interface |
+---------------------+----------------+-------+------------+----------------+-------+------------+-----------+-------------------------------+-----------+
| pod-1/bl205-eu-spdc | 172.31.2.25    | down  | 1090519041 | 172.31.2.54    | down  | 0          | multihop  | overlay-1                     | lo3       | 
| pod-1/bl206-eu-spdc | 172.31.2.26    | down  | 1090519041 | 172.31.2.54    | down  | 0          | multihop  | overlay-1                     | lo3       | 
| pod-1/cl201-eu-spdc | 15.254.101.4   | down  | 1090519041 | 15.100.7.41    | down  | 0          | singlehop | common:smi5Gc-cvim1-N3-N4_VRF | vlan468   | 
| pod-1/cl201-eu-spdc | 15.254.103.252 | up    | 1090519045 | 15.254.103.192 | up    | 3          | singlehop | common:smi5Gc-cvim1-N3-N4_VRF | vlan469   | 
| pod-1/cl201-eu-spdc | 15.254.103.252 | up    | 1090519047 | 15.254.103.191 | up    | 3          | singlehop | common:smi5Gc-cvim1-N3-N4_VRF | vlan469   | 
| pod-1/cl201-eu-spdc | 15.254.106.252 | up    | 1090519043 | 15.254.106.191 | up    | 1          | singlehop | common:smi5Gc-cvim1-N6_VRF    | vlan473   | 
| pod-1/cl201-eu-spdc | 15.254.106.252 | up    | 1090519049 | 15.254.106.192 | up    | 1          | singlehop | common:smi5Gc-cvim1-N6_VRF    | vlan473   | 
+---------------------+----------------+-------+------------+----------------+-------+------------+-----------+-------------------------------+-----------+
```

Developer

```
# iserver get aci proto bfd --apic apic11 --node cl201-eu-spdc --node bl

{
    "duration": 3391,
    "apic": {
        "read": true,
        "success": 11,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 10,
        "connect_time": 387,
        "disconnect_time": 0,
        "mo_time": 2886,
        "total_time": 3273
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
True	300	11	apic11o.emea-sp.cisco.com class fabricNode
True	279	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bfd/inst
True	274	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	297	8	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	278	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bfd/inst
True	289	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	284	12	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	294	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst
True	305	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst query query-target=children&target-subtree-class=bfdSess
True	286	15	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
```

[[Back]](./ProtocolBfd.md)