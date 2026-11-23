# Cilium

Delete cilium cli on the cluster [management node](../ManagementServer.md)

## Workflow

- remove /usr/local/bin/cilium binary if exists

## Requirements

Cluster [connector](../Access.md) must be defined with management ip
Ssh access to management node must work

## Configurable options

```
# iserver delete ocp cli-cilium 
  --cluster TEXT  OCP cluster name
```

## Example

```
# iserver delete ocp cli-cilium --cluster bm1

OpenShift Workflow - CLI - Delete cilium
========================================

OpenShift Cluster: bm1
Delete file: /usr/local/bin/cilium
Ssh cmd: sudo rm -f /usr/local/bin/cilium

Completed tasks
- cilium deleted

+----+---------+-------+---------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow      | Changes | Success | Duration [s] |
+----+---------+-------+---------------+---------+---------+--------------+
| 1  | ocp:bm1 | cli   | delete cilium | 0       | V       | 3            | 
+----+---------+-------+---------------+---------+---------+--------------+
```

[[Back]](./README.md)