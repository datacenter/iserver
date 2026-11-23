# Butane

Delete butane cli on the cluster [management node](../ManagementServer.md)

## Workflow

- remove /usr/local/bin/butane binary if exists

## Requirements

Cluster [connector](../Access.md) must be defined with management ip
Ssh access to management node must work

## Configurable options

```
# iserver delete ocp cli-butane 
  --cluster TEXT  OCP cluster name
```

## Example

```
# iserver delete ocp cli-butane --cluster bm1

OpenShift Workflow - CLI - Delete butane
========================================

OpenShift Cluster: bm1
Delete file: /usr/local/bin/butane

Completed tasks
- butane deleted

+----+---------+-------+---------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow      | Changes | Success | Duration [s] |
+----+---------+-------+---------------+---------+---------+--------------+
| 1  | ocp:bm1 | cli   | delete butane | 0       | V       | 2            | 
+----+---------+-------+---------------+---------+---------+--------------+
```

[[Back]](./README.md)