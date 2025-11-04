# LVM Storage Operator - Create via Task

## Input

### Default generated LVMCluster CRD

```
[
    {
        "lvm": {
            "operator": {
                "channel": "abc"
            },
            "cluster": {
            }
        }
    }
]
```

### Device-based generated LVMCluster CRD

```
[
    {
        "lvm": {
            "operator": {
                "channel": "abc"
            },
            "cluster": {
                "filename": "xyz"
            }
        }
    }
]
```

### Custom LVMCluster CRD

```
[
    {
        "lvm": {
            "operator": {
                "channel": "abc"
            },
            "cluster": {
                "device": [
                  "sda",
                  "sdb"
                ]
            }
        }
    }
]
```

Notes:
- [operator](./create_operator.md) and [cluster](./create_cluster.md) trigger workflow execution with optional input parameters
- not all workflows have to be defined however be aware of workflow execution requirements and dependencies
- cluster.filename is optional must contain LVMCluster CRD in YAML format
  - the path defined in cluster.filename can be relative and then expected to be in the same directory as task.json file
  - the path defined in cluster.filename can be absolute

## Requirements

None

## Configurable options

```
# iserver set ocp task 
  --cluster TEXT   Cluster Name
  --filename TEXT  Tasks filename
  --validate       Validate only
  --break          Break on error
  --no-confirm     Confirmation mode
```

## Example

```
[
    {
        "lvm": {
            "operator": {},
            "cluster": {
                "device": ["sda", "sdb"]
            }
        }
    }
]
```

