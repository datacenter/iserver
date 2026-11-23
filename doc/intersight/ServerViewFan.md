# Intersight Server

## fan view

```
# iserver get server --group test -v fan

iaccount demo (cache: any)
Select servers...
Selected servers: 8
Collect server api objects...


Fan [#58]
---------

+-----------+-------+----------------------+-----------+----------+
| Server    | State | Fan                  | OperState | Presence |
+-----------+-------+----------------------+-----------+----------+
| Server855 | V     | Fan Module 1 - Fan 1 | operable  | equipped |
| Server855 | V     | Fan Module 1 - Fan 2 | operable  | equipped |
| Server855 | V     | Fan Module 2 - Fan 1 | operable  | equipped |
| Server855 | V     | Fan Module 2 - Fan 2 | operable  | equipped |
| Server855 | V     | Fan Module 3 - Fan 1 | operable  | equipped |
| Server855 | V     | Fan Module 3 - Fan 2 | operable  | equipped |
| Server855 | V     | Fan Module 4 - Fan 1 | operable  | equipped |
| Server855 | V     | Fan Module 4 - Fan 2 | operable  | equipped |
| Server855 | V     | Fan Module 5 - Fan 1 | operable  | equipped |
| Server855 | V     | Fan Module 5 - Fan 2 | operable  | equipped |
| Server855 | V     | Fan Module 6 - Fan 1 | operable  | equipped |
| Server855 | V     | Fan Module 6 - Fan 2 | operable  | equipped |
| Server855 | X     | Fan Module 7 - Fan 1 | unknown   | missing  |
| Server855 | X     | Fan Module 7 - Fan 2 | unknown   | missing  |
| Server736 | V     | Fan Module 1 - Fan 1 | operable  | equipped |
| Server736 | V     | Fan Module 1 - Fan 2 | operable  | equipped |
| Server736 | V     | Fan Module 2 - Fan 1 | operable  | equipped |
| Server736 | V     | Fan Module 2 - Fan 2 | operable  | equipped |
| Server736 | V     | Fan Module 3 - Fan 1 | operable  | equipped |
| Server736 | V     | Fan Module 3 - Fan 2 | operable  | equipped |
| Server736 | V     | Fan Module 4 - Fan 1 | operable  | equipped |
| Server736 | V     | Fan Module 4 - Fan 2 | operable  | equipped |
| Server736 | V     | Fan Module 5 - Fan 1 | operable  | equipped |
| Server736 | V     | Fan Module 5 - Fan 2 | operable  | equipped |
| Server736 | V     | Fan Module 6 - Fan 1 | operable  | equipped |
| Server736 | V     | Fan Module 6 - Fan 2 | operable  | equipped |
| Server736 | X     | Fan Module 7 - Fan 1 | unknown   | missing  |
| Server736 | X     | Fan Module 7 - Fan 2 | unknown   | missing  |
| Server842 | V     | Fan Module 1 - Fan 1 | operable  | equipped |
| Server842 | V     | Fan Module 1 - Fan 2 | operable  | equipped |
| Server842 | V     | Fan Module 2 - Fan 1 | operable  | equipped |
| Server842 | V     | Fan Module 2 - Fan 2 | operable  | equipped |
| Server842 | V     | Fan Module 3 - Fan 1 | operable  | equipped |
| Server842 | V     | Fan Module 3 - Fan 2 | operable  | equipped |
| Server842 | V     | Fan Module 4 - Fan 1 | operable  | equipped |
| Server842 | V     | Fan Module 4 - Fan 2 | operable  | equipped |
| Server842 | V     | Fan Module 5 - Fan 1 | operable  | equipped |
| Server842 | V     | Fan Module 5 - Fan 2 | operable  | equipped |
| Server842 | V     | Fan Module 6 - Fan 1 | operable  | equipped |
| Server842 | V     | Fan Module 6 - Fan 2 | operable  | equipped |
| Server842 | X     | Fan Module 7 - Fan 1 | unknown   | missing  |
| Server842 | X     | Fan Module 7 - Fan 2 | unknown   | missing  |
| Server334 | V     | Fan Module 1 - Fan 1 | operable  | equipped |
| Server334 | V     | Fan Module 1 - Fan 2 | operable  | equipped |
| Server334 | V     | Fan Module 2 - Fan 1 | operable  | equipped |
| Server334 | V     | Fan Module 2 - Fan 2 | operable  | equipped |
| Server334 | V     | Fan Module 3 - Fan 1 | operable  | equipped |
| Server334 | V     | Fan Module 3 - Fan 2 | operable  | equipped |
| Server334 | V     | Fan Module 4 - Fan 1 | operable  | equipped |
| Server334 | V     | Fan Module 4 - Fan 2 | operable  | equipped |
| Server334 | V     | Fan Module 5 - Fan 1 | operable  | equipped |
| Server334 | V     | Fan Module 5 - Fan 2 | operable  | equipped |
| Server334 | V     | Fan Module 6 - Fan 1 | operable  | equipped |
| Server334 | V     | Fan Module 6 - Fan 2 | operable  | equipped |
| Server334 | X     | Fan Module 7 - Fan 1 | unknown   | equipped |
| Server334 | X     | Fan Module 7 - Fan 2 | unknown   | equipped |
| Server334 | X     | Fan Module 8 - Fan 1 | unknown   | equipped |
| Server334 | X     | Fan Module 8 - Fan 2 | unknown   | equipped |
+-----------+-------+----------------------+-----------+----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)