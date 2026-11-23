# Tetragon - Create Policy

## Workflow

- create tetragon crds from user-provided locations
- multiple locations can be defined, each can be filename or directory

## Requirements

- Tetragon Enterprise operator [installed](./create_operator.md)
- directory is expected to have files (no subdirectories)
- files or files in directory must be yaml with Tetragon CRD

## Configurable options

```
# iserver set ocp tetragon --mode crd
  --cluster TEXT         Cluster Name
  --filename TEXT        Tetragon policy directory or file
  --no-confirm           Confirmation mode
```

## Example

```
# iserver set ocp tetragon --cluster bm1 --mode crd --filename C:\tmp\policy

OpenShift Workflow - Tetragon - Create Policy
=============================================

OpenShift Cluster: bm1
File: C:\tmp\policy\policy.yaml

Create TracingPolicy
--------------------
- name: upper-layers

~~~
apiVersion: cilium.io/v1alpha1
kind: TracingPolicy
metadata:
  name: upper-layers
spec:
  parser:
    burstExitGen:
      enable: true
      interval: 1000
    dns:
      enable: true
    http:
      enable: true
      http2: true
      selectors:
      - matchPorts:
        - 8080
        - 80
    icmp:
      enable: true
    interface:
      enable: true
      packet: true
    tcp:
      enable: true
      histogram:
        enable: true
        max: 50000
        min: 0
      statsInterval: 20
    udp:
      cgroup: true
      enable: true
      statsInterval: 20
~~~
TracingPolicy [upper-layers] created
- wait for TracingPolicy upper-layers [timeout:60s]

Completed tasks
- CRDs applied

+----+---------+----------+------------+---------+---------+--------------+
| ID | Target  | Scope    | Workflow   | Changes | Success | Duration [s] |
+----+---------+----------+------------+---------+---------+--------------+
| 1  | ocp:bm1 | tetragon | create crd | 1       | V       | 3            | 
+----+---------+----------+------------+---------+---------+--------------+
```

[[Back]](./README.md)