# Intersight Server

## Filter by psu

Examples

```
--psu state:ok
--psu state:nok
--psu model:ps-2112
--psu serial:myserial
--psu vendor:cisco
```

## PSU off

```
# iserver get server --psu state:nok -v psu

iaccount demo (cache: any)
Select servers...
Selected servers: 121
Collect server api objects...


PSU [#14]
---------

+-----------+--------+-------+---------+---------+---------------+--------+-------------------+
| Server    | Name   | State | Present | Voltage | Model         | Serial | Vendor            |
+-----------+--------+-------+---------+---------+---------------+--------+-------------------+
| Server650 | PSU #1 | X     | X       | unknown |               | SN-90  |                   |
| Server650 | PSU #2 | X     | X       | unknown |               | SN-43  |                   |
| Server358 | PSU #1 | X     | V       | unknown | PS-2771-1S-LF | SN-12  | Cisco Systems Inc |
| Server358 | PSU #2 | X     | V       | unknown | PS-2771-1S-LF | SN-36  | Cisco Systems Inc |
| Server687 | PSU #1 | X     | V       | unknown | PS-2771-1S-LF | SN-56  | Cisco Systems Inc |
| Server687 | PSU #2 | X     | V       | unknown | PS-2771-1S-LF | SN-52  | Cisco Systems Inc |
| Server756 | PSU #1 | X     | V       | unknown | PS-2771-1S-LF | SN-55  | Cisco Systems Inc |
| Server756 | PSU #2 | X     | V       | unknown | PS-2771-1S-LF | SN-16  | Cisco Systems Inc |
| Server145 | PSU #1 | X     | V       | unknown | PS-2771-1S-LF | SN-29  | Cisco Systems Inc |
| Server145 | PSU #2 | X     | V       | unknown | PS-2771-1S-LF | SN-37  | Cisco Systems Inc |
| Server884 | PSU #1 | X     | V       | unknown | PS-2771-1S-LF | SN-45  | Cisco Systems Inc |
| Server884 | PSU #2 | X     | V       | unknown | PS-2771-1S-LF | SN-83  | Cisco Systems Inc |
| Server721 | PSU #1 | X     | V       | unknown | DPST-1200DB A | SN-56  | Cisco Systems Inc |
| Server721 | PSU #2 | X     | V       | unknown | DPST-1200DB A | SN-34  | Cisco Systems Inc |
+-----------+--------+-------+---------+---------+---------------+--------+-------------------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

## PSU serial

```
# iserver get server
    --psu serial:xyz -v psu

iaccount demo (cache: any)
Select servers...
Selected servers: 121
Collect server api objects...


PSU [#8]
--------

+-----------+--------+-------+---------+---------+------------+--------+-------------------+
| Server    | Name   | State | Present | Voltage | Model      | Serial | Vendor            |
+-----------+--------+-------+---------+---------+------------+--------+-------------------+
| Server511 | PSU #1 | V     | V       | ok      | PS-2162-9S | SN-36  | Cisco Systems Inc |
| Server511 | PSU #2 | V     | V       | ok      | PS-2162-9S | SN-61  | Cisco Systems Inc |
| Server297 | PSU #1 | V     | V       | ok      | PS-2162-9S | SN-71  | Cisco Systems Inc |
| Server297 | PSU #2 | V     | V       | ok      | PS-2162-9S | SN-20  | Cisco Systems Inc |
| Server243 | PSU #1 | V     | V       | ok      | PS-2162-9S | SN-23  | Cisco Systems Inc |
| Server243 | PSU #2 | V     | V       | ok      | PS-2162-9S | SN-19  | Cisco Systems Inc |
| Server592 | PSU #1 | V     | V       | ok      | PS-2162-9S | SN-55  | Cisco Systems Inc |
| Server592 | PSU #2 | V     | V       | ok      | PS-2162-9S | SN-91  | Cisco Systems Inc |
+-----------+--------+-------+---------+---------+------------+--------+-------------------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

## PSU model

```
# iserver get server --psu model:2162 -v psu

iaccount demo (cache: any)
Select servers...
Selected servers: 121
Collect server api objects...


PSU [#14]
---------

+-----------+--------+-------+---------+---------+------------+--------+-------------------+
| Server    | Name   | State | Present | Voltage | Model      | Serial | Vendor            |
+-----------+--------+-------+---------+---------+------------+--------+-------------------+
| Server502 | PSU #1 | V     | V       | ok      | PS-2162-9S | SN-50  | Cisco Systems Inc |
| Server502 | PSU #2 | V     | V       | ok      | PS-2162-9S | SN-68  | Cisco Systems Inc |
| Server296 | PSU #3 | V     | V       | ok      | PS-2162-9S | SN-53  | Cisco Systems Inc |
| Server296 | PSU #4 | V     | V       | ok      | PS-2162-9S | SN-83  | Cisco Systems Inc |
| Server914 | PSU #1 | V     | V       | ok      | PS-2162-9S | SN-73  | Cisco Systems Inc |
| Server914 | PSU #2 | V     | V       | ok      | PS-2162-9S | SN-90  | Cisco Systems Inc |
| Server860 | PSU #1 | V     | V       | ok      | PS-2162-9S | SN-15  | Cisco Systems Inc |
| Server860 | PSU #2 | V     | V       | ok      | PS-2162-9S | SN-82  | Cisco Systems Inc |
| Server579 | PSU #1 | V     | V       | ok      | PS-2162-9S | SN-35  | Cisco Systems Inc |
| Server579 | PSU #2 | V     | V       | ok      | PS-2162-9S | SN-92  | Cisco Systems Inc |
| Server464 | PSU #1 | V     | V       | ok      | PS-2162-9S | SN-55  | Cisco Systems Inc |
| Server464 | PSU #2 | V     | V       | ok      | PS-2162-9S | SN-89  | Cisco Systems Inc |
| Server310 | PSU #1 | V     | V       | ok      | PS-2162-9S | SN-79  | Cisco Systems Inc |
| Server310 | PSU #2 | V     | V       | ok      | PS-2162-9S | SN-28  | Cisco Systems Inc |
+-----------+--------+-------+---------+---------+------------+--------+-------------------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)