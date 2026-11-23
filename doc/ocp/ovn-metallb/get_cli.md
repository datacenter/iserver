# MetalLB - Get FRR CLI access command

[[Back]](./README.md) [[State]](./get_state.md) [[Cli]](./get_cli.md) [[CRD]](./get_crd.md) [[Exec]](./get_exec.md) [[FRR]](./get_frr.md)

```
# iserver get ocp metallb --cluster bm1 -v cli

OpenShift Workflow - OVNKubernetes - Get metallb information
============================================================

OpenShift Cluster: bm1

+----+-------+------------------------------+-------+-------------------------------------------------------------+
| ID | Host  | Pod                          | Ready | FRR cli                                                     |
+----+-------+------------------------------+-------+-------------------------------------------------------------+
| 1  | bm1-1 | metallb-system/speaker-wlgdt | 6/6   | oc exec -it -n metallb-system speaker-wlgdt -c frr -- vtysh |
| 2  | bm1-2 | metallb-system/speaker-d4lr8 | 6/6   | oc exec -it -n metallb-system speaker-d4lr8 -c frr -- vtysh |
| 3  | bm1-3 | metallb-system/speaker-g8lz6 | 6/6   | oc exec -it -n metallb-system speaker-g8lz6 -c frr -- vtysh |
+----+-------+------------------------------+-------+-------------------------------------------------------------+
```

[[Back]](./README.md) [[State]](./get_state.md) [[Cli]](./get_cli.md) [[CRD]](./get_crd.md) [[Exec]](./get_exec.md) [[FRR]](./get_frr.md)