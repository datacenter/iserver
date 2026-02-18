# Example 3-node cluster peering with ACI

## Intent

- enable bgp peering between OpenShift cluster running on bare metal servers and ACI nodes
- bgp should run on every node
- eBGP with multihop (1) for directly connected bgp neighbors
- everything advertised i.e. pod cidr and all possible services

```
+----+-------+-------+-------+--------+------+-----+-----+--------+-------------------+------+
| ID | Node  | Ready | Taint | Memory | Disk | PID | MCP | Role   | IP                | Age  |
+----+-------+-------+-------+--------+------+-----+-----+--------+-------------------+------+
| 1  | bm1-1 | V     | ---   | V      | V    | V   | V   | Master | 10.10.10.10 (int) | 121d |
|    |       |       |       |        |      |     |     | Worker |                   |      | 
+----+-------+-------+-------+--------+------+-----+-----+--------+-------------------+------+
| 2  | bm1-2 | V     | ---   | V      | V    | V   | V   | Master | 10.10.10.11 (int) | 120d |
|    |       |       |       |        |      |     |     | Worker |                   |      |
+----+-------+-------+-------+--------+------+-----+-----+--------+-------------------+------+
| 3  | bm1-3 | V     | ---   | V      | V    | V   | V   | Master | 10.10.10.12 (int) | 121d |
|    |       |       |       |        |      |     |     | Worker |                   |      |
+----+-------+-------+-------+--------+------+-----+-----+--------+-------------------+------+
```

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
          "pod": {},
          "cluster": {},
          "lb": {},
          "ext": {}
        }
      },
      "wipe": {}
    }
  }
]
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
  name: advertise-cluster
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
```

## State

```
+----+-------+----------+-------+-----------+-------------+----------+-------------+-----------+------+------+---------+-----+-----+
| ID | Node  | Instance | ASN   | Peer name | Peer IP     | Peer ASN | State       | Keepalive | Hold | AFI  | SAFI    | Adv | Rcv |
+----+-------+----------+-------+-----------+-------------+----------+-------------+-----------+------+------+---------+-----+-----+
| 1  | bm1-1 | bgp      | 64661 | tor1      | 10.10.10.20 | 64001    | established | 30        | 90   | ipv4 | unicast | 76  | 0   |
| 2  | bm1-1 | bgp      | 64661 | tor2      | 10.10.10.21 | 64001    | established | 30        | 90   | ipv4 | unicast | 76  | 0   |
| 3  | bm1-2 | bgp      | 64661 | tor1      | 10.10.10.20 | 64001    | established | 30        | 90   | ipv4 | unicast | 76  | 0   |
| 4  | bm1-2 | bgp      | 64661 | tor2      | 10.10.10.21 | 64001    | established | 30        | 90   | ipv4 | unicast | 76  | 0   |
| 5  | bm1-3 | bgp      | 64661 | tor1      | 10.10.10.20 | 64001    | established | 30        | 90   | ipv4 | unicast | 76  | 0   |
| 6  | bm1-3 | bgp      | 64661 | tor2      | 10.10.10.21 | 64001    | established | 30        | 90   | ipv4 | unicast | 76  | 0   | 
+----+-------+----------+-------+-----------+-------------+----------+-------------+-----------+------+------+---------+-----+-----+
```

```
# cilium bgp peers -n cilium
Node    Local AS   Peer AS   Peer Address   Session State   Uptime   Family         Received   Advertised
bm1-1   64661      64001     10.10.10.20    established     56s      ipv4/unicast   0          76
        64661      64001     10.10.10.21    established     57s      ipv4/unicast   0          76
bm1-2   64661      64001     10.10.10.20    established     56s      ipv4/unicast   0          76
        64661      64001     10.10.10.21    established     56s      ipv4/unicast   0          76
bm1-3   64661      64001     10.10.10.20    established     57s      ipv4/unicast   0          76
        64661      64001     10.10.10.21    established     57s      ipv4/unicast   0          76
```

[[Back]](./README.md)