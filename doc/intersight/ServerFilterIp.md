# Intersight Server

## Filter by ip

Examples

```
--ip 10.1.1.1
--ip 10.1.1.0/24
```

## IP Address

```
# iserver get server --ip 10.106.38.155

iaccount demo (cache: any)
Select servers...
Selected servers: 1
Collect server api objects...


Server Summary [#1]
-------------------

+---------+-----+-----------+------------+-----+--------------------+--------+---------------+------------+-----------+
| SF      | MF  | Name      | Moid       | Tag | Model              | Serial | IP            | CPU        | Memory    |
+---------+-----+-----------+------------+-----+--------------------+--------+---------------+------------+-----------+
| P+ I(1) | CRi | Server813 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-49  | 10.106.38.155 | 2S 40C 80T | 384 [GiB] |
+---------+-----+-----------+------------+-----+--------------------+--------+---------------+------------+-----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

## IP Subnet

```
# iserver get server --ip 10.0.0.0/8

iaccount demo (cache: any)
Select servers...
Selected servers: 13
Collect server api objects...


Server Summary [#13]
--------------------

+---------+-----+-----------+------------+-----+--------------------+--------+----------------+------------+-----------+
| SF      | MF  | Name      | Moid       | Tag | Model              | Serial | IP             | CPU        | Memory    |
+---------+-----+-----------+------------+-----+--------------------+--------+----------------+------------+-----------+
| P+ H    | CRi | Server733 | Moid-value | --  | (R) UCSC-C240-M5SN | SN-57  | 10.32.235.95   | 2S 40C 80T | 384 [GiB] |
| P+ H    | CRi | Server619 | Moid-value | --  | (R) UCSC-C240-M5SN | SN-42  | 10.213.27.55   | 2S 40C 80T | 384 [GiB] |
| P+ H    | CRi | Server675 | Moid-value | --  | (R) UCSC-C240-M5SN | SN-87  | 10.98.86.77    | 2S 40C 80T | 384 [GiB] |
| P+ H    | CRi | Server155 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-17  | 10.13.180.173  | 2S 40C 80T | 384 [GiB] |
| P+ C(1) | CRi | Server181 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-21  | 10.161.17.63   | 2S 40C 80T | 384 [GiB] |
| P+ H    | CRi | Server442 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-53  | 10.217.146.177 | 2S 40C 80T | 384 [GiB] |
| P+ I(1) | CRi | Server136 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-99  | 10.203.92.16   | 2S 40C 80T | 384 [GiB] |
| P+ I(1) | CRi | Server550 | Moid-value | --  | (R) UCSC-C240-M4SX | SN-77  | 10.209.104.78  | 2S 16C 32T | 128 [GiB] |
| P+ I(1) | Cri | Server451 | Moid-value | --  | (R) UCSC-C240-M4SX | SN-57  | 10.231.173.19  | 2S 16C 32T | 128 [GiB] |
| P+ I(1) | Cri | Server195 | Moid-value | --  | (R) UCSC-C240-M4SX | SN-73  | 10.53.221.110  | 2S 16C 32T | 128 [GiB] |
| P+ H    | CRi | Server654 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-80  | 10.171.5.126   | 2S 40C 80T | 384 [GiB] |
| P+ H    | CRi | Server794 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-20  | 10.133.236.241 | 2S 48C 96T | 512 [GiB] |
| P+ H    | CRi | Server746 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-59  | 10.200.120.170 | 2S 48C 96T | 512 [GiB] |
+---------+-----+-----------+------------+-----+--------------------+--------+----------------+------------+-----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)