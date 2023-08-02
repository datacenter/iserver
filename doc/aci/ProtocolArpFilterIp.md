# Node Protocol - ARP

## Filter adjacencies by IP address

```
# iserver get aci proto arp
    --apic apic21
    --node bl2205-eu-spdc
    --ip 192.168.254.74
    --view adj

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Protocol ARP - Adjacency [#1]
-----------------------------

+----------------------+-------------------------+-------------------+----------------+--------+------------+---------------+-------------------------------+
| Node                 | VRF                     | MAC               | IP             | State  | Interface  | Phy Interface | Timestamp                     |
+----------------------+-------------------------+-------------------+----------------+--------+------------+---------------+-------------------------------+
| pod-1/bl2205-eu-spdc | common:Infra_privIP_VRF | 00:A3:8E:EB:B3:3F | 192.168.254.74 | normal | eth1/25.17 | eth1/25       | 2023-08-02T14:28:36.062+02:00 | 
+----------------------+-------------------------+-------------------+----------------+--------+------------+---------------+-------------------------------+

Protocol ARP - Interface Adjacency Summary [#1]
-----------------------------------------------

+----------------------+------------+-----------+
| Node                 | Interface  | Adjacency |
+----------------------+------------+-----------+
| pod-1/bl2205-eu-spdc | eth1/25.17 | 1         | 
+----------------------+------------+-----------+
```

Developer

```
# iserver get aci proto arp
    --apic apic21
    --node bl2205-eu-spdc
    --ip 192.168.254.74
    --view adj

{
    "duration": 1374,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 377,
        "disconnect_time": 0,
        "mo_time": 832,
        "total_time": 1209
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

True	377	-	connect apic21o.emea-sp.cisco.com:443
True	275	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	290	12	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/arpDom query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	267	13	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
```

[[Back]](./ProtocolArp.md)