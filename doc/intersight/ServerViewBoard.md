# Intersight Server

## board view

```
# iserver get server --group test -v board

iaccount demo (cache: any)
Select servers...
Selected servers: 8
Collect server api objects...


Motherboard Hardware Summary [#8]
---------------------------------

+-----------+----------+-------------------+-----+--------+------------+------------------+----------+--------------+----------------+---------------+-----+-----+
| Server    | Board Id | Vendor            | CPU | MemArr | PCI Switch | PCI Cooprocessor | Graphics | Storage Ctrl | FlexFlash Ctrl | FlexUtil Ctrl | Sec | TPM |
+-----------+----------+-------------------+-----+--------+------------+------------------+----------+--------------+----------------+---------------+-----+-----+
| Server799 | 0        | Cisco Systems Inc | 2   | 1      | 0          | 0                | 0        | 2            | 0              | 1             | 0   | 1   |
| Server657 | 0        | Cisco Systems Inc | 2   | 1      | 0          | 0                | 0        | 2            | 0              | 1             | 0   | 1   |
| Server737 | 0        | Cisco Systems Inc | 2   | 1      | 0          | 0                | 0        | 2            | 0              | 1             | 0   | 1   |
| Server926 | 0        | Cisco Systems Inc | 2   | 1      | 0          | 0                | 1        | 2            | 0              | 0             | 0   | 1   |
| Server219 | 0        | Cisco Systems Inc | 2   | 1      | 0          | 0                | 0        | 2            | 0              | 0             | 0   | 0   |
| Server539 | 0        | Cisco Systems Inc | 2   | 1      | 0          | 0                | 0        | 2            | 0              | 0             | 0   | 0   |
| Server102 | 0        | Cisco Systems Inc | 2   | 1      | 0          | 0                | 0        | 2            | 0              | 0             | 0   | 0   |
| Server709 | 0        | Cisco Systems Inc | 2   | 1      | 0          | 0                | 0        | 2            | 0              | 0             | 0   | 0   |
+-----------+----------+-------------------+-----+--------+------------+------------------+----------+--------------+----------------+---------------+-----+-----+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)