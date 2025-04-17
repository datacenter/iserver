# Intersight Server

## Filter by model

```
# iserver get server --model *m5sn*

iaccount demo (cache: any)
Select servers...
Selected servers: 10
Collect server api objects...


Server Summary [#10]
--------------------

+---------+-----+-----------+------------+-----+--------------------+--------+----------------+------------+-----------+
| SF      | MF  | Name      | Moid       | Tag | Model              | Serial | IP             | CPU        | Memory    |
+---------+-----+-----------+------------+-----+--------------------+--------+----------------+------------+-----------+
| P+ H    | CRi | Server661 | Moid-value | --  | (R) UCSC-C240-M5SN | SN-31  | 10.62.149.9    | 2S 40C 80T | 384 [GiB] |
| P+ H    | CRi | Server767 | Moid-value | --  | (R) UCSC-C240-M5SN | SN-28  | 10.127.39.61   | 2S 40C 80T | 384 [GiB] |
| P+ H    | CRi | Server565 | Moid-value | --  | (R) UCSC-C240-M5SN | SN-53  | 10.220.209.140 | 2S 40C 80T | 384 [GiB] |
| P+ H    | Cu  | Server565 | Moid-value | --  | (R) HXAF220C-M5SN  | SN-94  | 10.212.158.92  | 2S 40C 80T | 384 [GiB] |
| P+ H    | Cu  | Server340 | Moid-value | --  | (R) HXAF220C-M5SN  | SN-54  | 10.173.74.184  | 2S 40C 80T | 384 [GiB] |
| P+ H    | Cu  | Server869 | Moid-value | --  | (R) HXAF220C-M5SN  | SN-41  | 10.194.113.218 | 2S 40C 80T | 384 [GiB] |
| P+ H    | Cu  | Server560 | Moid-value | --  | (R) HXAF220C-M5SN  | SN-29  | 10.143.29.31   | 2S 40C 80T | 384 [GiB] |
| P+ H    | CRi | Server707 | Moid-value | --  | (R) UCSC-C240-M5SN | SN-82  | 10.245.210.199 | 2S 40C 80T | 384 [GiB] |
| P+ C(1) | CRi | Server374 | Moid-value | --  | (R) UCSC-C240-M5SN | SN-33  | 10.56.66.61    | 2S 40C 80T | 384 [GiB] |
| P+ H    | CRi | Server236 | Moid-value | --  | (R) UCSC-C240-M5SN | SN-25  | 10.145.142.55  | 2S 40C 80T | 384 [GiB] |
+---------+-----+-----------+------------+-----+--------------------+--------+----------------+------------+-----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)