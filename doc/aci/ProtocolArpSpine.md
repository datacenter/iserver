# Node Protocol - ARP

## Spine nodes adjacencies

```
# iserver get aci proto arp --apic apic11 --role spine

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: s101-eu-spdc
- node: s102-eu-spdc

+--------------------+-----------+-------------------+-------------+--------+------------+---------------+-------------------------------+
| Node               | VRF       | MAC               | IP          | State  | Interface  | Phy Interface | Timestamp                     |
+--------------------+-----------+-------------------+-------------+--------+------------+---------------+-------------------------------+
| pod-1/s101-eu-spdc | overlay-1 | 00:8A:96:1C:7C:D4 | 192.168.1.2 | normal | eth1/16.16 | eth1/16       | 2023-06-14T07:49:06.374+02:00 | 
| pod-1/s102-eu-spdc | overlay-1 | 00:8A:96:1C:7C:D0 | 192.168.1.6 | normal | eth1/16.16 | eth1/16       | 2023-06-14T07:49:15.327+02:00 | 
+--------------------+-----------+-------------------+-------------+--------+------------+---------------+-------------------------------+
```

Developer

```
# iserver get aci proto arp --apic apic11 --role spine

{
    "duration": 2368,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 435,
        "disconnect_time": 0,
        "mo_time": 1675,
        "total_time": 2110
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

True	435	-	connect apic11o.emea-sp.cisco.com
True	335	13	apic11o.emea-sp.cisco.com class fabricNode
True	325	4	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/arpDom
True	337	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
True	344	4	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/arpDom
True	334	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
```

[[Back]](./ProtocolArp.md)