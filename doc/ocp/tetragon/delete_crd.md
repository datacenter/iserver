# Tetragon - Delete Policy

## Workflow

- delete tetragon crds from user-provided locations
- multiple locations can be defined, each can be filename or directory

## Requirements

- Tetragon Enterprise operator must be installed
- directory is expected to have files (no subdirectories)
- files or files in directory must be yaml with Tetragon CRD

## Configurable options

```
# iserver delete ocp tetragon --mode crd
  --cluster TEXT            Cluster Name
  --crd TEXT                Tetragon policy directory or file
```

## Example

```
# iserver delete ocp tetragon --cluster bm1 --mode crd --filename C:\tmp\policy

OpenShift Workflow - Tetragon - Delete Policy
=============================================

OpenShift Cluster: bm1
File: .\tasks\tetragon\policy\policy.yaml

Delete TracingPolicy
--------------------
- name: upper-layers
- deleted
- wait for no TracingPolicy upper-layers [timeout:60s]

Completed tasks
- CRDs deleted

+----+---------+----------+------------+---------+---------+--------------+
| ID | Target  | Scope    | Workflow   | Changes | Success | Duration [s] |
+----+---------+----------+------------+---------+---------+--------------+
| 1  | ocp:bm1 | tetragon | delete crd | 1       | V       | 2            | 
+----+---------+----------+------------+---------+---------+--------------+
```

[[Back]](./README.md)