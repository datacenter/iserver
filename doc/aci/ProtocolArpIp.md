# Node Protocol - ARP

## Filter adjacencies by IP address

```
# iserver get aci proto arp --apic apic11 --ip 15.2.7.1

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+---------------------+----------------------+-------------+----------+------------+-----------+-------------------------------+
| Node                | VRF                  | MAC         | IP       | State      | Interface | Timestamp                     |
+---------------------+----------------------+-------------+----------+------------+-----------+-------------------------------+
| pod-1/bl205-eu-spdc | MPC-F5T:F5-OUT_VRF   | unspecified | 15.2.7.1 | incomplete | vlan56    | 2023-06-14T08:06:45.049+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF | unspecified | 15.2.7.1 | incomplete | vlan67    | 2023-06-14T08:07:01.065+02:00 | 
+---------------------+----------------------+-------------+----------+------------+-----------+-------------------------------+
```

Developer

```
# iserver get aci proto arp --apic apic11 --ip 15.2.7.1

{
    "duration": 1516,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 406,
        "disconnect_time": 0,
        "mo_time": 939,
        "total_time": 1345
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

True	406	-	connect apic11o.emea-sp.cisco.com
True	322	13	apic11o.emea-sp.cisco.com class fabricNode
True	304	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/arpDom
True	313	13	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
```

[[Back]](./ProtocolArp.md)