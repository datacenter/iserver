# Intersight Server

## Filter by serial

Examples

```
--serial abc --serial xyz
```

## Serial

```
# iserver get server
    --serial abc
    --serial xyz

iaccount demo (cache: any)
Select servers...
Selected servers: 2
Collect server api objects...


Server Summary [#2]
-------------------

+---------+-----+-----------+------------+-----+--------------------+--------+---------------+------------+-----------+
| SF      | MF  | Name      | Moid       | Tag | Model              | Serial | IP            | CPU        | Memory    |
+---------+-----+-----------+------------+-----+--------------------+--------+---------------+------------+-----------+
| P+ C(1) | CRi | Server980 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-82  | 10.119.77.212 | 2S 40C 80T | 384 [GiB] |
| P+ H    | CRi | Server654 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-47  | 10.87.23.36   | 2S 40C 80T | 384 [GiB] |
+---------+-----+-----------+------------+-----+--------------------+--------+---------------+------------+-----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)