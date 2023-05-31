# Node Protocol - ARP

## Filter adjacencies by VRF name

```
# iserver get aci proto arp --apic apic11 --vrf *infra*

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-------------------------+-------------------+----------------+--------+------------+---------------+-------------------------------+
| Node                | VRF                     | MAC               | IP             | State  | Interface  | Phy Interface | Timestamp                     |
+---------------------+-------------------------+-------------------+----------------+--------+------------+---------------+-------------------------------+
| pod-1/bl205-eu-spdc | common:Infra_BGP_VRF    | 00:A3:8E:EB:B3:3F | 192.168.254.1  | normal | eth1/24.62 | eth1/24       | 2023-05-30T18:20:51.579+02:00 | 
| pod-1/bl205-eu-spdc | common:Infra_privIP_VRF | 00:A3:8E:EB:B3:3F | 192.168.254.66 | normal | eth1/24.36 | eth1/24       | 2023-05-30T18:08:08.346+02:00 | 
+---------------------+-------------------------+-------------------+----------------+--------+------------+---------------+-------------------------------+
```

Developer

```
# iserver get aci proto arp --apic apic11 --vrf *infra*

{
    "duration": 5616,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 731,
        "disconnect_time": 0,
        "mo_time": 4677,
        "total_time": 5408
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

True	731	-	connect apic11o.emea-sp.cisco.com
True	1115	11	apic11o.emea-sp.cisco.com class fabricNode
True	1114	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/arpDom
True	2448	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
```

[[Back]](./ProtocolArp.md)