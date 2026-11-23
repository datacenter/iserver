# Cilium BGP Control Plane - Get state

## Workflow

- check cilium cni
- check bgp control plane enabled
- get `IsovalentBGPNodeConfig` CRD

## Requirements

None

## Configurable options

```
# iserver get ocp cilium bgp -v state
  --cluster TEXT     Cluster Name
```

## Example

```
# iserver get ocp cilium bgp --cluster bm1 -v state

OpenShift Workflow - Cilium BGP Control Plane - Get
===================================================

OpenShift Cluster: bm1
Cilium cni found
BGP control plane enabled

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

[[Back]](./README.md)