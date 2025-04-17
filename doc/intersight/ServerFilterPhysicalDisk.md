# Intersight Server

## Filter by physical disk

Examples

```
--pd count:le2
--pd type:ssd
--pd proto:sata
--pd pid:UCS-SD960G6I1X-EV
--pd model:ST1200MM0009
--pd vendor:ata
--pd serial:myserial
```

## Count

```
# iserver get server
    --group test
    --pd count:le2 -v pd
    --iaccount demo
    --ttl 0
    --anonymize

iaccount demo (cache: any)
Select servers...
Selected servers: 8
Collect server api objects...


Physical Disk - State [#8]
--------------------------

+-----------+-------+------------+---------+----+------------+------+----------+----------+------------+---------+--------+----------+
| Server    | State | Controller | Disk Id | VD | Size       | Type | Protocol | Bootable | Link Speed | Fw      | State  | Presence |
+-----------+-------+------------+---------+----+------------+------+----------+----------+------------+---------+--------+----------+
| Server850 | V     | 1          | 1       | -- | 299.0 [GB] | HDD  | SAS      | X        | 12-gbps    | 1.0(1a) | online | equipped | 
| Server850 | V     | 1          | 2       | -- | 299.0 [GB] | HDD  | SAS      | X        | 12-gbps    | 1.0(1a) | online | equipped | 
| Server389 | V     | 1          | 1       | -- | 299.0 [GB] | HDD  | SAS      | X        | 12-gbps    | 1.0(1a) | online | equipped | 
| Server389 | V     | 1          | 2       | -- | 299.0 [GB] | HDD  | SAS      | X        | 12-gbps    | 1.0(1a) | online | equipped | 
| Server256 | V     | 1          | 1       | -- | 299.0 [GB] | HDD  | SAS      | X        | 12-gbps    | 1.0(1a) | online | equipped | 
| Server256 | V     | 1          | 2       | -- | 299.0 [GB] | HDD  | SAS      | X        | 12-gbps    | 1.0(1a) | online | equipped | 
| Server838 | V     | 1          | 1       | -- | 299.0 [GB] | HDD  | SAS      | X        | 12-gbps    | 1.0(1a) | online | equipped | 
| Server838 | V     | 1          | 2       | -- | 299.0 [GB] | HDD  | SAS      | X        | 12-gbps    | 1.0(1a) | online | equipped | 
+-----------+-------+------------+---------+----+------------+------+----------+----------+------------+---------+--------+----------+

Physical Disk - Inventory [#8]
------------------------------

+-----------+---------+--------+-----------+-------+---------+--------+
| Server    | Disk Id | Pid    | Model     | PN    | Vendor  | Serial |
+-----------+---------+--------+-----------+-------+---------+--------+
| Server850 | 1       | PID-29 | Model-XYZ | PN-49 | SEAGATE | SN-91  | 
| Server850 | 2       | PID-34 | Model-XYZ | PN-76 | SEAGATE | SN-13  | 
| Server389 | 1       | PID-23 | Model-XYZ | PN-49 | SEAGATE | SN-48  | 
| Server389 | 2       | PID-99 | Model-XYZ | PN-64 | SEAGATE | SN-32  | 
| Server256 | 1       | PID-13 | Model-XYZ | PN-38 | SEAGATE | SN-32  | 
| Server256 | 2       | PID-96 | Model-XYZ | PN-14 | SEAGATE | SN-28  | 
| Server838 | 1       | PID-55 | Model-XYZ | PN-92 | SEAGATE | SN-32  | 
| Server838 | 2       | PID-36 | Model-XYZ | PN-49 | SEAGATE | SN-83  | 
+-----------+---------+--------+-----------+-------+---------+--------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

## Type

```
# iserver get server
    --group test
    --pd type:ssd -v pd
    --iaccount demo
    --ttl 0
    --anonymize

iaccount demo (cache: any)
Select servers...
Selected servers: 8
Collect server api objects...


