# Cilium BGP Control Plane - Create via Task

## Input

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
          ],
          "af": [
            "v4"
          ],
          "multihop": 5,
          "timer": {
            "retry": 5,
            "hold": 9,
            "keepalive": 3
          },
          "port": 179,
          "secret": null,
          "graceful": {
            "enabled": true,
            "restart": 120
          }
        },
        "advertise": {
          "pod": {
            "enabled": true,
            "community": [
              "64661:100",
              "blackhole"
            ]
          },
          "cluster": {
              "enabled": true,
              "selector": [
                {
                  "key": "bgp",
                  "operator": "In",
                  "values": [
                    "aaa",
                    "bbb"
                  ]
                }
              ]
          },
          "lb": {
              "enabled": true,
              "aggregatev4": 24,
              "aggregatev6": 100
          },
          "ext": {}
        }
      },
      "wipe": {}
    }
  }
]
```

Notes:
- peer:af supported values v4, v6, vpn, defaults to v4
- peer:multihop default value 1
- peer:port default value 179
- peer:secret is the name reference to secret with password in `cilium` namespace, default  null
- peer:graceful default disabled
- peer:timer defauls keepalive 30, hold 90, retry 120
- advertise section options pod, cluster, lb, ext and egw
- if advertise section not defined, it is disabled by default
- all advertise section besides pod can have community, selector and aggregate options while pod can have community only
- if selector is not defined then by default dummy selector is defined that should select all services (see below for example)
- `wipe` ignored and used in [delete task workflow](./delete_task.md)

## Requirements

None

## Configurable options

```
# iserver set ocp task 
  --cluster TEXT   Cluster Name
  --filename TEXT  Tasks filename
  --validate       Validate only
  --break          Break on error
  --no-confirm     Confirmation mode
```

## Expected Outcome

```
# iserver get ocp cilium bgp --cluster bm1

+----+-------+----------+-------+-----------+-------------+----------+-------------+-----------+------+------+---------+-----+-----+
| ID | Node  | Instance | ASN   | Peer name | Peer IP     | Peer ASN | State       | Keepalive | Hold | AFI  | SAFI    | Adv | Rcv |
+----+-------+----------+-------+-----------+-------------+----------+-------------+-----------+------+------+---------+-----+-----+
| 1  | bm1-1 | bgp      | 64661 | tor1      | 10.10.10.20 | 64001    | established | 3         | 9    | ipv4 | unicast | 2   | 0   |
| 2  | bm1-1 | bgp      | 64661 | tor2      | 10.10.10.21 | 64001    | established | 3         | 9    | ipv4 | unicast | 2   | 0   |
| 3  | bm1-2 | bgp      | 64661 | tor1      | 10.10.10.20 | 64001    | established | 3         | 9    | ipv4 | unicast | 2   | 0   | 
| 4  | bm1-2 | bgp      | 64661 | tor2      | 10.10.10.21 | 64001    | established | 3         | 9    | ipv4 | unicast | 2   | 0   |
| 5  | bm1-3 | bgp      | 64661 | tor1      | 10.10.10.20 | 64001    | established | 3         | 9    | ipv4 | unicast | 2   | 0   |
| 6  | bm1-3 | bgp      | 64661 | tor2      | 10.10.10.21 | 64001    | established | 3         | 9    | ipv4 | unicast | 2   | 0   |
+----+-------+----------+-------+-----------+-------------+----------+-------------+-----------+------+------+---------+-----+-----+
```

```
# iserver get ocp cilium bgp --cluster bm1 -v cli

OpenShift Workflow - Cilium BGP Control Plane - Get
===================================================

OpenShift Cluster: bm1

~~~
# cilium bgp peers -n cilium
Node    Local AS   Peer AS   Peer Address   Session State   Uptime   Family         Received   Advertised
bm1-1   64661      64001     10.10.10.20    established     1m1s     ipv4/unicast   0          2
        64661      64001     10.10.10.21    established     1m1s     ipv4/unicast   0          2
