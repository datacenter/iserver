# POD CIDR w/community

## Task

```
[
  {
    "cilium-bgp": {
      "feature": {},
      "cluster": {
        "asn": 64661,
        "peer": {
          "asn": 64001,
          "ip": [
            "10.10.10.20",
            "10.10.10.21"
          ]
        },
        "advertise": {
          "pod": {
            "community": [
              "64661:666",
              "no-advertise"
            ]
          }
        }
      },
      "wipe": {}
    }
  }
]
```

## CRD

```
apiVersion: isovalent.com/v1
kind: IsovalentBGPClusterConfig
metadata:
  name: cluster
spec:
  bgpInstances:
  - localASN: 64661
    name: bgp
    peers:
    - name: tor1
      peerASN: 64001
      peerAddress: 10.10.10.20
      peerConfigRef:
        name: peer
    - name: tor2
      peerASN: 64001
      peerAddress: 10.10.10.21
      peerConfigRef:
        name: peer
---
apiVersion: isovalent.com/v1
kind: IsovalentBGPPeerConfig
metadata:
  name: peer
spec:
  ebgpMultihop: 1
  families:
  - advertisements:
      matchLabels:
        advertise: bgp
    afi: ipv4
    safi: unicast
  gracefulRestart:
    enabled: false
    restartTimeSeconds: 120
  timers:
    connectRetryTimeSeconds: 120
    holdTimeSeconds: 90
    keepAliveTimeSeconds: 30
  transport:
    peerPort: 179
---
apiVersion: isovalent.com/v1
kind: IsovalentBGPAdvertisement
metadata:
  labels:
    advertise: bgp
  name: advertise-pod
spec:
  advertisements:
  - advertisementType: PodCIDR
    attributes:
      communities:
        standard:
        - 64661:666
        wellKnown:
        - no-advertise
```

## State

```
+----+-------+----------+-------+-----------+-------------+----------+-------------+-----------+------+------+---------+-----+-----+    
| ID | Node  | Instance | ASN   | Peer name | Peer IP     | Peer ASN | State       | Keepalive | Hold | AFI  | SAFI    | Adv | Rcv |    
+----+-------+----------+-------+-----------+-------------+----------+-------------+-----------+------+------+---------+-----+-----+    
| 1  | bm1-1 | bgp      | 64661 | tor1      | 10.10.10.20 | 64001    | established | 30        | 90   | ipv4 | unicast | 1   | 0   |    
| 2  | bm1-1 | bgp      | 64661 | tor2      | 10.10.10.21 | 64001    | established | 30        | 90   | ipv4 | unicast | 1   | 0   |    
| 3  | bm1-2 | bgp      | 64661 | tor1      | 10.10.10.20 | 64001    | established | 30        | 90   | ipv4 | unicast | 1   | 0   |    
| 4  | bm1-2 | bgp      | 64661 | tor2      | 10.10.10.21 | 64001    | established | 30        | 90   | ipv4 | unicast | 1   | 0   |    
| 5  | bm1-3 | bgp      | 64661 | tor1      | 10.10.10.20 | 64001    | established | 30        | 90   | ipv4 | unicast | 1   | 0   |    
| 6  | bm1-3 | bgp      | 64661 | tor2      | 10.10.10.21 | 64001    | established | 30        | 90   | ipv4 | unicast | 1   | 0   |    
+----+-------+----------+-------+-----------+-------------+----------+-------------+-----------+------+------+---------+-----+-----+ 
```

```
~~~
# cilium bgp peers -n cilium
Node    Local AS   Peer AS   Peer Address   Session State   Uptime   Family         Received   Advertised
bm1-1   64661      64001     10.10.10.20    established     7m35s    ipv4/unicast   0          1
        64661      64001     10.10.10.21    established     7m35s    ipv4/unicast   0          1
bm1-2   64661      64001     10.10.10.20    established     7m35s    ipv4/unicast   0          1
        64661      64001     10.10.10.21    established     7m35s    ipv4/unicast   0          1
bm1-3   64661      64001     10.10.10.20    established     7m36s    ipv4/unicast   0          1
        64661      64001     10.10.10.21    established     7m36s    ipv4/unicast   0          1

~~~

~~~
# cilium bgp routes advertised ipv4 unicast -n cilium
Node    VRouter   Peer          Prefix          NextHop       Age     Attrs
bm1-1   64661     10.10.10.20   10.128.2.0/23   10.10.10.10   7m37s   [{Origin: i} {AsPath: 64661} {Nexthop: 10.10.10.10} {Communities: 64661:666, no-advertise}]
        64661     10.10.10.21   10.128.2.0/23   10.10.10.10   7m37s   [{Origin: i} {AsPath: 64661} {Nexthop: 10.10.10.10} {Communities: 64661:666, no-advertise}]
bm1-2   64661     10.10.10.20   10.128.4.0/23   10.10.10.11   7m37s   [{Origin: i} {AsPath: 64661} {Nexthop: 10.10.10.11} {Communities: 64661:666, no-advertise}]
        64661     10.10.10.21   10.128.4.0/23   10.10.10.11   7m37s   [{Origin: i} {AsPath: 64661} {Nexthop: 10.10.10.11} {Communities: 64661:666, no-advertise}]
bm1-3   64661     10.10.10.20   10.128.0.0/23   10.10.10.12   7m38s   [{Origin: i} {AsPath: 64661} {Nexthop: 10.10.10.12} {Communities: 64661:666, no-advertise}]
        64661     10.10.10.21   10.128.0.0/23   10.10.10.12   7m38s   [{Origin: i} {AsPath: 64661} {Nexthop: 10.10.10.12} {Communities: 64661:666, no-advertise}]

~~~
```

## ACI

```
node# show bgp ipv4 unicast 10.128.0.0/23 vrf common:MyVRF
  AS-Path: 64661 , path sourced external to AS
      Origin IGP, MED not set, localpref 100, weight 0 tag 0, propagate 0, floating svi 0, tunnel resolved 0
      Community: 64661:666 no-advertise
      Extcommunity:
          RT:64001:2818048
          VNID:2818048
```

[[Back]](./README.md)