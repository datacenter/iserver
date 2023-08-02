# Node Protocol - ARP

## Filter adjacencies by MAC address

```
# iserver get aci proto arp
    --apic apic21
    --node bl2205-eu-spdc
    --mac b33f
    --view adj

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Protocol ARP - Adjacency [#3]
-----------------------------

+----------------------+-------------------------+-------------------+----------------+--------+------------+---------------+-------------------------------+
| Node                 | VRF                     | MAC               | IP             | State  | Interface  | Phy Interface | Timestamp                     |
+----------------------+-------------------------+-------------------+----------------+--------+------------+---------------+-------------------------------+
| pod-1/bl2205-eu-spdc | common:Infra_privIP_VRF | 00:A3:8E:EB:B3:3F | 192.168.254.74 | normal | eth1/25.17 | eth1/25       | 2023-08-02T14:28:36.062+02:00 | 
| pod-1/bl2205-eu-spdc | common:Infra_VRF        | 00:A3:8E:EB:B3:3F | 192.168.254.9  | normal | eth1/25.18 | eth1/25       | 2023-08-02T14:28:37.342+02:00 | 
| pod-1/bl2205-eu-spdc | mgmt:inb                | 00:A3:8E:EB:B3:3F | 192.168.254.25 | normal | eth1/25.19 | eth1/25       | 2023-08-02T14:28:36.112+02:00 | 
+----------------------+-------------------------+-------------------+----------------+--------+------------+---------------+-------------------------------+

Protocol ARP - Interface Adjacency Summary [#3]
-----------------------------------------------

+----------------------+------------+-----------+
| Node                 | Interface  | Adjacency |
+----------------------+------------+-----------+
| pod-1/bl2205-eu-spdc | eth1/25.17 | 1         | 
| pod-1/bl2205-eu-spdc | eth1/25.18 | 1         | 
| pod-1/bl2205-eu-spdc | eth1/25.19 | 1         | 
+----------------------+------------+-----------+
```

Developer

```
# iserver get aci proto arp
    --apic apic21
    --node bl2205-eu-spdc
    --mac b33f
    --view adj

{
    "duration": 1342,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 413,
        "disconnect_time": 0,
        "mo_time": 802,
        "total_time": 1215
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

True	413	-	connect apic21o.emea-sp.cisco.com:443
True	268	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	270	12	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/arpDom query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	264	13	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
```

[[Back]](./ProtocolArp.md)