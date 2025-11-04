# LVM Storage Operator - Test

## Workflow

- check lvm storage operator subscription
- check lvm storage operator resources (deployments and daemon_sets)
- check lvmcluster CRD and its state
- check storage class
- create test namespace controlled with --test-namespace and test-lvm as default value
- create pvc "for every node"
- create pod tainted to each node and mounting one pvc
- pod should be up and pvc should be bound
- create volume snapshot for every pvc
- check resources consistency (pod, pvc, pv, volume snapshot, topolvm logical volume, linux-level logical volume)
- delete all resources (use --keep to override)

## Requirements

- LVM Cluster instance must exist and be ready

## Configurable options

```
# iserver set ocp lvm --mode test
  --cluster TEXT                  Cluster Name
  --test-namespace TEXT           Test namespace  [default: test-lvm]
  --keep                          Keep test resources
  --no-confirm                    Confirmation mode
```

## Example

```
# iserver set ocp lvm --mode test

OpenShift Workflow - LVM Operator - Functional Test
===================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "test-namespace": "test-lvm",
    "ssh-required": true,
    "cleanup": true,
    "confirmation": true,
    "check-verbose": true,
    "cleanup-on-error": false,
    "namespace": "openshift-storage",
    "name": "lvms-operator",
    "operator-group-name": "lvm-operator-group",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok
- cluster node [10.10.10.10] [key:C:\Users\user\.itool\ocp-clusters\bm1\ssh.pub]: ok


LVM Operator
------------
LVM Operator [openshift-storage/lvms] with csv [lvms-operator.v4.18.3]
LVM Subscription resources deployed
LVM Cluster instance: openshift-storage/lvmcluster
LVM Cluster instance: ready
Storage class: lvms-vg1
Prepare test resources
- namespace: test-lvm
- namespace does not exist
- namespace created
- pvc [test-lvm/ocp-bm1] created
- wait for pvc [timeout:60s]...
- pod [test-lvm/ocp-bm1] created
- wait for pod running [timeout:600s]...
- wait for pvc [test-lvm/ocp-bm1] bound [timeout:60s]...
- volume snapshot [test-lvm/ocp-bm1-snap] created

PODs
----

+----------+-------+---------+--------------------+------+---------+-------------+-----+-----+----------+
| Pod      | Ready | Status  | Condition          | Age  | Node    | IP          | Net | Svc | Restarts |
+----------+-------+---------+--------------------+------+---------+-------------+-----+-----+----------+
| test-lvm | 1/1   | Running | Initialized: ✓     | 2h3m | ocp-bm1 | 10.128.1.95 | 0   | --  | 0        |
| ocp-bm1  |       |         | PodScheduled: ✓    |      |         |             |     |     |          |
|          |       |         | ContainersReady: ✓ |      |         |             |     |     |          |
|          |       |         | Ready: ✓           |      |         |             |     |     |          |
+----------+-------+---------+--------------------+------+---------+-------------+-----+-----+----------+

Persistent Volume Claims
------------------------

+-----------+---------+--------+------------------------------------------+------+---------------+---------------+------------------+-------+------+
| Namespace | Name    | Status | Volume                                   | Size | Access Mode   | Storage Class | Usage            | Owner | Age  |
+-----------+---------+--------+------------------------------------------+------+---------------+---------------+------------------+-------+------+
| test-lvm  | ocp-bm1 | Bound  | pvc-24fa102e-6ab5-4595-a0d2-391f0b5ad95a | 1Gi  | ReadWriteOnce | lvms-vg1      | test-lvm/ocp-bm1 | --    | 2h3m |
+-----------+---------+--------+------------------------------------------+------+---------------+---------------+------------------+-------+------+

Persistent Volumes
------------------

+------------------------------------------+--------+-------+----------+------+---------------+------------+--------------------------------------+--------+------------------+------+
| Name                                     | Status | Mode  | SC       | Size | Access Mode   | CSI Driver | CSI Handle                           | Device | PVC              | Age  |
+------------------------------------------+--------+-------+----------+------+---------------+------------+--------------------------------------+--------+------------------+------+
| pvc-24fa102e-6ab5-4595-a0d2-391f0b5ad95a | Bound  | Block | lvms-vg1 | 1Gi  | ReadWriteOnce | topolvm.io | 30a74474-1e6e-4022-9ce1-8063a72803c4 | --     | test-lvm/ocp-bm1 | 2h3m |
+------------------------------------------+--------+-------+----------+------+---------------+------------+--------------------------------------+--------+------------------+------+

Volume Snapshots
----------------

+-----------+--------------+-------+---------+----------+------+------+
| Namespace | Name         | Ready | PVC     | Class    | Size | Age  |
+-----------+--------------+-------+---------+----------+------+------+
| test-lvm  | ocp-bm1-snap | ✓     | ocp-bm1 | lvms-vg1 | 1Gi  | 2h0m |
+-----------+--------------+-------+---------+----------+------+------+

Logical Volumes (TopoLVM)
-------------------------

+------------------------------------------+---------+--------------+----------+-----------+--------------------------------------+
| Name                                     | Node    | Device Class | Req Size | Curr Size | Volume                               |
+------------------------------------------+---------+--------------+----------+-----------+--------------------------------------+
| pvc-24fa102e-6ab5-4595-a0d2-391f0b5ad95a | ocp-bm1 | vg1          | 1Gi      | 1Gi       | 30a74474-1e6e-4022-9ce1-8063a72803c4 |
+------------------------------------------+---------+--------------+----------+-----------+--------------------------------------+

Collect linux level lv state...

Logical Volumes (LVM) [ocp-bm1]
-------------------------------

+------------------------------------------+-----+-------------+-------+---------+-------+--------+--------------+------+-------------------------+
| LV Name                                  | VG  | LV Pool     | Dev   | LV Size | MSize | Layout | Role         | Snap | K8s Usage               |
+------------------------------------------+-----+-------------+-------+---------+-------+--------+--------------+------+-------------------------+
| 30a74474-1e6e-4022-9ce1-8063a72803c4     | vg1 | thin-pool-1 | 253:4 | 1.00g   | 0.00% | thin   | public       | 1    | (pvc) test-lvm/ocp-bm1  |
|                                          |     |             |       |         |       | sparse | origin       |      |                         |
|                                          |     |             |       |         |       |        | thinorigin   |      |                         |
+------------------------------------------+-----+-------------+-------+---------+-------+--------+--------------+------+-------------------------+
| 7b328a42-d38b-4174-9362-1670d85cbeef     | vg1 | thin-pool-1 | 253:5 | 1.00g   | 0.00% | thin   | public       | --   | (snap) test-lvm/ocp-bm1 |
| [S] 30a74474-1e6e-4022-9ce1-8063a72803c4 |     |             |       |         |       | sparse | snapshot     |      |                         |
|                                          |     |             |       |         |       |        | thinsnapshot |      |                         |
+------------------------------------------+-----+-------------+-------+---------+-------+--------+--------------+------+-------------------------+

Consistency Checks
------------------
- pvc: test-lvm/ocp-bm1 [node:ocp-bm1]
- pv found: [name:pvc-24fa102e-6ab5-4595-a0d2-391f0b5ad95a] [csi handle:30a74474-1e6e-4022-9ce1-8063a72803c4]
- topolvm logical volume found: [name:pvc-24fa102e-6ab5-4595-a0d2-391f0b5ad95a] [volume:30a74474-1e6e-4022-9ce1-8063a72803c4] with csi handle match
- lv found: [node:ocp-bm1] [name:30a74474-1e6e-4022-9ce1-8063a72803c4] [uuid:EdyimH-tJRt-B95o-12rU-QwLr-FTXu-EX1Fb7]

Delete test resources
- delete pod test-lvm/ocp-bm1
- pod delete request successful
- wait for no pod...
- all pods deleted
- delete snapshot test-lvm/ocp-bm1-snap
- volume snapshot delete request successful
- wait for no snapshot...
- all snapshots deleted
- delete pvc test-lvm/ocp-bm1
- pvc delete request successful
- wait for no pvc...
- all pvcs deleted
- namespace deleted: test-lvm
```

[[Back]](./README.md)