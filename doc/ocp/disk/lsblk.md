# Block devices

## Workflow 

- get block devices of OpenShift cluster nodes using Linux command: 'sudo lsblk -O --json'

## Configurable options

```
# iserver get linux lsblk
  --server TEXT                Linux server name
```

### Get block devices on all nodes of selected cluster

```
# iserver get linux lsblk --server ocp:[cluster-name]
```

### Get block devices on selected cluster node

```
# iserver get linux lsblk --server ocp:[cluster-name]:[node-name]
```

## Requirements

- cluster  with [ssh access](../Access.md)

## Example

```
# iserver get linux lsblk --server ocp:bm1:bm1-1

Block Devices [ocp:bm1:bm1-1]
-----------------------------

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

[[Back]](./README.md)