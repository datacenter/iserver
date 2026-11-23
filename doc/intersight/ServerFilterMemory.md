# Intersight Server

## Filter by memory

Examples

```
--mem size:gt512
--mem dimm:gt12
--mem model:E2
--mem serial:myserial
```

Memory size filtering options:
- "--memory 128" will select servers with 128 [GiB] of memory
- "--memory gt128" will select servers with >128 [GiB] of memory
- "--memory ge128" will select servers with >=128 [GiB] of memory
- "--memory le128" will select servers with <=128 [GiB] of memory
- "--memory lt128" will select servers with <128 [GiB] of memory
- "--memory ne128" will select servers with !=128 [GiB] of memory

## Size Equal

```
# iserver get server --mem size:512

iaccount demo (cache: any)
Select servers...
Selected servers: 121
Collect server api objects...


Server Summary [#31]
--------------------

+---------+-----+-----------+------------+-----+--------------------+--------+----------------+--------------+-----------+
| SF      | MF  | Name      | Moid       | Tag | Model              | Serial | IP             | CPU          | Memory    |
+---------+-----+-----------+------------+-----+--------------------+--------+----------------+--------------+-----------+
| P+ H    | Cri | Server653 | Moid-value | --  | (R) UCSC-C240-M5SX | SN-22  | 10.45.34.175   | 2S 56C 112T  | 512 [GiB] |
| P+ C(1) | CRi | Server164 | Moid-value | --  | (R) UCSC-C240-M6N  | SN-18  | 10.67.254.185  | 2S 64C 128T  | 512 [GiB] |
| P+ H    | Cri | Server800 | Moid-value | --  | (R) UCSC-C240-M6SN | SN-52  | 10.2.28.192    | 2S 64C 128T  | 512 [GiB] |
| P+ H    | CRi | Server302 | Moid-value | --  | (R) UCSC-C240-M6N  | SN-40  | 10.135.73.166  | 2S 64C 128T  | 512 [GiB] |
| P+ C(1) | CRi | Server890 | Moid-value | --  | (R) UCSC-C240-M6SN | SN-66  | 10.66.142.22   | 2S 64C 128T  | 512 [GiB] |
| P+ H    | CRi | Server218 | Moid-value | --  | (R) UCSC-C245-M6SX | SN-86  | 10.13.192.154  | 2S 48C 96T   | 512 [GiB] |
| P+ H    | CRi | Server524 | Moid-value | --  | (R) UCSC-C240-M6N  | SN-15  | 10.238.34.9    | 2S 64C 128T  | 512 [GiB] |
| P+ H    | Cri | Server273 | Moid-value | --  | (R) UCSC-C240-M6SN | SN-55  | 10.222.2.18    | 2S 64C 128T  | 512 [GiB] |
| P+ H    | CRi | Server342 | Moid-value | --  | (R) UCSC-C240-M6N  | SN-57  | 10.183.148.92  | 2S 64C 128T  | 512 [GiB] |
| P+ H    | CRi | Server541 | Moid-value | --  | (R) UCSC-C240-M6SN | SN-50  | 10.185.107.239 | 2S 64C 128T  | 512 [GiB] |
| P+ H    | CRi | Server692 | Moid-value | --  | (R) UCSC-C245-M6SX | SN-74  | 10.100.94.18   | 2S 128C 256T | 512 [GiB] |
| P+ C(1) | CRi | Server560 | Moid-value | --  | (R) UCSC-C240-M6N  | SN-64  | 10.13.144.97   | 2S 64C 128T  | 512 [GiB] |
| P+ H    | CRi | Server278 | Moid-value | --  | (R) UCSC-C240-M6N  | SN-83  | 10.60.165.19   | 2S 64C 128T  | 512 [GiB] |
| P+ H    | CRi | Server845 | Moid-value | --  | (R) UCSC-C240-M6SN | SN-68  | 10.183.202.74  | 2S 64C 128T  | 512 [GiB] |
| P+ C(1) | CRi | Server842 | Moid-value | --  | (R) UCSC-C225-M6S  | SN-23  | 10.103.109.161 | 1S 64C 128T  | 512 [GiB] |
| P+ H    | CRi | Server725 | Moid-value | --  | (R) UCSC-C225-M6S  | SN-35  | 10.100.107.36  | 1S 32C 64T   | 512 [GiB] |
| P+ H    | CRi | Server573 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-76  | 10.128.178.215 | 2S 48C 96T   | 512 [GiB] |
| P+ H    | Cri | Server619 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-63  | 10.176.124.152 | 2S 48C 96T   | 512 [GiB] |
| P+ H    | CRi | Server940 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-45  | 10.37.102.96   | 2S 48C 96T   | 512 [GiB] |
| P+ H    | CRi | Server358 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-74  | 10.16.95.173   | 2S 48C 96T   | 512 [GiB] |
| P- C(1) | cRi | Server148 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-42  | 10.208.152.152 | 2S 36C 72T   | 512 [GiB] |
| P+ C(1) | CRi | Server877 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-38  | 10.154.179.31  | 2S 36C 72T   | 512 [GiB] |
| P- W(1) | Cu  | Server692 | Moid-value | --  | (B) UCSB-B200-M4   | SN-21  | 10.184.52.220  | 2S 24C 48T   | 512 [GiB] |
| P- W(1) | Cu  | Server367 | Moid-value | --  | (B) UCSB-B200-M4   | SN-92  | 10.146.87.176  | 2S 24C 48T   | 512 [GiB] |
| P+ H    | Cu  | Server862 | Moid-value | --  | (B) UCSB-B200-M5   | SN-53  | 10.151.37.74   | 2S 40C 80T   | 512 [GiB] |
| P+ H    | Cu  | Server943 | Moid-value | --  | (B) UCSB-B200-M5   | SN-18  | 10.217.67.213  | 2S 40C 80T   | 512 [GiB] |
| P+ H    | Cu  | Server200 | Moid-value | --  | (B) UCSB-B200-M5   | SN-11  | 10.124.83.193  | 2S 40C 80T   | 512 [GiB] |
| P+ H    | Cu  | Server169 | Moid-value | --  | (B) UCSB-B200-M5   | SN-75  | 10.222.121.86  | 2S 40C 80T   | 512 [GiB] |
| P+ H    | Cri | Server535 | Moid-value | --  | (B) UCSX-210C-M6   | SN-21  | 10.111.14.224  | 2S 64C 128T  | 512 [GiB] |
| P- H    | Cri | Server977 | Moid-value | --  | (B) UCSX-210C-M6   | SN-28  | 10.165.5.104   | 2S 64C 128T  | 512 [GiB] |
| P- H    | Cri | Server284 | Moid-value | --  | (B) UCSX-210C-M6   | SN-36  | 10.168.141.237 | 2S 64C 128T  | 512 [GiB] |
+---------+-----+-----------+------------+-----+--------------------+--------+----------------+--------------+-----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

## Size Lower or Equal

```
# iserver get server --mem size:le128

