# LVM Storage - Create cluster - Explicit LVMCluster CRD

[[Back]](./README.md) [[discovery]](./create_cluster_discovery.md) [[device]](create_cluster_device.md) [[explicit]](create_cluster_explicit.md)

## Example

```
# iserver set ocp lvm --mode cluster --cluster bm1 --filename C:\tmp\lvmcluster.yaml --no-confirm

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
Devices not defined

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


+-------+------------------+--------+----------+-----------+-------------------------------------------------------------------------+
| Node  | Discovery Policy | Status | Devices  | Excluded  | Reason                                                                  |
+-------+------------------+--------+----------+-----------+-------------------------------------------------------------------------+
| bm1-1 | RuntimeDynamic   | Ready  | /dev/sda | /dev/sdg  | /dev/sdg has children block devices and could not be considered         | 
|       |                  |        | /dev/sdb | /dev/sdg1 | /dev/sdg1 has an invalid partition label "BIOS-BOOT"                    | 
|       |                  |        | /dev/sdc | /dev/sdg2 | /dev/sdg2 has an invalid filesystem signature (vfat) and cannot be used | 
|       |                  |        | /dev/sdd | /dev/sdg3 | /dev/sdg3 has an invalid filesystem signature (ext4) and cannot be used | 
|       |                  |        | /dev/sde | /dev/sdg4 | /dev/sdg3 has an invalid partition label "boot"                         | 
|       |                  |        | /dev/sdf |           | /dev/sdg4 has an invalid filesystem signature (xfs) and cannot be used  | 
|       |                  |        | /dev/sdh |           |                                                                         | 
|       |                  |        | /dev/sdi |           |                                                                         | 
|       |                  |        | /dev/sdj |           |                                                                         | 
|       |                  |        | /dev/sdk |           |                                                                         | 
+-------+------------------+--------+----------+-----------+-------------------------------------------------------------------------+
| bm1-2 | RuntimeDynamic   | Ready  | /dev/sda | /dev/sdh  | /dev/sdh has children block devices and could not be considered         | 
|       |                  |        | /dev/sdb | /dev/sdh1 | /dev/sdh1 has an invalid partition label "BIOS-BOOT"                    | 
|       |                  |        | /dev/sdc | /dev/sdh2 | /dev/sdh2 has an invalid filesystem signature (vfat) and cannot be used | 
|       |                  |        | /dev/sdd | /dev/sdh3 | /dev/sdh3 has an invalid filesystem signature (ext4) and cannot be used | 
|       |                  |        | /dev/sde | /dev/sdh4 | /dev/sdh3 has an invalid partition label "boot"                         | 
|       |                  |        | /dev/sdf |           | /dev/sdh4 has an invalid filesystem signature (xfs) and cannot be used  | 
|       |                  |        | /dev/sdg |           |                                                                         | 
|       |                  |        | /dev/sdi |           |                                                                         | 
|       |                  |        | /dev/sdj |           |                                                                         | 
|       |                  |        | /dev/sdk |           |                                                                         | 
+-------+------------------+--------+----------+-----------+-------------------------------------------------------------------------+
| bm1-3 | RuntimeDynamic   | Ready  | /dev/sda | /dev/sdh  | /dev/sdh has an invalid filesystem signature (xfs) and cannot be used   | 
|       |                  |        | /dev/sdb | /dev/sdk  | /dev/sdk has children block devices and could not be considered         | 
|       |                  |        | /dev/sdc | /dev/sdk1 | /dev/sdk1 has an invalid partition label "BIOS-BOOT"                    | 
|       |                  |        | /dev/sdd | /dev/sdk2 | /dev/sdk2 has an invalid filesystem signature (vfat) and cannot be used | 
|       |                  |        | /dev/sde | /dev/sdk3 | /dev/sdk3 has an invalid filesystem signature (ext4) and cannot be used | 
|       |                  |        | /dev/sdf | /dev/sdk4 | /dev/sdk3 has an invalid partition label "boot"                         | 
|       |                  |        | /dev/sdg |           | /dev/sdk4 has an invalid filesystem signature (xfs) and cannot be used  | 
|       |                  |        | /dev/sdi |           |                                                                         | 
|       |                  |        | /dev/sdj |           |                                                                         | 
+-------+------------------+--------+----------+-----------+-------------------------------------------------------------------------+


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
| 1  | ocp:bm1 | lvm   | create cluster | 1       | ✓       | 141          | 
+----+---------+-------+----------------+---------+---------+--------------+
```

[[Back]](./README.md) [[discovery]](./create_cluster_discovery.md) [[device]](create_cluster_device.md) [[explicit]](create_cluster_explicit.md)