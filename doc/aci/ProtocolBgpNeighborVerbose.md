# Node Protocol - BGP

## Show details of selected BGP neighbors

```
# iserver get aci proto bgp
    --apic apic11
    --node rl301
    --nbr-ip 172.24.3.3
    --view verbose

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: rl301-eu-spdc

+---------------------+--------------------------+------------------+-------------+-------+------+-----+-----------------+
| Node                | VRF                      | Neighbor Address | BGP State   | ASN   | Type | TTL | Paths (AF IPv4) |
+---------------------+--------------------------+------------------+-------------+-------+------+-----+-----------------+
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3       | established | 64371 | ebgp | 4   | 3               | 
+---------------------+--------------------------+------------------+-------------+-------+------+-----+-----------------+

BGP Neighbor
------------
- VRF                         : MPC-E:MPC-E-sPBR-OUT_VRF
- Admin State                 : enabled
- BGP State                   : established
- Neighbor Address            : 172.24.3.3
- Remote Router Id            : 172.24.3.3
- Remote Port                 : 1899
- Remote ASN                  : 64371
- Received Capabilities       : as4,cap,gr,ipv4-ucast,refresh,refresh-old
- Session Type                : ebgp
- TTL                         : 4
- Peer Index                  : 2
- Update Source Intf          : lo9
- Local IP                    : 172.24.3.15
- Local Port                  : 179
- Advertised Capabilities     : as4,dynamic,dynamic-gr,dynamic-mp,dynamic-old,dynamic-refresh,gr-helper,ipv4-ucast,refresh,refresh-old
- Hold Timer                  : 90
- Keepalive Timer             : 30
- Connection Attempts         : 202
- Connection Established      : 1
- Connection Dropped          : 0
- Accepted IPv4 Unicast Paths : 3


+----------------+-------+----------+
| Message Type   | Sent  | Received |
+----------------+-------+----------+
| Opens          | 1     | 1        | 
| Notifications  | 0     | 0        | 
| Updates        | 2     | 2        | 
| Keepalives     | 4773  | 4772     | 
| Route Refresh  | 0     | 0        | 
| Capability     | 0     | 0        | 
| Total          | 4776  | 4775     | 
| Total Bytes    | 90733 | 90747    | 
| Bytes in Queue | 0     | 0        | 
+----------------+-------+----------+

+---------------------+--------------------------+--------------+---------------+------+-----------+--------------------------+------------+--------+------------+
| Node                | VRF                      | Prefix       | Next Hop      | Type | Source    | NH VRF                   | MPLS Label | Active | Preference |
+---------------------+--------------------------+--------------+---------------+------+-----------+--------------------------+------------+--------+------------+
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 33.99.8.0/22 | 172.24.3.3/32 | ebgp | bgp-50000 | MPC-E:MPC-E-sPBR-OUT_VRF | 0          | yes    | 20         | 
+---------------------+--------------------------+--------------+---------------+------+-----------+--------------------------+------------+--------+------------+
```

Developer

```
# iserver get aci proto bgp
    --apic apic11
    --node rl301
    --nbr-ip 172.24.3.3
    --view verbose

{
    "duration": 4534,
    "apic": {
        "read": true,
        "success": 7,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 6,
        "connect_time": 885,
        "disconnect_time": 0,
        "mo_time": 2148,
        "total_time": 3033
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

True	885	-	connect apic11o.emea-sp.cisco.com
True	337	13	apic11o.emea-sp.cisco.com class fabricNode
True	362	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bgp/inst
True	351	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom
True	345	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	365	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bgp/inst/dom-MPC-E:MPC-E-sPBR-OUT_VRF/peer-[172.24.3.3/32]/ent-[172.24.3.3]/peerstats
True	388	36	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-MPC-E:MPC-E-sPBR-OUT_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
```

[[Back]](./ProtocolBgp.md)