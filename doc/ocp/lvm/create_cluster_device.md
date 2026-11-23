# LVM Storage - Create cluster - Generated LVMCluster CRD with dynamic resource discovery

[[Back]](./README.md) [[discovery]](./create_cluster_discovery.md) [[device]](create_cluster_device.md) [[explicit]](create_cluster_explicit.md)

> [!NOTE]
> if device name is used then it **must** resolve to the same path across the nodes. use iserver get linux lsblk` to find device names to path binding

## LVMCluster CRD

```yaml
apiVersion: lvm.topolvm.io/v1alpha1
kind: LVMCluster
metadata:
  name: my-lvmcluster
  namespace: openshift-storage
spec:
  storage:
    deviceClasses:
    - default: false
      deviceSelector:
        paths:
        - /dev/disk/by-path/pci-0000:3c:00.0-scsi-0:2:1:0
        - /dev/disk/by-path/pci-0000:00:11.5-ata-1.0
      fstype: xfs
      name: vg1
      thinPoolConfig:
        chunkSizeCalculationPolicy: Static
        metadataSizeCalculationPolicy: Host
        name: thin-pool-1
        overprovisionRatio: 10
        sizePercent: 90
```

## HowTo

```
# iserver set ocp lvm --cluster bm1 --mode cluster --device sda --device sdc
```

```
# iserver set ocp lvm --cluster bm1 --mode cluster --device pci-0000:3c:00.0-scsi-0:2:1:0 --device pci-0000:00:11.5-ata-1.0
```

```
# iserver set ocp lvm --mode cluster --cluster bm1 --device sdb

OpenShift Workflow - LVM - Create Instance
==========================================

OpenShift Cluster: bm1

LVM Operator
------------

Operator
- subscription          : openshift-storage/lvms
- package               : openshift-marketplace/redhat-operators/lvms-operator
- channel               : stable-4.18
- install plan          : openshift-storage/install-2658c
- install plan approved : ✓
- installed csv         : lvms-operator.v4.18.4
- latest_csv            : ✓

LVM Operator [openshift-storage/lvms] with csv [lvms-operator.v4.18.4]
LVM Subscription resources deployed
LVM Cluster instance not found
Target block devices
- /dev/sdb


Collect linux level lsblk per node...

Block Devices [bm1-1]
---------------------

+----------+-------+------+---------+--------+------------------+-------------+-------+---------+--------------------------------------------+
| Path     | KName | Boot | Maj:Min | Size   | Model            | Serial      | Group | FS Type | Disk ID                                    |
+----------+-------+------+---------+--------+------------------+-------------+-------+---------+--------------------------------------------+
| /dev/sdb | sdb   |      | 8:16    | 894.3G | Micron_5100_MTFD | AAA         | disk  | ---     | /dev/disk/by-path/pci-0000:00:11.5-ata-3.0 | 
|          |       |      |         |        |                  |             |       |         | /dev/disk/by-id/wwn-0xaaa                  | 
+----------+-------+------+---------+--------+------------------+-------------+-------+---------+--------------------------------------------+

Block Devices [bm1-2]
---------------------

+----------+-------+------+---------+--------+------------------+-------------+-------+---------+--------------------------------------------+
| Path     | KName | Boot | Maj:Min | Size   | Model            | Serial      | Group | FS Type | Disk ID                                    |
+----------+-------+------+---------+--------+------------------+-------------+-------+---------+--------------------------------------------+
| /dev/sdb | sdb   |      | 8:16    | 894.3G | Micron_5100_MTFD | BBB         | disk  | ---     | /dev/disk/by-path/pci-0000:00:11.5-ata-3.0 | 
|          |       |      |         |        |                  |             |       |         | /dev/disk/by-id/wwn-0xbbb                  | 
+----------+-------+------+---------+--------+------------------+-------------+-------+---------+--------------------------------------------+

Block Devices [bm1-3]
---------------------

+----------+-------+------+---------+--------+------------------+-------------+-------+---------+--------------------------------------------+
| Path     | KName | Boot | Maj:Min | Size   | Model            | Serial      | Group | FS Type | Disk ID                                    |
+----------+-------+------+---------+--------+------------------+-------------+-------+---------+--------------------------------------------+
| /dev/sdb | sdb   |      | 8:16    | 894.3G | Micron_5100_MTFD | CCC         | disk  | ---     | /dev/disk/by-path/pci-0000:00:11.5-ata-3.0 | 
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
- Nodes Ready     : 3/3


