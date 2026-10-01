# Private Network - local access connectivity test

[[Back]](./README.md) [[Next]](./tor.md)

![Overview](../../images/pnet/la.png)

Kubernetes nodes use dedicated local network devices (VLAN or physical interfaces) for private network traffic
- identify non-kube interfaces and how they are connected to upstream infra
- configure device in Cilium config
- define `PrivateNetworkNodeAttachment` to attach `ClusterwidePrivateNetwork` to network interface(s)

## Step #1 - identify device

Notes:
- local-access can be limited to selected nodes in Kubernetes cluster
- physical interface name **must** be the same
- the interface **cannot** be used as primary Kuberentes interface

You could use [nmstate](../../nmstate/README.md) feature to ease interface discovery incl. neighboring devices

```
# iserver get k8s nns -v lldp --name bm3-1
Cluster: bm3 (type: ocp)
|
+----+-------+------------+-------------------+-------+------+-------------------+---------------+
| ID | Node  | Ethernet   | MAC               | State | LLDP | Nei System        | Nei Interface |
+----+-------+------------+-------------------+-------+------+-------------------+---------------+
| 1  | bm3-1 | eno1       | AA:AA:AA:AA:AA:01 | X     | X    |                   |               |
| 2  | bm3-1 | eno2       | AA:AA:AA:AA:AA:02 | X     | X    |                   |               |
| 3  | bm3-1 | eno5       | AA:AA:AA:AA:AA:03 | V     | V    | leaf-a.domain.com | Ethernet1/15  |
| 4  | bm3-1 | eno6       | AA:AA:AA:AA:AA:04 | V     | V    | leaf-b.domain.com | Ethernet1/15  |
| 5  | bm3-1 | eno7       | AA:AA:AA:AA:AA:05 | V     | V    | leaf-c.domain.com | Eth1/2/1      |
| 6  | bm3-1 | eno8       | AA:AA:AA:AA:AA:06 | V     | V    | leaf-d.domain.com | Eth1/2/1      |
| 7  | bm3-1 | enp216s0f0 | AA:AA:AA:AA:AA:07 | V     | V    |                   |               |
| 8  | bm3-1 | enp216s0f1 | AA:AA:AA:AA:AA:08 | V     | V    |                   |               |
| 9  | bm3-1 | ens1f0     | AA:AA:AA:AA:AA:09 | V     | V    |                   |               |
| 10 | bm3-1 | ens1f1     | AA:AA:AA:AA:AA:0A | V     | V    |                   |               |
+----+-------+------------+-------------------+-------+------+-------------------+---------------+
```

Choice of attachment interface: eno5

## Step #2 - CiliumConfig device

The attachment interface must be selected by Cilium e.g.,

```
```

## Step #3 - PrivateNetworkNodeAttachment

[[Back]](./README.md) [[Next]](./tor.md)