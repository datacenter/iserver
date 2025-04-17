# Intersight Server

## Filter by disconnected

```
# iserver get server --disc

iaccount demo (cache: any)
Select servers...
Selected servers: 121
Collect server api objects...


Server Summary [#18]
--------------------

+---------+-----+-----------+------------+-----+--------------------+--------+----------------+------------+-----------+
| SF      | MF  | Name      | Moid       | Tag | Model              | Serial | IP             | CPU        | Memory    |
+---------+-----+-----------+------------+-----+--------------------+--------+----------------+------------+-----------+
| P+ C(1) | cri | Server142 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-22  | 10.95.66.98    | 2S 40C 80T | 384 [GiB] |
| P+ H    | cri | Server997 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-90  | 10.246.97.111  | 2S 40C 80T | 384 [GiB] |
| P+ I(1) | cRi | Server218 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-61  | 10.219.242.121 | 2S 24C 48T | 256 [GiB] |
| P- H    | cRi | Server250 | Moid-value | --  | (R) UCSC-C240-M5SX | SN-53  | 10.211.116.150 | 2S 48C 96T | 384 [GiB] |
| P- H    | cRi | Server275 | Moid-value | --  | (R) UCSC-C240-M5SX | SN-26  | 10.8.145.157   | 2S 24C 24T | 384 [GiB] |
| P- H    | cRi | Server731 | Moid-value | --  | (R) UCSC-C240-M5SX | SN-70  | 10.135.220.206 | 2S 24C 48T | 384 [GiB] |
| P- H    | cRi | Server531 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-81  | 10.188.201.178 | 2S 16C 16T | 384 [GiB] |
| P- H    | cRi | Server794 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-80  | 10.43.111.205  | 2S 24C 24T | 384 [GiB] |
| P- H    | cRi | Server529 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-27  | 10.119.108.245 | 2S 28C 56T | 256 [GiB] |
| P- H    | cRi | Server502 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-19  | 10.102.187.200 | 2S 28C 56T | 256 [GiB] |
| P- I(1) | cri | Server925 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-49  | 10.150.142.74  | 2S 16C 32T | 256 [GiB] |
| P- H    | cri | Server342 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-98  | 10.117.158.121 | 2S 28C 56T | 256 [GiB] |
| P- C(1) | cRi | Server194 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-44  | 10.99.125.246  | 2S 36C 72T | 512 [GiB] |
| P+ H    | cri | Server914 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-37  | 10.111.16.2    | 2S 24C 48T | 192 [GiB] |
| P+ C(1) | cRi | Server878 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-83  | 10.252.190.77  | 2S 28C 56T | 256 [GiB] |
| P- H    | cri | Server629 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-77  | 10.194.134.123 | 2S 16C 32T | 256 [GiB] |
| P+ H    | cri | Server173 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-13  | 10.188.70.187  | 2S 28C 56T | 256 [GiB] |
| P- H    | cri | Server914 | Moid-value | --  | (R) UCSC-C240-M4SX | SN-69  | 10.229.39.177  | 2S 16C 32T | 128 [GiB] |
+---------+-----+-----------+------------+-----+--------------------+--------+----------------+------------+-----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)