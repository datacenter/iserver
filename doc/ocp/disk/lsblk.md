# Block devices

[[Back]](./README.md)

## Workflow 

- `sudo lsblk -O --json` to get all block devices
- `sudo lsblk --discard --json` to get the TRIM support for blkdiscard ([zap](./zap.md))

## Configurable options

```
# iserver get linux lsblk
  --server TEXT                Linux server name
```

```
# iserver get linux lsblk --server ocp:[cluster-name]
```

```
# iserver get linux lsblk --server ocp:[cluster-name]:[node-name]
```

## Example

```
# iserver get linux lsblk --server ocp:bm1:bm1-1

Block Devices [ocp:bm1:bm1-1]
-----------------------------

+----+----------------+------+------+---------+--------+----------------------------------+------+--------------------------------------------------------+
| ID | Path           | Boot | Trim | Maj:Min | Size   | HW                               | FS   | Disk ID                                                |
+----+----------------+------+------+---------+--------+----------------------------------+------+--------------------------------------------------------+
| 1  | /dev/sda (sda) | V    | V    | 8:0     | 894.3G | UCSC-RAID12G-2GB                 | ---  | /dev/disk/by-path/pci-0000:00:11.5-ata-1.0             | 
|    |                |      |      |         |        | abc                              |      | /dev/disk/by-id/wwn-0x500a07511c54a9e9                 | 
+----+----------------+------+------+---------+--------+----------------------------------+------+--------------------------------------------------------+
| 2  | /dev/sdb (sdb) |      | V    | 8:16    | 894.3G | Micron_5100_MTFD                 | LVM2 | /dev/disk/by-path/pci-0000:00:11.5-ata-3.0             | 
|    |                |      |      |         |        | def                              |      | /dev/disk/by-id/wwn-0x500a07511c5401fc                 | 
+----+----------------+------+------+---------+--------+----------------------------------+------+--------------------------------------------------------+
| 3  | /dev/sdc (sdc) |      | X    | 8:32    | 894.3G | SSDSC2KB960G7K                   | Ceph | /dev/disk/by-path/pci-0000:18:00.0-scsi-0:0:9:0        | 
|    |                |      |      |         |        | xyz                              |      | /dev/disk/by-id/wwn-0x55cd2e414e3ba1bd                 | 
+----+----------------+------+------+---------+--------+----------------------------------+------+--------------------------------------------------------+
```

[[Back]](./README.md)