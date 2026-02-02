# CDI Data Import Cron - Wipe

## Workflow

- get cnv operator state
- get hyperconverged instance state
- disable cdi data import cron
- wipe all cron associated dv/pvc

## Requirements

- cnv operator installed
- hyperconverged instance created

## Configurable options

```
# iserver delete ocp cnv --mode import --wipe
  --cluster TEXT          Cluster Name
  --no-confirm            Confirmation mode
```

## Example

```
# iserver delete ocp cnv --cluster bm1 --mode import --wipe

OpenShift Workflow - Container Virtualization Operator - Disable Data Import Cron
=================================================================================

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

Data import cron already disabled

+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| ID | Data Volume                        | POD | Bound | Ready | Access Mode | Storage | Cron | PVC                          | Phase     | Progress | Age |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| 1  | openshift-virtualization-os-images | ✗   | ✓     | ✓     | ---         | ---     | ✓    | centos-stream10-e87658ffc71c | Succeeded | 100.0%   | 5d  |
|    | centos-stream10-e87658ffc71c       |     |       |       |             |         |      |                              |           |          |     |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| 2  | openshift-virtualization-os-images | ✗   | ✓     | ✓     | ---         | ---     | ✓    | centos-stream9-9e58d88d8e30  | Succeeded | 100.0%   | 5d  |
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
Continue [Y/N]? y

Delete Data Volume
------------------
- namespace: openshift-virtualization-os-images
- name: centos-stream10-e87658ffc71c
- wait for no data volume

Delete Data Volume
------------------
- namespace: openshift-virtualization-os-images
- name: centos-stream9-9e58d88d8e30
- wait for no data volume

Delete Data Volume
------------------
- namespace: openshift-virtualization-os-images
- name: centos-stream9-e6457949d4bb
- wait for no data volume

Delete Data Volume
------------------
- namespace: openshift-virtualization-os-images
- name: fedora-b37907f3bbf8
- wait for no data volume

Delete Data Volume
------------------
- namespace: openshift-virtualization-os-images
- name: rhel10-c03936a065f2
- wait for no data volume

Delete Data Volume
------------------
- namespace: openshift-virtualization-os-images
- name: rhel8-4ccd8b6aee47
- wait for no data volume

Delete Data Volume
------------------
- namespace: openshift-virtualization-os-images
- name: rhel9-ab4ec16077fe
- wait for no data volume
```

[[Back]](./README.md)