+-------+------------------+--------+----------+-----------+----------------------------------------------------------------------------------------------+
| Node  | Discovery Policy | Status | Devices  | Excluded  | Reason                                                                                       |
+-------+------------------+--------+----------+-----------+----------------------------------------------------------------------------------------------+
| bm1-1 | Preconfigured    | Ready  | /dev/sdb | /dev/sda  | /dev/sda is not part of the device selector or could not be resolved via symlink resolution  | 
|       |                  |        |          | /dev/sdc  | /dev/sdc is not part of the device selector or could not be resolved via symlink resolution  | 
|       |                  |        |          | /dev/sdd  | /dev/sdd is not part of the device selector or could not be resolved via symlink resolution  | 
|       |                  |        |          | /dev/sde  | /dev/sde is not part of the device selector or could not be resolved via symlink resolution  | 
|       |                  |        |          | /dev/sdf  | /dev/sdf is not part of the device selector or could not be resolved via symlink resolution  | 
|       |                  |        |          | /dev/sdg  | /dev/sdg has children block devices and could not be considered                              | 
|       |                  |        |          | /dev/sdg1 | /dev/sdg is not part of the device selector or could not be resolved via symlink resolution  | 
|       |                  |        |          | /dev/sdg2 | /dev/sdg1 has an invalid partition label "BIOS-BOOT"                                         | 
|       |                  |        |          | /dev/sdg3 | /dev/sdg1 is not part of the device selector or could not be resolved via symlink resolution | 
|       |                  |        |          | /dev/sdg4 | /dev/sdg2 has an invalid filesystem signature (vfat) and cannot be used                      | 
|       |                  |        |          | /dev/sdh  | /dev/sdg2 is not part of the device selector or could not be resolved via symlink resolution | 
|       |                  |        |          | /dev/sdi  | /dev/sdg3 has an invalid filesystem signature (ext4) and cannot be used                      | 
|       |                  |        |          | /dev/sdj  | /dev/sdg3 has an invalid partition label "boot"                                              | 
|       |                  |        |          | /dev/sdk  | /dev/sdg3 is not part of the device selector or could not be resolved via symlink resolution | 
|       |                  |        |          |           | /dev/sdg4 has an invalid filesystem signature (xfs) and cannot be used                       | 
|       |                  |        |          |           | /dev/sdg4 is not part of the device selector or could not be resolved via symlink resolution | 
|       |                  |        |          |           | /dev/sdh is not part of the device selector or could not be resolved via symlink resolution  | 
|       |                  |        |          |           | /dev/sdi is not part of the device selector or could not be resolved via symlink resolution  | 
|       |                  |        |          |           | /dev/sdj is not part of the device selector or could not be resolved via symlink resolution  | 
|       |                  |        |          |           | /dev/sdk is not part of the device selector or could not be resolved via symlink resolution  | 
+-------+------------------+--------+----------+-----------+----------------------------------------------------------------------------------------------+
| bm1-2 | Preconfigured    | Ready  | /dev/sdb | /dev/sda  | /dev/sda is not part of the device selector or could not be resolved via symlink resolution  | 
|       |                  |        |          | /dev/sdc  | /dev/sdc is not part of the device selector or could not be resolved via symlink resolution  | 
|       |                  |        |          | /dev/sdd  | /dev/sdd is not part of the device selector or could not be resolved via symlink resolution  | 
|       |                  |        |          | /dev/sde  | /dev/sde is not part of the device selector or could not be resolved via symlink resolution  | 
|       |                  |        |          | /dev/sdf  | /dev/sdf is not part of the device selector or could not be resolved via symlink resolution  | 
|       |                  |        |          | /dev/sdg  | /dev/sdg is not part of the device selector or could not be resolved via symlink resolution  | 
|       |                  |        |          | /dev/sdh  | /dev/sdh has children block devices and could not be considered                              | 
|       |                  |        |          | /dev/sdh1 | /dev/sdh is not part of the device selector or could not be resolved via symlink resolution  | 
|       |                  |        |          | /dev/sdh2 | /dev/sdh1 has an invalid partition label "BIOS-BOOT"                                         | 
|       |                  |        |          | /dev/sdh3 | /dev/sdh1 is not part of the device selector or could not be resolved via symlink resolution | 
|       |                  |        |          | /dev/sdh4 | /dev/sdh2 has an invalid filesystem signature (vfat) and cannot be used                      | 
|       |                  |        |          | /dev/sdi  | /dev/sdh2 is not part of the device selector or could not be resolved via symlink resolution | 
|       |                  |        |          | /dev/sdj  | /dev/sdh3 has an invalid filesystem signature (ext4) and cannot be used                      | 
|       |                  |        |          | /dev/sdk  | /dev/sdh3 has an invalid partition label "boot"                                              | 
|       |                  |        |          |           | /dev/sdh3 is not part of the device selector or could not be resolved via symlink resolution | 
|       |                  |        |          |           | /dev/sdh4 has an invalid filesystem signature (xfs) and cannot be used                       | 
|       |                  |        |          |           | /dev/sdh4 is not part of the device selector or could not be resolved via symlink resolution | 
|       |                  |        |          |           | /dev/sdi is not part of the device selector or could not be resolved via symlink resolution  | 
|       |                  |        |          |           | /dev/sdj is not part of the device selector or could not be resolved via symlink resolution  | 
|       |                  |        |          |           | /dev/sdk is not part of the device selector or could not be resolved via symlink resolution  | 
+-------+------------------+--------+----------+-----------+----------------------------------------------------------------------------------------------+
| bm1-3 | Preconfigured    | Ready  | /dev/sdb | /dev/sda  | /dev/sda is not part of the device selector or could not be resolved via symlink resolution  | 
|       |                  |        |          | /dev/sdc  | /dev/sdc is not part of the device selector or could not be resolved via symlink resolution  | 
|       |                  |        |          | /dev/sdd  | /dev/sdd is not part of the device selector or could not be resolved via symlink resolution  | 
|       |                  |        |          | /dev/sde  | /dev/sde is not part of the device selector or could not be resolved via symlink resolution  | 
|       |                  |        |          | /dev/sdf  | /dev/sdf is not part of the device selector or could not be resolved via symlink resolution  | 
|       |                  |        |          | /dev/sdg  | /dev/sdg is not part of the device selector or could not be resolved via symlink resolution  | 
|       |                  |        |          | /dev/sdh  | /dev/sdh has an invalid filesystem signature (xfs) and cannot be used                        | 
|       |                  |        |          | /dev/sdi  | /dev/sdh is not part of the device selector or could not be resolved via symlink resolution  | 
|       |                  |        |          | /dev/sdj  | /dev/sdi is not part of the device selector or could not be resolved via symlink resolution  | 
|       |                  |        |          | /dev/sdk  | /dev/sdj is not part of the device selector or could not be resolved via symlink resolution  | 
|       |                  |        |          | /dev/sdk1 | /dev/sdk has children block devices and could not be considered                              | 
|       |                  |        |          | /dev/sdk2 | /dev/sdk is not part of the device selector or could not be resolved via symlink resolution  | 
|       |                  |        |          | /dev/sdk3 | /dev/sdk1 has an invalid partition label "BIOS-BOOT"                                         | 
|       |                  |        |          | /dev/sdk4 | /dev/sdk1 is not part of the device selector or could not be resolved via symlink resolution | 
|       |                  |        |          |           | /dev/sdk2 has an invalid filesystem signature (vfat) and cannot be used                      | 
|       |                  |        |          |           | /dev/sdk2 is not part of the device selector or could not be resolved via symlink resolution | 
|       |                  |        |          |           | /dev/sdk3 has an invalid filesystem signature (ext4) and cannot be used                      | 
|       |                  |        |          |           | /dev/sdk3 has an invalid partition label "boot"                                              | 
|       |                  |        |          |           | /dev/sdk3 is not part of the device selector or could not be resolved via symlink resolution | 
|       |                  |        |          |           | /dev/sdk4 has an invalid filesystem signature (xfs) and cannot be used                       | 
|       |                  |        |          |           | /dev/sdk4 is not part of the device selector or could not be resolved via symlink resolution | 
+-------+------------------+--------+----------+-----------+----------------------------------------------------------------------------------------------+


+----+---------------+---------+-------------+----------------+----------------------+------------------------+
| ID | Storage Class | Default | Provisioner | Reclaim Policy | Volume Binding Mode  | Allow Volume Expansion |
+----+---------------+---------+-------------+----------------+----------------------+------------------------+
| 1  | lvms-vg1      |         | topolvm.io  | Delete         | WaitForFirstConsumer | True                   | 
+----+---------------+---------+-------------+----------------+----------------------+------------------------+

Completed tasks
- LVM Cluster instance created and ready
- Storage class ready

+----+---------+-------+----------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow       | Changes | Success | Duration [s] |
+----+---------+-------+----------------+---------+---------+--------------+
| 1  | ocp:bm1 | lvm   | create cluster | 1       | ✓       | 276          | 
+----+---------+-------+----------------+---------+---------+--------------+
```

[[Back]](./README.md) [[discovery]](./create_cluster_discovery.md) [[device]](create_cluster_device.md) [[explicit]](create_cluster_explicit.md)