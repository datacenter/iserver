# Intersight Server

## Filter by cpu

Examples

```
--cpu core:ge128
--cpu socket:eq1
--cpu thread:ge128
--cpu vendor:amd
--cpu arch:zen
--cpu model:7413
```

Core filtering options:
- "--cpu core:28" will select servers with 28 CPU cores
- "--cpu core:gt28" will select servers with >28 CPU cores
- "--cpu core:ge28" will select servers with >=28 CPU cores
- "--cpu core:le28" will select servers with <=28 CPU cores
- "--cpu core:lt28" will select servers with <28 CPU cores
- "--cpu core:ne28" will select servers with !=28 CPU cores

The same applies to socket and thread filtering.

## Equal

```
# iserver get server --cpu core:40

iaccount demo (cache: any)
Select servers...
Selected servers: 121
Collect server api objects...


Server Summary [#23]
--------------------

+---------+-----+-----------+------------+-----+--------------------+--------+----------------+------------+-----------+
| SF      | MF  | Name      | Moid       | Tag | Model              | Serial | IP             | CPU        | Memory    |
+---------+-----+-----------+------------+-----+--------------------+--------+----------------+------------+-----------+
| P+ C(1) | cri | Server524 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-41  | 10.46.188.253  | 2S 40C 80T | 384 [GiB] |
| P+ H    | cri | Server335 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-90  | 10.81.65.177   | 2S 40C 80T | 384 [GiB] |
| P+ H    | Cri | Server543 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-10  | 10.60.128.139  | 2S 40C 80T | 352 [GiB] |
| P+ H    | CRi | Server434 | Moid-value | --  | (R) UCSC-C240-M5SN | SN-38  | 10.10.113.226  | 2S 40C 80T | 384 [GiB] |
| P+ H    | CRi | Server986 | Moid-value | --  | (R) UCSC-C240-M5SN | SN-23  | 10.17.78.137   | 2S 40C 80T | 384 [GiB] |
| P+ H    | CRi | Server790 | Moid-value | --  | (R) UCSC-C240-M5SN | SN-25  | 10.130.240.179 | 2S 40C 80T | 384 [GiB] |
| P+ H    | CRi | Server730 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-54  | 10.234.63.249  | 2S 40C 80T | 384 [GiB] |
| P+ C(1) | CRi | Server750 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-13  | 10.200.62.172  | 2S 40C 80T | 384 [GiB] |
| P+ H    | CRi | Server547 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-14  | 10.139.3.50    | 2S 40C 80T | 384 [GiB] |
| P+ I(1) | CRi | Server250 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-72  | 10.149.94.92   | 2S 40C 80T | 384 [GiB] |
| P+ C(1) | CRi | Server349 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-91  | 10.11.13.229   | 2S 40C 40T | 384 [GiB] |
| P+ H    | CRi | Server152 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-46  | 10.138.53.66   | 2S 40C 80T | 384 [GiB] |
| P+ H    | Cu  | Server230 | Moid-value | --  | (R) HXAF220C-M5SN  | SN-43  | 10.199.136.83  | 2S 40C 80T | 384 [GiB] |
| P+ H    | Cu  | Server301 | Moid-value | --  | (R) HXAF220C-M5SN  | SN-86  | 10.94.54.170   | 2S 40C 80T | 384 [GiB] |
| P+ H    | Cu  | Server489 | Moid-value | --  | (B) UCSB-B200-M5   | SN-71  | 10.22.175.221  | 2S 40C 80T | 512 [GiB] |
| P+ H    | Cu  | Server352 | Moid-value | --  | (B) UCSB-B200-M5   | SN-17  | 10.114.217.207 | 2S 40C 80T | 512 [GiB] |
| P+ H    | Cu  | Server957 | Moid-value | --  | (B) UCSB-B200-M5   | SN-82  | 10.141.213.173 | 2S 40C 80T | 512 [GiB] |
| P+ H    | Cu  | Server490 | Moid-value | --  | (B) UCSB-B200-M5   | SN-34  | 10.38.126.32   | 2S 40C 80T | 512 [GiB] |
| P+ H    | Cu  | Server577 | Moid-value | --  | (R) HXAF220C-M5SN  | SN-34  | 10.17.233.160  | 2S 40C 80T | 384 [GiB] |
| P+ H    | Cu  | Server140 | Moid-value | --  | (R) HXAF220C-M5SN  | SN-22  | 10.96.196.191  | 2S 40C 80T | 384 [GiB] |
| P+ H    | CRi | Server478 | Moid-value | --  | (R) UCSC-C240-M5SN | SN-17  | 10.22.155.174  | 2S 40C 80T | 384 [GiB] |
| P+ C(1) | CRi | Server332 | Moid-value | --  | (R) UCSC-C240-M5SN | SN-75  | 10.138.220.145 | 2S 40C 80T | 384 [GiB] |
| P+ H    | CRi | Server661 | Moid-value | --  | (R) UCSC-C240-M5SN | SN-90  | 10.148.134.149 | 2S 40C 80T | 384 [GiB] |
+---------+-----+-----------+------------+-----+--------------------+--------+----------------+------------+-----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

## Lower or Equal

```
# iserver get server --cpu core:le30

