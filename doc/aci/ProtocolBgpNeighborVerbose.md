# Node Protocol - BGP

## Show details of selected BGP neighbors

```
# iserver get aci proto bgp
    --apic apic11
    --node rl301
    --nbr-ip 172.24.3.3
    --view verbose

Apic: apic11o.emea-sp.cisco.com
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
- Remote Port                 : 179
- Remote ASN                  : 64371
- Received Capabilities       : as4,cap,gr,ipv4-ucast,refresh,refresh-old
- Session Type                : ebgp
- TTL                         : 4
- Peer Index                  : 1
- Update Source Intf          : lo8
- Local IP                    : 172.24.3.15
- Local Port                  : 38418
- Advertised Capabilities     : as4,dynamic,dynamic-gr,dynamic-mp,dynamic-old,dynamic-refresh,gr-helper,ipv4-ucast,refresh,refresh-old
- Hold Timer                  : 90
- Keepalive Timer             : 30
- Connection Attempts         : 8
- Connection Established      : 3
- Connection Dropped          : 2
- Accepted IPv4 Unicast Paths : 3


+----------------+---------+----------+
| Message Type   | Sent    | Received |
+----------------+---------+----------+
| Opens          | 3       | 3        | 
| Notifications  | 2       | 0        | 
| Updates        | 8       | 9        | 
| Keepalives     | 255479  | 255484   | 
| Route Refresh  | 1       | 0        | 
| Capability     | 0       | 0        | 
| Total          | 255493  | 255496   | 
| Total Bytes    | 4854369 | 4854555  | 
| Bytes in Queue | 0       | 0        | 
+----------------+---------+----------+

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
    "duration": 2388,
    "apic": {
        "read": true,
        "success": 7,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 6,
        "connect_time": 395,
        "disconnect_time": 0,
        "mo_time": 1782,
        "total_time": 2177
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

True	395	-	connect apic11o.emea-sp.cisco.com
True	296	11	apic11o.emea-sp.cisco.com class fabricNode
True	278	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bgp/inst
True	293	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom
True	347	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	277	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bgp/inst/dom-MPC-E:MPC-E-sPBR-OUT_VRF/peer-[172.24.3.3/32]/ent-[172.24.3.3]/peerstats
True	291	44	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-MPC-E:MPC-E-sPBR-OUT_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
```

[[Back]](./ProtocolBgp.md)