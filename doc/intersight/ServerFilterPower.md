# Intersight Server

## Filter by power state

Examples

```
--power on
--power off
```

## Power off

```
# iserver get server --power off

iaccount demo (cache: any)
Select servers...
Selected servers: 121
Collect server api objects...


Server Summary [#18]
--------------------

+---------+-----+-----------+------------+-----+--------------------+--------+----------------+-------------+-----------+
| SF      | MF  | Name      | Moid       | Tag | Model              | Serial | IP             | CPU         | Memory    |
+---------+-----+-----------+------------+-----+--------------------+--------+----------------+-------------+-----------+
| P- H    | cRi | Server849 | Moid-value | --  | (R) UCSC-C240-M5SX | SN-67  | 10.249.55.121  | 2S 48C 96T  | 384 [GiB] |
| P- H    | cRi | Server460 | Moid-value | --  | (R) UCSC-C240-M5SX | SN-81  | 10.141.12.103  | 2S 24C 24T  | 384 [GiB] |
| P- H    | cRi | Server157 | Moid-value | --  | (R) UCSC-C240-M5SX | SN-65  | 10.156.234.113 | 2S 24C 48T  | 384 [GiB] |
| P- H    | cRi | Server877 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-75  | 10.15.183.12   | 2S 16C 16T  | 384 [GiB] |
| P- H    | cRi | Server472 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-20  | 10.16.218.211  | 2S 24C 24T  | 384 [GiB] |
| P- H    | cRi | Server131 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-61  | 10.6.190.225   | 2S 28C 56T  | 256 [GiB] |
| P- H    | cRi | Server329 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-68  | 10.204.138.59  | 2S 28C 56T  | 256 [GiB] |
| P- I(1) | cri | Server791 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-83  | 10.81.8.71     | 2S 16C 32T  | 256 [GiB] |
| P- H    | cri | Server629 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-53  | 10.181.110.133 | 2S 28C 56T  | 256 [GiB] |
| P- C(1) | cRi | Server427 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-30  | 10.32.126.173  | 2S 36C 72T  | 512 [GiB] |
| P- H    | cri | Server891 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-84  | 10.70.30.62    | 2S 16C 32T  | 256 [GiB] |
| P- W(1) | Cu  | Server764 | Moid-value | --  | (B) UCSB-B200-M4   | SN-11  | 10.32.151.104  | 2S 24C 48T  | 512 [GiB] |
| P- W(1) | Cu  | Server776 | Moid-value | --  | (B) UCSB-B200-M4   | SN-49  | 10.220.162.70  | 2S 24C 48T  | 512 [GiB] |
| P- W(1) | Cu  | Server482 | Moid-value | --  | (B) UCSB-B200-M4   | SN-63  | 10.70.18.135   | 2S 24C 48T  | 256 [GiB] |
| P- C(9) | Cu  | Server847 | Moid-value | --  | (B) UCSB-B200-M4   | SN-55  | 10.158.90.121  | 2S 24C 48T  | 256 [GiB] |
| P- H    | Cri | Server425 | Moid-value | --  | (B) UCSX-210C-M6   | SN-23  | 10.192.201.153 | 2S 64C 128T | 512 [GiB] |
| P- H    | Cri | Server804 | Moid-value | --  | (B) UCSX-210C-M6   | SN-25  | 10.23.127.239  | 2S 64C 128T | 512 [GiB] |
| P- H    | cri | Server195 | Moid-value | --  | (R) UCSC-C240-M4SX | SN-25  | 10.42.153.94   | 2S 16C 32T  | 128 [GiB] |
+---------+-----+-----------+------------+-----+--------------------+--------+----------------+-------------+-----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)