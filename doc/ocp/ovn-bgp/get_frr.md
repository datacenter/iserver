# OVNKubernetes BGP - Get FRR configuration

[[Back]](./README.md)

> [!NOTE]
> FRR configuration is populated by frr configuration [objects](./get_config.md)

```
# iserver get ocp ovn-bgp --cluster bm1 --node bm1-1 -v frr

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

[[Back]](./README.md)