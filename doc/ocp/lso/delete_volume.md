# Local Storage Operator - Delete volume

## Workflow

- delete local volume, local volume set and local volume discovery resources
- unlabel storage nodes

## Requirements

None

## Configurable options

```
# iserver delete ocp lso --mode volume
  --cluster TEXT                  Cluster Name
```

## Example (volumes created in discovery-all mode)

```
# iserver delete ocp lso --cluster bm1 --mode volume


OpenShift Workflow - Local Storage Operator - Delete Local Volume
=================================================================

OpenShift Cluster: bm1

Local Storage Operator Subscription
-----------------------------------
- subscription: openshift-local-storage/local-storage-operator
- package: local-storage-operator
- csv: local-storage-operator.v4.18.0-202602132343

Local Storage Operator Resources
--------------------------------
- deployment openshift-local-storage/local-storage-operator ready

Collect cluster state and validate input values
-----------------------------------------------
- get kubernetes node names
- get local volume discovery
- get local volume sets
- get local volumes

Delete local volumes
--------------------
No local volumes found

Delete local volume sets
------------------------

+----+-------------------------+---------------+-------------+-----------+------------+-----------+
| ID | Local Volume Set        | Storage Class | Volume Mode | Available | Disk Maker | # Devices |
+----+-------------------------+---------------+-------------+-----------+------------+-----------+
| 1  | openshift-local-storage | local-sc      | Block       | V         | V          | 6         | 
|    | my-local-disks          |               |             |           |            |           | 
+----+-------------------------+---------------+-------------+-----------+------------+-----------+
- openshift-local-storage/my-local-disks
	REST API successful
	Wait for no local volume set [timeout:60]...

Delete local volume discovieries
--------------------------------

+----+-------------------------+-----------+-------------+
| ID | Local Volume Discovery  | Available | Phase       |
+----+-------------------------+-----------+-------------+
| 1  | openshift-local-storage | V         | Discovering | 
|    | auto-discover-devices   |           |             | 
+----+-------------------------+-----------+-------------+
- openshift-local-storage/auto-discover-devices
	REST API successful
	Wait for no local volume discovery [timeout:60]...

Unlabel Storage Nodes
---------------------
- node label: cluster.ocs.openshift.io/openshift-storage=""
- node: bm1-1
- node: bm1-2
- node: bm1-3

Completed tasks
- Volumes deleted
- Node labels removed
```

## Example (volumes created in discovery-node mode)

```
# iserver delete ocp lso --cluster bm1 --mode volume

OpenShift Workflow - Local Storage Operator - Delete Local Volume
=================================================================

OpenShift Cluster: bm1

Local Storage Operator Subscription
-----------------------------------
- subscription: openshift-local-storage/local-storage-operator
- package: local-storage-operator
- csv: local-storage-operator.v4.18.0-202602132343

Local Storage Operator Resources
--------------------------------
- deployment openshift-local-storage/local-storage-operator ready

Collect cluster state and validate input values
-----------------------------------------------
- get kubernetes node names
- get local volume discovery
- get local volume sets
- get local volumes

Delete local volumes
--------------------
No local volumes found

Delete local volume sets
------------------------

+----+-------------------------+---------------+-------------+-----------+------------+-----------+
| ID | Local Volume Set        | Storage Class | Volume Mode | Available | Disk Maker | # Devices |
+----+-------------------------+---------------+-------------+-----------+------------+-----------+
| 1  | openshift-local-storage | local-sc      | Block       | V         | V          | 4         | 
|    | my-local-disks          |               |             |           |            |           | 
+----+-------------------------+---------------+-------------+-----------+------------+-----------+
- openshift-local-storage/my-local-disks
	REST API successful
	Wait for no local volume set [timeout:60]...

Delete local volume discovieries
--------------------------------

+----+-------------------------+-----------+-------------+
| ID | Local Volume Discovery  | Available | Phase       |
+----+-------------------------+-----------+-------------+
| 1  | openshift-local-storage | V         | Discovering | 
|    | auto-discover-devices   |           |             | 
+----+-------------------------+-----------+-------------+
- openshift-local-storage/auto-discover-devices
	REST API successful
	Wait for no local volume discovery [timeout:60]...

Unlabel Storage Nodes
---------------------
- node label: cluster.ocs.openshift.io/openshift-storage=""
- node: bm1-1
- node: bm1-2
- node: bm1-3

Completed tasks
- Volumes deleted
- Node labels removed
```

## Example (volumes created in explicit mode)

```
# iserver delete ocp lso --cluster bm1 --mode volume

OpenShift Workflow - Local Storage Operator - Delete Local Volume
=================================================================

OpenShift Cluster: bm1

Local Storage Operator Subscription
-----------------------------------
- subscription: openshift-local-storage/local-storage-operator
- package: local-storage-operator
- csv: local-storage-operator.v4.18.0-202602132343

Local Storage Operator Resources
--------------------------------
- deployment openshift-local-storage/local-storage-operator ready

Collect cluster state and validate input values
-----------------------------------------------
- get kubernetes node names
- get local volume discovery
- get local volume sets
- get local volumes

Delete local volumes
--------------------

+----+--------------------------+-------+------------------------+---------------+-------+
| ID | Local Volume             | Node  | Device                 | Storage Class | Mode  |
+----+--------------------------+-------+------------------------+---------------+-------+
| 1  | openshift-local-storage  | bm1-2 | wwn-0x500a07511c54ae16 | local-sc      | Block | 
|    | local-disks-73bd95395a50 |       |                        |               |       | 
+----+--------------------------+-------+------------------------+---------------+-------+
| 2  | openshift-local-storage  | bm1-1 | wwn-0x55cd2e414e3ba224 | local-sc      | Block | 
|    | local-disks-93e8611f3e62 |       |                        |               |       | 
+----+--------------------------+-------+------------------------+---------------+-------+

Associated Persistent Volumes
-----------------------------


+----+-------------------+-----------+-------+----------+-------+--------+-----+------+
| ID | Persistent Volume | Status    | Mode  | SC       | Size  | Access | PVC | Age  |
+----+-------------------+-----------+-------+----------+-------+--------+-----+------+
| 1  | local-pv-290dd896 | Available | Block | local-sc | 894Gi | RWO    | --  | 1h1m | 
| 2  | local-pv-21e09790 | Available | Block | local-sc | 894Gi | RWO    | --  | 1h1m | 
+----+-------------------+-----------+-------+----------+-------+--------+-----+------+
- openshift-local-storage/local-disks-73bd95395a50
	REST API successful
	Wait for no local volume [timeout:60]...
- openshift-local-storage/local-disks-93e8611f3e62
	REST API successful
	Wait for no local volume [timeout:60]...

Delete local volume sets
------------------------
No local volume set found

Delete local volume discovieries
--------------------------------
No local volume discover found

Unlabel Storage Nodes
---------------------
- node label: cluster.ocs.openshift.io/openshift-storage=""
- node: bm1-1
- node: bm1-2
- node: bm1-3

Completed tasks
- Volumes deleted
- Node labels removed
```

[[Back]](./README.md)