```
# iserver set ocp task --filename C:\tmp\task.json --no-confirm
OpenShift Cluster: bm1

Cluster: bm1 (type: ocp)

OpenShift Workflow - Create Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - LVM Operator - Create Operator
===================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "confirmation": false,
    "channel": "__default__",
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


Create Namespace
----------------
- name: openshift-storage
- labels
        openshift.io/cluster-monitoring:true
        pod-security.kubernetes.io/enforce:privileged
        pod-security.kubernetes.io/audit:privileged
        pod-security.kubernetes.io/warn:privileged

~~~
apiVersion: v1
kind: Namespace
metadata:
  labels:
    openshift.io/cluster-monitoring: 'true'
    pod-security.kubernetes.io/audit: privileged
    pod-security.kubernetes.io/enforce: privileged
    pod-security.kubernetes.io/warn: privileged
  name: openshift-storage

~~~

Namespace created

Wait for namespace [timeout:60]...

Check labels
- openshift.io/cluster-monitoring:true
- pod-security.kubernetes.io/enforce:privileged
- pod-security.kubernetes.io/audit:privileged
- pod-security.kubernetes.io/warn:privileged

Create Operator Group
---------------------
Operator group: openshift-storage/openshift-storage-operatorgroup
Target namespaces: openshift-storage

~~~
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: openshift-storage-operatorgroup
  namespace: openshift-storage
spec:
  targetNamespaces:
  - openshift-storage

~~~

Operator group created

Wait for operator group [timeout:60]...

Create Subscription
-------------------
Subscription: openshift-storage/lvms
Source: openshift-marketplace/redhat-operators/lvms-operator
Install plan approval: Automatic
Getting subscription and packege manifest information...
Resolving channel name...
Channel: stable-4.18
- CSV [lvms-operator.v4.18.3]
- CSV Display name [LVM Storage]
- CVS Version [4.18.3]
- CSV Provider [{'name': 'Red Hat'}]
- CSV Maturity [alpha]

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: lvms
  namespace: openshift-storage
spec:
  channel: stable-4.18
  installPlanApproval: Automatic
  name: lvms-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace

~~~

Subscription created

Wait for subscription install plan started [timeout:360]...
Install plan: install-m2jhn
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployments ready (optional: False, allow zero replicas: False)...
- openshift-storage/lvms-operator

Completed tasks
- LVM storage operator installed

OpenShift Workflow - LVM Operator - Create Cluster
==================================================

Workflow Parameters
-------------------
{
    "device": [
        "sda",
        "sdb"
    ],
    "cluster": "bm1",
    "confirmation": false,
    "ssh-check": true,
    "check-verbose": true,
    "instance": null,
    "ssh-required": true,
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
LVM Cluster instance not found
Target block devices
- /dev/sda
- /dev/sdb


Collect linux level lsblk per node...

Block Devices [ocp-bm1]
-----------------------

+----------+-------+------+---------+--------+------------------+-------------+-------+---------+--------------------------------------------+
| Path     | KName | Boot | Maj:Min | Size   | Model            | Serial      | Group | FS Type | Disk ID                                    |
+----------+-------+------+---------+--------+------------------+-------------+-------+---------+--------------------------------------------+
| /dev/sda | sda   |      | 8:0     | 894.3G | Micron_5100_MTFD | xxxxxxxxxxx | disk  | ---     | /dev/disk/by-path/pci-0000:00:11.5-ata-1.0 |
|          |       |      |         |        |                  |             |       |         | /dev/disk/by-id/wwn-0x500a07511c556087     |
+----------+-------+------+---------+--------+------------------+-------------+-------+---------+--------------------------------------------+
| /dev/sdb | sdb   |      | 8:16    | 894.3G | Micron_5100_MTFD | xxxxxxxxxxx | disk  | ---     | /dev/disk/by-path/pci-0000:00:11.5-ata-3.0 |
|          |       |      |         |        |                  |             |       |         | /dev/disk/by-id/wwn-0x500a07511c5560db     |
+----------+-------+------+---------+--------+------------------+-------------+-------+---------+--------------------------------------------+

Create LVM Cluster
------------------
- namespace: openshift-storage
- name: lvmcluster

~~~
apiVersion: lvm.topolvm.io/v1alpha1
kind: LVMCluster
metadata:
  name: lvmcluster
  namespace: openshift-storage
spec:
  storage:
    deviceClasses:
    - default: false
      deviceSelector:
        paths:
        - /dev/disk/by-path/pci-0000:00:11.5-ata-1.0
        - /dev/disk/by-path/pci-0000:00:11.5-ata-3.0
      fstype: xfs
      name: vg1
      thinPoolConfig:
        chunkSizeCalculationPolicy: Static
        metadataSizeCalculationPolicy: Host
        name: thin-pool-1
        overprovisionRatio: 10
        sizePercent: 90

~~~
Wait until ready or degraded [timeout:180s]...
Wait for lvm storage class [timeout:180s]...


LVMCluster
----------
- Namespace : openshift-storage
- Name      : lvmcluster
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


+---------+------------------+--------+----------+-----------+----------------------------------------------------------------------------------------------+
| Node    | Discovery Policy | Status | Devices  | Excluded  | Reason                                                                                       |
+---------+------------------+--------+----------+-----------+----------------------------------------------------------------------------------------------+
| ocp-bm1 | Preconfigured    | Ready  | /dev/sda | /dev/sdc  | /dev/sdc has children block devices and could not be considered                              |
|         |                  |        | /dev/sdb | /dev/sdc1 | /dev/sdc is not part of the device selector or could not be resolved via symlink resolution  |
|         |                  |        |          | /dev/sdc2 | /dev/sdc1 has an invalid partition label "BIOS-BOOT"                                         |
|         |                  |        |          | /dev/sdc3 | /dev/sdc1 is not part of the device selector or could not be resolved via symlink resolution |
|         |                  |        |          | /dev/sdc4 | /dev/sdc2 has an invalid filesystem signature (vfat) and cannot be used                      |
|         |                  |        |          | /dev/sdd  | /dev/sdc2 is not part of the device selector or could not be resolved via symlink resolution |
|         |                  |        |          |           | /dev/sdc3 has an invalid filesystem signature (ext4) and cannot be used                      |
|         |                  |        |          |           | /dev/sdc3 has an invalid partition label "boot"                                              |
|         |                  |        |          |           | /dev/sdc3 is not part of the device selector or could not be resolved via symlink resolution |
|         |                  |        |          |           | /dev/sdc4 has an invalid filesystem signature (xfs) and cannot be used                       |
|         |                  |        |          |           | /dev/sdc4 is not part of the device selector or could not be resolved via symlink resolution |
|         |                  |        |          |           | /dev/sdd is not part of the device selector or could not be resolved via symlink resolution  |
+---------+------------------+--------+----------+-----------+----------------------------------------------------------------------------------------------+


+----------+---------+-------------+----------------+----------------------+------------------------+
| Name     | Default | Provisioner | Reclaim Policy | Volume Binding Mode  | Allow Volume Expansion |
+----------+---------+-------------+----------------+----------------------+------------------------+
| lvms-vg1 |         | topolvm.io  | Delete         | WaitForFirstConsumer | True                   |
+----------+---------+-------------+----------------+----------------------+------------------------+

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
| /dev/sdd | sdd   |      | 8:48    | 1.1T   | UCSC-RAID12G-2GB | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx | disk  | ---     |
+----------+-------+------+---------+--------+------------------+----------------------------------+-------+---------+

Physical Volume (LVM) [ocp-bm1]
-------------------------------

+----------+-----+------+------+---------+---------+
| PV       | VG  | Fmt  | Attr | PSize   | PFree   |
+----------+-----+------+------+---------+---------+
| /dev/sda | vg1 | lvm2 | a--  | 894.25g | 178.85g |
| /dev/sdb | vg1 | lvm2 | a--  | 894.25g | 0       |
+----------+-----+------+------+---------+---------+

Volume Groups (LVM) [ocp-bm1]
-----------------------------

+-----+-----+-----+--------+--------+---------+
| VG  | #PV | #LV | Attr   | VSize  | VFree   |
+-----+-----+-----+--------+--------+---------+
| vg1 | 2   | 1   | wz--n- | <1.75t | 178.85g |
+-----+-----+-----+--------+--------+---------+

Logical Volumes (LVM) [ocp-bm1]
-------------------------------

+-------------+-----+---------+-------+---------+-------+--------+---------+------+-----------+
| LV Name     | VG  | LV Pool | Dev   | LV Size | MSize | Layout | Role    | Snap | K8s Usage |
+-------------+-----+---------+-------+---------+-------+--------+---------+------+-----------+
| thin-pool-1 | vg1 |         | 253:2 | 1.57t   | 0.00% | thin   | private | --   | N/A       |
|             |     |         |       |         |       | pool   |         |      |           |
+-------------+-----+---------+-------+---------+-------+--------+---------+------+-----------+

Completed tasks
- LVM Cluster instance created and ready
- Storage class ready
```

[[Back]](./README.md)