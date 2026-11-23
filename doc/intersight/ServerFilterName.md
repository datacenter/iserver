# Intersight Server

## Filter by name

```
# iserver get server --name *Server*

iaccount demo (cache: any)
Select servers...
Selected servers: 7
Collect server api objects...


Server Summary [#7]
-------------------

+---------+-----+-----------+------------+-----+--------------------+--------+----------------+------------+-----------+
| SF      | MF  | Name      | Moid       | Tag | Model              | Serial | IP             | CPU        | Memory    |
+---------+-----+-----------+------------+-----+--------------------+--------+----------------+------------+-----------+
| P+ H    | CRi | Server940 | Moid-value | --  | (R) UCSC-C240-M5SN | SN-88  | 10.4.144.211   | 2S 40C 80T | 384 [GiB] |
| P+ H    | CRi | Server864 | Moid-value | --  | (R) UCSC-C240-M5SN | SN-81  | 10.40.238.73   | 2S 40C 80T | 384 [GiB] |
| P+ H    | CRi | Server282 | Moid-value | --  | (R) UCSC-C240-M5SN | SN-13  | 10.115.69.102  | 2S 40C 80T | 384 [GiB] |
| P+ H    | CRi | Server756 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-76  | 10.40.12.198   | 2S 40C 80T | 384 [GiB] |
| P+ C(1) | CRi | Server255 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-16  | 10.34.65.109   | 2S 40C 80T | 384 [GiB] |
| P+ H    | CRi | Server563 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-14  | 10.148.222.247 | 2S 40C 80T | 384 [GiB] |
| P+ I(1) | CRi | Server658 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-72  | 10.174.236.88  | 2S 40C 80T | 384 [GiB] |
+---------+-----+-----------+------------+-----+--------------------+--------+----------------+------------+-----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)