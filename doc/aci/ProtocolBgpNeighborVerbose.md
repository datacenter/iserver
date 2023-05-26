# Node Protocol - BGP

## Show details of selected BGP neighbors

```
# iserver get aci proto bgp
    --apic apic11
    --node rl301
    --nbr-ip 172.24.3.3 -o verbose

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
| Keepalives     | 237306  | 237310   | 
| Route Refresh  | 1       | 0        | 
| Capability     | 0       | 0        | 
| Total          | 237320  | 237322   | 
| Total Bytes    | 4509082 | 4509249  | 
| Bytes in Queue | 0       | 0        | 
+----------------+---------+----------+

+---------------------+--------------------------+--------------+---------------+------+-----------+--------------------------+------------+--------+------------+
| Node                | VRF                      | Prefix       | Next Hop      | Type | Source    | NH VRF                   | MPLS Label | Active | Preference |
+---------------------+--------------------------+--------------+---------------+------+-----------+--------------------------+------------+--------+------------+
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 33.99.8.0/22 | 172.24.3.3/32 | ebgp | bgp-50000 | MPC-E:MPC-E-sPBR-OUT_VRF | 0          | yes    | 20         | 
+---------------------+--------------------------+--------------+---------------+------+-----------+--------------------------+------------+--------+------------+
```

[[Back]](./ProtocolBgp.md)