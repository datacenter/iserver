# Logical Volume Manager

[[Back]](./README.md)

## Workflow

Collect all LVM related information
- Block devices: `sudo lsblk -O --json`
- Volume group: `sudo vgs --reportformat json -o all`
- Logical volume: `sudo lvs --reportformat json -o all`
- Physical volume: `sudo pvs --reportformat json`

## Example

```
# iserver get linux lvm --server ocp:bm1:bm1-1

Block Devices [ocp:bm1:bm1-1]
-----------------------------

+----------+-------+------+---------+--------+------------------+----------------------------------+-------+---------+-------------------------------------------------+
| Path     | KName | Boot | Maj:Min | Size   | Model            | Serial                           | Group | FS Type | Disk Path                                       |
+----------+-------+------+---------+--------+------------------+----------------------------------+-------+---------+-------------------------------------------------+
| /dev/sda | sda   |      | 8:0     | 1.1T   | UCSC-RAID12G-2GB | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx | disk  | LVM2    | /dev/disk/by-path/pci-0000:3c:00.0-scsi-0:2:1:0 | 
| /dev/sdb | sdb   | V    | 8:16    | 1.1T   | UCSC-RAID12G-2GB | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx | disk  | ---     | /dev/disk/by-path/pci-0000:3c:00.0-scsi-0:2:0:0 | 
| /dev/sdg | sdg   |      | 8:96    | 894.3G | Micron_5100_MTFD | xxxxxxxxxxx                      | disk  | LVM2    | /dev/disk/by-path/pci-0000:00:11.5-ata-1.0      |
| /dev/sdh | sdh   |      | 8:112   | 894.3G | Micron_5100_MTFD | xxxxxxxxxxx                      | disk  | LVM2    | /dev/disk/by-path/pci-0000:00:11.5-ata-3.0      |
+----------+-------+------+---------+--------+------------------+----------------------------------+-------+---------+-------------------------------------------------+

Physical Volume (LVM) [ocp:bm1:bm1-1]
-------------------------------------

+----------+-----+------+------+---------+---------+
| PV       | VG  | Fmt  | Attr | PSize   | PFree   |
+----------+-----+------+------+---------+---------+
| /dev/sda | vg1 | lvm2 | a--  | 1.09t   | 0       |
| /dev/sdg | vg1 | lvm2 | a--  | 894.25g | 200.31g |
| /dev/sdh | vg1 | lvm2 | a--  | 894.25g | 87.64g  |
+----------+-----+------+------+---------+---------+

Volume Groups (LVM) [ocp:bm1:bm1-1]
-----------------------------------

+-----+-----+-----+--------+--------+----------+
| VG  | #PV | #LV | Attr   | VSize  | VFree    |
+-----+-----+-----+--------+--------+----------+
| vg1 | 3   | 2   | wz--n- | <2.84t | <287.96g |
+-----+-----+-----+--------+--------+----------+

Logical Volumes (LVM) [ocp:bm1:bm1-1]
-------------------------------------

+--------------------------------------+-----+-------------+-------+---------+-------+--------+---------+------+-----------+
| LV Name                              | VG  | LV Pool     | Dev   | LV Size | MSize | Layout | Role    | Snap | K8s Usage |
+--------------------------------------+-----+-------------+-------+---------+-------+--------+---------+------+-----------+
| 868c9f34-afa2-4c68-a932-d5e0a3c0a812 | vg1 | thin-pool-1 | 253:4 | 1.00g   | 0.00% | thin   | public  | --   | --        |
|                                      |     |             |       |         |       | sparse |         |      |           |
+--------------------------------------+-----+-------------+-------+---------+-------+--------+---------+------+-----------+
| thin-pool-1                          | vg1 |             | 253:2 | 2.55t   | 0.00% | thin   | private | --   | N/A       |
|                                      |     |             |       |         |       | pool   |         |      |           |
+--------------------------------------+-----+-------------+-------+---------+-------+--------+---------+------+-----------+
```

[[Back]](./README.md)