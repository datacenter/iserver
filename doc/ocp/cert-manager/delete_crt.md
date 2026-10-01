# Certificate Manager - Delete certificate

[[Back]](./README.md)

## Workflow

- delete `Certificate` object(s) selected by namespace and name
- delete associated `Secret`

## Requirements

- Certificate manager [installed](./enable.md)

## Configurable options

```
# iserver delete ocp cert-manager --mode crt
  --cluster TEXT           Cluster name
  --namespace TEXT         CRD namespace
  --name TEXT              CRD name
```

## Example

```
# iserver delete ocp cert-manager \
    --cluster bm1 \
    --mode issuer \
    --namespace default


OpenShift Workflow - Certificate Manager - Delete certificate
=============================================================

OpenShift Cluster: bm1

+----+-------------+-----------------------------+--------+-------+
| ID | Certificate | Issuer                      | Secret | Ready |
+----+-------------+-----------------------------+--------+-------+
| 1  | default     | "group": "cert-manager.io", | test   | ✓     | 
|    | test        | "kind": "ClusterIssuer",    |        |       | 
|    |             | "name": "cilium-root-ca"    |        |       | 
+----+-------------+-----------------------------+--------+-------+

Delete Certificate
------------------
- namespace: default
- name: test
- deleted
Wait for no Certificate default/test [timeout:60s]

Delete Secret
-------------
- namespace: default
- name: test
- deleted
Wait for no Secret default/test [timeout:60s]

Completed tasks
- certificate deleted

+----+---------+--------------+------------+---------+---------+--------------+
| ID | Target  | Scope        | Workflow   | Changes | Success | Duration [s] |
+----+---------+--------------+------------+---------+---------+--------------+
| 1  | ocp:bm1 | cert-manager | delete crt | 2       | ✓       | 5            | 
+----+---------+--------------+------------+---------+---------+--------------+
```

[[Back]](./README.md)