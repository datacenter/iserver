# Intersight Server

## state view

```
# iserver get server --group test

iaccount demo (cache: any)
Select servers...
Selected servers: 8
Collect server api objects...


Server Summary [#8]
-------------------

+---------+-----+-----------+------------+-----+--------------------+--------+----------------+-------------+-----------+
| SF      | MF  | Name      | Moid       | Tag | Model              | Serial | IP             | CPU         | Memory    |
+---------+-----+-----------+------------+-----+--------------------+--------+----------------+-------------+-----------+
| P+ H    | CRi | Server722 | Moid-value | --  | (R) UCSC-C240-M5SN | SN-22  | 10.144.240.70  | 2S 40C 80T  | 384 [GiB] |
| P+ H    | CRi | Server686 | Moid-value | --  | (R) UCSC-C240-M5SN | SN-75  | 10.186.4.69    | 2S 40C 80T  | 384 [GiB] |
| P+ H    | CRi | Server319 | Moid-value | --  | (R) UCSC-C240-M5SN | SN-32  | 10.65.182.94   | 2S 40C 80T  | 384 [GiB] |
| P+ C(1) | CRi | Server620 | Moid-value | --  | (R) UCSC-C225-M6S  | SN-47  | 10.135.23.168  | 1S 64C 128T | 512 [GiB] |
| P+ H    | Cu  | Server847 | Moid-value | --  | (B) UCSB-B200-M5   | SN-38  | 10.112.184.163 | 2S 40C 80T  | 512 [GiB] |
| P+ H    | Cu  | Server321 | Moid-value | --  | (B) UCSB-B200-M5   | SN-71  | 10.76.202.182  | 2S 40C 80T  | 512 [GiB] |
| P+ H    | Cu  | Server483 | Moid-value | --  | (B) UCSB-B200-M5   | SN-38  | 10.137.146.32  | 2S 40C 80T  | 512 [GiB] |
| P+ H    | Cu  | Server728 | Moid-value | --  | (B) UCSB-B200-M5   | SN-90  | 10.44.75.148   | 2S 40C 80T  | 512 [GiB] |
+---------+-----+-----------+------------+-----+--------------------+--------+----------------+-------------+-----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)