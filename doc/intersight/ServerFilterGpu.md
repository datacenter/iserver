# Intersight Server

## Filter by gpu

Examples

```
--gpu slot:gt0
--gpu model:nvidia
```

GPU count filtering options:
- "--gpu slot:1" will select servers with 1 GPU
- "--gpu slot:gt1" will select servers with >1 GPU cores
- "--gpu slot:ge1" will select servers with >=1 GPU cores
- "--gpu slot:le2" will select servers with <=2 GPU cores
- "--gpu slot:lt2" will select servers with <2 GPU cores
- "--gpu slot:ne1" will select servers with !=1 GPU cores

## At least one GPU

```
# iserver get server --gpu slot:gt0 -v gpu

iaccount demo (cache: any)
Select servers...
Selected servers: 121
Collect server api objects...


GPU [#2]
--------

+-----------+------------------------------+----------------+--------+--------+--------+----------+
| Server    | GPU Device Model             | Pid            | Serial | SlotId | Vendor | Firmware |
+-----------+------------------------------+----------------+--------+--------+--------+----------+
| Server112 | NVIDIA A16 PCIe FHFL DS 250W | UCSC-GPU-A16   | SN-54  | 7      | 0x10de | 1.0(1a)  |
| Server986 | NVIDIA T4 PCIe 16GB 70W      | UCSC-GPU-T4-16 | SN-28  | 3      | 0x10de | 1.0(1a)  |
+-----------+------------------------------+----------------+--------+--------+--------+----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

## GPU model

```
# iserver get server
    --gpu model:nvidia -v gpu

iaccount demo (cache: any)
Select servers...
Selected servers: 121
Collect server api objects...


GPU [#2]
--------

+-----------+------------------------------+----------------+--------+--------+--------+----------+
| Server    | GPU Device Model             | Pid            | Serial | SlotId | Vendor | Firmware |
+-----------+------------------------------+----------------+--------+--------+--------+----------+
| Server760 | NVIDIA A16 PCIe FHFL DS 250W | UCSC-GPU-A16   | SN-85  | 7      | 0x10de | 1.0(1a)  |
| Server224 | NVIDIA T4 PCIe 16GB 70W      | UCSC-GPU-T4-16 | SN-35  | 3      | 0x10de | 1.0(1a)  |
+-----------+------------------------------+----------------+--------+--------+--------+----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)