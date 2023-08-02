# Node Protocol - BGP

## Inst view

```
# iserver get aci proto bgp --apic apic11 --node rl301 --view inst

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: rl301-eu-spdc

Protocol BGP - Instance [#1]
----------------------------

+---------------------+--------+---------+---------+-------+----------------+----------------------+-----------------+-------------------+---------------+-----------+--------------+
| Node                | Health | Faults  | Admin   | ASN   | VRF (Up/Count) | Neighbors (Up/Count) | AS Path Entries | Attribute Entries | Memory Status | SNMP Trap | Syslog Level |
+---------------------+--------+---------+---------+-------+----------------+----------------------+-----------------+-------------------+---------------+-----------+--------------+
| pod-1/rl301-eu-spdc | 100    | 0 0 0 0 | enabled | 50000 | 18/18          | 7/7                  | 28              | 284               | normal        | disable   | err          | 
+---------------------+--------+---------+---------+-------+----------------+----------------------+-----------------+-------------------+---------------+-----------+--------------+
```

Developer

```
# iserver get aci proto bgp --apic apic11 --node rl301 --view inst

{
    "duration": 1770,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 382,
        "disconnect_time": 0,
        "mo_time": 1252,
        "total_time": 1634
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

True	382	-	connect apic11o.emea-sp.cisco.com:443
True	315	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	275	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp query query-target=children&rsp-subtree-include=health,fault-count
True	381	18	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-301/bgpDom query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	281	27	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-301/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
```

[[Back]](./ProtocolBgp.md)