# Intersight Server

## gpu view

```
# iserver get server --group test -v gpu

iaccount demo (cache: any)
Select servers...
Selected servers: 8
Collect server api objects...


GPU [#1]
--------

+-----------+-------------------------+----------------+--------+--------+--------+----------+
| Server    | GPU Device Model        | Pid            | Serial | SlotId | Vendor | Firmware |
+-----------+-------------------------+----------------+--------+--------+--------+----------+
| Server176 | NVIDIA T4 PCIe 16GB 70W | UCSC-GPU-T4-16 | SN-85  | 3      | 0x10de | 1.0(1a)  |
+-----------+-------------------------+----------------+--------+--------+--------+----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)