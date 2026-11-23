# Storate Template

[[Next]](./TemplateThermal.md) [[Back]](./README.md)

```
# iserver.py get redfish template \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    -v storage

+----+-------------+------------------+------------------------------------------------------------------+-------------------+------------+----------+---------+--------+----------+--------------+----+----+
| ID | Controller  | Pid              | Model                                                            | Vendor            | Serial     | Firmware | State   | Health | PCI Slot | Raid Support | PD | VD |
+----+-------------+------------------+------------------------------------------------------------------+-------------------+------------+----------+---------+--------+----------+--------------+----+----+
| 1  | MRAID       | UCSC-RAID-M5     | Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) | Cisco Systems Inc | Serial123  | 1.1      | Enabled | OK     | MRAID    | RAID0        | 10 | 1  | 
|    |             |                  |                                                                  |                   |            |          |         |        |          | RAID1        |    |    | 
|    |             |                  |                                                                  |                   |            |          |         |        |          | RAID5        |    |    | 
|    |             |                  |                                                                  |                   |            |          |         |        |          | RAID6        |    |    | 
|    |             |                  |                                                                  |                   |            |          |         |        |          | RAID10       |    |    | 
|    |             |                  |                                                                  |                   |            |          |         |        |          | RAID50       |    |    | 
|    |             |                  |                                                                  |                   |            |          |         |        |          | RAID60       |    |    | 
+----+-------------+------------------+------------------------------------------------------------------+-------------------+------------+----------+---------+--------+----------+--------------+----+----+
| 2  | PCIe-Switch | PFX 48XG3        | NVME-MSWITCH                                                     | MICROSEM          | ---        | 1.1      | ---     | OK     | ---      | ---          | 0  | 0  | 
+----+-------------+------------------+------------------------------------------------------------------+-------------------+------------+----------+---------+--------+----------+--------------+----+----+

+----+------------+-------+------------+------------+------+----------+----------+------------+--------+---------------------------------------------+----------+----+-----------+
| ID | PhyDisk Id | State | Controller | Size       | Type | Protocol | Bootable | Link Speed | Pid    | Model                                       | Vendor   | Fw | Serial    |
+----+------------+-------+------------+------------+------+----------+----------+------------+--------+---------------------------------------------+----------+----+-----------+
| 1  | 9          | V     | MRAID      | 960.2 [GB] | SSD  | SATA     | X        | 6 gb/s     | UCS-SD | 960GB 2.5 inch Enterprise Value 6G SATA SSD | V1       | ab | Serial123 | 
| 2  | 10         | V     | MRAID      | 960.2 [GB] | SSD  | SATA     | X        | 6 gb/s     | UCS-SD | 960GB 2.5 inch Enterprise Value 6G SATA SSD | V1       | ab | Serial123 | 
| 3  | 11         | V     | MRAID      | 960.2 [GB] | SSD  | SATA     | X        | 6 gb/s     | UCS-SD | 960GB 2.5 inch Enterprise Value 6G SATA SSD | V1       | ab | Serial123 | 
| 4  | 12         | V     | MRAID      | 960.2 [GB] | SSD  | SATA     | X        | 6 gb/s     | UCS-SD | 960GB 2.5 inch Enterprise Value 6G SATA SSD | V1       | ab | Serial123 | 
| 5  | 13         | V     | MRAID      | 1.2 [TB]   | HDD  | SAS      | X        | 12 gb/s    | UCS-HD | 1.2TB 12G SAS 10K RPM SFF HDD               | V2       | ab | Serial123 | 
| 6  | 14         | V     | MRAID      | 1.2 [TB]   | HDD  | SAS      | X        | 12 gb/s    | UCS-HD | 1.2TB 12G SAS 10K RPM SFF HDD               | V2       | ab | Serial123 | 
| 7  | 15         | V     | MRAID      | 1.2 [TB]   | HDD  | SAS      | X        | 12 gb/s    | UCS-HD | 1.2TB 12G SAS 10K RPM SFF HDD               | V2       | ab | Serial123 | 
| 8  | 16         | V     | MRAID      | 1.2 [TB]   | HDD  | SAS      | X        | 12 gb/s    | UCS-HD | 1.2TB 12G SAS 10K RPM SFF HDD               | V2       | ab | Serial123 | 
| 9  | 17         | V     | MRAID      | 1.2 [TB]   | HDD  | SAS      | X        | 12 gb/s    | UCS-HD | 1.2TB 12G SAS 10K RPM SFF HDD               | V2       | ab | Serial123 | 
| 10 | 18         | V     | MRAID      | 1.2 [TB]   | HDD  | SAS      | X        | 12 gb/s    | UCS-HD | 1.2TB 12G SAS 10K RPM SFF HDD               | V3       | ab | Serial123 | 
+----+------------+-------+------------+------------+------+----------+----------+------------+--------+---------------------------------------------+----------+----+-----------+

+----+------------------+-------+------------+----------+-------+-------+------+----------+--------------+-------------------------+
| ID | Virtual Drive Id | State | Controller | Size     | Disks | Type  | Name | Bootable | Write Cache  | Raid SupportDrive State |
+----+------------------+-------+------------+----------+-------+-------+------+----------+--------------+-------------------------+
| 1  | 0                | V     | MRAID      | 1.2 [TB] | 2     | RAID1 | vd-0 | V        | WriteThrough | Optimal                 |
+----+------------------+-------+------------+----------+-------+-------+------+----------+--------------+-------------------------+

View: access, account, bios, cpu, fan, gpu, hw, identity (def), mem, net, pci, power, psu, role, storage, thermal, all
```

[[Back]](./README.md)