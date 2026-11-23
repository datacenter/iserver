# Intersight Server

## Psu view

```
# iserver get server --group test -v psu

iaccount demo (cache: any)
Select servers...
Selected servers: 8
Collect server api objects...


PSU [#8]
--------

+-----------+--------+-------+---------+---------+---------------+--------+-------------------+
| Server    | Name   | State | Present | Voltage | Model         | Serial | Vendor            |
+-----------+--------+-------+---------+---------+---------------+--------+-------------------+
| Server362 | PSU #1 | V     | V       | ok      | PS-2112-9S-LF | SN-45  | Cisco Systems Inc |
| Server362 | PSU #2 | V     | V       | ok      | PS-2112-9S-LF | SN-26  | Cisco Systems Inc |
| Server302 | PSU #1 | V     | V       | ok      | PS-2112-9S-LF | SN-66  | Cisco Systems Inc |
| Server302 | PSU #2 | V     | V       | ok      | PS-2112-9S-LF | SN-87  | Cisco Systems Inc |
| Server558 | PSU #1 | V     | V       | ok      | PS-2112-9S-LF | SN-62  | Cisco Systems Inc |
| Server558 | PSU #2 | V     | V       | ok      | PS-2112-9S-LF | SN-13  | Cisco Systems Inc |
| Server679 | PSU #1 | V     | V       | ok      | PS-2112-9S-LF | SN-55  | Cisco Systems Inc |
| Server679 | PSU #2 | V     | V       | ok      | PS-2112-9S-LF | SN-75  | Cisco Systems Inc |
+-----------+--------+-------+---------+---------+---------------+--------+-------------------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)