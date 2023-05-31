# Node Protocol - ARP

## Filter adjacencies by IP address

```
# iserver get aci proto arp --apic apic11 --ip 15.2.7.1

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+----------------------+-------------------+----------+--------+-----------+---------------+-------------------------------+
| Node                | VRF                  | MAC               | IP       | State  | Interface | Phy Interface | Timestamp                     |
+---------------------+----------------------+-------------------+----------+--------+-----------+---------------+-------------------------------+
| pod-1/bl205-eu-spdc | MPC-F5T:F5-OUT_VRF   | 00:50:56:B2:80:63 | 15.2.7.1 | normal | vlan63    | tunnel2       | 2023-05-30T18:22:42.541+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF | 00:50:56:B2:D5:AB | 15.2.7.1 | normal | vlan61    | po5           | 2023-05-30T18:22:15.727+02:00 | 
+---------------------+----------------------+-------------------+----------+--------+-----------+---------------+-------------------------------+
```

Developer

```
# iserver get aci proto arp --apic apic11 --ip 15.2.7.1

{
    "duration": 1333,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 384,
        "disconnect_time": 0,
        "mo_time": 862,
        "total_time": 1246
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

True	384	-	connect apic11o.emea-sp.cisco.com
True	296	11	apic11o.emea-sp.cisco.com class fabricNode
True	290	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/arpDom
True	276	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
```

[[Back]](./ProtocolArp.md)