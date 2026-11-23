# LVM Storage - Get

## Workflow

- check lvm storage operator subscription
- check lvm storage operator resources (deployments and daemon_sets)
- check lvmcluster CRD and its state
- check storage class
- check linux lvm resources

## Example

```
# iserver get ocp lvm --cluster bm1

OpenShift Workflow - LVM - Get Information
==========================================

OpenShift Cluster: bm1

Collecting state...


Operator
- package   : openshift-marketplace/redhat-operators/lvms-operator
- csv       : lvms-operator.v4.18.4
- resources : ✓



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



LVM Related Resources
---------------------
- storage class : 1
- pvc           : 0
- dv            : ---
- pv            : ---
- snapshot      : ---


View: state (def), res, lvm, all
```

[[Back]](./README.md)