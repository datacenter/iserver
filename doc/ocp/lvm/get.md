# LVM Storage Operator - Get

## Workflow

- check lvm storage operator subscription
- check lvm storage operator resources (deployments and daemon_sets)
- check lvmcluster CRD and its state
- check storage class
- check linux lvm resources

## Example

```
# iserver get ocp lvm 

OpenShift Workflow - LVM Operator - Get Information
===================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "ssh-check": true,
    "check-verbose": true,
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

Operator
--------
- subscription: openshift-storage/lvms
- csv: lvms-operator.v4.18.3


LVMCluster
----------
- Namespace : openshift-storage
- Name      : my-lvmcluster
- State     : Ready
- Ready     : ✓
- Resources : ✓
- VGs       : ✓


Device Class
------------
- Name            : vg1
- Filesystem Type : xfs
- Default         : ✗
- Nodes Ready     : 1/1


+---------+------------------+--------+----------+-----------+-------------------------------------------------------------------------+
| Node    | Discovery Policy | Status | Devices  | Excluded  | Reason                                                                  |
+---------+------------------+--------+----------+-----------+-------------------------------------------------------------------------+
| ocp-bm1 | RuntimeDynamic   | Ready  | /dev/sda | /dev/sdc  | /dev/sdc has children block devices and could not be considered         |
|         |                  |        | /dev/sdb | /dev/sdc1 | /dev/sdc1 has an invalid partition label "BIOS-BOOT"                    |
|         |                  |        | /dev/sdd | /dev/sdc2 | /dev/sdc2 has an invalid filesystem signature (vfat) and cannot be used |
|         |                  |        |          | /dev/sdc3 | /dev/sdc3 has an invalid filesystem signature (ext4) and cannot be used |
|         |                  |        |          | /dev/sdc4 | /dev/sdc3 has an invalid partition label "boot"                         |
|         |                  |        |          |           | /dev/sdc4 has an invalid filesystem signature (xfs) and cannot be used  |
+---------+------------------+--------+----------+-----------+-------------------------------------------------------------------------+


LVM storage class
-----------------

+----------+---------+-------------+----------------+----------------------+------------------------+
| Name     | Default | Provisioner | Reclaim Policy | Volume Binding Mode  | Allow Volume Expansion |
+----------+---------+-------------+----------------+----------------------+------------------------+
| lvms-vg1 |         | topolvm.io  | Delete         | WaitForFirstConsumer | True                   |
+----------+---------+-------------+----------------+----------------------+------------------------+

Perstistent Volume Claims
-------------------------
None

Collect linux level lvm state...
- ocp-bm1: collected [blks, lvs, vgs, pvs]

Block Devices [ocp-bm1]
-----------------------

+----------+-------+------+---------+--------+------------------+----------------------------------+-------+---------+
| Path     | KName | Boot | Maj:Min | Size   | Model            | Serial                           | Group | FS Type |
+----------+-------+------+---------+--------+------------------+----------------------------------+-------+---------+
| /dev/sda | sda   |      | 8:0     | 894.3G | Micron_5100_MTFD | xxxxxxxxxxx                      | disk  | LVM2    |
+----------+-------+------+---------+--------+------------------+----------------------------------+-------+---------+
| /dev/sdb | sdb   |      | 8:16    | 894.3G | Micron_5100_MTFD | xxxxxxxxxxx                      | disk  | LVM2    |
+----------+-------+------+---------+--------+------------------+----------------------------------+-------+---------+
| /dev/sdc | sdc   | ✓    | 8:32    | 1.1T   | UCSC-RAID12G-2GB | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx | disk  | ---     |
+----------+-------+------+---------+--------+------------------+----------------------------------+-------+---------+
| /dev/sdd | sdd   |      | 8:48    | 1.1T   | UCSC-RAID12G-2GB | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx | disk  | LVM2    |
+----------+-------+------+---------+--------+------------------+----------------------------------+-------+---------+

Physical Volume (LVM) [ocp-bm1]
-------------------------------

+----------+-----+------+------+---------+----------+
| PV       | VG  | Fmt  | Attr | PSize   | PFree    |
+----------+-----+------+------+---------+----------+
| /dev/sda | vg1 | lvm2 | a--  | 894.25g | <290.52g |
| /dev/sdb | vg1 | lvm2 | a--  | 894.25g | 0        |
| /dev/sdd | vg1 | lvm2 | a--  | 1.09t   | 0        | 
+----------+-----+------+------+---------+----------+

Volume Groups (LVM) [ocp-bm1]
-----------------------------

+-----+-----+-----+--------+--------+----------+
| VG  | #PV | #LV | Attr   | VSize  | VFree    |
+-----+-----+-----+--------+--------+----------+
| vg1 | 3   | 1   | wz--n- | <2.84t | <290.52g |
+-----+-----+-----+--------+--------+----------+

Logical Volumes (LVM) [ocp-bm1]
-------------------------------

+-------------+-----+---------+-------+---------+-------+--------+---------+------+-----------+
| LV Name     | VG  | LV Pool | Dev   | LV Size | MSize | Layout | Role    | Snap | K8s Usage |
+-------------+-----+---------+-------+---------+-------+--------+---------+------+-----------+
| thin-pool-1 | vg1 |         | 253:2 | 2.55t   | 0.00% | thin   | private | --   | N/A       |
|             |     |         |       |         |       | pool   |         |      |           |
+-------------+-----+---------+-------+---------+-------+--------+---------+------+-----------+

Summary
-------
- operator: lvms-operator.v4.18.3
- lvm cluster: openshift-storage/my-lvmcluster [Ready]
- storage class [not default]: lvms-vg1
- no persistent volume claims
- server lvm info fully collected
- all logical volumes back by kube resources
```

[[Back]](./README.md)