Physical Disk - State [#18]
---------------------------

+-----------+-------+------------+---------+----+-------------+------+----------+----------+------------+---------+-------+----------+
| Server    | State | Controller | Disk Id | VD | Size        | Type | Protocol | Bootable | Link Speed | Fw      | State | Presence |
+-----------+-------+------------+---------+----+-------------+------+----------+----------+------------+---------+-------+----------+
| Server412 | V     | MRAID      | 9       | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server412 | V     | MRAID      | 10      | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server412 | V     | MRAID      | 11      | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server412 | V     | MRAID      | 12      | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server214 | V     | MRAID      | 9       | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server214 | V     | MRAID      | 10      | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server214 | V     | MRAID      | 11      | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server214 | V     | MRAID      | 12      | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server943 | V     | MRAID      | 9       | 0  | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server943 | V     | MRAID      | 10      | 0  | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server943 | V     | MRAID      | 11      | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server943 | V     | MRAID      | 12      | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server820 | V     | MRAID      | 1       | -- | 1.92 [TB]   | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server820 | V     | MRAID      | 2       | -- | 1.92 [TB]   | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server820 | V     | MRAID      | 3       | -- | 1.92 [TB]   | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server820 | V     | MRAID      | 4       | -- | 1.92 [TB]   | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server820 | V     | MSTOR-RAID | 253     | 0  | 240.06 [GB] | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server820 | V     | MSTOR-RAID | 254     | 0  | 240.06 [GB] | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
+-----------+-------+------------+---------+----+-------------+------+----------+----------+------------+---------+-------+----------+

Physical Disk - Inventory [#18]
-------------------------------

+-----------+---------+--------+-----------+-------+--------+--------+
| Server    | Disk Id | Pid    | Model     | PN    | Vendor | Serial |
+-----------+---------+--------+-----------+-------+--------+--------+
| Server412 | 9       | PID-82 | Model-XYZ | PN-12 | ATA    | SN-21  | 
| Server412 | 10      | PID-46 | Model-XYZ | PN-91 | ATA    | SN-58  | 
| Server412 | 11      | PID-40 | Model-XYZ | PN-40 | ATA    | SN-44  | 
| Server412 | 12      | PID-79 | Model-XYZ | PN-69 | ATA    | SN-59  | 
| Server214 | 9       | PID-70 | Model-XYZ | PN-29 | ATA    | SN-72  | 
| Server214 | 10      | PID-40 | Model-XYZ | PN-94 | ATA    | SN-93  | 
| Server214 | 11      | PID-76 | Model-XYZ | PN-17 | ATA    | SN-25  | 
| Server214 | 12      | PID-89 | Model-XYZ | PN-95 | ATA    | SN-43  | 
| Server943 | 9       | PID-38 | Model-XYZ | PN-36 | ATA    | SN-43  | 
| Server943 | 10      | PID-55 | Model-XYZ | PN-21 | ATA    | SN-83  | 
| Server943 | 11      | PID-78 | Model-XYZ | PN-93 | ATA    | SN-37  | 
| Server943 | 12      | PID-81 | Model-XYZ | PN-58 | ATA    | SN-28  | 
| Server820 | 1       | PID-58 | Model-XYZ | PN-58 | ATA    | SN-14  | 
| Server820 | 2       | PID-83 | Model-XYZ | PN-60 | ATA    | SN-53  | 
| Server820 | 3       | PID-44 | Model-XYZ | PN-63 | ATA    | SN-37  | 
| Server820 | 4       | PID-52 | Model-XYZ | PN-62 | ATA    | SN-88  | 
| Server820 | 253     | PID-28 | Model-XYZ | PN-77 | ATA    | SN-97  | 
| Server820 | 254     | PID-52 | Model-XYZ | PN-75 | ATA    | SN-11  | 
+-----------+---------+--------+-----------+-------+--------+--------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

## Proto

```
# iserver get server
    --group test
    --pd proto:sas -v pd
    --iaccount demo
    --ttl 0
    --anonymize

iaccount demo (cache: any)
Select servers...
Selected servers: 8
Collect server api objects...


Physical Disk - State [#26]
---------------------------

+-----------+-------+------------+---------+----+------------+------+----------+----------+------------+---------+--------+----------+
| Server    | State | Controller | Disk Id | VD | Size       | Type | Protocol | Bootable | Link Speed | Fw      | State  | Presence |
+-----------+-------+------------+---------+----+------------+------+----------+----------+------------+---------+--------+----------+
| Server707 | V     | MRAID      | 13      | -- | 1.2 [TB]   | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped | 
| Server707 | V     | MRAID      | 14      | -- | 1.2 [TB]   | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped | 
| Server707 | V     | MRAID      | 15      | -- | 1.2 [TB]   | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped | 
| Server707 | V     | MRAID      | 16      | -- | 1.2 [TB]   | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped | 
| Server707 | V     | MRAID      | 17      | 0  | 1.2 [TB]   | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped | 
| Server707 | V     | MRAID      | 18      | 0  | 1.2 [TB]   | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped | 
| Server217 | V     | MRAID      | 13      | -- | 1.2 [TB]   | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped | 
| Server217 | V     | MRAID      | 14      | -- | 1.2 [TB]   | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped | 
| Server217 | V     | MRAID      | 15      | -- | 1.2 [TB]   | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped | 
| Server217 | V     | MRAID      | 16      | -- | 1.2 [TB]   | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped | 
| Server217 | V     | MRAID      | 17      | 0  | 1.2 [TB]   | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped | 
| Server217 | V     | MRAID      | 18      | 0  | 1.2 [TB]   | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped | 
| Server607 | V     | MRAID      | 13      | -- | 1.2 [TB]   | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped | 
| Server607 | V     | MRAID      | 14      | -- | 1.2 [TB]   | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped | 
| Server607 | V     | MRAID      | 15      | -- | 1.2 [TB]   | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped | 
| Server607 | V     | MRAID      | 16      | -- | 1.2 [TB]   | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped | 
| Server607 | V     | MRAID      | 17      | -- | 1.2 [TB]   | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped | 
| Server607 | V     | MRAID      | 18      | -- | 1.2 [TB]   | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped | 
| Server115 | V     | 1          | 1       | -- | 299.0 [GB] | HDD  | SAS      | X        | 12-gbps    | 1.0(1a) | online | equipped | 
| Server115 | V     | 1          | 2       | -- | 299.0 [GB] | HDD  | SAS      | X        | 12-gbps    | 1.0(1a) | online | equipped | 
| Server282 | V     | 1          | 1       | -- | 299.0 [GB] | HDD  | SAS      | X        | 12-gbps    | 1.0(1a) | online | equipped | 
| Server282 | V     | 1          | 2       | -- | 299.0 [GB] | HDD  | SAS      | X        | 12-gbps    | 1.0(1a) | online | equipped | 
| Server786 | V     | 1          | 1       | -- | 299.0 [GB] | HDD  | SAS      | X        | 12-gbps    | 1.0(1a) | online | equipped | 
| Server786 | V     | 1          | 2       | -- | 299.0 [GB] | HDD  | SAS      | X        | 12-gbps    | 1.0(1a) | online | equipped | 
| Server448 | V     | 1          | 1       | -- | 299.0 [GB] | HDD  | SAS      | X        | 12-gbps    | 1.0(1a) | online | equipped | 
| Server448 | V     | 1          | 2       | -- | 299.0 [GB] | HDD  | SAS      | X        | 12-gbps    | 1.0(1a) | online | equipped | 
+-----------+-------+------------+---------+----+------------+------+----------+----------+------------+---------+--------+----------+

Physical Disk - Inventory [#26]
-------------------------------

+-----------+---------+--------+-----------+-------+---------+--------+
| Server    | Disk Id | Pid    | Model     | PN    | Vendor  | Serial |
+-----------+---------+--------+-----------+-------+---------+--------+
| Server707 | 13      | PID-80 | Model-XYZ | PN-31 | SEAGATE | SN-79  | 
| Server707 | 14      | PID-21 | Model-XYZ | PN-91 | SEAGATE | SN-12  | 
| Server707 | 15      | PID-72 | Model-XYZ | PN-87 | SEAGATE | SN-66  | 
| Server707 | 16      | PID-34 | Model-XYZ | PN-84 | SEAGATE | SN-37  | 
| Server707 | 17      | PID-40 | Model-XYZ | PN-76 | SEAGATE | SN-85  | 
| Server707 | 18      | PID-35 | Model-XYZ | PN-45 | TOSHIBA | SN-33  | 
| Server217 | 13      | PID-49 | Model-XYZ | PN-52 | SEAGATE | SN-47  | 
| Server217 | 14      | PID-70 | Model-XYZ | PN-12 | SEAGATE | SN-71  | 
| Server217 | 15      | PID-72 | Model-XYZ | PN-52 | SEAGATE | SN-36  | 
| Server217 | 16      | PID-82 | Model-XYZ | PN-14 | SEAGATE | SN-89  | 
| Server217 | 17      | PID-72 | Model-XYZ | PN-51 | SEAGATE | SN-60  | 
| Server217 | 18      | PID-65 | Model-XYZ | PN-18 | SEAGATE | SN-17  | 
| Server607 | 13      | PID-17 | Model-XYZ | PN-35 | SEAGATE | SN-50  | 
| Server607 | 14      | PID-57 | Model-XYZ | PN-27 | SEAGATE | SN-84  | 
| Server607 | 15      | PID-24 | Model-XYZ | PN-89 | SEAGATE | SN-17  | 
| Server607 | 16      | PID-41 | Model-XYZ | PN-48 | SEAGATE | SN-45  | 
| Server607 | 17      | PID-40 | Model-XYZ | PN-38 | SEAGATE | SN-15  | 
| Server607 | 18      | PID-83 | Model-XYZ | PN-80 | TOSHIBA | SN-95  | 
| Server115 | 1       | PID-80 | Model-XYZ | PN-23 | SEAGATE | SN-38  | 
| Server115 | 2       | PID-12 | Model-XYZ | PN-42 | SEAGATE | SN-78  | 
| Server282 | 1       | PID-73 | Model-XYZ | PN-87 | SEAGATE | SN-70  | 
| Server282 | 2       | PID-26 | Model-XYZ | PN-17 | SEAGATE | SN-55  | 
| Server786 | 1       | PID-52 | Model-XYZ | PN-17 | SEAGATE | SN-10  | 
| Server786 | 2       | PID-41 | Model-XYZ | PN-39 | SEAGATE | SN-81  | 
| Server448 | 1       | PID-87 | Model-XYZ | PN-57 | SEAGATE | SN-15  | 
| Server448 | 2       | PID-55 | Model-XYZ | PN-51 | SEAGATE | SN-76  | 
+-----------+---------+--------+-----------+-------+---------+--------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

## PID

```
# iserver get server
    --group test
    --pd pid:SD960G6I1X -v pd
    --iaccount demo
    --ttl 0
    --anonymize

iaccount demo (cache: any)
Select servers...
Selected servers: 8
Collect server api objects...


Physical Disk - State [#12]
---------------------------

+-----------+-------+------------+---------+----+------------+------+----------+----------+------------+---------+-------+----------+
| Server    | State | Controller | Disk Id | VD | Size       | Type | Protocol | Bootable | Link Speed | Fw      | State | Presence |
+-----------+-------+------------+---------+----+------------+------+----------+----------+------------+---------+-------+----------+
| Server104 | V     | MRAID      | 9       | -- | 959.0 [GB] | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server104 | V     | MRAID      | 10      | -- | 959.0 [GB] | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server104 | V     | MRAID      | 11      | -- | 959.0 [GB] | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server104 | V     | MRAID      | 12      | -- | 959.0 [GB] | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server189 | V     | MRAID      | 9       | -- | 959.0 [GB] | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server189 | V     | MRAID      | 10      | -- | 959.0 [GB] | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server189 | V     | MRAID      | 11      | -- | 959.0 [GB] | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server189 | V     | MRAID      | 12      | -- | 959.0 [GB] | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server357 | V     | MRAID      | 9       | 0  | 959.0 [GB] | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server357 | V     | MRAID      | 10      | 0  | 959.0 [GB] | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server357 | V     | MRAID      | 11      | -- | 959.0 [GB] | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server357 | V     | MRAID      | 12      | -- | 959.0 [GB] | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
+-----------+-------+------------+---------+----+------------+------+----------+----------+------------+---------+-------+----------+

Physical Disk - Inventory [#12]
-------------------------------

+-----------+---------+--------+-----------+-------+--------+--------+
| Server    | Disk Id | Pid    | Model     | PN    | Vendor | Serial |
+-----------+---------+--------+-----------+-------+--------+--------+
| Server104 | 9       | PID-56 | Model-XYZ | PN-67 | ATA    | SN-75  | 
| Server104 | 10      | PID-31 | Model-XYZ | PN-16 | ATA    | SN-57  | 
| Server104 | 11      | PID-91 | Model-XYZ | PN-52 | ATA    | SN-59  | 
| Server104 | 12      | PID-41 | Model-XYZ | PN-43 | ATA    | SN-85  | 
| Server189 | 9       | PID-83 | Model-XYZ | PN-91 | ATA    | SN-92  | 
| Server189 | 10      | PID-16 | Model-XYZ | PN-99 | ATA    | SN-94  | 
| Server189 | 11      | PID-96 | Model-XYZ | PN-99 | ATA    | SN-59  | 
| Server189 | 12      | PID-46 | Model-XYZ | PN-14 | ATA    | SN-54  | 
| Server357 | 9       | PID-23 | Model-XYZ | PN-78 | ATA    | SN-56  | 
| Server357 | 10      | PID-86 | Model-XYZ | PN-99 | ATA    | SN-77  | 
| Server357 | 11      | PID-40 | Model-XYZ | PN-32 | ATA    | SN-67  | 
| Server357 | 12      | PID-11 | Model-XYZ | PN-69 | ATA    | SN-95  | 
+-----------+---------+--------+-----------+-------+--------+--------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

## Model

```
# iserver get server
    --group test
    --pd model:ST1200MM0009 -v pd
    --iaccount demo
    --ttl 0
    --anonymize

iaccount demo (cache: any)
Select servers...
Selected servers: 8
Collect server api objects...


Physical Disk - State [#15]
---------------------------

+-----------+-------+------------+---------+----+----------+------+----------+----------+------------+---------+-------+----------+
| Server    | State | Controller | Disk Id | VD | Size     | Type | Protocol | Bootable | Link Speed | Fw      | State | Presence |
+-----------+-------+------------+---------+----+----------+------+----------+----------+------------+---------+-------+----------+
| Server366 | V     | MRAID      | 13      | -- | 1.2 [TB] | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good  | equipped | 
| Server366 | V     | MRAID      | 14      | -- | 1.2 [TB] | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good  | equipped | 
| Server366 | V     | MRAID      | 15      | -- | 1.2 [TB] | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good  | equipped | 
| Server366 | V     | MRAID      | 16      | -- | 1.2 [TB] | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good  | equipped | 
| Server366 | V     | MRAID      | 17      | 0  | 1.2 [TB] | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good  | equipped | 
| Server383 | V     | MRAID      | 13      | -- | 1.2 [TB] | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good  | equipped | 
| Server383 | V     | MRAID      | 14      | -- | 1.2 [TB] | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good  | equipped | 
| Server383 | V     | MRAID      | 15      | -- | 1.2 [TB] | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good  | equipped | 
| Server383 | V     | MRAID      | 16      | -- | 1.2 [TB] | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good  | equipped | 
| Server383 | V     | MRAID      | 17      | 0  | 1.2 [TB] | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good  | equipped | 
| Server262 | V     | MRAID      | 13      | -- | 1.2 [TB] | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good  | equipped | 
| Server262 | V     | MRAID      | 14      | -- | 1.2 [TB] | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good  | equipped | 
| Server262 | V     | MRAID      | 15      | -- | 1.2 [TB] | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good  | equipped | 
| Server262 | V     | MRAID      | 16      | -- | 1.2 [TB] | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good  | equipped | 
| Server262 | V     | MRAID      | 17      | -- | 1.2 [TB] | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good  | equipped | 
+-----------+-------+------------+---------+----+----------+------+----------+----------+------------+---------+-------+----------+

Physical Disk - Inventory [#15]
-------------------------------

+-----------+---------+--------+-----------+-------+---------+--------+
| Server    | Disk Id | Pid    | Model     | PN    | Vendor  | Serial |
+-----------+---------+--------+-----------+-------+---------+--------+
| Server366 | 13      | PID-15 | Model-XYZ | PN-68 | SEAGATE | SN-11  | 
| Server366 | 14      | PID-27 | Model-XYZ | PN-37 | SEAGATE | SN-91  | 
| Server366 | 15      | PID-92 | Model-XYZ | PN-85 | SEAGATE | SN-50  | 
| Server366 | 16      | PID-38 | Model-XYZ | PN-22 | SEAGATE | SN-42  | 
| Server366 | 17      | PID-84 | Model-XYZ | PN-61 | SEAGATE | SN-41  | 
| Server383 | 13      | PID-73 | Model-XYZ | PN-91 | SEAGATE | SN-91  | 
| Server383 | 14      | PID-11 | Model-XYZ | PN-61 | SEAGATE | SN-46  | 
| Server383 | 15      | PID-59 | Model-XYZ | PN-45 | SEAGATE | SN-53  | 
| Server383 | 16      | PID-74 | Model-XYZ | PN-47 | SEAGATE | SN-58  | 
| Server383 | 17      | PID-88 | Model-XYZ | PN-77 | SEAGATE | SN-70  | 
| Server262 | 13      | PID-89 | Model-XYZ | PN-20 | SEAGATE | SN-43  | 
| Server262 | 14      | PID-70 | Model-XYZ | PN-33 | SEAGATE | SN-12  | 
| Server262 | 15      | PID-30 | Model-XYZ | PN-61 | SEAGATE | SN-81  | 
| Server262 | 16      | PID-95 | Model-XYZ | PN-41 | SEAGATE | SN-71  | 
| Server262 | 17      | PID-69 | Model-XYZ | PN-38 | SEAGATE | SN-60  | 
+-----------+---------+--------+-----------+-------+---------+--------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

## Serial

```
# iserver get server
    --group test
    --pd serial:PHYS74600 -v pd
    --iaccount demo
    --ttl 0
    --anonymize

iaccount demo (cache: any)
Select servers...
Selected servers: 8
Collect server api objects...


Physical Disk - State [#8]
--------------------------

+-----------+-------+------------+---------+----+------------+------+----------+----------+------------+---------+-------+----------+
| Server    | State | Controller | Disk Id | VD | Size       | Type | Protocol | Bootable | Link Speed | Fw      | State | Presence |
+-----------+-------+------------+---------+----+------------+------+----------+----------+------------+---------+-------+----------+
| Server896 | V     | MRAID      | 9       | -- | 959.0 [GB] | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server896 | V     | MRAID      | 10      | -- | 959.0 [GB] | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server896 | V     | MRAID      | 11      | -- | 959.0 [GB] | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server349 | V     | MRAID      | 10      | -- | 959.0 [GB] | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server349 | V     | MRAID      | 11      | -- | 959.0 [GB] | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server349 | V     | MRAID      | 12      | -- | 959.0 [GB] | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server630 | V     | MRAID      | 9       | 0  | 959.0 [GB] | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server630 | V     | MRAID      | 11      | -- | 959.0 [GB] | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
+-----------+-------+------------+---------+----+------------+------+----------+----------+------------+---------+-------+----------+

Physical Disk - Inventory [#8]
------------------------------

+-----------+---------+--------+-----------+-------+--------+--------+
| Server    | Disk Id | Pid    | Model     | PN    | Vendor | Serial |
+-----------+---------+--------+-----------+-------+--------+--------+
| Server896 | 9       | PID-51 | Model-XYZ | PN-94 | ATA    | SN-70  | 
| Server896 | 10      | PID-12 | Model-XYZ | PN-74 | ATA    | SN-75  | 
| Server896 | 11      | PID-40 | Model-XYZ | PN-18 | ATA    | SN-36  | 
| Server349 | 10      | PID-77 | Model-XYZ | PN-15 | ATA    | SN-18  | 
| Server349 | 11      | PID-66 | Model-XYZ | PN-75 | ATA    | SN-33  | 
| Server349 | 12      | PID-58 | Model-XYZ | PN-34 | ATA    | SN-69  | 
| Server630 | 9       | PID-90 | Model-XYZ | PN-36 | ATA    | SN-15  | 
| Server630 | 11      | PID-43 | Model-XYZ | PN-54 | ATA    | SN-21  | 
+-----------+---------+--------+-----------+-------+--------+--------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

## Vendor

```
# iserver get server
    --group test
    --pd vendor:ata -v pd
    --iaccount demo
    --ttl 0
    --anonymize

iaccount demo (cache: any)
Select servers...
Selected servers: 8
Collect server api objects...


Physical Disk - State [#18]
---------------------------

+-----------+-------+------------+---------+----+-------------+------+----------+----------+------------+---------+-------+----------+
| Server    | State | Controller | Disk Id | VD | Size        | Type | Protocol | Bootable | Link Speed | Fw      | State | Presence |
+-----------+-------+------------+---------+----+-------------+------+----------+----------+------------+---------+-------+----------+
| Server424 | V     | MRAID      | 9       | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server424 | V     | MRAID      | 10      | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server424 | V     | MRAID      | 11      | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server424 | V     | MRAID      | 12      | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server821 | V     | MRAID      | 9       | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server821 | V     | MRAID      | 10      | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server821 | V     | MRAID      | 11      | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server821 | V     | MRAID      | 12      | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server464 | V     | MRAID      | 9       | 0  | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server464 | V     | MRAID      | 10      | 0  | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server464 | V     | MRAID      | 11      | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server464 | V     | MRAID      | 12      | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server761 | V     | MRAID      | 1       | -- | 1.92 [TB]   | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server761 | V     | MRAID      | 2       | -- | 1.92 [TB]   | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server761 | V     | MRAID      | 3       | -- | 1.92 [TB]   | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server761 | V     | MRAID      | 4       | -- | 1.92 [TB]   | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server761 | V     | MSTOR-RAID | 253     | 0  | 240.06 [GB] | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
| Server761 | V     | MSTOR-RAID | 254     | 0  | 240.06 [GB] | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good  | equipped | 
+-----------+-------+------------+---------+----+-------------+------+----------+----------+------------+---------+-------+----------+

Physical Disk - Inventory [#18]
-------------------------------

+-----------+---------+--------+-----------+-------+--------+--------+
| Server    | Disk Id | Pid    | Model     | PN    | Vendor | Serial |
+-----------+---------+--------+-----------+-------+--------+--------+
| Server424 | 9       | PID-61 | Model-XYZ | PN-41 | ATA    | SN-30  | 
| Server424 | 10      | PID-10 | Model-XYZ | PN-30 | ATA    | SN-58  | 
| Server424 | 11      | PID-62 | Model-XYZ | PN-65 | ATA    | SN-38  | 
| Server424 | 12      | PID-91 | Model-XYZ | PN-97 | ATA    | SN-72  | 
| Server821 | 9       | PID-49 | Model-XYZ | PN-74 | ATA    | SN-20  | 
| Server821 | 10      | PID-39 | Model-XYZ | PN-52 | ATA    | SN-57  | 
| Server821 | 11      | PID-63 | Model-XYZ | PN-78 | ATA    | SN-70  | 
| Server821 | 12      | PID-64 | Model-XYZ | PN-17 | ATA    | SN-76  | 
| Server464 | 9       | PID-54 | Model-XYZ | PN-72 | ATA    | SN-22  | 
| Server464 | 10      | PID-16 | Model-XYZ | PN-18 | ATA    | SN-43  | 
| Server464 | 11      | PID-79 | Model-XYZ | PN-40 | ATA    | SN-20  | 
| Server464 | 12      | PID-58 | Model-XYZ | PN-88 | ATA    | SN-43  | 
| Server761 | 1       | PID-86 | Model-XYZ | PN-39 | ATA    | SN-25  | 
| Server761 | 2       | PID-42 | Model-XYZ | PN-49 | ATA    | SN-78  | 
| Server761 | 3       | PID-17 | Model-XYZ | PN-65 | ATA    | SN-84  | 
| Server761 | 4       | PID-94 | Model-XYZ | PN-36 | ATA    | SN-86  | 
| Server761 | 253     | PID-95 | Model-XYZ | PN-58 | ATA    | SN-52  | 
| Server761 | 254     | PID-61 | Model-XYZ | PN-26 | ATA    | SN-95  | 
+-----------+---------+--------+-----------+-------+--------+--------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)