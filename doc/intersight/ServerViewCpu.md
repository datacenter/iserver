# Intersight Server

## cpu view

```
# iserver get server --group test -v cpu

iaccount demo (cache: any)
Select servers...
Selected servers: 8
Collect server api objects...


CPU [#15]
---------

+-----------+-------+--------+--------+----------------------+------+-------------------------------------------------+-------+---------+---------+-------------+----------+----------+-----------+---------+
| Server    | State | CPU Id | Socket | Vendor               | Arch | Model                                           | Cores | Enabled | Threads | Speed [GHz] | Stepping | Presence | OperState | Thermal |
+-----------+-------+--------+--------+----------------------+------+-------------------------------------------------+-------+---------+---------+-------------+----------+----------+-----------+---------+
| Server379 | V     | 1      | CPU1   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20      | 40      | 2.5         | 7        | equipped | operable  |         |
| Server379 | V     | 2      | CPU2   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20      | 40      | 2.5         | 7        | equipped | operable  |         |
| Server687 | V     | 1      | CPU1   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20      | 40      | 2.5         | 7        | equipped | operable  |         |
| Server687 | V     | 2      | CPU2   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20      | 40      | 2.5         | 7        | equipped | operable  |         |
| Server743 | V     | 1      | CPU1   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20      | 40      | 2.5         | 7        | equipped | operable  |         |
| Server743 | V     | 2      | CPU2   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20      | 40      | 2.5         | 7        | equipped | operable  |         |
| Server869 | V     | 1      | CPU1   | AMD                  | Zen  | AMD EPYC 7763 64-Core Processor                 | 64    | 64      | 128     | 2.45        | 1        | equipped | operable  |         |
| Server216 | V     | 1      | CPU1   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20      | 40      | 2.5         | 7        | equipped | operable  | ok      |
| Server216 | V     | 2      | CPU2   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20      | 40      | 2.5         | 7        | equipped | operable  | ok      |
| Server439 | V     | 1      | CPU1   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20      | 40      | 2.5         | 7        | equipped | operable  | ok      |
| Server439 | V     | 2      | CPU2   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20      | 40      | 2.5         | 7        | equipped | operable  | ok      |
| Server520 | V     | 1      | CPU1   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20      | 40      | 2.5         | 7        | equipped | operable  | ok      |
| Server520 | V     | 2      | CPU2   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20      | 40      | 2.5         | 7        | equipped | operable  | ok      |
| Server540 | V     | 1      | CPU1   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20      | 40      | 2.5         | 7        | equipped | operable  | ok      |
| Server540 | V     | 2      | CPU2   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20      | 40      | 2.5         | 7        | equipped | operable  | ok      |
+-----------+-------+--------+--------+----------------------+------+-------------------------------------------------+-------+---------+---------+-------------+----------+----------+-----------+---------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)