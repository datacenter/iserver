# Node Protocol - ARP

## Filter adjacencies by VRF name

```
# iserver get aci proto arp --apic apic11 --vrf *infra*

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+---------------------+-------------------------+-------------------+----------------+--------+------------+---------------+-------------------------------+
| Node                | VRF                     | MAC               | IP             | State  | Interface  | Phy Interface | Timestamp                     |
+---------------------+-------------------------+-------------------+----------------+--------+------------+---------------+-------------------------------+
| pod-1/bl205-eu-spdc | common:Infra_BGP_VRF    | 00:A3:8E:EB:B3:3F | 192.168.254.1  | normal | eth1/24.48 | eth1/24       | 2023-06-14T07:59:40.468+02:00 | 
| pod-1/bl205-eu-spdc | common:Infra_privIP_VRF | 00:A3:8E:EB:B3:3F | 192.168.254.66 | normal | eth1/24.47 | eth1/24       | 2023-06-14T07:55:52.820+02:00 | 
+---------------------+-------------------------+-------------------+----------------+--------+------------+---------------+-------------------------------+
```

Developer

```
# iserver get aci proto arp --apic apic11 --vrf *infra*

{
    "duration": 1745,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 441,
        "disconnect_time": 0,
        "mo_time": 983,
        "total_time": 1424
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

True	441	-	connect apic11o.emea-sp.cisco.com
True	343	13	apic11o.emea-sp.cisco.com class fabricNode
True	311	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/arpDom
True	329	12	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
```

[[Back]](./ProtocolArp.md)