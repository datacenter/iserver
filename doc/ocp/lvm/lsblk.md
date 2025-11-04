# Block devices

```
# iserver get linux lsblk
Server [10.10.10.10]: 
Username [core]: 
Password: 
SSH Public Key [C:\Users\user\.ssh\id_ed25519.pub]: 
\
Block Devices [10.10.10.10]
---------------------------

+----------+-------+------+---------+--------+------------------+----------------------------------+-------+---------+-------------------------------------------------+
| Path     | KName | Boot | Maj:Min | Size   | Model            | Serial                           | Group | FS Type | Disk Path                                       |
+----------+-------+------+---------+--------+------------------+----------------------------------+-------+---------+-------------------------------------------------+
| /dev/sda | sda   |      | 8:0     | 1.1T   | UCSC-RAID12G-2GB | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx | disk  | LVM2    | /dev/disk/by-path/pci-0000:3c:00.0-scsi-0:2:1:0 |
| /dev/sdb | sdb   | ✓    | 8:16    | 1.1T   | UCSC-RAID12G-2GB | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx | disk  | ---     | /dev/disk/by-path/pci-0000:3c:00.0-scsi-0:2:0:0 | 
| /dev/sdg | sdg   |      | 8:96    | 894.3G | Micron_5100_MTFD | xxxxxxxxxxx                      | disk  | LVM2    | /dev/disk/by-path/pci-0000:00:11.5-ata-1.0      |
| /dev/sdh | sdh   |      | 8:112   | 894.3G | Micron_5100_MTFD | xxxxxxxxxxx                      | disk  | LVM2    | /dev/disk/by-path/pci-0000:00:11.5-ata-3.0      |
+----------+-------+------+---------+--------+------------------+----------------------------------+-------+---------+-------------------------------------------------+
```

[[Back]](./README.md)