iaccount demo (cache: any)
Select servers...
Selected servers: 121
Collect server api objects...


Server Summary [#11]
--------------------

+---------+-----+-----------+------------+-----+--------------------+--------+----------------+------------+-----------+
| SF      | MF  | Name      | Moid       | Tag | Model              | Serial | IP             | CPU        | Memory    |
+---------+-----+-----------+------------+-----+--------------------+--------+----------------+------------+-----------+
| P+ H    | CRi | Server339 | Moid-value | --  | (R) APIC-SERVER-M3 | SN-99  | 10.22.114.61   | 2S 16C 16T | 96 [GiB]  |
| P+ H    | CRi | Server467 | Moid-value | --  | (R) APIC-SERVER-M3 | SN-34  | 10.160.147.98  | 2S 16C 16T | 96 [GiB]  |
| P+ H L  | CRi | Server384 | Moid-value | --  | (R) APIC-SERVER-M3 | SN-47  | 10.85.173.231  | 2S 16C 16T | 96 [GiB]  |
| P+ H L  | CRi | Server607 | Moid-value | --  | (R) APIC-SERVER-M3 | SN-97  | 10.191.220.140 | 2S 16C 16T | 96 [GiB]  |
| P+ H    | CRi | Server442 | Moid-value | --  | (R) APIC-SERVER-M3 | SN-85  | 10.74.80.202   | 2S 16C 16T | 96 [GiB]  |
| P+ H    | CRi | Server196 | Moid-value | --  | (R) APIC-SERVER-M3 | SN-66  | 10.210.163.77  | 2S 16C 16T | 96 [GiB]  |
| P+ I(1) | Cri | Server963 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-35  | 10.90.222.163  | 2S 16C 32T | 128 [GiB] |
| P+ I(1) | CRi | Server475 | Moid-value | --  | (R) UCSC-C240-M4SX | SN-30  | 10.29.58.180   | 2S 16C 32T | 128 [GiB] |
| P+ I(1) | Cri | Server224 | Moid-value | --  | (R) UCSC-C240-M4SX | SN-18  | 10.23.245.13   | 2S 16C 32T | 128 [GiB] |
| P+ I(1) | Cri | Server241 | Moid-value | --  | (R) UCSC-C240-M4SX | SN-28  | 10.138.127.226 | 2S 16C 32T | 128 [GiB] |
| P- H    | cri | Server527 | Moid-value | --  | (R) UCSC-C240-M4SX | SN-84  | 10.133.45.70   | 2S 16C 32T | 128 [GiB] |
+---------+-----+-----------+------------+-----+--------------------+--------+----------------+------------+-----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

## Size Greater or Equal

```
# iserver get server --mem size:ge512

iaccount demo (cache: any)
Select servers...
Selected servers: 121
Collect server api objects...


Server Summary [#34]
--------------------

+---------+-----+-----------+------------+-----+--------------------+--------+----------------+--------------+-----------+
| SF      | MF  | Name      | Moid       | Tag | Model              | Serial | IP             | CPU          | Memory    |
+---------+-----+-----------+------------+-----+--------------------+--------+----------------+--------------+-----------+
| P+ H    | Cri | Server150 | Moid-value | --  | (R) UCSC-C240-M5SX | SN-47  | 10.111.35.103  | 2S 56C 112T  | 512 [GiB] |
| P+ C(1) | CRi | Server295 | Moid-value | --  | (R) UCSC-C240-M6N  | SN-68  | 10.112.29.77   | 2S 64C 128T  | 512 [GiB] |
| P+ H    | Cri | Server547 | Moid-value | --  | (R) UCSC-C240-M6SN | SN-72  | 10.204.83.102  | 2S 64C 128T  | 512 [GiB] |
| P+ H    | CRi | Server828 | Moid-value | --  | (R) UCSC-C240-M6N  | SN-32  | 10.19.205.74   | 2S 64C 128T  | 512 [GiB] |
| P+ C(1) | CRi | Server308 | Moid-value | --  | (R) UCSC-C240-M6SN | SN-93  | 10.250.198.254 | 2S 64C 128T  | 512 [GiB] |
| P+ H    | CRi | Server703 | Moid-value | --  | (R) UCSC-C245-M6SX | SN-90  | 10.229.252.211 | 2S 48C 96T   | 512 [GiB] |
| P+ H    | CRi | Server435 | Moid-value | --  | (R) UCSC-C240-M6N  | SN-95  | 10.213.119.80  | 2S 64C 128T  | 512 [GiB] |
| P+ H    | Cri | Server888 | Moid-value | --  | (R) UCSC-C240-M6SN | SN-67  | 10.137.26.159  | 2S 64C 128T  | 512 [GiB] |
| P+ H    | CRi | Server288 | Moid-value | --  | (R) UCSC-C240-M6N  | SN-37  | 10.144.219.79  | 2S 64C 128T  | 512 [GiB] |
| P+ H    | CRi | Server788 | Moid-value | --  | (R) UCSC-C240-M6SN | SN-73  | 10.166.34.220  | 2S 64C 128T  | 512 [GiB] |
| P+ H    | CRi | Server700 | Moid-value | --  | (R) UCSC-C245-M6SX | SN-11  | 10.236.20.170  | 2S 128C 256T | 512 [GiB] |
| P+ C(1) | CRi | Server173 | Moid-value | --  | (R) UCSC-C240-M6N  | SN-30  | 10.192.133.30  | 2S 64C 128T  | 512 [GiB] |
| P+ H    | CRi | Server148 | Moid-value | --  | (R) UCSC-C240-M6N  | SN-13  | 10.212.114.124 | 2S 64C 128T  | 512 [GiB] |
| P+ H    | CRi | Server929 | Moid-value | --  | (R) UCSC-C240-M6SN | SN-32  | 10.101.6.194   | 2S 64C 128T  | 512 [GiB] |
| P+ C(1) | CRi | Server148 | Moid-value | --  | (R) UCSC-C225-M6S  | SN-80  | 10.4.200.169   | 1S 64C 128T  | 512 [GiB] |
| P+ H    | CRi | Server340 | Moid-value | --  | (R) UCSC-C225-M6S  | SN-87  | 10.109.141.40  | 1S 32C 64T   | 512 [GiB] |
| P+ H    | CRi | Server795 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-67  | 10.72.160.33   | 2S 48C 96T   | 512 [GiB] |
| P+ H    | Cri | Server581 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-47  | 10.215.181.65  | 2S 48C 96T   | 512 [GiB] |
| P+ H    | CRi | Server141 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-42  | 10.125.89.154  | 2S 48C 96T   | 512 [GiB] |
| P+ H    | CRi | Server466 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-67  | 10.101.141.116 | 2S 48C 96T   | 512 [GiB] |
| P- C(1) | cRi | Server308 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-72  | 10.5.40.205    | 2S 36C 72T   | 512 [GiB] |
| P+ C(1) | CRi | Server229 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-95  | 10.10.82.78    | 2S 36C 72T   | 512 [GiB] |
| P- W(1) | Cu  | Server771 | Moid-value | --  | (B) UCSB-B200-M4   | SN-82  | 10.234.25.66   | 2S 24C 48T   | 512 [GiB] |
| P- W(1) | Cu  | Server896 | Moid-value | --  | (B) UCSB-B200-M4   | SN-15  | 10.50.105.164  | 2S 24C 48T   | 512 [GiB] |
| P+ H    | Cu  | Server907 | Moid-value | --  | (B) UCSB-B200-M5   | SN-26  | 10.22.72.57    | 2S 40C 80T   | 512 [GiB] |
| P+ H    | Cu  | Server235 | Moid-value | --  | (B) UCSB-B200-M5   | SN-38  | 10.14.175.231  | 2S 40C 80T   | 512 [GiB] |
| P+ H    | Cu  | Server446 | Moid-value | --  | (B) UCSB-B200-M5   | SN-21  | 10.209.209.212 | 2S 40C 80T   | 512 [GiB] |
| P+ H    | Cu  | Server443 | Moid-value | --  | (B) UCSB-B200-M5   | SN-27  | 10.189.237.19  | 2S 40C 80T   | 512 [GiB] |
| P+ H    | Cu  | Server934 | Moid-value | --  | (R) HXAF240C-M5SX  | SN-12  | 10.238.170.92  | 2S 52C 104T  | 768 [GiB] |
| P+ H    | Cu  | Server255 | Moid-value | --  | (R) HXAF240C-M5SX  | SN-58  | 10.60.117.167  | 2S 52C 104T  | 768 [GiB] |
| P+ H    | Cu  | Server810 | Moid-value | --  | (R) HXAF240C-M5SX  | SN-81  | 10.133.251.252 | 2S 52C 104T  | 768 [GiB] |
| P+ H    | Cri | Server968 | Moid-value | --  | (B) UCSX-210C-M6   | SN-42  | 10.109.70.135  | 2S 64C 128T  | 512 [GiB] |
| P- H    | Cri | Server514 | Moid-value | --  | (B) UCSX-210C-M6   | SN-84  | 10.120.90.187  | 2S 64C 128T  | 512 [GiB] |
| P- H    | Cri | Server585 | Moid-value | --  | (B) UCSX-210C-M6   | SN-83  | 10.240.92.241  | 2S 64C 128T  | 512 [GiB] |
+---------+-----+-----------+------------+-----+--------------------+--------+----------------+--------------+-----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

## DIMM count

```
# iserver get server
    --name p1c
    --mem dimm:gt12 -v mem

iaccount demo (cache: any)
Select servers...
Selected servers: 0
```

## Model

```
# iserver get server
    --mem model:3g2r1 -v mem

iaccount demo (cache: any)
Select servers...
Selected servers: 121
Collect server api objects...


Memory [#176]
-------------

+-----------+----------+----------+----+-------+------+------------+----------+-------+-------------+------+----------+--------+
| Server    | Oper     | Presence | Id | Array | Bank | Location   | Capacity | Clock | Form Factor | Type | Model    | Serial |
+-----------+----------+----------+----+-------+------+------------+----------+-------+-------------+------+----------+--------+
| Server105 | operable | equipped | 1  | 1     | 0    | DIMM_P1_A1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-34 | SN-36  |
| Server105 | operable | equipped | 3  | 1     | 0    | DIMM_P1_B1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-27 | SN-91  |
| Server105 | operable | equipped | 5  | 1     | 0    | DIMM_P1_C1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-20 | SN-90  |
| Server105 | operable | equipped | 7  | 1     | 0    | DIMM_P1_D1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-38 | SN-15  |
| Server105 | operable | equipped | 9  | 1     | 0    | DIMM_P1_E1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-74 | SN-43  |
| Server105 | operable | equipped | 11 | 1     | 0    | DIMM_P1_F1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-63 | SN-67  |
| Server105 | operable | equipped | 13 | 1     | 0    | DIMM_P1_G1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-25 | SN-83  |
| Server105 | operable | equipped | 15 | 1     | 0    | DIMM_P1_H1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-68 | SN-47  |
| Server105 | operable | equipped | 17 | 1     | 0    | DIMM_P2_A1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-80 | SN-32  |
| Server105 | operable | equipped | 19 | 1     | 0    | DIMM_P2_B1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-75 | SN-15  |
| Server105 | operable | equipped | 21 | 1     | 0    | DIMM_P2_C1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-91 | SN-91  |
| Server105 | operable | equipped | 23 | 1     | 0    | DIMM_P2_D1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-99 | SN-26  |
| Server105 | operable | equipped | 25 | 1     | 0    | DIMM_P2_E1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-36 | SN-75  |
| Server105 | operable | equipped | 27 | 1     | 0    | DIMM_P2_F1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-98 | SN-42  |
| Server105 | operable | equipped | 29 | 1     | 0    | DIMM_P2_G1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-19 | SN-55  |
| Server105 | operable | equipped | 31 | 1     | 0    | DIMM_P2_H1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-10 | SN-90  |
| Server890 | operable | equipped | 1  | 1     | 0    | DIMM_P1_A1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-16 | SN-55  |
| Server890 | operable | equipped | 3  | 1     | 0    | DIMM_P1_B1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-76 | SN-99  |
| Server890 | operable | equipped | 5  | 1     | 0    | DIMM_P1_C1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-77 | SN-54  |
| Server890 | operable | equipped | 7  | 1     | 0    | DIMM_P1_D1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-38 | SN-58  |
| Server890 | operable | equipped | 9  | 1     | 0    | DIMM_P1_E1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-52 | SN-85  |
| Server890 | operable | equipped | 11 | 1     | 0    | DIMM_P1_F1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-87 | SN-53  |
| Server890 | operable | equipped | 13 | 1     | 0    | DIMM_P1_G1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-12 | SN-73  |
| Server890 | operable | equipped | 15 | 1     | 0    | DIMM_P1_H1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-10 | SN-65  |
| Server890 | operable | equipped | 17 | 1     | 0    | DIMM_P2_A1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-26 | SN-31  |
| Server890 | operable | equipped | 19 | 1     | 0    | DIMM_P2_B1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-35 | SN-48  |
| Server890 | operable | equipped | 21 | 1     | 0    | DIMM_P2_C1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-26 | SN-16  |
| Server890 | operable | equipped | 23 | 1     | 0    | DIMM_P2_D1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-12 | SN-38  |
| Server890 | operable | equipped | 25 | 1     | 0    | DIMM_P2_E1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-85 | SN-22  |
| Server890 | operable | equipped | 27 | 1     | 0    | DIMM_P2_F1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-29 | SN-95  |
| Server890 | operable | equipped | 29 | 1     | 0    | DIMM_P2_G1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-46 | SN-88  |
| Server890 | operable | equipped | 31 | 1     | 0    | DIMM_P2_H1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-70 | SN-91  |
| Server431 | operable | equipped | 1  | 1     | 0    | DIMM_P1_A1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-20 | SN-46  |
| Server431 | operable | equipped | 3  | 1     | 0    | DIMM_P1_B1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-43 | SN-88  |
| Server431 | operable | equipped | 5  | 1     | 0    | DIMM_P1_C1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-19 | SN-22  |
| Server431 | operable | equipped | 7  | 1     | 0    | DIMM_P1_D1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-72 | SN-22  |
| Server431 | operable | equipped | 9  | 1     | 0    | DIMM_P1_E1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-37 | SN-57  |
| Server431 | operable | equipped | 11 | 1     | 0    | DIMM_P1_F1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-10 | SN-91  |
| Server431 | operable | equipped | 13 | 1     | 0    | DIMM_P1_G1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-70 | SN-95  |
| Server431 | operable | equipped | 15 | 1     | 0    | DIMM_P1_H1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-98 | SN-45  |
| Server431 | operable | equipped | 17 | 1     | 0    | DIMM_P2_A1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-19 | SN-72  |
| Server431 | operable | equipped | 19 | 1     | 0    | DIMM_P2_B1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-12 | SN-52  |
| Server431 | operable | equipped | 21 | 1     | 0    | DIMM_P2_C1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-39 | SN-32  |
| Server431 | operable | equipped | 23 | 1     | 0    | DIMM_P2_D1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-93 | SN-98  |
| Server431 | operable | equipped | 25 | 1     | 0    | DIMM_P2_E1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-92 | SN-84  |
| Server431 | operable | equipped | 27 | 1     | 0    | DIMM_P2_F1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-60 | SN-13  |
| Server431 | operable | equipped | 29 | 1     | 0    | DIMM_P2_G1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-38 | SN-21  |
| Server431 | operable | equipped | 31 | 1     | 0    | DIMM_P2_H1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-22 | SN-64  |
| Server795 | operable | equipped | 1  | 1     | 0    | DIMM_P1_A1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-60 | SN-42  |
| Server795 | operable | equipped | 3  | 1     | 0    | DIMM_P1_B1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-74 | SN-13  |
| Server795 | operable | equipped | 5  | 1     | 0    | DIMM_P1_C1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-41 | SN-34  |
| Server795 | operable | equipped | 7  | 1     | 0    | DIMM_P1_D1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-45 | SN-12  |
| Server795 | operable | equipped | 9  | 1     | 0    | DIMM_P1_E1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-58 | SN-20  |
| Server795 | operable | equipped | 11 | 1     | 0    | DIMM_P1_F1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-33 | SN-34  |
| Server795 | operable | equipped | 13 | 1     | 0    | DIMM_P1_G1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-78 | SN-45  |
| Server795 | operable | equipped | 15 | 1     | 0    | DIMM_P1_H1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-51 | SN-54  |
| Server795 | operable | equipped | 17 | 1     | 0    | DIMM_P2_A1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-24 | SN-91  |
| Server795 | operable | equipped | 19 | 1     | 0    | DIMM_P2_B1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-10 | SN-92  |
| Server795 | operable | equipped | 21 | 1     | 0    | DIMM_P2_C1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-69 | SN-17  |
| Server795 | operable | equipped | 23 | 1     | 0    | DIMM_P2_D1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-97 | SN-82  |
| Server795 | operable | equipped | 25 | 1     | 0    | DIMM_P2_E1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-79 | SN-43  |
| Server795 | operable | equipped | 27 | 1     | 0    | DIMM_P2_F1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-26 | SN-70  |
| Server795 | operable | equipped | 29 | 1     | 0    | DIMM_P2_G1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-45 | SN-98  |
| Server795 | operable | equipped | 31 | 1     | 0    | DIMM_P2_H1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-22 | SN-25  |
| Server306 | operable | equipped | 1  | 1     | 0    | DIMM_P1_A1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-98 | SN-32  |
| Server306 | operable | equipped | 3  | 1     | 0    | DIMM_P1_B1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-19 | SN-72  |
| Server306 | operable | equipped | 5  | 1     | 0    | DIMM_P1_C1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-73 | SN-26  |
| Server306 | operable | equipped | 7  | 1     | 0    | DIMM_P1_D1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-42 | SN-73  |
| Server306 | operable | equipped | 9  | 1     | 0    | DIMM_P1_E1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-92 | SN-91  |
| Server306 | operable | equipped | 11 | 1     | 0    | DIMM_P1_F1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-94 | SN-87  |
| Server306 | operable | equipped | 13 | 1     | 0    | DIMM_P1_G1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-17 | SN-22  |
| Server306 | operable | equipped | 15 | 1     | 0    | DIMM_P1_H1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-68 | SN-66  |
| Server306 | operable | equipped | 17 | 1     | 0    | DIMM_P2_A1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-70 | SN-74  |
| Server306 | operable | equipped | 19 | 1     | 0    | DIMM_P2_B1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-37 | SN-31  |
| Server306 | operable | equipped | 21 | 1     | 0    | DIMM_P2_C1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-71 | SN-27  |
| Server306 | operable | equipped | 23 | 1     | 0    | DIMM_P2_D1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-25 | SN-52  |
| Server306 | operable | equipped | 25 | 1     | 0    | DIMM_P2_E1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-51 | SN-26  |
| Server306 | operable | equipped | 27 | 1     | 0    | DIMM_P2_F1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-28 | SN-42  |
| Server306 | operable | equipped | 29 | 1     | 0    | DIMM_P2_G1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-59 | SN-50  |
| Server306 | operable | equipped | 31 | 1     | 0    | DIMM_P2_H1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-88 | SN-20  |
| Server427 | operable | equipped | 1  | 1     | 0    | DIMM_P1_A1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-52 | SN-30  |
| Server427 | operable | equipped | 3  | 1     | 0    | DIMM_P1_B1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-78 | SN-95  |
| Server427 | operable | equipped | 5  | 1     | 0    | DIMM_P1_C1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-30 | SN-78  |
| Server427 | operable | equipped | 7  | 1     | 0    | DIMM_P1_D1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-21 | SN-26  |
| Server427 | operable | equipped | 9  | 1     | 0    | DIMM_P1_E1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-91 | SN-39  |
| Server427 | operable | equipped | 11 | 1     | 0    | DIMM_P1_F1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-76 | SN-74  |
| Server427 | operable | equipped | 13 | 1     | 0    | DIMM_P1_G1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-23 | SN-75  |
| Server427 | operable | equipped | 15 | 1     | 0    | DIMM_P1_H1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-47 | SN-31  |
| Server427 | operable | equipped | 17 | 1     | 0    | DIMM_P2_A1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-78 | SN-32  |
| Server427 | operable | equipped | 19 | 1     | 0    | DIMM_P2_B1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-80 | SN-79  |
| Server427 | operable | equipped | 21 | 1     | 0    | DIMM_P2_C1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-36 | SN-82  |
| Server427 | operable | equipped | 23 | 1     | 0    | DIMM_P2_D1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-13 | SN-80  |
| Server427 | operable | equipped | 25 | 1     | 0    | DIMM_P2_E1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-11 | SN-31  |
| Server427 | operable | equipped | 27 | 1     | 0    | DIMM_P2_F1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-95 | SN-91  |
| Server427 | operable | equipped | 29 | 1     | 0    | DIMM_P2_G1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-84 | SN-95  |
| Server427 | operable | equipped | 31 | 1     | 0    | DIMM_P2_H1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-40 | SN-30  |
| Server840 | operable | equipped | 1  | 1     | 0    | DIMM_P1_A1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-66 | SN-70  |
| Server840 | operable | equipped | 3  | 1     | 0    | DIMM_P1_B1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-41 | SN-47  |
| Server840 | operable | equipped | 5  | 1     | 0    | DIMM_P1_C1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-79 | SN-39  |
| Server840 | operable | equipped | 7  | 1     | 0    | DIMM_P1_D1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-28 | SN-90  |
| Server840 | operable | equipped | 9  | 1     | 0    | DIMM_P1_E1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-93 | SN-19  |
| Server840 | operable | equipped | 11 | 1     | 0    | DIMM_P1_F1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-37 | SN-58  |
| Server840 | operable | equipped | 13 | 1     | 0    | DIMM_P1_G1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-87 | SN-92  |
| Server840 | operable | equipped | 15 | 1     | 0    | DIMM_P1_H1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-75 | SN-34  |
| Server840 | operable | equipped | 17 | 1     | 0    | DIMM_P2_A1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-96 | SN-31  |
| Server840 | operable | equipped | 19 | 1     | 0    | DIMM_P2_B1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-47 | SN-41  |
| Server840 | operable | equipped | 21 | 1     | 0    | DIMM_P2_C1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-93 | SN-67  |
| Server840 | operable | equipped | 23 | 1     | 0    | DIMM_P2_D1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-22 | SN-48  |
| Server840 | operable | equipped | 25 | 1     | 0    | DIMM_P2_E1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-79 | SN-29  |
| Server840 | operable | equipped | 27 | 1     | 0    | DIMM_P2_F1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-53 | SN-96  |
| Server840 | operable | equipped | 29 | 1     | 0    | DIMM_P2_G1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-71 | SN-97  |
| Server840 | operable | equipped | 31 | 1     | 0    | DIMM_P2_H1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-39 | SN-37  |
| Server907 | operable | equipped | 1  | 1     | 0    | DIMM_P1_A1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-83 | SN-49  |
| Server907 | operable | equipped | 3  | 1     | 0    | DIMM_P1_B1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-20 | SN-14  |
| Server907 | operable | equipped | 5  | 1     | 0    | DIMM_P1_C1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-22 | SN-94  |
| Server907 | operable | equipped | 7  | 1     | 0    | DIMM_P1_D1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-44 | SN-91  |
| Server907 | operable | equipped | 9  | 1     | 0    | DIMM_P1_E1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-99 | SN-69  |
| Server907 | operable | equipped | 11 | 1     | 0    | DIMM_P1_F1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-83 | SN-76  |
| Server907 | operable | equipped | 13 | 1     | 0    | DIMM_P1_G1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-47 | SN-73  |
| Server907 | operable | equipped | 15 | 1     | 0    | DIMM_P1_H1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-80 | SN-74  |
| Server907 | operable | equipped | 17 | 1     | 0    | DIMM_P2_A1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-72 | SN-31  |
| Server907 | operable | equipped | 19 | 1     | 0    | DIMM_P2_B1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-28 | SN-89  |
| Server907 | operable | equipped | 21 | 1     | 0    | DIMM_P2_C1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-59 | SN-86  |
| Server907 | operable | equipped | 23 | 1     | 0    | DIMM_P2_D1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-87 | SN-83  |
| Server907 | operable | equipped | 25 | 1     | 0    | DIMM_P2_E1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-28 | SN-90  |
| Server907 | operable | equipped | 27 | 1     | 0    | DIMM_P2_F1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-19 | SN-42  |
| Server907 | operable | equipped | 29 | 1     | 0    | DIMM_P2_G1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-53 | SN-39  |
| Server907 | operable | equipped | 31 | 1     | 0    | DIMM_P2_H1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-49 | SN-74  |
| Server674 | operable | equipped | 1  | 1     | 0    | DIMM_P1_A1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-14 | SN-74  |
| Server674 | operable | equipped | 3  | 1     | 0    | DIMM_P1_B1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-98 | SN-58  |
| Server674 | operable | equipped | 5  | 1     | 0    | DIMM_P1_C1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-19 | SN-43  |
| Server674 | operable | equipped | 7  | 1     | 0    | DIMM_P1_D1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-34 | SN-76  |
| Server674 | operable | equipped | 9  | 1     | 0    | DIMM_P1_E1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-18 | SN-59  |
| Server674 | operable | equipped | 11 | 1     | 0    | DIMM_P1_F1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-37 | SN-59  |
| Server674 | operable | equipped | 13 | 1     | 0    | DIMM_P1_G1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-38 | SN-66  |
| Server674 | operable | equipped | 15 | 1     | 0    | DIMM_P1_H1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-30 | SN-30  |
| Server674 | operable | equipped | 17 | 1     | 0    | DIMM_P2_A1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-63 | SN-61  |
| Server674 | operable | equipped | 19 | 1     | 0    | DIMM_P2_B1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-67 | SN-34  |
| Server674 | operable | equipped | 21 | 1     | 0    | DIMM_P2_C1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-97 | SN-21  |
| Server674 | operable | equipped | 23 | 1     | 0    | DIMM_P2_D1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-15 | SN-80  |
| Server674 | operable | equipped | 25 | 1     | 0    | DIMM_P2_E1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-80 | SN-47  |
| Server674 | operable | equipped | 27 | 1     | 0    | DIMM_P2_F1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-60 | SN-52  |
| Server674 | operable | equipped | 29 | 1     | 0    | DIMM_P2_G1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-20 | SN-79  |
| Server674 | operable | equipped | 31 | 1     | 0    | DIMM_P2_H1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-45 | SN-41  |
| Server638 | operable | equipped | 1  | 1     | 0    | DIMM_P1_A1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-24 | SN-54  |
| Server638 | operable | equipped | 3  | 1     | 0    | DIMM_P1_B1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-35 | SN-53  |
| Server638 | operable | equipped | 5  | 1     | 0    | DIMM_P1_C1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-34 | SN-34  |
| Server638 | operable | equipped | 7  | 1     | 0    | DIMM_P1_D1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-86 | SN-38  |
| Server638 | operable | equipped | 9  | 1     | 0    | DIMM_P1_E1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-44 | SN-24  |
| Server638 | operable | equipped | 11 | 1     | 0    | DIMM_P1_F1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-38 | SN-18  |
| Server638 | operable | equipped | 13 | 1     | 0    | DIMM_P1_G1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-83 | SN-85  |
| Server638 | operable | equipped | 15 | 1     | 0    | DIMM_P1_H1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-51 | SN-11  |
| Server638 | operable | equipped | 17 | 1     | 0    | DIMM_P2_A1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-97 | SN-13  |
| Server638 | operable | equipped | 19 | 1     | 0    | DIMM_P2_B1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-93 | SN-72  |
| Server638 | operable | equipped | 21 | 1     | 0    | DIMM_P2_C1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-81 | SN-40  |
| Server638 | operable | equipped | 23 | 1     | 0    | DIMM_P2_D1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-92 | SN-14  |
| Server638 | operable | equipped | 25 | 1     | 0    | DIMM_P2_E1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-65 | SN-24  |
| Server638 | operable | equipped | 27 | 1     | 0    | DIMM_P2_F1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-48 | SN-79  |
| Server638 | operable | equipped | 29 | 1     | 0    | DIMM_P2_G1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-42 | SN-96  |
| Server638 | operable | equipped | 31 | 1     | 0    | DIMM_P2_H1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-13 | SN-91  |
| Server156 | operable | equipped | 1  | 1     | 0    | DIMM_P1_A1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-95 | SN-50  |
| Server156 | operable | equipped | 3  | 1     | 0    | DIMM_P1_B1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-85 | SN-58  |
| Server156 | operable | equipped | 5  | 1     | 0    | DIMM_P1_C1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-68 | SN-36  |
| Server156 | operable | equipped | 7  | 1     | 0    | DIMM_P1_D1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-45 | SN-96  |
| Server156 | operable | equipped | 9  | 1     | 0    | DIMM_P1_E1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-69 | SN-93  |
| Server156 | operable | equipped | 11 | 1     | 0    | DIMM_P1_F1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-68 | SN-42  |
| Server156 | operable | equipped | 13 | 1     | 0    | DIMM_P1_G1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-30 | SN-51  |
| Server156 | operable | equipped | 15 | 1     | 0    | DIMM_P1_H1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-25 | SN-52  |
| Server156 | operable | equipped | 17 | 1     | 0    | DIMM_P2_A1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-26 | SN-63  |
| Server156 | operable | equipped | 19 | 1     | 0    | DIMM_P2_B1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-98 | SN-68  |
| Server156 | operable | equipped | 21 | 1     | 0    | DIMM_P2_C1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-72 | SN-78  |
| Server156 | operable | equipped | 23 | 1     | 0    | DIMM_P2_D1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-54 | SN-38  |
| Server156 | operable | equipped | 25 | 1     | 0    | DIMM_P2_E1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-26 | SN-56  |
| Server156 | operable | equipped | 27 | 1     | 0    | DIMM_P2_F1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-77 | SN-61  |
| Server156 | operable | equipped | 29 | 1     | 0    | DIMM_P2_G1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-64 | SN-33  |
| Server156 | operable | equipped | 31 | 1     | 0    | DIMM_P2_H1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-31 | SN-88  |
+-----------+----------+----------+----+-------+------+------------+----------+-------+-------------+------+----------+--------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

## Serial

```
# iserver get server
    --mem serial:2212-D0 -v mem

iaccount demo (cache: any)
Select servers...
Selected servers: 121
Collect server api objects...


Memory [#80]
------------

+-----------+----------+----------+----+-------+------+------------+----------+-------+-------------+------+----------+--------+
| Server    | Oper     | Presence | Id | Array | Bank | Location   | Capacity | Clock | Form Factor | Type | Model    | Serial |
+-----------+----------+----------+----+-------+------+------------+----------+-------+-------------+------+----------+--------+
| Server880 | operable | equipped | 1  | 1     | 0    | DIMM_P1_A1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-58 | SN-37  |
| Server880 | operable | equipped | 3  | 1     | 0    | DIMM_P1_B1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-73 | SN-74  |
| Server880 | operable | equipped | 5  | 1     | 0    | DIMM_P1_C1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-48 | SN-85  |
| Server880 | operable | equipped | 7  | 1     | 0    | DIMM_P1_D1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-85 | SN-34  |
| Server880 | operable | equipped | 9  | 1     | 0    | DIMM_P1_E1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-96 | SN-31  |
| Server880 | operable | equipped | 11 | 1     | 0    | DIMM_P1_F1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-86 | SN-66  |
| Server880 | operable | equipped | 13 | 1     | 0    | DIMM_P1_G1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-46 | SN-50  |
| Server880 | operable | equipped | 15 | 1     | 0    | DIMM_P1_H1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-36 | SN-36  |
| Server880 | operable | equipped | 17 | 1     | 0    | DIMM_P2_A1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-14 | SN-47  |
| Server880 | operable | equipped | 19 | 1     | 0    | DIMM_P2_B1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-61 | SN-92  |
| Server880 | operable | equipped | 21 | 1     | 0    | DIMM_P2_C1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-26 | SN-58  |
| Server880 | operable | equipped | 23 | 1     | 0    | DIMM_P2_D1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-11 | SN-42  |
| Server880 | operable | equipped | 25 | 1     | 0    | DIMM_P2_E1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-39 | SN-39  |
| Server880 | operable | equipped | 27 | 1     | 0    | DIMM_P2_F1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-70 | SN-35  |
| Server880 | operable | equipped | 29 | 1     | 0    | DIMM_P2_G1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-66 | SN-65  |
| Server880 | operable | equipped | 31 | 1     | 0    | DIMM_P2_H1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-89 | SN-75  |
| Server273 | operable | equipped | 1  | 1     | 0    | DIMM_P1_A1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-31 | SN-78  |
| Server273 | operable | equipped | 3  | 1     | 0    | DIMM_P1_B1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-40 | SN-92  |
| Server273 | operable | equipped | 5  | 1     | 0    | DIMM_P1_C1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-59 | SN-12  |
| Server273 | operable | equipped | 7  | 1     | 0    | DIMM_P1_D1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-31 | SN-31  |
| Server273 | operable | equipped | 9  | 1     | 0    | DIMM_P1_E1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-44 | SN-60  |
| Server273 | operable | equipped | 11 | 1     | 0    | DIMM_P1_F1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-74 | SN-34  |
| Server273 | operable | equipped | 13 | 1     | 0    | DIMM_P1_G1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-45 | SN-55  |
| Server273 | operable | equipped | 15 | 1     | 0    | DIMM_P1_H1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-41 | SN-48  |
| Server273 | operable | equipped | 17 | 1     | 0    | DIMM_P2_A1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-11 | SN-66  |
| Server273 | operable | equipped | 19 | 1     | 0    | DIMM_P2_B1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-49 | SN-26  |
| Server273 | operable | equipped | 21 | 1     | 0    | DIMM_P2_C1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-26 | SN-53  |
| Server273 | operable | equipped | 23 | 1     | 0    | DIMM_P2_D1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-62 | SN-30  |
| Server273 | operable | equipped | 25 | 1     | 0    | DIMM_P2_E1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-53 | SN-32  |
| Server273 | operable | equipped | 27 | 1     | 0    | DIMM_P2_F1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-44 | SN-49  |
| Server273 | operable | equipped | 29 | 1     | 0    | DIMM_P2_G1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-52 | SN-93  |
| Server273 | operable | equipped | 31 | 1     | 0    | DIMM_P2_H1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-39 | SN-44  |
| Server222 | operable | equipped | 1  | 1     | 0    | DIMM_P1_A1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-74 | SN-71  |
| Server222 | operable | equipped | 3  | 1     | 0    | DIMM_P1_B1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-29 | SN-25  |
| Server222 | operable | equipped | 5  | 1     | 0    | DIMM_P1_C1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-20 | SN-60  |
| Server222 | operable | equipped | 7  | 1     | 0    | DIMM_P1_D1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-29 | SN-21  |
| Server222 | operable | equipped | 9  | 1     | 0    | DIMM_P1_E1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-38 | SN-47  |
| Server222 | operable | equipped | 11 | 1     | 0    | DIMM_P1_F1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-66 | SN-59  |
| Server222 | operable | equipped | 13 | 1     | 0    | DIMM_P1_G1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-76 | SN-11  |
| Server222 | operable | equipped | 15 | 1     | 0    | DIMM_P1_H1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-54 | SN-13  |
| Server222 | operable | equipped | 17 | 1     | 0    | DIMM_P2_A1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-63 | SN-27  |
| Server222 | operable | equipped | 19 | 1     | 0    | DIMM_P2_B1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-17 | SN-39  |
| Server222 | operable | equipped | 21 | 1     | 0    | DIMM_P2_C1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-41 | SN-67  |
| Server222 | operable | equipped | 23 | 1     | 0    | DIMM_P2_D1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-23 | SN-88  |
| Server222 | operable | equipped | 25 | 1     | 0    | DIMM_P2_E1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-32 | SN-39  |
| Server222 | operable | equipped | 27 | 1     | 0    | DIMM_P2_F1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-12 | SN-26  |
| Server222 | operable | equipped | 29 | 1     | 0    | DIMM_P2_G1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-31 | SN-10  |
| Server222 | operable | equipped | 31 | 1     | 0    | DIMM_P2_H1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-97 | SN-25  |
| Server892 | operable | equipped | 1  | 1     | 0    | DIMM_P1_A1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-10 | SN-16  |
| Server892 | operable | equipped | 3  | 1     | 0    | DIMM_P1_B1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-55 | SN-16  |
| Server892 | operable | equipped | 5  | 1     | 0    | DIMM_P1_C1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-19 | SN-62  |
| Server892 | operable | equipped | 7  | 1     | 0    | DIMM_P1_D1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-37 | SN-32  |
| Server892 | operable | equipped | 9  | 1     | 0    | DIMM_P1_E1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-84 | SN-65  |
| Server892 | operable | equipped | 11 | 1     | 0    | DIMM_P1_F1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-91 | SN-13  |
| Server892 | operable | equipped | 13 | 1     | 0    | DIMM_P1_G1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-98 | SN-24  |
| Server892 | operable | equipped | 15 | 1     | 0    | DIMM_P1_H1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-82 | SN-69  |
| Server892 | operable | equipped | 17 | 1     | 0    | DIMM_P2_A1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-19 | SN-25  |
| Server892 | operable | equipped | 19 | 1     | 0    | DIMM_P2_B1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-34 | SN-75  |
| Server892 | operable | equipped | 21 | 1     | 0    | DIMM_P2_C1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-71 | SN-61  |
| Server892 | operable | equipped | 23 | 1     | 0    | DIMM_P2_D1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-96 | SN-82  |
| Server892 | operable | equipped | 25 | 1     | 0    | DIMM_P2_E1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-51 | SN-80  |
| Server892 | operable | equipped | 27 | 1     | 0    | DIMM_P2_F1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-22 | SN-35  |
| Server892 | operable | equipped | 29 | 1     | 0    | DIMM_P2_G1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-25 | SN-84  |
| Server892 | operable | equipped | 31 | 1     | 0    | DIMM_P2_H1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-39 | SN-14  |
| Server294 | operable | equipped | 1  | 1     | 0    | DIMM_P1_A1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-35 | SN-94  |
| Server294 | operable | equipped | 3  | 1     | 0    | DIMM_P1_B1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-12 | SN-73  |
| Server294 | operable | equipped | 5  | 1     | 0    | DIMM_P1_C1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-77 | SN-17  |
| Server294 | operable | equipped | 7  | 1     | 0    | DIMM_P1_D1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-29 | SN-83  |
| Server294 | operable | equipped | 9  | 1     | 0    | DIMM_P1_E1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-47 | SN-93  |
| Server294 | operable | equipped | 11 | 1     | 0    | DIMM_P1_F1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-79 | SN-27  |
| Server294 | operable | equipped | 13 | 1     | 0    | DIMM_P1_G1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-58 | SN-28  |
| Server294 | operable | equipped | 15 | 1     | 0    | DIMM_P1_H1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-86 | SN-28  |
| Server294 | operable | equipped | 17 | 1     | 0    | DIMM_P2_A1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-23 | SN-97  |
| Server294 | operable | equipped | 19 | 1     | 0    | DIMM_P2_B1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-66 | SN-34  |
| Server294 | operable | equipped | 21 | 1     | 0    | DIMM_P2_C1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-39 | SN-81  |
| Server294 | operable | equipped | 23 | 1     | 0    | DIMM_P2_D1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-82 | SN-42  |
| Server294 | operable | equipped | 25 | 1     | 0    | DIMM_P2_E1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-54 | SN-87  |
| Server294 | operable | equipped | 27 | 1     | 0    | DIMM_P2_F1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-23 | SN-65  |
| Server294 | operable | equipped | 29 | 1     | 0    | DIMM_P2_G1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-52 | SN-10  |
| Server294 | operable | equipped | 31 | 1     | 0    | DIMM_P2_H1 | 32 [GiB] | 3200  | DIMM        | DDR4 | Model-53 | SN-80  |
+-----------+----------+----------+----+-------+------+------------+----------+-------+-------------+------+----------+--------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)