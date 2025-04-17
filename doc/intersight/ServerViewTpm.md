# Intersight Server

## tpm view

```
# iserver get server --group test -v tpm

iaccount demo (cache: any)
Select servers...
Selected servers: 8
Collect server api objects...


Trusted Platform Module [#4]
----------------------------

+-----------+----------+-------------------+-------------+------------+------------------+-------------------+--------+------------------+
| Server    | TPM      | Activation Status | Admin State | Version    | Model            | Vendor            | Serial | Firmware Version |
+-----------+----------+-------------------+-------------+------------+------------------+-------------------+--------+------------------+
| Server126 | empty    | unknown           | unknown     | Version-93 | NA               | NA                | SN-74  | Version-29       |
| Server738 | empty    | unknown           | unknown     | Version-16 | NA               | NA                | SN-78  | Version-59       |
| Server710 | empty    | unknown           | unknown     | Version-55 | NA               | NA                | SN-51  | Version-13       |
| Server814 | equipped | activated         | enabled     | Version-48 | UCSX-TPM2-002B-C | Cisco Systems Inc | SN-88  | Version-15       |
+-----------+----------+-------------------+-------------+------------+------------------+-------------------+--------+------------------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)