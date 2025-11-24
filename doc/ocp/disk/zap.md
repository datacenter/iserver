# Zap block devices

Storage subystem even if removed can leave some data on the disk that will 
- keep fs type of the disk to non-empty value
- prevent the disk from being used again

For example you can install [lvm cluster](../lvm/create_cluster.md) on all available disk and end with the following error

```
+-------+------------------+--------+---------+-----------+----------------------------------------------------------------------------------+
| Node  | Discovery Policy | Status | Devices | Excluded  | Reason                                                                           |
+-------+------------------+--------+---------+-----------+----------------------------------------------------------------------------------+
| bm3-1 | RuntimeDynamic   | Failed |         | /dev/sda  | /dev/sda has children block devices and could not be considered                  | 
|       |                  |        |         | /dev/sda1 | /dev/sda1 has an invalid partition label "BIOS-BOOT"                             | 
|       |                  |        |         | /dev/sda2 | /dev/sda2 has an invalid filesystem signature (vfat) and cannot be used          | 
|       |                  |        |         | /dev/sda3 | /dev/sda3 has an invalid filesystem signature (ext4) and cannot be used          | 
|       |                  |        |         | /dev/sda4 | /dev/sda3 has an invalid partition label "boot"                                  | 
|       |                  |        |         | /dev/sdb  | /dev/sda4 has an invalid filesystem signature (xfs) and cannot be used           | 
|       |                  |        |         | /dev/sdc  | /dev/sdb has an invalid filesystem signature (ceph_bluestore) and cannot be used | 
|       |                  |        |         |           | /dev/sdc has an invalid filesystem signature (ceph_bluestore) and cannot be used | 
+-------+------------------+--------+---------+-----------+----------------------------------------------------------------------------------+
```

where /dev/sdb and /dev/sdc 

```
+----------+-------+------+---------+--------+------------------+---------+-------+---------+--------------------------------------------------------+
| Path     | KName | Boot | Maj:Min | Size   | Model            | Serial  | Group | FS Type | Disk ID                                                |
+----------+-------+------+---------+--------+------------------+---------+-------+---------+--------------------------------------------------------+
| /dev/sda | sda   | ✓    | 8:0     | 1.1T   | UCSC-RAID12G-2GB | abc     | disk  | ---     | /dev/disk/by-path/pci-0000:3c:00.0-scsi-0:2:0:0        | 
|          |       |      |         |        |                  |         |       |         | /dev/disk/by-id/wwn-0x6cc167e973700fc029771bd1c31a36fa |
+----------+-------+------+---------+--------+------------------+---------+-------+---------+--------------------------------------------------------+
| /dev/sdb | sdb   |      | 8:16    | 894.3G | Micron_5100_MTFD | def     | disk  | Ceph    | /dev/disk/by-path/pci-0000:00:11.5-ata-1.0             | 
|          |       |      |         |        |                  |         |       |         | /dev/disk/by-id/wwn-0x500a075118ef25c1                 |
+----------+-------+------+---------+--------+------------------+---------+-------+---------+--------------------------------------------------------+
| /dev/sdc | sdc   |      | 8:32    | 894.3G | Micron_5100_MTFD | xyz     | disk  | Ceph    | /dev/disk/by-path/pci-0000:00:11.5-ata-3.0             |
|          |       |      |         |        |                  |         |       |         | /dev/disk/by-id/wwn-0x500a075118ef2777                 |
+----------+-------+------+---------+--------+------------------+---------+-------+---------+--------------------------------------------------------+
```

## Workflow 

Execute the following commands on the selected block device
- sudo sgdisk --zap-all device-name
- sudo blkdiscard -f device-name
- sudo lsblk -O --json

Reference [document](https://rook.io/docs/rook/v1.12/Getting-Started/ceph-teardown/#delete-the-data-on-hosts)

## Configurable options

```
# iserver set linux disk --mode zap
  --server TEXT  Linux server name
  --device TEXT  Block device name
  --no-confirm   Confirmation mode
```

### Zap all non-boot block devices on all nodes of selected cluster

```
# iserver set linux disk --server ocp:[cluster-name] --mode zap 
```

### Zap all non-boot block devices on selected cluster node

```
# iserver set linux disk --server ocp:[cluster-name]:[node-name] --mode zap 
```

### Zap selected block devices on selected cluster node

```
# iserver set linux disk --server ocp:[cluster-name]:[node-name] --device [device-name] --mode zap 
```

## Requirements

- cluster with [ssh access](../Access.md)

## Example

```
# iserver set linux disk --server ocp:bm1:bm1-1 --device sdb --mode zap

Linux - Disk - Zap
==================

Check ssh access
----------------
- ocp:bm3:bm3-1: ok

Server: ocp:bm3:bm3-1
---------------------

+----------+-------+------+---------+--------+------------------+--------------+-------+---------+--------------------------------------------+
| Path     | KName | Boot | Maj:Min | Size   | Model            | Serial       | Group | FS Type | Disk ID                                    |
+----------+-------+------+---------+--------+------------------+--------------+-------+---------+--------------------------------------------+
| /dev/sdb | sdb   |      | 8:16    | 894.3G | Micron_5100_MTFD | abc          | disk  | Ceph    | /dev/disk/by-path/pci-0000:00:11.5-ata-1.0 | 
|          |       |      |         |        |                  |              |       |         | /dev/disk/by-id/wwn-0x500a075118ef25c1     | 
+----------+-------+------+---------+--------+------------------+--------------+-------+---------+--------------------------------------------+

Zap device: /dev/sdb
Command: sudo sgdisk --zap-all /dev/sdb
~~~
Creating new GPT entries in memory.
GPT data structures destroyed! You may now partition the disk using fdisk or
other utilities.
 
~~~
Command: sudo blkdiscard -f  /dev/sdb
~~~
 blkdiscard: Operation forced, data will be lost!

~~~

+----------+-------+------+---------+--------+------------------+--------------+-------+---------+--------------------------------------------+
| Path     | KName | Boot | Maj:Min | Size   | Model            | Serial       | Group | FS Type | Disk ID                                    |
+----------+-------+------+---------+--------+------------------+--------------+-------+---------+--------------------------------------------+
| /dev/sdb | sdb   |      | 8:16    | 894.3G | Micron_5100_MTFD | abc          | disk  | ---     | /dev/disk/by-path/pci-0000:00:11.5-ata-1.0 | 
|          |       |      |         |        |                  |              |       |         | /dev/disk/by-id/wwn-0x500a075118ef25c1     | 
+----------+-------+------+---------+--------+------------------+--------------+-------+---------+--------------------------------------------+
```

[[Back]](./README.md)