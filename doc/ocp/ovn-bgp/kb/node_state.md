# OVNKubernetes BGP - Node State

[[Back]](../README.md)

`FRRNodeState` CRD shows the status of FRR-k8s daemon running inside the pod incl. configuration that is indirectly controlled with [FRRConfiguration](./configuration.md) CRD.

> [!NOTE]
> FRRNodeState CRD is added to the cluster once BGP is [enabled](./enable.md)

## CLI

FRR-k8s daemon state is exposed per node

```
$ oc get frrnodestate
NAME    AGE
bm1-1   13h
bm1-2   13h
bm1-3   13h
```

```
# oc get frrnodestate bm1-1 -o yaml
apiVersion: frrk8s.metallb.io/v1beta1
kind: FRRNodeState
metadata:
  name: bm1-1
spec: {}
status:
  lastConversionResult: success
  lastReloadResult: success
  runningConfig: |
    Building configuration...

    Current configuration:
    !
    frr version 8.5.3
    frr defaults traditional
    hostname bm1-1
    log file /etc/frr/frr.log informational
    log timestamp precision 3
    no ipv6 forwarding
    service integrated-vtysh-config
    !
    ip nht resolve-via-default
    !
    ipv6 nht resolve-via-default
    !
    end
```

## iserver

```
# iserver get ocp ovn-bgp -v config --node bm1-1

OpenShift Workflow - OVNKubernetes - Get frr-k8s information
============================================================

OpenShift Cluster: bm1

+----+-------+------------+--------+-----------------------------------------+
| ID | Node  | Conversion | Reload | Config                                  |
+----+-------+------------+--------+-----------------------------------------+
| 1  | bm1-1 | V          | V      | Building configuration...               |
|    |       |            |        |                                         |
|    |       |            |        | Current configuration:                  |
|    |       |            |        | !                                       |
|    |       |            |        | frr version 8.5.3                       |
|    |       |            |        | frr defaults traditional                |
|    |       |            |        | hostname bm1-1                          |
|    |       |            |        | log file /etc/frr/frr.log informational |
|    |       |            |        | log timestamp precision 3               |
|    |       |            |        | no ip forwarding                        |
|    |       |            |        | no ipv6 forwarding                      |
|    |       |            |        | service integrated-vtysh-config         |
|    |       |            |        | !                                       |
|    |       |            |        | ip nht resolve-via-default              |
|    |       |            |        | !                                       |
|    |       |            |        | ipv6 nht resolve-via-default            |
|    |       |            |        | !                                       |
|    |       |            |        | end                                     |
|    |       |            |        |                                         |
+----+-------+------------+--------+-----------------------------------------+
```

[[Back]](../README.md)