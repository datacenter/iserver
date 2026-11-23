# Intersight Server

## Default output

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
| P+ H    | CRi | Server382 | Moid-value | --  | (R) UCSC-C240-M5SN | SN-31  | 10.69.37.10    | 2S 40C 80T  | 384 [GiB] |
| P+ H    | CRi | Server330 | Moid-value | --  | (R) UCSC-C240-M5SN | SN-28  | 10.233.79.49   | 2S 40C 80T  | 384 [GiB] |
| P+ H    | CRi | Server782 | Moid-value | --  | (R) UCSC-C240-M5SN | SN-19  | 10.146.172.12  | 2S 40C 80T  | 384 [GiB] |
| P+ C(1) | CRi | Server171 | Moid-value | --  | (R) UCSC-C225-M6S  | SN-44  | 10.235.70.63   | 1S 64C 128T | 512 [GiB] |
| P+ H    | Cu  | Server786 | Moid-value | --  | (B) UCSB-B200-M5   | SN-87  | 10.28.52.208   | 2S 40C 80T  | 512 [GiB] |
| P+ H    | Cu  | Server898 | Moid-value | --  | (B) UCSB-B200-M5   | SN-11  | 10.58.122.15   | 2S 40C 80T  | 512 [GiB] |
| P+ H    | Cu  | Server115 | Moid-value | --  | (B) UCSB-B200-M5   | SN-73  | 10.47.33.132   | 2S 40C 80T  | 512 [GiB] |
| P+ H    | Cu  | Server996 | Moid-value | --  | (B) UCSB-B200-M5   | SN-42  | 10.119.247.182 | 2S 40C 80T  | 512 [GiB] |
+---------+-----+-----------+------------+-----+--------------------+--------+----------------+-------------+-----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)