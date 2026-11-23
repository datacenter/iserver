# Intersight Server

## Filter by fan

Examples

```
--fan mod:gt6
--fan unit:gt10
--fan state:nok
```

## Module

```
# iserver get server --fan mod:lt6 -v fan

iaccount demo (cache: any)
Select servers...
Selected servers: 121
Collect server api objects...


Fan [#8]
--------

+-----------+-------+----------------------+-----------+----------+
| Server    | State | Fan                  | OperState | Presence |
+-----------+-------+----------------------+-----------+----------+
| Server983 | X     | Fan Module 1 - Fan 1 | unknown   | equipped |
| Server983 | X     | Fan Module 1 - Fan 2 | unknown   | equipped |
| Server983 | X     | Fan Module 2 - Fan 1 | unknown   | equipped |
| Server983 | X     | Fan Module 2 - Fan 2 | unknown   | equipped |
| Server983 | X     | Fan Module 3 - Fan 1 | unknown   | equipped |
| Server983 | X     | Fan Module 3 - Fan 2 | unknown   | equipped |
| Server983 | X     | Fan Module 4 - Fan 1 | unknown   | equipped |
| Server983 | X     | Fan Module 4 - Fan 2 | unknown   | equipped |
+-----------+-------+----------------------+-----------+----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

## Unit

```
# iserver get server --fan unit:le8 -v fan

iaccount demo (cache: any)
Select servers...
Selected servers: 121
Collect server api objects...


Fan [#38]
---------

+-----------+-------+----------------------+-----------+----------+
| Server    | State | Fan                  | OperState | Presence |
+-----------+-------+----------------------+-----------+----------+
| Server819 | V     | Fan Module 1 - Fan 1 | operable  | equipped |
| Server819 | V     | Fan Module 2 - Fan 1 | operable  | equipped |
| Server819 | V     | Fan Module 3 - Fan 1 | operable  | equipped |
| Server819 | V     | Fan Module 4 - Fan 1 | operable  | equipped |
| Server819 | V     | Fan Module 5 - Fan 1 | operable  | equipped |
| Server819 | V     | Fan Module 6 - Fan 1 | operable  | equipped |
| Server609 | X     | Fan Module 1 - Fan 1 | unknown   | equipped |
| Server609 | X     | Fan Module 1 - Fan 2 | unknown   | equipped |
| Server609 | X     | Fan Module 2 - Fan 1 | unknown   | equipped |
| Server609 | X     | Fan Module 2 - Fan 2 | unknown   | equipped |
| Server609 | X     | Fan Module 3 - Fan 1 | unknown   | equipped |
| Server609 | X     | Fan Module 3 - Fan 2 | unknown   | equipped |
| Server609 | X     | Fan Module 4 - Fan 1 | unknown   | equipped |
| Server609 | X     | Fan Module 4 - Fan 2 | unknown   | equipped |
| Server485 | V     | Fan Module 1 - Fan 1 | operable  | equipped |
| Server485 | V     | Fan Module 2 - Fan 1 | operable  | equipped |
| Server485 | V     | Fan Module 3 - Fan 1 | operable  | equipped |
| Server485 | V     | Fan Module 4 - Fan 1 | operable  | equipped |
| Server485 | V     | Fan Module 5 - Fan 1 | operable  | equipped |
| Server485 | V     | Fan Module 6 - Fan 1 | operable  | equipped |
| Server317 | V     | Fan Module 1 - Fan 1 | operable  | equipped |
| Server317 | V     | Fan Module 2 - Fan 1 | operable  | equipped |
| Server317 | V     | Fan Module 3 - Fan 1 | operable  | equipped |
| Server317 | V     | Fan Module 4 - Fan 1 | operable  | equipped |
| Server317 | V     | Fan Module 5 - Fan 1 | operable  | equipped |
| Server317 | V     | Fan Module 6 - Fan 1 | operable  | equipped |
| Server665 | V     | Fan Module 1 - Fan 1 | operable  | equipped |
| Server665 | V     | Fan Module 2 - Fan 1 | operable  | equipped |
| Server665 | V     | Fan Module 3 - Fan 1 | operable  | equipped |
| Server665 | V     | Fan Module 4 - Fan 1 | operable  | equipped |
| Server665 | V     | Fan Module 5 - Fan 1 | operable  | equipped |
| Server665 | V     | Fan Module 6 - Fan 1 | operable  | equipped |
| Server184 | X     | Fan Module 1 - Fan 1 | unknown   | equipped |
| Server184 | X     | Fan Module 2 - Fan 1 | unknown   | equipped |
| Server184 | X     | Fan Module 3 - Fan 1 | unknown   | equipped |
| Server184 | X     | Fan Module 4 - Fan 1 | unknown   | equipped |
| Server184 | X     | Fan Module 5 - Fan 1 | unknown   | equipped |
| Server184 | X     | Fan Module 6 - Fan 1 | unknown   | equipped |
+-----------+-------+----------------------+-----------+----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

## State

```
# iserver get server
    --group test
    --fan state:nok -v fan

iaccount demo (cache: any)
Select servers...
Selected servers: 7
Collect server api objects...


Fan [#6]
--------

+-----------+-------+----------------------+-----------+----------+
| Server    | State | Fan                  | OperState | Presence |
+-----------+-------+----------------------+-----------+----------+
| Server155 | X     | Fan Module 7 - Fan 1 | unknown   | missing  |
| Server155 | X     | Fan Module 7 - Fan 2 | unknown   | missing  |
| Server898 | X     | Fan Module 7 - Fan 1 | unknown   | missing  |
| Server898 | X     | Fan Module 7 - Fan 2 | unknown   | missing  |
| Server333 | X     | Fan Module 7 - Fan 1 | unknown   | missing  |
| Server333 | X     | Fan Module 7 - Fan 2 | unknown   | missing  |
+-----------+-------+----------------------+-----------+----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)