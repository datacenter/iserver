# Local Storage - Delete volumes created in discovery-all mode

[[Back]](./README.md) [[discovery-all]](./delete_volume_all.md) [[nodes]](./delete_volume_nodes.md) [[explicit]](./delete_volume_explicit.md)

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

[[Back]](./README.md) [[discovery-all]](./delete_volume_all.md) [[nodes]](./delete_volume_nodes.md) [[explicit]](./delete_volume_explicit.md)