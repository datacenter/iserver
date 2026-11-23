# Intersight Fabric Interconnect - Inventory view

[[Back]](./FiInventory.md)

> [!NOTE]
> inventory output to csv file requires `-v inv` and `--csv filename` options

```
# iserver get fi --name fi1* -v inv

Fabric Interconnect: fi1 FI-A [ID:A]
------------------------------------

+----+-------+----------------------+-----------------+---------------------+-------------+-----------------+
| ID | Type  | Name                 | Model           | Vendor              | Serial      | Pid             |
+----+-------+----------------------+-----------------+---------------------+-------------+-----------------+
| 1  | FI    | Chassis              | UCS-FI-6454     | Cisco Systems, Inc. | Serial123   | UCS-FI-6454     |
| 2  | Fan   | Fan Module 1 - Fan 1 | CISCO-FAN-12345 | Cisco Systems, Inc. | N/A         | CISCO-FAN-12345 |
| 3  | Fan   | Fan Module 1 - Fan 2 | CISCO-FAN-12345 | Cisco Systems, Inc. | N/A         | CISCO-FAN-12345 |
| 4  | Fan   | Fan Module 2 - Fan 1 | CISCO-FAN-12345 | Cisco Systems, Inc. | N/A         | CISCO-FAN-12345 |
| 5  | Fan   | Fan Module 2 - Fan 2 | CISCO-FAN-12345 | Cisco Systems, Inc. | N/A         | CISCO-FAN-12345 | 
| 6  | Fan   | Fan Module 3 - Fan 1 | CISCO-FAN-12345 | Cisco Systems, Inc. | N/A         | CISCO-FAN-12345 |
| 7  | Fan   | Fan Module 3 - Fan 2 | CISCO-FAN-12345 | Cisco Systems, Inc. | N/A         | CISCO-FAN-12345 |
| 8  | Fan   | Fan Module 4 - Fan 1 | CISCO-FAN-12345 | Cisco Systems, Inc. | N/A         | CISCO-FAN-12345 |
| 9  | Fan   | Fan Module 4 - Fan 2 | CISCO-FAN-12345 | Cisco Systems, Inc. | N/A         | CISCO-FAN-12345 |
| 10 | PSU   | PSU #1               | UCS-PSU-123     | Cisco Systems, Inc. | Serial456   | UCS-PSU-123     |
| 11 | PSU   | PSU #2               | UCS-PSU-123     | Cisco Systems, Inc. | Serial789   | UCS-PSU-123     |
+----+-------+----------------------+-----------------+---------------------+-------------+-----------------+

Filter: name, serial, model
View:   state (def), eth, pc, fc, fpc, fanm, fan, psu, storage, inv, all
```

[[Back]](./FiInventory.md)