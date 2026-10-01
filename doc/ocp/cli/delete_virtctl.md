# Virtctl

Delete virtctl cli on the cluster [management node](../ManagementServer.md)

## Workflow

- remove /usr/local/bin/virtctl binary if exists

## Requirements

Cluster [connector](../Access.md) must be defined with management ip
Ssh access to management node must work

## Configurable options

```
# iserver delete ocp cli-virtctl 
  --cluster TEXT  OCP cluster name
```

## Example

```
# iserver delete ocp cli-virtctl --cluster bm1

OpenShift Workflow - CLI - Delete virtctl
=========================================

OpenShift Cluster: bm1
Delete file: /usr/local/bin/virtctl
Ssh cmd: sudo rm -f /usr/local/bin/virtctl

Completed tasks
- virtctl deleted

+----+---------+-------+----------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow       | Changes | Success | Duration [s] |
+----+---------+-------+----------------+---------+---------+--------------+
| 1  | ocp:bm1 | cli   | delete virtctl | 0       | V       | 3            | 
+----+---------+-------+----------------+---------+---------+--------------+
```

[[Back]](./README.md)