# CDI Data Import Cron - Get State

## Workflow

- get cnv operator state
- get hyperconverged instance state
- collect data sources 
- collect data volumes (cron related)
- collect pvcs (cron related)

## Example (data import cron enabled)

```
# iserver get ocp cnv --cluster bm1 --view import

OpenShift Workflow - Container Virtualization Operator - Get Data Import Cron
=============================================================================

OpenShift Cluster: bm1

Operator
--------
- subscription: openshift-cnv/kubevirt-hyperconverged
- channel: stable
- csv: kubevirt-hyperconverged-operator.v4.18.23

HyperConverged
--------------
- instance: kubevirt-hyperconverged
- data import cron: enabled

+----+-----------------+-----------------+-------+------------------------------+-----------+-----------+
| ID | Data Source     | Import Schedule | Ready | DV / PVC                     | DV Phase  | PVC Phase |
+----+-----------------+-----------------+-------+------------------------------+-----------+-----------+
| 1  | centos-stream10 | 4 7/12 * * *    | ✓     | centos-stream10-e87658ffc71c | Succeeded | Bound     |
| 2  | centos-stream9  | 4 7/12 * * *    | ✓     | centos-stream9-e6457949d4bb  | Succeeded | Bound     |
| 3  | fedora          | 4 7/12 * * *    | ✓     | fedora-b37907f3bbf8          | Succeeded | Bound     |
| 4  | rhel10          | 4 7/12 * * *    | ✓     | rhel10-c03936a065f2          | Succeeded | Bound     |
| 5  | rhel7           | ---             | ✗     | rhel7                        | Not found | Not found |
| 6  | rhel8           | 4 7/12 * * *    | ✓     | rhel8-4ccd8b6aee47           | Succeeded | Bound     |
| 7  | rhel9           | 4 7/12 * * *    | ✓     | rhel9-ab4ec16077fe           | Succeeded | Bound     |
| 8  | win10           | ---             | ✗     | win10                        | Not found | Not found |
| 9  | win11           | ---             | ✗     | win11                        | Not found | Not found |
| 10 | win2k16         | ---             | ✗     | win2k16                      | Not found | Not found |
| 11 | win2k19         | ---             | ✗     | win2k19                      | Not found | Not found |
| 12 | win2k22         | ---             | ✗     | win2k22                      | Not found | Not found |
| 13 | win2k25         | ---             | ✗     | win2k25                      | Not found | Not found |
+----+-----------------+-----------------+-------+------------------------------+-----------+-----------+

+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| ID | Data Volume                        | POD | Bound | Ready | Access Mode | Storage | Cron | PVC                          | Phase     | Progress | Age |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| 1  | openshift-virtualization-os-images | ✗   | ✓     | ✓     | ---         | ---     | ✓    | centos-stream10-e87658ffc71c | Succeeded | 100.0%   | 4d  |
|    | centos-stream10-e87658ffc71c       |     |       |       |             |         |      |                              |           |          |     |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| 2  | openshift-virtualization-os-images | ✗   | ✓     | ✓     | ---         | ---     | ✓    | centos-stream9-9e58d88d8e30  | Succeeded | 100.0%   | 4d  |
|    | centos-stream9-9e58d88d8e30        |     |       |       |             |         |      |                              |           |          |     |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| 3  | openshift-virtualization-os-images | ✗   | ✓     | ✓     | ---         | ---     | ✓    | centos-stream9-e6457949d4bb  | Succeeded | 100.0%   | 4d  |
|    | centos-stream9-e6457949d4bb        |     |       |       |             |         |      |                              |           |          |     |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| 4  | openshift-virtualization-os-images | ✗   | ✓     | ✓     | ---         | ---     | ✓    | fedora-b37907f3bbf8          | Succeeded | 100.0%   | 24d | 
|    | fedora-b37907f3bbf8                |     |       |       |             |         |      |                              |           |          |     |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| 5  | openshift-virtualization-os-images | ✗   | ✓     | ✓     | ---         | ---     | ✓    | rhel10-c03936a065f2          | Succeeded | 100.0%   | 24d |
|    | rhel10-c03936a065f2                |     |       |       |             |         |      |                              |           |          |     |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| 6  | openshift-virtualization-os-images | ✗   | ✓     | ✓     | ---         | ---     | ✓    | rhel8-4ccd8b6aee47           | Succeeded | 100.0%   | 24d |
|    | rhel8-4ccd8b6aee47                 |     |       |       |             |         |      |                              |           |          |     |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| 7  | openshift-virtualization-os-images | ✗   | ✓     | ✓     | ---         | ---     | ✓    | rhel9-ab4ec16077fe           | Succeeded | 100.0%   | 24d | 
|    | rhel9-ab4ec16077fe                 |     |       |       |             |         |      |                              |           |          |     |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+

+----+------------------------------------+--------+------+------------------------------------------+-------+------+---------------+---------------+-----+
| ID | PVC                                | Status | Cron | PV                                       | Mode  | Size | Access Mode   | Storage Class | Age |
+----+------------------------------------+--------+------+------------------------------------------+-------+------+---------------+---------------+-----+
| 1  | openshift-virtualization-os-images | Bound  | ✓    | pvc-21431568-44c4-4349-82c5-aca9f59d54b6 | Block | 30Gi | ReadWriteOnce | lvms-vg1      | 4d  |
|    | centos-stream10-e87658ffc71c       |        |      |                                          |       |      |               |               |     |
+----+------------------------------------+--------+------+------------------------------------------+-------+------+---------------+---------------+-----+
| 2  | openshift-virtualization-os-images | Bound  | ✓    | pvc-7447c4b4-f1ea-4e90-93b2-d10f697cf7c0 | Block | 30Gi | ReadWriteOnce | lvms-vg1      | 4d  |
|    | centos-stream9-9e58d88d8e30        |        |      |                                          |       |      |               |               |     |
+----+------------------------------------+--------+------+------------------------------------------+-------+------+---------------+---------------+-----+
| 3  | openshift-virtualization-os-images | Bound  | ✓    | pvc-2afe4bab-3fff-456d-8e22-2141d7e9de84 | Block | 30Gi | ReadWriteOnce | lvms-vg1      | 4d  |
|    | centos-stream9-e6457949d4bb        |        |      |                                          |       |      |               |               |     |
+----+------------------------------------+--------+------+------------------------------------------+-------+------+---------------+---------------+-----+
| 4  | openshift-virtualization-os-images | Bound  | ✓    | pvc-ae0e8eb9-89f3-479a-83d9-9b822cfbcb2f | Block | 30Gi | ReadWriteOnce | lvms-vg1      | 4d  |
|    | fedora-b37907f3bbf8                |        |      |                                          |       |      |               |               |     |
+----+------------------------------------+--------+------+------------------------------------------+-------+------+---------------+---------------+-----+
| 5  | openshift-virtualization-os-images | Bound  | ✓    | pvc-b896862a-9b74-40b6-b8a6-a0af28e43f57 | Block | 30Gi | ReadWriteOnce | lvms-vg1      | 4d  |
|    | rhel10-c03936a065f2                |        |      |                                          |       |      |               |               |     |
+----+------------------------------------+--------+------+------------------------------------------+-------+------+---------------+---------------+-----+
| 6  | openshift-virtualization-os-images | Bound  | ✓    | pvc-0a98f2bb-20d9-4de1-8546-f47b917d0949 | Block | 30Gi | ReadWriteOnce | lvms-vg1      | 4d  |
|    | rhel8-4ccd8b6aee47                 |        |      |                                          |       |      |               |               |     |
+----+------------------------------------+--------+------+------------------------------------------+-------+------+---------------+---------------+-----+
| 7  | openshift-virtualization-os-images | Bound  | ✓    | pvc-c4e91a28-cd5b-48ad-aaad-43ceed83afc3 | Block | 30Gi | ReadWriteOnce | lvms-vg1      | 4d  |
|    | rhel9-ab4ec16077fe                 |        |      |                                          |       |      |               |               |     |
+----+------------------------------------+--------+------+------------------------------------------+-------+------+---------------+---------------+-----+
```

