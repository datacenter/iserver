# Intersight Server

## boot view

```
# iserver get server --group test -v boot

iaccount demo (cache: any)
Select servers...
Selected servers: 8
Collect server api objects...


Boot [#8]
---------

+-----------+----------------------+------------------+-------------+-------+----------------+----------+----------+
| Server    | Configured Boot Mode | Actual Boot Mode | Secure Boot | Order | Name           | Type     | State    |
+-----------+----------------------+------------------+-------------+-------+----------------+----------+----------+
| Server700 | Legacy               | Legacy           | disabled    | 1     | localhdd       | LOCALHDD | Disabled |
|           |                      |                  |             | 2     | pxeboot        | PXE      | Disabled |
|           |                      |                  |             | 3     | vmedia         | VMEDIA   | Disabled |
+-----------+----------------------+------------------+-------------+-------+----------------+----------+----------+
| Server528 | Uefi                 | Uefi             | disabled    | 1     | localhdd       | LOCALHDD | Enabled  |
|           |                      |                  |             | 2     | pxeboot        | PXE      | Enabled  |
|           |                      |                  |             | 3     | vmedia         | VMEDIA   | Enabled  |
+-----------+----------------------+------------------+-------------+-------+----------------+----------+----------+
| Server712 | Uefi                 | Uefi             | disabled    | 1     | localhdd       | LOCALHDD | Enabled  |
|           |                      |                  |             | 2     | pxeboot        | PXE      | Enabled  |
|           |                      |                  |             | 3     | vmedia         | VMEDIA   | Enabled  |
+-----------+----------------------+------------------+-------------+-------+----------------+----------+----------+
| Server943 | Uefi                 | Uefi             | disabled    | 1     | KVM-Mapped-DVD | VMEDIA   | Enabled  |
|           |                      |                  |             | 2     | M2-boot        | LOCALHDD | Enabled  |
+-----------+----------------------+------------------+-------------+-------+----------------+----------+----------+
| Server692 | None                 | None             | None        |       |                |          |          |
+-----------+----------------------+------------------+-------------+-------+----------------+----------+----------+
| Server733 | None                 | None             | None        |       |                |          |          |
+-----------+----------------------+------------------+-------------+-------+----------------+----------+----------+
| Server538 | None                 | None             | None        |       |                |          |          |
+-----------+----------------------+------------------+-------------+-------+----------------+----------+----------+
| Server314 | None                 | None             | None        |       |                |          |          |
+-----------+----------------------+------------------+-------------+-------+----------------+----------+----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)