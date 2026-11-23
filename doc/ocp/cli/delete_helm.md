# Helm

Delete helm cli on the cluster [management node](../ManagementServer.md)

## Workflow

- remove /usr/local/bin/helm binary if exists

## Requirements

Cluster [connector](../Access.md) must be defined with management ip
Ssh access to management node must work

## Configurable options

```
# iserver delete ocp cli-helm 
  --cluster TEXT  OCP cluster name
```

## Example

```
# iserver delete ocp cli-helm --cluster bm1

OpenShift Workflow - CLI - Delete helm
======================================

OpenShift Cluster: bm1
Delete file: /usr/local/bin/helm
Ssh cmd: sudo rm -f /usr/local/bin/helm

Completed tasks
- helm deleted

+----+---------+-------+-------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow    | Changes | Success | Duration [s] |
+----+---------+-------+-------------+---------+---------+--------------+
| 1  | ocp:bm1 | cli   | delete helm | 0       | V       | 3            | 
+----+---------+-------+-------------+---------+---------+--------------+
```

[[Back]](./README.md)