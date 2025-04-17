# Intersight Server

## contract view

```
# iserver get server
    --group test -v contract
    --iaccount demo
    --ttl 0
    --anonymize

iaccount demo (cache: any)
Select servers...
Selected servers: 8
Collect server api objects...


Contract [#8]
-------------

+-----------+-----------------+----------------------+----------------------+--------------------------+--------------------------------------------------------------+-----------------------+--------------------+
| Server    | Contract Status | Start Date           | End Date             | Last Updated             | Service Description                                          | Purchase Order Number | Sales Order Number |
+-----------+-----------------+----------------------+----------------------+--------------------------+--------------------------------------------------------------+-----------------------+--------------------+
| Server902 | Not Covered     | 0001-01-01T00:00:00Z | 0001-01-01T00:00:00Z | 2025-01-01T00:00:00.000Z | UCS C240 M5 10 NVMe + 16 SAS/SATA SFF w/o CPU,mem,HD,PCIe,PS | PO160                 | SO40               | 
| Server190 | Not Covered     | 0001-01-01T00:00:00Z | 0001-01-01T00:00:00Z | 2025-01-01T00:00:00.000Z | UCS C240 M5 10 NVMe + 16 SAS/SATA SFF w/o CPU,mem,HD,PCIe,PS | PO147                 | SO141              | 
| Server215 | Not Covered     | 0001-01-01T00:00:00Z | 0001-01-01T00:00:00Z | 2025-01-01T00:00:00.000Z | UCS C240 M5 10 NVMe + 16 SAS/SATA SFF w/o CPU,mem,HD,PCIe,PS | PO110                 | SO131              | 
| Server954 | Not Covered     | 0001-01-01T00:00:00Z | 0001-01-01T00:00:00Z | 2025-01-01T00:00:00.000Z | UCS C225 M6 Rack w/o CPU, mem, drv, 1U wSFF 10HDD backplane  | PO236                 | SO129              | 
| Server403 | Not Covered     | 0001-01-01T00:00:00Z | 0001-01-01T00:00:00Z | 2025-01-01T00:00:00.000Z | UCS B200 M5 Blade w/o CPU, mem, HDD, mezz (UPG)              | PO100                 | SO121              | 
| Server603 | Not Covered     | 0001-01-01T00:00:00Z | 0001-01-01T00:00:00Z | 2025-01-01T00:00:00.000Z | UCS B200 M5 Blade w/o CPU, mem, HDD, mezz (UPG)              | PO120                 | SO33               | 
| Server459 | Not Covered     | 0001-01-01T00:00:00Z | 0001-01-01T00:00:00Z | 2025-01-01T00:00:00.000Z | UCS B200 M5 Blade w/o CPU, mem, HDD, mezz (UPG)              | PO143                 | SO220              | 
| Server856 | Not Covered     | 0001-01-01T00:00:00Z | 0001-01-01T00:00:00Z | 2025-01-01T00:00:00.000Z | UCS B200 M5 Blade w/o CPU, mem, HDD, mezz (UPG)              | PO57                  | SO89               | 
+-----------+-----------------+----------------------+----------------------+--------------------------+--------------------------------------------------------------+-----------------------+--------------------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)