## Example (data import cron disabled)

```
# iserver get ocp cnv --cluster bm1 -v import

OpenShift Workflow - Container Virtualization Operator - Get Data Import Cron
=============================================================================

OpenShift Cluster: bm1

Operator
--------
- subscription: openshift-cnv/kubevirt-hyperconverged
- channel: stable
- csv: kubevirt-hyperconverged-operator.v4.18.23

HyperConverged
--------------
- instance: kubevirt-hyperconverged
- data import cron: disabled

+----+-----------------+-----------------+-------+------------------------------+-----------+-----------+
| ID | Data Source     | Import Schedule | Ready | DV / PVC                     | DV Phase  | PVC Phase |
+----+-----------------+-----------------+-------+------------------------------+-----------+-----------+
| 1  | centos-stream10 | ---             | ✓     | centos-stream10-e87658ffc71c | Succeeded | Bound     |
| 2  | centos-stream9  | ---             | ✗     | centos-stream9               | Not found | Not found |
| 3  | fedora          | ---             | ✗     | fedora                       | Not found | Not found |
| 4  | rhel10          | ---             | ✓     | rhel10-c03936a065f2          | Succeeded | Bound     |
| 5  | rhel7           | ---             | ✗     | rhel7                        | Not found | Not found |
| 6  | rhel8           | ---             | ✗     | rhel8                        | Not found | Not found |
| 7  | rhel9           | ---             | ✗     | rhel9                        | Not found | Not found |
| 8  | win10           | ---             | ✗     | win10                        | Not found | Not found |
| 9  | win11           | ---             | ✗     | win11                        | Not found | Not found |
| 10 | win2k16         | ---             | ✗     | win2k16                      | Not found | Not found |
| 11 | win2k19         | ---             | ✗     | win2k19                      | Not found | Not found |
| 12 | win2k22         | ---             | ✗     | win2k22                      | Not found | Not found |
| 13 | win2k25         | ---             | ✗     | win2k25                      | Not found | Not found |
+----+-----------------+-----------------+-------+------------------------------+-----------+-----------+

+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| ID | Data Volume                        | POD | Bound | Ready | Access Mode | Storage | Cron | PVC                          | Phase     | Progress | Age |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| 1  | openshift-virtualization-os-images | ✗   | ✓     | ✓     | ---         | ---     | ✓    | centos-stream10-e87658ffc71c | Succeeded | 100.0%   | 4d  | 
|    | centos-stream10-e87658ffc71c       |     |       |       |             |         |      |                              |           |          |     |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| 2  | openshift-virtualization-os-images | ✗   | ✓     | ✓     | ---         | ---     | ✓    | centos-stream9-9e58d88d8e30  | Succeeded | 100.0%   | 4d  |
|    | centos-stream9-9e58d88d8e30        |     |       |       |             |         |      |                              |           |          |     |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| 3  | openshift-virtualization-os-images | ✗   | ✓     | ✓     | ---         | ---     | ✓    | centos-stream9-e6457949d4bb  | Succeeded | 100.0%   | 4d  |
|    | centos-stream9-e6457949d4bb        |     |       |       |             |         |      |                              |           |          |     |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| 4  | openshift-virtualization-os-images | ✗   | ✓     | ✓     | ---         | ---     | ✓    | fedora-b37907f3bbf8          | Succeeded | 100.0%   | 24d |
|    | fedora-b37907f3bbf8                |     |       |       |             |         |      |                              |           |          |     |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| 5  | openshift-virtualization-os-images | ✗   | ✓     | ✓     | ---         | ---     | ✓    | rhel10-c03936a065f2          | Succeeded | 100.0%   | 24d |
|    | rhel10-c03936a065f2                |     |       |       |             |         |      |                              |           |          |     |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| 6  | openshift-virtualization-os-images | ✗   | ✓     | ✓     | ---         | ---     | ✓    | rhel8-4ccd8b6aee47           | Succeeded | 100.0%   | 24d |
|    | rhel8-4ccd8b6aee47                 |     |       |       |             |         |      |                              |           |          |     |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| 7  | openshift-virtualization-os-images | ✗   | ✓     | ✓     | ---         | ---     | ✓    | rhel9-ab4ec16077fe           | Succeeded | 100.0%   | 24d |
|    | rhel9-ab4ec16077fe                 |     |       |       |             |         |      |                              |           |          |     |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+

+----+------------------------------------+--------+------+------------------------------------------+-------+------+---------------+---------------+-----+
| ID | PVC                                | Status | Cron | PV                                       | Mode  | Size | Access Mode   | Storage Class | Age |
+----+------------------------------------+--------+------+------------------------------------------+-------+------+---------------+---------------+-----+
| 1  | openshift-virtualization-os-images | Bound  | ✓    | pvc-21431568-44c4-4349-82c5-aca9f59d54b6 | Block | 30Gi | ReadWriteOnce | lvms-vg1      | 4d  |
|    | centos-stream10-e87658ffc71c       |        |      |                                          |       |      |               |               |     |
+----+------------------------------------+--------+------+------------------------------------------+-------+------+---------------+---------------+-----+
| 2  | openshift-virtualization-os-images | Bound  | ✓    | pvc-7447c4b4-f1ea-4e90-93b2-d10f697cf7c0 | Block | 30Gi | ReadWriteOnce | lvms-vg1      | 4d  |
|    | centos-stream9-9e58d88d8e30        |        |      |                                          |       |      |               |               |     |
+----+------------------------------------+--------+------+------------------------------------------+-------+------+---------------+---------------+-----+
| 3  | openshift-virtualization-os-images | Bound  | ✓    | pvc-2afe4bab-3fff-456d-8e22-2141d7e9de84 | Block | 30Gi | ReadWriteOnce | lvms-vg1      | 4d  |
|    | centos-stream9-e6457949d4bb        |        |      |                                          |       |      |               |               |     |
+----+------------------------------------+--------+------+------------------------------------------+-------+------+---------------+---------------+-----+
| 4  | openshift-virtualization-os-images | Bound  | ✓    | pvc-ae0e8eb9-89f3-479a-83d9-9b822cfbcb2f | Block | 30Gi | ReadWriteOnce | lvms-vg1      | 4d  |
|    | fedora-b37907f3bbf8                |        |      |                                          |       |      |               |               |     |
+----+------------------------------------+--------+------+------------------------------------------+-------+------+---------------+---------------+-----+
| 5  | openshift-virtualization-os-images | Bound  | ✓    | pvc-b896862a-9b74-40b6-b8a6-a0af28e43f57 | Block | 30Gi | ReadWriteOnce | lvms-vg1      | 4d  |
|    | rhel10-c03936a065f2                |        |      |                                          |       |      |               |               |     |
+----+------------------------------------+--------+------+------------------------------------------+-------+------+---------------+---------------+-----+
| 6  | openshift-virtualization-os-images | Bound  | ✓    | pvc-0a98f2bb-20d9-4de1-8546-f47b917d0949 | Block | 30Gi | ReadWriteOnce | lvms-vg1      | 4d  |
|    | rhel8-4ccd8b6aee47                 |        |      |                                          |       |      |               |               |     |
+----+------------------------------------+--------+------+------------------------------------------+-------+------+---------------+---------------+-----+
| 7  | openshift-virtualization-os-images | Bound  | ✓    | pvc-c4e91a28-cd5b-48ad-aaad-43ceed83afc3 | Block | 30Gi | ReadWriteOnce | lvms-vg1      | 4d  |
|    | rhel9-ab4ec16077fe                 |        |      |                                          |       |      |               |               |     |
+----+------------------------------------+--------+------+------------------------------------------+-------+------+---------------+---------------+-----+
```

[[Back]](./README.md)