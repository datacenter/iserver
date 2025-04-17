# Intersight Server

## Filter by storage controller

Examples

```
--sc vendor:lsi
--sc serial:myserial
```

## Serial

```
# iserver get server
    --sc serial:SK00188839 -v sc

iaccount demo (cache: any)
Select servers...
Selected servers: 121
Collect server api objects...


Storage Controller [#1]
-----------------------

+------------+----------------------------+-----------+--------+----------+----------+--------------+----+----+
| Controller | Model                      | Vendor    | Serial | Presence | PCI Slot | Raid Support | PD | VD |
+------------+----------------------------+-----------+--------+----------+----------+--------------+----+----+
| MRAID      | Cisco 12G Modular Raid     | LSI Logic | SN-68  | equipped | MRAID    | yes          | 10 | 1  |
|            | Controller with 2GB cache  |           |        |          |          |              |    |    |
|            | (max 16 drives)            |           |        |          |          |              |    |    |
+------------+----------------------------+-----------+--------+----------+----------+--------------+----+----+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

## Vendor

```
# iserver get server --sc vendor:lsi -v sc

iaccount demo (cache: any)
Select servers...
Selected servers: 121
Collect server api objects...


Storage Controller [#91]
------------------------

+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server    | Controller | Model                          | Vendor    | Serial | Presence | PCI Slot | Raid Support | PD | VD |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server282 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-57  | equipped | MRAID    | yes          | 4  | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server502 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-90  | equipped | MRAID    | yes          | 4  | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server615 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-51  | equipped | MRAID    | yes          | 4  | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server977 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-58  | equipped | MRAID    | yes          | 8  | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server406 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-66  | equipped | MRAID    | yes          | 8  | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server769 | SLOT-HBA   | Cisco 12G SAS Modular Raid     | LSI Logic | SN-95  | equipped | SLOT-HBA | yes          | 2  | 1  |
|           |            | Controller                     |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server493 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-75  | equipped | MRAID    | yes          | 7  | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server399 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-29  | equipped | MRAID    | yes          | 7  | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server274 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-49  | equipped | MRAID    | yes          | 7  | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server443 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-34  | equipped | MRAID    | yes          | 5  | 0  |
|           |            | Controller with 4GB cache      |           |        |          |          |              |    |    |
|           |            | (max 26 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server592 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-14  | equipped | MRAID    | yes          | 3  | 2  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server386 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-42  | equipped | MRAID    | yes          | 3  | 2  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server378 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-17  | equipped | MRAID    | yes          | 3  | 2  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server850 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-44  | equipped | MRAID    | yes          | 3  | 2  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server957 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-49  | equipped | MRAID    | yes          | 3  | 2  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server584 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-91  | equipped | MRAID    | yes          | 3  | 2  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server576 | SLOT-HBA   | Cisco 12G SAS Modular Raid     | LSI Logic | SN-30  | equipped | SLOT-HBA | yes          | 2  | 1  |
|           |            | Controller                     |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server227 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-25  | equipped | MRAID    | yes          | 8  | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server287 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-17  | equipped | MRAID    | yes          | 5  | 1  |
|           |            | Controller with 4GB cache      |           |        |          |          |              |    |    |
|           |            | (max 26 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server134 | RAID       | Cisco 12G Modular Raid         | LSI Logic | SN-18  | equipped | RAID     | yes          | 3  | 1  |
|           |            | Controller with 4GB cache      |           |        |          |          |              |    |    |
|           |            | (max 26 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server175 | SLOT-HBA   | Cisco 12G SAS Modular Raid     | LSI Logic | SN-89  | equipped | SLOT-HBA | yes          | 2  | 1  |
|           |            | Controller                     |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server952 | SLOT-HBA   | Cisco 12G SAS Modular Raid     | LSI Logic | SN-69  | equipped | SLOT-HBA | yes          | 2  | 1  |
|           |            | Controller                     |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server605 | SLOT-HBA   | Cisco 12G SAS Modular Raid     | LSI Logic | SN-77  | equipped | SLOT-HBA | yes          | 2  | 2  |
|           |            | Controller                     |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server933 | SLOT-HBA   | Cisco 12G SAS Modular Raid     | LSI Logic | SN-35  | equipped | SLOT-HBA | yes          | 2  | 1  |
|           |            | Controller                     |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server716 | SLOT-HBA   | Cisco 12G SAS Modular Raid     | LSI Logic | SN-72  | equipped | SLOT-HBA | yes          | 2  | 1  |
|           |            | Controller                     |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server912 | SLOT-HBA   | Cisco 12G SAS Modular Raid     | LSI Logic | SN-27  | equipped | SLOT-HBA | yes          | 2  | 1  |
|           |            | Controller                     |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server907 | SLOT-HBA   | Cisco 12G SAS Modular Raid     | LSI Logic | SN-14  | equipped | SLOT-HBA | yes          | 2  | 1  |
|           |            | Controller                     |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server113 | SLOT-HBA   | Cisco 12G SAS Modular Raid     | LSI Logic | SN-15  | equipped | SLOT-HBA | yes          | 2  | 1  |
|           |            | Controller                     |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server385 | SLOT-HBA   | Cisco 12G SAS Modular Raid     | LSI Logic | SN-92  | equipped | SLOT-HBA | yes          | 2  | 1  |
|           |            | Controller                     |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server437 | SLOT-HBA   | Cisco 12G SAS Modular Raid     | LSI Logic | SN-63  | equipped | SLOT-HBA | yes          | 2  | 1  |
|           |            | Controller                     |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server682 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-68  | equipped | MRAID    | yes          | 10 | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server351 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-83  | equipped | MRAID    | yes          | 10 | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server293 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-85  | equipped | MRAID    | yes          | 10 | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server116 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-83  | equipped | MRAID    | yes          | 2  | 2  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server484 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-26  | equipped | MRAID    | yes          | 2  | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server187 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-36  | equipped | MRAID    | yes          | 2  | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server968 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-72  | equipped | MRAID    | yes          | 2  | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server102 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-36  | equipped | MRAID    | yes          | 7  | 1  |
|           |            | Controller with 4GB cache      |           |        |          |          |              |    |    |
|           |            | (max 26 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server876 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-83  | equipped | MRAID    | yes          | 2  | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server410 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-83  | equipped | MRAID    | yes          | 2  | 1  |
|           |            | Controller with 4GB cache      |           |        |          |          |              |    |    |
|           |            | (max 26 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server598 | SLOT-HBA   | Cisco 12G SAS Modular Raid     | LSI Logic | SN-91  | equipped | SLOT-HBA | yes          | 7  | 1  |
|           |            | Controller                     |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server251 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-49  | equipped | MRAID    | yes          | 2  | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server749 | MRAID1     | Cisco 12G SAS RAID Controller  | LSI Logic | SN-35  | equipped | MRAID1   | yes          | 4  | 0  |
|           |            | with 4GB FBWC (28 Drives)      |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server280 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-57  | equipped | MRAID    | yes          | 2  | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server950 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-34  | equipped | MRAID    | yes          | 6  | 1  |
|           |            | Controller with 4GB cache      |           |        |          |          |              |    |    |
|           |            | (max 26 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server397 | SLOT-HBA   | Cisco 12G SAS Modular Raid     | LSI Logic | SN-30  | equipped | SLOT-HBA | yes          | 7  | 1  |
|           |            | Controller                     |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server813 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-96  | equipped | MRAID    | yes          | 2  | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server820 | MRAID1     | Cisco 12G SAS RAID Controller  | LSI Logic | SN-51  | equipped | MRAID1   | yes          | 4  | 0  |
|           |            | with 4GB FBWC (28 Drives)      |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server141 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-95  | equipped | MRAID    | yes          | 2  | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server897 | SLOT-HBA   | Cisco 12G SAS Modular Raid     | LSI Logic | SN-87  | equipped | SLOT-HBA | yes          | 7  | 1  |
|           |            | Controller                     |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server679 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-50  | equipped | MRAID    | yes          | 2  | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server751 | MRAID      | Cisco 12G SAS RAID Controller  | LSI Logic | SN-19  | equipped | MRAID    | yes          | 4  | 0  |
|           |            | with 4GB FBWC (16 Drives)      |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server541 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-72  | equipped | MRAID    | yes          | 2  | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server292 | SLOT-HBA   | Cisco 12G SAS Modular Raid     | LSI Logic | SN-60  | equipped | SLOT-HBA | yes          | 2  | 1  |
|           |            | Controller                     |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server634 | MRAID      | Cisco 12G SAS RAID Controller  | LSI Logic | SN-67  | equipped | MRAID    | yes          | 4  | 0  |
|           |            | with 4GB FBWC (16 Drives)      |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server949 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-47  | equipped | MRAID    | yes          | 2  | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server536 | SLOT-HBA   | Cisco 12G SAS Modular Raid     | LSI Logic | SN-58  | equipped | SLOT-HBA | yes          | 2  | 1  |
|           |            | Controller                     |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server378 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-31  | equipped | MRAID    | yes          | 2  | 1  |
|           |            | Controller with 4GB cache      |           |        |          |          |              |    |    |
|           |            | (max 26 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server840 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-29  | equipped | MRAID    | yes          | 2  | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server256 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-18  | equipped | MRAID    | yes          | 4  | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server403 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-92  | equipped | MRAID    | yes          | 4  | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server116 | SLOT-HBA   | Cisco 12G SAS Modular Raid     | LSI Logic | SN-92  | equipped | SLOT-HBA | yes          | 2  | 1  |
|           |            | Controller                     |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server389 | SLOT-HBA   | Cisco 12G SAS Modular Raid     | LSI Logic | SN-20  | equipped | SLOT-HBA | yes          | 2  | 1  |
|           |            | Controller                     |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server792 | SLOT-HBA   | Cisco 12G SAS Modular Raid     | LSI Logic | SN-41  | equipped | SLOT-HBA | yes          | 2  | 1  |
|           |            | Controller                     |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server899 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-18  | equipped | MRAID    | yes          | 2  | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server883 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-87  | equipped | MRAID    | yes          | 2  | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server680 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-12  | equipped | MRAID    | yes          | 3  | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server632 | SLOT-HBA   | Cisco 12G SAS Modular Raid     | LSI Logic | SN-84  | equipped | SLOT-HBA | yes          | 8  | 2  |
|           |            | Controller                     |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server347 | SLOT-HBA   | Cisco 12G SAS Modular Raid     | LSI Logic | SN-81  | equipped | SLOT-HBA | yes          | 8  | 2  |
|           |            | Controller                     |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server232 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-39  | equipped | MRAID    | yes          | 4  | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server874 | SLOT-HBA   | Cisco 12G SAS Modular Raid     | LSI Logic | SN-28  | equipped | SLOT-HBA | yes          | 2  | 1  |
|           |            | Controller                     |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server100 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-92  | equipped | MRAID    | yes          | 24 | 1  |
|           |            | Controller with 4GB cache      |           |        |          |          |              |    |    |
|           |            | (max 26 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server990 | SLOT-HBA   | Cisco 12G SAS Modular Raid     | LSI Logic | SN-85  | equipped | SLOT-HBA | yes          | 2  | 1  |
|           |            | Controller                     |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server926 | SLOT-HBA   | Cisco 12G SAS Modular Raid     | LSI Logic | SN-46  | equipped | SLOT-HBA | yes          | 2  | 1  |
|           |            | Controller                     |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server523 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-76  | equipped | MRAID    | yes          | 8  | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server861 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-97  | equipped | MRAID    | yes          | 8  | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server697 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-66  | equipped | MRAID    | yes          | 5  | 5  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server403 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-65  | equipped | MRAID    | yes          | 5  | 5  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server221 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-13  | equipped | MRAID    | yes          | 6  | 6  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server296 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-17  | equipped | MRAID    | yes          | 11 | 0  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server525 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-63  | equipped | MRAID    | yes          | 8  | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server302 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-60  | equipped | MRAID    | yes          | 11 | 1  |
|           |            | Controller with 2GB cache      |           |        |          |          |              |    |    |
|           |            | (max 16 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server821 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-11  | equipped | MRAID    | yes          | 20 | 1  |
|           |            | Controller with 4GB cache      |           |        |          |          |              |    |    |
|           |            | (max 26 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server101 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-18  | equipped | MRAID    | yes          | 23 | 1  |
|           |            | Controller with 4GB cache      |           |        |          |          |              |    |    |
|           |            | (max 26 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server189 | SLOT-HBA   | Cisco 12G SAS Modular Raid     | LSI Logic | SN-23  | equipped | SLOT-HBA | yes          | 5  | 2  |
|           |            | Controller                     |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server250 | SLOT-HBA   | Cisco 12G SAS Modular Raid     | LSI Logic | SN-61  | equipped | SLOT-HBA | yes          | 5  | 2  |
|           |            | Controller                     |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server849 | SLOT-HBA   | Cisco 12G SAS Modular Raid     | LSI Logic | SN-71  | equipped | SLOT-HBA | yes          | 5  | 2  |
|           |            | Controller                     |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server265 | SLOT-HBA   | Cisco 12G SAS Modular Raid     | LSI Logic | SN-31  | equipped | SLOT-HBA | yes          | 5  | 2  |
|           |            | Controller                     |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server474 | SLOT-HBA   | Cisco 12G Modular SAS Pass     | LSI Logic | SN-22  | equipped | SLOT-HBA | no           | 23 | 0  |
|           |            | through Controller             |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server934 | SBMezz1    | Cisco UCS C3000 RAID           | LSI Logic | SN-98  | equipped | SBMezz1  | yes          | 0  | 1  |
|           |            | Controller for M4 Server       |           |        |          |          |              |    |    |
|           |            | Blade with 4G RAID Cache       |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+
| Server316 | MRAID      | Cisco 12G Modular Raid         | LSI Logic | SN-13  | equipped | MRAID    | yes          | 26 | 1  |
|           |            | Controller with 4GB cache      |           |        |          |          |              |    |    |
|           |            | (max 26 drives)                |           |        |          |          |              |    |    |
+-----------+------------+--------------------------------+-----------+--------+----------+----------+--------------+----+----+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)