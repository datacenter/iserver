# Tridentctl

Delete tridentctl cli on the cluster [management node](../ManagementServer.md)

## Workflow

- remove /usr/local/bin/tridentctl binary if exists

## Requirements

Cluster [connector](../Access.md) must be defined with management ip
Ssh access to management node must work

## Configurable options

```
# iserver delete ocp cli-tridentctl 
  --cluster TEXT  OCP cluster name
```

## Example

```
# iserver delete ocp cli-tridentctl --cluster bm1

OpenShift Workflow - CLI - Delete tridentctl
============================================

OpenShift Cluster: bm1
Delete file: /usr/local/bin/tridentctl
Ssh cmd: sudo rm -f /usr/local/bin/tridentctl

Completed tasks
- tridentctl deleted

+----+---------+-------+-------------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow          | Changes | Success | Duration [s] |
+----+---------+-------+-------------------+---------+---------+--------------+
| 1  | ocp:bm1 | cli   | delete tridentctl | 0       | V       | 3            | 
+----+---------+-------+-------------------+---------+---------+--------------+
```

[[Back]](./README.md)