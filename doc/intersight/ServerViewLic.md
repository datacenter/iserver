# Intersight Server

## lic view

```
# iserver get server --group test -v lic

iaccount demo (cache: any)
Select servers...
Selected servers: 8
Collect server api objects...


License [#8]
------------

+-----------+-----------+
| Server    | License   |
+-----------+-----------+
| Server645 | Advantage |
| Server720 | Advantage |
| Server405 | Advantage |
| Server384 | Advantage |
| Server857 | Advantage |
| Server978 | Advantage |
| Server897 | Advantage |
| Server626 | Advantage |
+-----------+-----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)