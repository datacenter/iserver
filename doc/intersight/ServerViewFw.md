# Intersight Server

## fw view

```
# iserver get server --group test -v fw

iaccount demo (cache: any)
Select servers...
Selected servers: 8
Collect server api objects...


Firmware [#8]
-------------

+-----------+-----------------+-----------+------------------+----------------+---------+--------------------------------------+
| Server    | Name            | Component | Type             | PackageVersion | Version | Dn                                   |
+-----------+-----------------+-----------+------------------+----------------+---------+--------------------------------------+
| Server554 | CIMC Controller | system    | blade-controller | 1.0(1a)        | 1.0(1a) | sys/rack-unit-1/mgmt/fw-system       |
| Server144 | CIMC Controller | system    | blade-controller | 1.0(1a)        | 1.0(1a) | sys/rack-unit-1/mgmt/fw-system       |
| Server546 | CIMC Controller | system    | blade-controller | 1.0(1a)        | 1.0(1a) | sys/rack-unit-1/mgmt/fw-system       |
| Server486 | CIMC Controller | system    | blade-controller | 1.0(1a)        | 1.0(1a) | sys/rack-unit-1/mgmt/fw-system       |
| Server762 | CIMC Controller | system    | blade-controller | 1.0(1a)        | 1.0(1a) | sys/chassis-2/blade-1/mgmt/fw-system |
| Server884 | CIMC Controller | system    | blade-controller | 1.0(1a)        | 1.0(1a) | sys/chassis-2/blade-2/mgmt/fw-system |
| Server765 | CIMC Controller | system    | blade-controller | 1.0(1a)        | 1.0(1a) | sys/chassis-2/blade-3/mgmt/fw-system |
| Server108 | CIMC Controller | system    | blade-controller | 1.0(1a)        | 1.0(1a) | sys/chassis-2/blade-4/mgmt/fw-system |
+-----------+-----------------+-----------+------------------+----------------+---------+--------------------------------------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)