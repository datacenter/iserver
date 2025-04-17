# Intersight Server

## Filter by mode

Examples

```
--mode imm
--mode ucsm
```

## UCSM

```
# iserver get server --mode ucsm

iaccount demo (cache: any)
Select servers...
Selected servers: 121
Collect server api objects...


Server Summary [#15]
--------------------

+---------+----+-----------+------------+-----+-------------------+--------+----------------+-------------+-----------+
| SF      | MF | Name      | Moid       | Tag | Model             | Serial | IP             | CPU         | Memory    |
+---------+----+-----------+------------+-----+-------------------+--------+----------------+-------------+-----------+
| P+ H    | Cu | Server797 | Moid-value | --  | (R) HXAF220C-M5SN | SN-21  | 10.123.165.81  | 2S 40C 80T  | 384 [GiB] |
| P- W(1) | Cu | Server750 | Moid-value | --  | (B) UCSB-B200-M4  | SN-92  | 10.110.208.112 | 2S 24C 48T  | 512 [GiB] |
| P- W(1) | Cu | Server683 | Moid-value | --  | (B) UCSB-B200-M4  | SN-76  | 10.19.191.63   | 2S 24C 48T  | 512 [GiB] |
| P- W(1) | Cu | Server238 | Moid-value | --  | (B) UCSB-B200-M4  | SN-44  | 10.128.44.9    | 2S 24C 48T  | 256 [GiB] |
| P- C(9) | Cu | Server359 | Moid-value | --  | (B) UCSB-B200-M4  | SN-57  | 10.172.179.229 | 2S 24C 48T  | 256 [GiB] |
| P+ H    | Cu | Server915 | Moid-value | --  | (R) HXAF220C-M5SN | SN-67  | 10.48.234.74   | 2S 40C 80T  | 384 [GiB] |
| P+ H    | Cu | Server961 | Moid-value | --  | (B) UCSB-B200-M5  | SN-35  | 10.147.230.156 | 2S 40C 80T  | 512 [GiB] |
| P+ H    | Cu | Server990 | Moid-value | --  | (B) UCSB-B200-M5  | SN-89  | 10.202.233.230 | 2S 40C 80T  | 512 [GiB] |
| P+ H    | Cu | Server131 | Moid-value | --  | (B) UCSB-B200-M5  | SN-62  | 10.90.43.253   | 2S 40C 80T  | 512 [GiB] |
| P+ H    | Cu | Server708 | Moid-value | --  | (B) UCSB-B200-M5  | SN-88  | 10.4.131.118   | 2S 40C 80T  | 512 [GiB] |
| P+ H    | Cu | Server521 | Moid-value | --  | (R) HXAF220C-M5SN | SN-48  | 10.92.225.218  | 2S 40C 80T  | 384 [GiB] |
| P+ H    | Cu | Server149 | Moid-value | --  | (R) HXAF220C-M5SN | SN-80  | 10.250.103.10  | 2S 40C 80T  | 384 [GiB] |
| P+ H    | Cu | Server983 | Moid-value | --  | (R) HXAF240C-M5SX | SN-81  | 10.156.231.35  | 2S 52C 104T | 768 [GiB] |
| P+ H    | Cu | Server860 | Moid-value | --  | (R) HXAF240C-M5SX | SN-58  | 10.78.171.3    | 2S 52C 104T | 768 [GiB] |
| P+ H    | Cu | Server956 | Moid-value | --  | (R) HXAF240C-M5SX | SN-42  | 10.175.148.158 | 2S 52C 104T | 768 [GiB] |
+---------+----+-----------+------------+-----+-------------------+--------+----------------+-------------+-----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)