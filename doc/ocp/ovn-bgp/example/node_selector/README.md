# OVNKubernetes BGP - Node selector

[[Back]](../../README.md)

## Frr Configuration

```
apiVersion: frrk8s.metallb.io/v1beta1
kind: FRRConfiguration
metadata:
  name: another-session
  namespace: openshift-frr-k8s
  labels:
    fabric: nxos
spec:
  bgp:
    routers:
    - asn: 64667
      neighbors:
      - address: 8.8.8.8
        asn: 64668
  nodeSelector:
    matchLabels:
      kubernetes.io/hostname: bm1-1
```

## Outcome

```
# iserver get ocp ovn-bgp --cluster bm1 -v session

OpenShift Workflow - OVNKubernetes - Get frr-k8s information
============================================================

OpenShift Cluster: bm1

+----+-------+---------------+---------+-------------+-----+
| ID | Node  | Pod           | Peer    | Status      | BFD |
+----+-------+---------------+---------+-------------+-----+
| 1  | bm1-1 | frr-k8s-c4jk4 | 8.8.8.8 | Active      | N/A |
| 2  | bm1-1 | frr-k8s-c4jk4 | 6.6.6.6 | Established | N/A |
| 3  | bm1-1 | frr-k8s-c4jk4 | 6.6.6.7 | Established | N/A |
| 4  | bm1-2 | frr-k8s-9ckzb | 6.6.6.7 | Established | N/A |
| 5  | bm1-2 | frr-k8s-9ckzb | 6.6.6.6 | Established | N/A |
| 6  | bm1-3 | frr-k8s-zpxj6 | 6.6.6.7 | Established | N/A |
| 7  | bm1-3 | frr-k8s-zpxj6 | 6.6.6.6 | Established | N/A |
+----+-------+---------------+---------+-------------+-----+
```

[[Back]](../../README.md)