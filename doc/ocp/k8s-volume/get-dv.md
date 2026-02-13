# Data Volume - Get

Data Volume is OpenShift Virtualization extension used to automate the creation of a PVC and the importation of virtual machine images from sources like HTTP, registries or manual (virtctl) uploads.

## Workflow

- get data volumes
- get extra information augmented with dv information
  - persistent volume claim
  - virtual machine

## Configurable options

```
# iserver get k8s dv
  --cluster TEXT                  Cluster name
  --namespace TEXT                Filter by namespace
  --name TEXT                     Filter by name
```

## Example

```
# iserver get k8s dv --cluster bm1
Cluster: bm1 (type: ocp)

+----+-----------------------------+-------+-------+-------------+----------+------+------------------------------------------------------------------+-------+
| ID | Data Volume                 | Bound | Ready | Phase       | Progress | Size | Usage                                                            | Age   |
+----+-----------------------------+-------+-------+-------------+----------+------+------------------------------------------------------------------+-------+
| 1  | default                     | V     | V     | Succeeded   | 100.0%   | 30Gi | [pvc] fedora-apricot-chickadee-80                                | 16d   |
|    | fedora-apricot-chickadee-80 |       |       |             |          |      | [vm] default/fedora-apricot-chickadee-80                         |       |
+----+-----------------------------+-------+-------+-------------+----------+------+------------------------------------------------------------------+-------+
| 2  | default                     | X     | X     | UploadReady | N/A      | 1Gi  | [pvc] test                                                       | 2h36m |
|    | test                        |       |       |             |          |      | [pvc] default/prime-98341667-4e95-42ae-9de5-7525903b6e71         |       |
|    |                             |       |       |             |          |      | [pod] cdi-upload-prime-98341667-4e95-42ae-9de5-7525903b6e71      |       |
|    |                             |       |       |             |          |      | [pvc] default/prime-98341667-4e95-42ae-9de5-7525903b6e71-scratch |       |
+----+-----------------------------+-------+-------+-------------+----------+------+------------------------------------------------------------------+-------+
```

[[Back]](./README.md)