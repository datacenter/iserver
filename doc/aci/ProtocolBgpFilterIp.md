# Node Protocol - BGP

## Filter BGP neighbors by neighbor IP Address

Example: IP address

```
# iserver get aci proto bgp
    --apic apic11
    --node rl301
    --nbr-ip 172.24.3.3
    --view nei

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: rl301-eu-spdc

Protocol BGP - Neighbor [#1]
----------------------------

+---------------------+--------------------------+-------------+------------+---------+-------------+-------+------+-----+----------+-------------+---------------+--------------+
| Node                | VRF                      | Nbr Address | Router Id  | Admin   | BGP         | ASN   | Type | TTL | Src Intf | Local IP    | Conns (A/D/E) | Paths        |
+---------------------+--------------------------+-------------+------------+---------+-------------+-------+------+-----+----------+-------------+---------------+--------------+
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3  | 172.24.3.3 | enabled | established | 64371 | ebgp | 4   | lo17     | 172.24.3.15 | 3/0/1         | IPv4-ucast:3 | 
+---------------------+--------------------------+-------------+------------+---------+-------------+-------+------+-----+----------+-------------+---------------+--------------+
```

Example: IP subnet

```
# iserver get aci proto bgp
    --apic apic11
    --node rl301
    --nbr-subnet 15.0.0.0/8
    --view nei

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: rl301-eu-spdc

Protocol BGP - Neighbor [#1]
----------------------------

+---------------------+-----------+-------------+-------------+---------+-------------+-------+------+-----+----------+-----------+---------------+
| Node                | VRF       | Nbr Address | Router Id   | Admin   | BGP         | ASN   | Type | TTL | Src Intf | Local IP  | Conns (A/D/E) |
+---------------------+-----------+-------------+-------------+---------+-------------+-------+------+-----+----------+-----------+---------------+
| pod-1/rl301-eu-spdc | overlay-1 | 15.16.3.1   | 35.35.35.35 | enabled | established | 64001 | ebgp | 1   | eth1/29  | 15.16.3.2 | 1/0/1         | 
+---------------------+-----------+-------------+-------------+---------+-------------+-------+------+-----+----------+-----------+---------------+
```

Developer

```
# iserver get aci proto bgp
    --apic apic11
    --node rl301
    --nbr-ip 172.24.3.3
    --view nei

{
    "duration": 2037,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 393,
        "disconnect_time": 0,
        "mo_time": 1457,
        "total_time": 1850
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

True	393	-	connect apic11o.emea-sp.cisco.com:443
True	292	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	275	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp query query-target=children&rsp-subtree-include=health,fault-count
True	340	18	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-301/bgpDom query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	280	27	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-301/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	270	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp/inst/dom-MPC-E:MPC-E-sPBR-OUT_VRF/peer-[172.24.3.3/32]/ent-[172.24.3.3]/peerstats
```

[[Back]](./ProtocolBgp.md)