# Tetragon - Delete tetragon resources

[[Back]](./README.md)

## Workflow

Delete tetragon-related resources
- AlertRule
- SandboxPolicy
- SandboxPolicyNamespaced
- TracingPolicy
- TracingPolicyNamespaced

## Requirements

Tetragon Enterprise operator [installed](./create_operator.md)

## Configurable options

```
# iserver delete ocp tetragon --mode wipe
  --cluster TEXT                  Cluster Name
```

## Example

```
# iserver delete ocp tetragon --cluster bm1 --mode wipe

OpenShift Workflow - Tetragon - Wipe
====================================

OpenShift Cluster: bm1

Delete TracingPolicy
--------------------
- name: upper-layers
- deleted
- wait for no TracingPolicy upper-layers [timeout:60s]

Completed tasks
- Tetragon resources deleted

+----+---------+----------+-------------+---------+---------+--------------+
| ID | Target  | Scope    | Workflow    | Changes | Success | Duration [s] |
+----+---------+----------+-------------+---------+---------+--------------+
| 1  | ocp:bm1 | tetragon | delete wipe | 1       | V       | 1            | 
+----+---------+----------+-------------+---------+---------+--------------+
```

[[Back]](./README.md)