bm1-2   64661      64001     10.10.10.20    established     1m2s     ipv4/unicast   0          2
        64661      64001     10.10.10.21    established     1m2s     ipv4/unicast   0          2
bm1-3   64661      64001     10.10.10.20    established     1m1s     ipv4/unicast   0          2
        64661      64001     10.10.10.21    established     1m1s     ipv4/unicast   0          2

~~~

~~~
# cilium bgp routes advertised ipv4 unicast -n cilium
Node    VRouter   Peer          Prefix          NextHop       Age    Attrs
bm1-1   64661     10.10.10.20   10.128.2.0/23   10.10.10.10   1m3s   [{Origin: i} {AsPath: 64661} {Nexthop: 10.10.10.10} {Communities: 64661:100, blackhole}]
        64661     10.10.10.21   10.128.2.0/23   10.10.10.10   1m3s   [{Origin: i} {AsPath: 64661} {Nexthop: 10.10.10.10} {Communities: 64661:100, blackhole}]
bm1-2   64661     10.10.10.20   10.128.4.0/23   10.10.10.11   1m3s   [{Origin: i} {AsPath: 64661} {Nexthop: 10.10.10.11} {Communities: 64661:100, blackhole}]
        64661     10.10.10.21   10.128.4.0/23   10.10.10.11   1m3s   [{Origin: i} {AsPath: 64661} {Nexthop: 10.10.10.11} {Communities: 64661:100, blackhole}]
bm1-3   64661     10.10.10.20   10.128.0.0/23   10.10.10.12   1m3s   [{Origin: i} {AsPath: 64661} {Nexthop: 10.10.10.12} {Communities: 64661:100, blackhole}]
        64661     10.10.10.21   10.128.0.0/23   10.10.10.12   1m3s   [{Origin: i} {AsPath: 64661} {Nexthop: 10.10.10.12} {Communities: 64661:100, blackhole}]

~~~

~~~
# cilium bgp routes advertised ipv4 mpls_vpn -n cilium
Node   VRouter   Peer   Prefix   NextHop   Age   Attrs

~~~

~~~
# cilium bgp routes advertised ipv6 unicast -n cilium
Node   VRouter   Peer   Prefix   NextHop   Age   Attrs

~~~
```

## CRDs

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
  ebgpMultihop: 5
  families:
  - advertisements:
      matchLabels:
        advertise: bgp
    afi: ipv4
    safi: unicast
  gracefulRestart:
    enabled: true
    restartTimeSeconds: 120
  timers:
    connectRetryTimeSeconds: 5
    holdTimeSeconds: 9
    keepAliveTimeSeconds: 3
  transport:
    peerPort: 179
---
apiVersion: isovalent.com/v1
kind: IsovalentBGPAdvertisement
metadata:
  labels:
    advertise: bgp
  name: advertise-cluster
spec:
  advertisements:
  - advertisementType: Service
    selector:
      matchExpressions:
      - key: bgp
        operator: In
        values:
        - aaa
        - bbb
    service:
      addresses:
      - ClusterIP
---
apiVersion: isovalent.com/v1
kind: IsovalentBGPAdvertisement
metadata:
  labels:
    advertise: bgp
  name: advertise-ext
spec:
  advertisements:
  - advertisementType: Service
    selector:
      matchExpressions:
      - key: dummy
        operator: NotIn
        values:
        - dummy
    service:
      addresses:
      - ExternalIP
---
apiVersion: isovalent.com/v1
kind: IsovalentBGPAdvertisement
metadata:
  labels:
    advertise: bgp
  name: advertise-lb
spec:
  advertisements:
  - advertisementType: Service
    selector:
      matchExpressions:
      - key: dummy
        operator: NotIn
        values:
        - dummy
    service:
      addresses:
      - LoadBalancerIP
      aggregationLengthIPv4: 24
      aggregationLengthIPv6: 100
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
        - 64661:100
        wellKnown:
        - blackhole
```

[[Back]](./README.md)