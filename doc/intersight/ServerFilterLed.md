# Intersight Server

## Filter by locator led

Examples

```
--led on
```

## Led on

```
# iserver get server --led on

iaccount demo (cache: any)
Select servers...
Selected servers: 121
Collect server api objects...


Server Summary [#3]
-------------------

+-----------+-----+-----------+------------+-----+--------------------+--------+----------------+------------+-----------+
| SF        | MF  | Name      | Moid       | Tag | Model              | Serial | IP             | CPU        | Memory    |
+-----------+-----+-----------+------------+-----+--------------------+--------+----------------+------------+-----------+
| P+ H L    | CRi | Server855 | Moid-value | --  | (R) APIC-SERVER-M3 | SN-86  | 10.44.87.62    | 2S 16C 16T | 96 [GiB]  |
| P+ H L    | CRi | Server215 | Moid-value | --  | (R) APIC-SERVER-M3 | SN-13  | 10.171.94.14   | 2S 16C 16T | 96 [GiB]  |
| P+ W(4) L | Cri | Server448 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-86  | 10.113.253.214 | 2S 28C 56T | 256 [GiB] |
+-----------+-----+-----------+------------+-----+--------------------+--------+----------------+------------+-----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)