iaccount demo (cache: any)
Select servers...
Selected servers: 121
Collect server api objects...


Server Summary [#57]
--------------------

+-----------+-----+-----------+------------+-----+--------------------+--------+----------------+------------+-----------+
| SF        | MF  | Name      | Moid       | Tag | Model              | Serial | IP             | CPU        | Memory    |
+-----------+-----+-----------+------------+-----+--------------------+--------+----------------+------------+-----------+
| P+ C(3)   | Cri | Server860 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-31  | 10.221.188.84  | 2S 20C 40T | 192 [GiB] |
| P+ C(1)   | Cri | Server131 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-58  | 10.6.156.101   | 2S 20C 40T | 192 [GiB] |
| P+ C(3)   | Cri | Server570 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-21  | 10.161.54.228  | 2S 20C 40T | 192 [GiB] |
| P+ H      | Cri | Server829 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-36  | 10.69.126.120  | 2S 28C 56T | 256 [GiB] |
| P+ H      | Cri | Server907 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-18  | 10.176.192.95  | 2S 28C 56T | 256 [GiB] |
| P+ C(1)   | Cri | Server907 | Moid-value | --  | (R) UCSC-C240-M4SX | SN-96  | 10.49.219.206  | 2S 24C 48T | 256 [GiB] |
| P+ H      | CRi | Server838 | Moid-value | --  | (R) APIC-SERVER-M3 | SN-99  | 10.172.130.242 | 2S 16C 16T | 96 [GiB]  |
| P+ H      | CRi | Server429 | Moid-value | --  | (R) APIC-SERVER-M3 | SN-43  | 10.38.7.189    | 2S 16C 16T | 96 [GiB]  |
| P+ H L    | CRi | Server821 | Moid-value | --  | (R) APIC-SERVER-M3 | SN-94  | 10.85.123.245  | 2S 16C 16T | 96 [GiB]  |
| P+ H L    | CRi | Server401 | Moid-value | --  | (R) APIC-SERVER-M3 | SN-50  | 10.18.240.163  | 2S 16C 16T | 96 [GiB]  |
| P+ H      | CRi | Server318 | Moid-value | --  | (R) APIC-SERVER-M3 | SN-26  | 10.160.3.142   | 2S 16C 16T | 96 [GiB]  |
| P+ H      | CRi | Server662 | Moid-value | --  | (R) APIC-SERVER-M3 | SN-95  | 10.164.70.202  | 2S 16C 16T | 96 [GiB]  |
| P+ W(2)   | Cri | Server429 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-27  | 10.139.72.137  | 2S 28C 56T | 256 [GiB] |
| P+ I(1)   | CRi | Server593 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-33  | 10.122.110.80  | 2S 16C 32T | 256 [GiB] |
| P+ I(1)   | Cri | Server229 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-98  | 10.30.232.112  | 2S 16C 32T | 128 [GiB] |
| P+ I(1)   | CRi | Server879 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-32  | 10.87.168.135  | 2S 28C 56T | 256 [GiB] |
| P+ H      | Cri | Server560 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-29  | 10.227.139.221 | 2S 16C 32T | 256 [GiB] |
| P+ I(1)   | CRi | Server622 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-26  | 10.154.98.177  | 2S 16C 32T | 256 [GiB] |
| P+ H      | CRi | Server740 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-33  | 10.32.195.190  | 2S 16C 32T | 256 [GiB] |
| P+ C(3)   | CRi | Server554 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-19  | 10.239.208.222 | 2S 28C 56T | 256 [GiB] |
| P+ I(1)   | CRi | Server114 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-40  | 10.212.152.196 | 2S 24C 48T | 256 [GiB] |
| P+ I(1)   | cRi | Server731 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-31  | 10.54.197.14   | 2S 24C 48T | 256 [GiB] |
| P+ H      | CRi | Server408 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-68  | 10.111.32.30   | 2S 28C 56T | 256 [GiB] |
| P- H      | cRi | Server781 | Moid-value | --  | (R) UCSC-C240-M5SX | SN-92  | 10.87.167.47   | 2S 24C 24T | 384 [GiB] |
| P+ I(1)   | CRi | Server746 | Moid-value | --  | (R) UCSC-C240-M4SX | SN-95  | 10.148.215.189 | 2S 16C 32T | 128 [GiB] |
| P- H      | cRi | Server960 | Moid-value | --  | (R) UCSC-C240-M5SX | SN-81  | 10.139.90.64   | 2S 24C 48T | 384 [GiB] |
| P+ I(1)   | Cri | Server807 | Moid-value | --  | (R) UCSC-C240-M4SX | SN-72  | 10.217.131.250 | 2S 16C 32T | 128 [GiB] |
| P- H      | cRi | Server165 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-33  | 10.94.164.163  | 2S 16C 16T | 384 [GiB] |
| P+ I(1)   | Cri | Server184 | Moid-value | --  | (R) UCSC-C240-M4SX | SN-32  | 10.90.159.185  | 2S 16C 32T | 128 [GiB] |
| P+ H      | Cri | Server334 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-78  | 10.175.29.119  | 2S 24C 24T | 256 [GiB] |
| P- H      | cRi | Server478 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-76  | 10.78.86.47    | 2S 24C 24T | 384 [GiB] |
| P+ W(4) L | Cri | Server967 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-27  | 10.8.254.225   | 2S 28C 56T | 256 [GiB] |
| P- H      | cRi | Server228 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-85  | 10.58.193.120  | 2S 28C 56T | 256 [GiB] |
| P+ H      | Cri | Server557 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-60  | 10.72.108.28   | 2S 24C 48T | 384 [GiB] |
| P- H      | cRi | Server144 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-99  | 10.48.186.27   | 2S 28C 56T | 256 [GiB] |
| P- I(1)   | cri | Server778 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-46  | 10.112.166.186 | 2S 16C 32T | 256 [GiB] |
| P- H      | cri | Server998 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-87  | 10.8.107.229   | 2S 28C 56T | 256 [GiB] |
| P+ H      | cri | Server398 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-89  | 10.253.22.39   | 2S 24C 48T | 192 [GiB] |
| P+ C(1)   | cRi | Server131 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-57  | 10.218.134.103 | 2S 28C 56T | 256 [GiB] |
| P+ H      | Cri | Server127 | Moid-value | --  | (R) UCSC-C240-M5SX | SN-73  | 10.184.38.242  | 2S 28C 56T | 384 [GiB] |
| P- H      | cri | Server162 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-94  | 10.191.144.209 | 2S 16C 32T | 256 [GiB] |
| P+ H      | cri | Server517 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-16  | 10.16.130.91   | 2S 28C 56T | 256 [GiB] |
| P- W(1)   | Cu  | Server662 | Moid-value | --  | (B) UCSB-B200-M4   | SN-50  | 10.237.72.189  | 2S 24C 48T | 512 [GiB] |
| P- W(1)   | Cu  | Server167 | Moid-value | --  | (B) UCSB-B200-M4   | SN-27  | 10.105.49.37   | 2S 24C 48T | 512 [GiB] |
| P- W(1)   | Cu  | Server333 | Moid-value | --  | (B) UCSB-B200-M4   | SN-35  | 10.229.11.61   | 2S 24C 48T | 256 [GiB] |
| P- C(9)   | Cu  | Server604 | Moid-value | --  | (B) UCSB-B200-M4   | SN-84  | 10.96.253.45   | 2S 24C 48T | 256 [GiB] |
| P+ C(1)   | CRi | Server217 | Moid-value | --  | (R) SE-NODE-G2     | SN-38  | 10.73.199.141  | 2S 20C 40T | 256 [GiB] |
| P+ H      | CRi | Server643 | Moid-value | --  | (R) SE-NODE-G2     | SN-81  | 10.3.158.152   | 2S 20C 40T | 256 [GiB] |
| P+ C(1)   | CRi | Server484 | Moid-value | --  | (R) SE-NODE-G2     | SN-51  | 10.165.158.22  | 2S 20C 40T | 256 [GiB] |
| P+ H      | Cri | Server495 | Moid-value | --  | (R) UCSC-C240-M5SX | SN-58  | 10.93.30.18    | 2S 28C 56T | 256 [GiB] |
| P+ H      | CRi | Server928 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-61  | 10.140.39.60   | 2S 16C 32T | 256 [GiB] |
| P+ I(1)   | Cri | Server692 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-86  | 10.35.187.65   | 2S 28C 56T | 256 [GiB] |
| P+ W(2)   | Cri | Server693 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-46  | 10.204.77.49   | 2S 28C 56T | 256 [GiB] |
| P+ C(1)   | Cri | Server121 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-60  | 10.230.201.248 | 2S 28C 56T | 256 [GiB] |
| P- H      | cri | Server480 | Moid-value | --  | (R) UCSC-C240-M4SX | SN-36  | 10.97.82.192   | 2S 16C 32T | 128 [GiB] |
| P+ H      | Cri | Server668 | Moid-value | --  | (B) UCSC-C3K-M4SRB | SN-17  | 10.254.92.119  | 2S 24C 48T | 256 [GiB] |
| P+ C(1)   | Cri | Server453 | Moid-value | --  | (R) UCSC-C240-M5SX | SN-19  | 10.6.199.107   | 2S 24C 48T | 256 [GiB] |
+-----------+-----+-----------+------------+-----+--------------------+--------+----------------+------------+-----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

## Greater or Equal

```
# iserver get server --cpu core:ge100

iaccount demo (cache: any)
Select servers...
Selected servers: 121
Collect server api objects...


Server Summary [#1]
-------------------

+------+-----+-----------+------------+-----+--------------------+--------+------------+--------------+-----------+
| SF   | MF  | Name      | Moid       | Tag | Model              | Serial | IP         | CPU          | Memory    |
+------+-----+-----------+------------+-----+--------------------+--------+------------+--------------+-----------+
| P+ H | CRi | Server621 | Moid-value | --  | (R) UCSC-C245-M6SX | SN-43  | 10.5.55.98 | 2S 128C 256T | 512 [GiB] |
+------+-----+-----------+------------+-----+--------------------+--------+------------+--------------+-----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

## Vendor

```
# iserver get server --cpu vendor:amd -v cpu

iaccount demo (cache: any)
Select servers...
Selected servers: 121
Collect server api objects...


CPU [#6]
--------

+-----------+-------+--------+--------+--------+------+-------------------------------------------------+-------+---------+---------+-------------+----------+----------+-----------+
| Server    | State | CPU Id | Socket | Vendor | Arch | Model                                           | Cores | Enabled | Threads | Speed [GHz] | Stepping | Presence | OperState |
+-----------+-------+--------+--------+--------+------+-------------------------------------------------+-------+---------+---------+-------------+----------+----------+-----------+
| Server367 | V     | 1      | CPU1   | AMD    | Zen  | AMD EPYC 7413 24-Core Processor                 | 24    | 24      | 48      | 2.65        | 1        | equipped | operable  |
| Server367 | V     | 2      | CPU2   | AMD    | Zen  | AMD EPYC 7413 24-Core Processor                 | 24    | 24      | 48      | 2.65        | 1        | equipped | operable  |
| Server832 | V     | 1      | CPU1   | AMD    | Zen  | AMD EPYC 7763 64-Core Processor                 | 64    | 64      | 128     | 2.45        | 1        | equipped | operable  |
| Server832 | V     | 2      | CPU2   | AMD    | Zen  | AMD EPYC 7763 64-Core Processor                 | 64    | 64      | 128     | 2.45        | 1        | equipped | operable  |
| Server372 | V     | 1      | CPU1   | AMD    | Zen  | AMD EPYC 7763 64-Core Processor                 | 64    | 64      | 128     | 2.45        | 1        | equipped | operable  |
| Server470 | V     | 1      | CPU1   | AMD    | Zen  | AMD EPYC 7543 32-Core Processor                 | 32    | 32      | 64      | 2.8         | 1        | equipped | operable  |
+-----------+-------+--------+--------+--------+------+-------------------------------------------------+-------+---------+---------+-------------+----------+----------+-----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

## arch

```
# iserver get server --cpu arch:zen -v cpu

iaccount demo (cache: any)
Select servers...
Selected servers: 121
Collect server api objects...


CPU [#6]
--------

+-----------+-------+--------+--------+--------+------+-------------------------------------------------+-------+---------+---------+-------------+----------+----------+-----------+
| Server    | State | CPU Id | Socket | Vendor | Arch | Model                                           | Cores | Enabled | Threads | Speed [GHz] | Stepping | Presence | OperState |
+-----------+-------+--------+--------+--------+------+-------------------------------------------------+-------+---------+---------+-------------+----------+----------+-----------+
| Server348 | V     | 1      | CPU1   | AMD    | Zen  | AMD EPYC 7413 24-Core Processor                 | 24    | 24      | 48      | 2.65        | 1        | equipped | operable  |
| Server348 | V     | 2      | CPU2   | AMD    | Zen  | AMD EPYC 7413 24-Core Processor                 | 24    | 24      | 48      | 2.65        | 1        | equipped | operable  |
| Server324 | V     | 1      | CPU1   | AMD    | Zen  | AMD EPYC 7763 64-Core Processor                 | 64    | 64      | 128     | 2.45        | 1        | equipped | operable  |
| Server324 | V     | 2      | CPU2   | AMD    | Zen  | AMD EPYC 7763 64-Core Processor                 | 64    | 64      | 128     | 2.45        | 1        | equipped | operable  |
| Server935 | V     | 1      | CPU1   | AMD    | Zen  | AMD EPYC 7763 64-Core Processor                 | 64    | 64      | 128     | 2.45        | 1        | equipped | operable  |
| Server594 | V     | 1      | CPU1   | AMD    | Zen  | AMD EPYC 7543 32-Core Processor                 | 32    | 32      | 64      | 2.8         | 1        | equipped | operable  |
+-----------+-------+--------+--------+--------+------+-------------------------------------------------+-------+---------+---------+-------------+----------+----------+-----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

## Model

```
# iserver get server --cpu model:7413 -v cpu

iaccount demo (cache: any)
Select servers...
Selected servers: 121
Collect server api objects...


CPU [#2]
--------

+-----------+-------+--------+--------+--------+------+-------------------------------------------------+-------+---------+---------+-------------+----------+----------+-----------+
| Server    | State | CPU Id | Socket | Vendor | Arch | Model                                           | Cores | Enabled | Threads | Speed [GHz] | Stepping | Presence | OperState |
+-----------+-------+--------+--------+--------+------+-------------------------------------------------+-------+---------+---------+-------------+----------+----------+-----------+
| Server576 | V     | 1      | CPU1   | AMD    | Zen  | AMD EPYC 7413 24-Core Processor                 | 24    | 24      | 48      | 2.65        | 1        | equipped | operable  |
| Server576 | V     | 2      | CPU2   | AMD    | Zen  | AMD EPYC 7413 24-Core Processor                 | 24    | 24      | 48      | 2.65        | 1        | equipped | operable  |
+-----------+-------+--------+--------+--------+------+-------------------------------------------------+-------+---------+---------+-------------+----------+----------+-----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)