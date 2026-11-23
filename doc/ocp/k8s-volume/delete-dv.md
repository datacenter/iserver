# Data Volume - Delete

## Workflow

- get data volumes selected by namespace, name, unused or all
- skip if data volume has associated pod, cron, virtual machine (unless force)
- delete data volumes one-by-one

## Requirements

None

## Configurable options

```
# iserver delete k8s dv 
  --cluster TEXT    Cluster Name
  --namespace TEXT  Filter by namespace
  --name TEXT       Filter by name
  --force           Force delete even if used
  --unused          Select unused data volumes
  --no-confirm      No confirmation mode
```

## Example

```
# iserver delete k8s dv --cluster bm1 --namespace default --name test --force

OpenShift Workflow - Data Volume - Delete
=========================================

OpenShift Cluster: bm1

+----+-------------+-------+-------+-------------+----------+------+------------------------------------------------------------------+------+
| ID | Data Volume | Bound | Ready | Phase       | Progress | Size | Usage                                                            | Age  |
+----+-------------+-------+-------+-------------+----------+------+------------------------------------------------------------------+------+
| 1  | default     | X     | X     | UploadReady | N/A      | 1Gi  | [pvc] test                                                       | 1h6m |
|    | test        |       |       |             |          |      | [pvc] default/prime-d1260ab3-8921-47de-84ed-2426bdaf41ed         |      |
|    |             |       |       |             |          |      | [pod] cdi-upload-prime-d1260ab3-8921-47de-84ed-2426bdaf41ed      |      |
|    |             |       |       |             |          |      | [pvc] default/prime-d1260ab3-8921-47de-84ed-2426bdaf41ed-scratch |      |
+----+-------------+-------+-------+-------------+----------+------+------------------------------------------------------------------+------+
Continue [Y/N]? y

Delete Data Volume
------------------
- namespace: default
- name: test
- used: True (force)
- wait for no data volume
- wait for no pvc
```

[[Back]](./README.md)