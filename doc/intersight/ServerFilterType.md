# Intersight Server

## Filter by type

Examples

```
--type blade
--type rack
```

## Blade Servers

```
# iserver get server --type blade

iaccount demo (cache: any)
Select servers...
Selected servers: 12
Collect server api objects...


Server Summary [#12]
--------------------

+---------+-----+-----------+------------+-----+--------------------+--------+----------------+-------------+-----------+
| SF      | MF  | Name      | Moid       | Tag | Model              | Serial | IP             | CPU         | Memory    |
+---------+-----+-----------+------------+-----+--------------------+--------+----------------+-------------+-----------+
| P- W(1) | Cu  | Server115 | Moid-value | --  | (B) UCSB-B200-M4   | SN-96  | 10.152.248.42  | 2S 24C 48T  | 512 [GiB] |
| P- W(1) | Cu  | Server785 | Moid-value | --  | (B) UCSB-B200-M4   | SN-26  | 10.80.32.7     | 2S 24C 48T  | 512 [GiB] |
| P- W(1) | Cu  | Server122 | Moid-value | --  | (B) UCSB-B200-M4   | SN-53  | 10.162.74.102  | 2S 24C 48T  | 256 [GiB] |
| P- C(9) | Cu  | Server120 | Moid-value | --  | (B) UCSB-B200-M4   | SN-61  | 10.174.180.150 | 2S 24C 48T  | 256 [GiB] |
| P+ H    | Cu  | Server458 | Moid-value | --  | (B) UCSB-B200-M5   | SN-76  | 10.17.162.191  | 2S 40C 80T  | 512 [GiB] |
| P+ H    | Cu  | Server192 | Moid-value | --  | (B) UCSB-B200-M5   | SN-52  | 10.40.16.214   | 2S 40C 80T  | 512 [GiB] |
| P+ H    | Cu  | Server518 | Moid-value | --  | (B) UCSB-B200-M5   | SN-70  | 10.198.129.192 | 2S 40C 80T  | 512 [GiB] |
| P+ H    | Cu  | Server547 | Moid-value | --  | (B) UCSB-B200-M5   | SN-40  | 10.189.211.42  | 2S 40C 80T  | 512 [GiB] |
| P+ H    | Cri | Server826 | Moid-value | --  | (B) UCSX-210C-M6   | SN-54  | 10.57.210.221  | 2S 64C 128T | 512 [GiB] |
| P- H    | Cri | Server185 | Moid-value | --  | (B) UCSX-210C-M6   | SN-79  | 10.50.75.123   | 2S 64C 128T | 512 [GiB] |
| P- H    | Cri | Server371 | Moid-value | --  | (B) UCSX-210C-M6   | SN-10  | 10.14.198.110  | 2S 64C 128T | 512 [GiB] |
| P+ H    | Cri | Server998 | Moid-value | --  | (B) UCSC-C3K-M4SRB | SN-53  | 10.40.213.76   | 2S 24C 48T  | 256 [GiB] |
+---------+-----+-----------+------------+-----+--------------------+--------+----------------+-------------+-----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

## Rack Servers

```
# iserver get server --type rack

iaccount demo (cache: any)
Select servers...
Selected servers: 109
Collect server api objects...


Server Summary [#109]
---------------------

+-----------+-----+-----------+------------+-----+--------------------+--------+----------------+--------------+-----------+
| SF        | MF  | Name      | Moid       | Tag | Model              | Serial | IP             | CPU          | Memory    |
+-----------+-----+-----------+------------+-----+--------------------+--------+----------------+--------------+-----------+
| P+ C(3)   | Cri | Server308 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-36  | 10.61.227.228  | 2S 20C 40T   | 192 [GiB] |
| P+ C(1)   | Cri | Server347 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-66  | 10.98.57.51    | 2S 20C 40T   | 192 [GiB] |
| P+ C(3)   | Cri | Server467 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-42  | 10.229.221.160 | 2S 20C 40T   | 192 [GiB] |
| P+ C(1)   | cri | Server490 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-16  | 10.137.223.85  | 2S 40C 80T   | 384 [GiB] |
| P+ H      | cri | Server543 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-56  | 10.107.177.139 | 2S 40C 80T   | 384 [GiB] |
| P+ H      | Cri | Server126 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-90  | 10.226.121.207 | 2S 28C 56T   | 256 [GiB] |
| P+ H      | CRi | Server887 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-31  | 10.241.40.121  | 2S 44C 88T   | 256 [GiB] |
| P+ H      | Cri | Server377 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-74  | 10.222.13.209  | 2S 28C 56T   | 256 [GiB] |
| P+ C(1)   | CRi | Server705 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-72  | 10.56.71.119   | 2S 44C 88T   | 256 [GiB] |
| P+ H      | CRi | Server563 | Moid-value | --  | (R) UCSC-C240-M5SX | SN-74  | 10.27.101.238  | 2S 48C 96T   | 384 [GiB] |
| P+ C(1)   | Cri | Server599 | Moid-value | --  | (R) UCSC-C240-M4SX | SN-90  | 10.99.111.92   | 2S 24C 48T   | 256 [GiB] |
| P+ H      | CRi | Server473 | Moid-value | --  | (R) APIC-SERVER-M3 | SN-20  | 10.172.72.124  | 2S 16C 16T   | 96 [GiB]  |
| P+ H      | CRi | Server871 | Moid-value | --  | (R) APIC-SERVER-M3 | SN-80  | 10.169.120.18  | 2S 16C 16T   | 96 [GiB]  |
| P+ H L    | CRi | Server232 | Moid-value | --  | (R) APIC-SERVER-M3 | SN-43  | 10.129.132.248 | 2S 16C 16T   | 96 [GiB]  |
| P+ H L    | CRi | Server903 | Moid-value | --  | (R) APIC-SERVER-M3 | SN-24  | 10.111.211.8   | 2S 16C 16T   | 96 [GiB]  |
| P+ H      | CRi | Server934 | Moid-value | --  | (R) APIC-SERVER-M3 | SN-22  | 10.244.251.119 | 2S 16C 16T   | 96 [GiB]  |
| P+ H      | CRi | Server336 | Moid-value | --  | (R) APIC-SERVER-M3 | SN-53  | 10.178.132.209 | 2S 16C 16T   | 96 [GiB]  |
| P+ W(2)   | Cri | Server247 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-18  | 10.99.156.176  | 2S 28C 56T   | 256 [GiB] |
| P+ H      | Cri | Server599 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-37  | 10.4.251.34    | 2S 40C 80T   | 352 [GiB] |
| P+ H      | Cri | Server739 | Moid-value | --  | (R) UCSC-C240-M5SX | SN-11  | 10.207.211.249 | 2S 56C 112T  | 512 [GiB] |
| P+ H      | Cri | Server850 | Moid-value | --  | (R) UCSC-C480-M5   | SN-69  | 10.103.50.154  | 4S 72C 144T  | 256 [GiB] |
| P+ I(1)   | CRi | Server951 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-57  | 10.173.24.231  | 2S 16C 32T   | 256 [GiB] |
| P+ I(1)   | Cri | Server857 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-97  | 10.169.187.244 | 2S 16C 32T   | 128 [GiB] |
| P+ I(1)   | CRi | Server887 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-47  | 10.207.118.242 | 2S 28C 56T   | 256 [GiB] |
| P+ H      | Cri | Server128 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-67  | 10.185.232.21  | 2S 16C 32T   | 256 [GiB] |
| P+ I(1)   | CRi | Server948 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-40  | 10.164.246.59  | 2S 16C 32T   | 256 [GiB] |
| P+ H      | CRi | Server253 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-22  | 10.221.120.110 | 2S 16C 32T   | 256 [GiB] |
| P+ C(3)   | CRi | Server602 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-78  | 10.53.25.103   | 2S 28C 56T   | 256 [GiB] |
| P+ I(1)   | CRi | Server729 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-62  | 10.253.1.229   | 2S 24C 48T   | 256 [GiB] |
| P+ I(1)   | cRi | Server624 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-98  | 10.134.81.144  | 2S 24C 48T   | 256 [GiB] |
| P+ H      | CRi | Server950 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-60  | 10.96.209.213  | 2S 28C 56T   | 256 [GiB] |
| P+ H      | CRi | Server319 | Moid-value | --  | (R) UCSC-C240-M5SN | SN-36  | 10.156.166.176 | 2S 40C 80T   | 384 [GiB] |
| P+ H      | CRi | Server429 | Moid-value | --  | (R) UCSC-C240-M5SN | SN-78  | 10.143.235.249 | 2S 40C 80T   | 384 [GiB] |
| P+ H      | CRi | Server578 | Moid-value | --  | (R) UCSC-C240-M5SN | SN-12  | 10.12.101.93   | 2S 40C 80T   | 384 [GiB] |
| P+ H      | CRi | Server923 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-53  | 10.29.80.143   | 2S 40C 80T   | 384 [GiB] |
| P+ C(1)   | CRi | Server923 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-63  | 10.145.46.211  | 2S 40C 80T   | 384 [GiB] |
| P+ H      | CRi | Server508 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-88  | 10.84.20.248   | 2S 40C 80T   | 384 [GiB] |
| P+ I(1)   | CRi | Server592 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-64  | 10.183.230.58  | 2S 40C 80T   | 384 [GiB] |
| P- H      | cRi | Server179 | Moid-value | --  | (R) UCSC-C240-M5SX | SN-84  | 10.215.98.145  | 2S 48C 96T   | 384 [GiB] |
| P+ H      | CRi | Server736 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-94  | 10.57.120.94   | 2S 48C 96T   | 256 [GiB] |
| P+ C(1)   | CRi | Server103 | Moid-value | --  | (R) UCSC-C240-M6N  | SN-42  | 10.64.111.244  | 2S 64C 128T  | 512 [GiB] |
| P+ H      | Cri | Server594 | Moid-value | --  | (R) UCSC-C240-M6SN | SN-50  | 10.182.5.161   | 2S 64C 128T  | 512 [GiB] |
| P- H      | cRi | Server934 | Moid-value | --  | (R) UCSC-C240-M5SX | SN-89  | 10.95.86.126   | 2S 24C 24T   | 384 [GiB] |
| P+ H      | CRi | Server722 | Moid-value | --  | (R) UCSC-C240-M6N  | SN-43  | 10.139.121.72  | 2S 64C 128T  | 512 [GiB] |
| P+ I(1)   | CRi | Server242 | Moid-value | --  | (R) UCSC-C240-M4SX | SN-88  | 10.253.254.141 | 2S 16C 32T   | 128 [GiB] |
| P+ C(1)   | CRi | Server720 | Moid-value | --  | (R) UCSC-C240-M6SN | SN-33  | 10.180.101.123 | 2S 64C 128T  | 512 [GiB] |
| P+ C(1)   | CRi | Server100 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-24  | 10.132.16.136  | 2S 40C 40T   | 384 [GiB] |
| P+ H      | CRi | Server341 | Moid-value | --  | (R) UCSC-C245-M6SX | SN-59  | 10.110.50.89   | 2S 48C 96T   | 512 [GiB] |
| P+ H      | CRi | Server740 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-39  | 10.240.21.222  | 2S 48C 96T   | 384 [GiB] |
| P+ H      | CRi | Server488 | Moid-value | --  | (R) UCSC-C240-M6N  | SN-76  | 10.253.49.146  | 2S 64C 128T  | 512 [GiB] |
| P+ H      | Cri | Server698 | Moid-value | --  | (R) UCSC-C240-M6SN | SN-57  | 10.5.150.41    | 2S 64C 128T  | 512 [GiB] |
| P- H      | cRi | Server152 | Moid-value | --  | (R) UCSC-C240-M5SX | SN-12  | 10.144.159.59  | 2S 24C 48T   | 384 [GiB] |
| P+ H      | CRi | Server919 | Moid-value | --  | (R) UCSC-C240-M6N  | SN-72  | 10.96.184.80   | 2S 64C 128T  | 512 [GiB] |
| P+ I(1)   | Cri | Server764 | Moid-value | --  | (R) UCSC-C240-M4SX | SN-10  | 10.170.91.4    | 2S 16C 32T   | 128 [GiB] |
| P+ H      | CRi | Server589 | Moid-value | --  | (R) UCSC-C240-M6SN | SN-42  | 10.61.190.60   | 2S 64C 128T  | 512 [GiB] |
| P+ H      | Cri | Server855 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-55  | 10.246.244.104 | 2S 48C 48T   | 384 [GiB] |
| P+ H      | CRi | Server522 | Moid-value | --  | (R) UCSC-C245-M6SX | SN-99  | 10.229.152.4   | 2S 128C 256T | 512 [GiB] |
| P+ C(1)   | CRi | Server235 | Moid-value | --  | (R) UCSC-C240-M6N  | SN-57  | 10.164.111.14  | 2S 64C 128T  | 512 [GiB] |
| P- H      | cRi | Server617 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-19  | 10.158.144.111 | 2S 16C 16T   | 384 [GiB] |
| P+ H      | CRi | Server967 | Moid-value | --  | (R) UCSC-C240-M6N  | SN-11  | 10.129.14.16   | 2S 64C 128T  | 512 [GiB] |
| P+ I(1)   | Cri | Server857 | Moid-value | --  | (R) UCSC-C240-M4SX | SN-62  | 10.214.24.24   | 2S 16C 32T   | 128 [GiB] |
| P+ H      | CRi | Server138 | Moid-value | --  | (R) UCSC-C240-M6SN | SN-84  | 10.198.149.150 | 2S 64C 128T  | 512 [GiB] |
| P+ H      | Cri | Server938 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-73  | 10.221.7.199   | 2S 24C 24T   | 256 [GiB] |
| P+ C(1)   | CRi | Server926 | Moid-value | --  | (R) UCSC-C225-M6S  | SN-81  | 10.43.89.79    | 1S 64C 128T  | 512 [GiB] |
| P- H      | cRi | Server442 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-49  | 10.150.164.3   | 2S 24C 24T   | 384 [GiB] |
| P+ W(4) L | Cri | Server424 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-44  | 10.71.77.5     | 2S 28C 56T   | 256 [GiB] |
| P+ H      | CRi | Server102 | Moid-value | --  | (R) UCSC-C225-M6S  | SN-79  | 10.131.193.103 | 1S 32C 64T   | 512 [GiB] |
| P+ H      | CRi | Server286 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-27  | 10.94.161.150  | 2S 48C 96T   | 384 [GiB] |
| P- H      | cRi | Server232 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-68  | 10.244.225.242 | 2S 28C 56T   | 256 [GiB] |
| P+ H      | CRi | Server258 | Moid-value | --  | (R) UCSC-C240-M5SX | SN-90  | 10.102.42.194  | 2S 48C 48T   | 384 [GiB] |
| P+ H      | CRi | Server931 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-47  | 10.80.141.200  | 2S 48C 96T   | 512 [GiB] |
| P+ H      | Cri | Server303 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-48  | 10.52.79.42    | 2S 48C 96T   | 512 [GiB] |
| P+ H      | Cri | Server762 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-86  | 10.188.204.23  | 2S 24C 48T   | 384 [GiB] |
| P- H      | cRi | Server349 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-57  | 10.130.139.2   | 2S 28C 56T   | 256 [GiB] |
| P- I(1)   | cri | Server953 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-51  | 10.243.105.43  | 2S 16C 32T   | 256 [GiB] |
| P- H      | cri | Server406 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-20  | 10.254.54.122  | 2S 28C 56T   | 256 [GiB] |
| P+ H      | CRi | Server551 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-98  | 10.100.35.227  | 2S 40C 80T   | 384 [GiB] |
| P+ H      | CRi | Server133 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-44  | 10.165.42.11   | 2S 48C 96T   | 512 [GiB] |
| P+ H      | CRi | Server909 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-39  | 10.90.127.218  | 2S 48C 96T   | 512 [GiB] |
| P- C(1)   | cRi | Server742 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-61  | 10.254.215.227 | 2S 36C 72T   | 512 [GiB] |
| P+ C(1)   | CRi | Server100 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-69  | 10.217.104.142 | 2S 36C 72T   | 512 [GiB] |
| P+ H      | cri | Server229 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-58  | 10.230.135.127 | 2S 24C 48T   | 192 [GiB] |
| P+ C(1)   | cRi | Server846 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-17  | 10.88.229.114  | 2S 28C 56T   | 256 [GiB] |
| P+ H      | Cri | Server945 | Moid-value | --  | (R) UCSC-C240-M5SX | SN-93  | 10.243.27.117  | 2S 28C 56T   | 384 [GiB] |
| P- H      | cri | Server323 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-54  | 10.224.63.162  | 2S 16C 32T   | 256 [GiB] |
| P+ H      | cri | Server413 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-42  | 10.126.168.153 | 2S 28C 56T   | 256 [GiB] |
| P+ H      | Cu  | Server233 | Moid-value | --  | (R) HXAF220C-M5SN  | SN-27  | 10.91.209.54   | 2S 40C 80T   | 384 [GiB] |
| P+ H      | Cu  | Server688 | Moid-value | --  | (R) HXAF220C-M5SN  | SN-82  | 10.32.124.17   | 2S 40C 80T   | 384 [GiB] |
| P+ H      | Cu  | Server723 | Moid-value | --  | (R) HXAF220C-M5SN  | SN-96  | 10.87.84.230   | 2S 40C 80T   | 384 [GiB] |
| P+ H      | Cu  | Server340 | Moid-value | --  | (R) HXAF220C-M5SN  | SN-17  | 10.127.224.202 | 2S 40C 80T   | 384 [GiB] |
| P+ H      | Cu  | Server122 | Moid-value | --  | (R) HXAF240C-M5SX  | SN-40  | 10.192.72.236  | 2S 52C 104T  | 768 [GiB] |
| P+ H      | Cu  | Server880 | Moid-value | --  | (R) HXAF240C-M5SX  | SN-23  | 10.147.249.183 | 2S 52C 104T  | 768 [GiB] |
| P+ H      | Cu  | Server960 | Moid-value | --  | (R) HXAF240C-M5SX  | SN-92  | 10.71.122.173  | 2S 52C 104T  | 768 [GiB] |
| P+ C(2)   | CRi | Server596 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-86  | 10.50.246.226  | 2S 48C 96T   | 256 [GiB] |
| P+ C(2)   | Cri | Server909 | Moid-value | --  | (R) UCSC-C220-M5SX | SN-92  | 10.170.239.33  | 2S 48C 96T   | 256 [GiB] |
| P+ C(1)   | CRi | Server571 | Moid-value | --  | (R) SE-NODE-G2     | SN-33  | 10.120.21.218  | 2S 20C 40T   | 256 [GiB] |
| P+ H      | CRi | Server706 | Moid-value | --  | (R) SE-NODE-G2     | SN-90  | 10.145.40.31   | 2S 20C 40T   | 256 [GiB] |
| P+ C(1)   | CRi | Server666 | Moid-value | --  | (R) SE-NODE-G2     | SN-65  | 10.191.179.125 | 2S 20C 40T   | 256 [GiB] |
| P+ H      | CRi | Server876 | Moid-value | --  | (R) UCSC-C240-M5SN | SN-72  | 10.204.12.128  | 2S 40C 80T   | 384 [GiB] |
| P+ C(1)   | CRi | Server446 | Moid-value | --  | (R) UCSC-C240-M5SN | SN-93  | 10.121.1.151   | 2S 40C 80T   | 384 [GiB] |
| P+ H      | CRi | Server728 | Moid-value | --  | (R) UCSC-C240-M5SN | SN-88  | 10.35.250.111  | 2S 40C 80T   | 384 [GiB] |
| P+ H      | CRi | Server282 | Moid-value | --  | (R) UCSC-C240-M5SX | SN-39  | 10.5.14.95     | 2S 48C 96T   | 384 [GiB] |
| P+ H      | Cri | Server951 | Moid-value | --  | (R) UCSC-C240-M5SX | SN-82  | 10.198.66.94   | 2S 28C 56T   | 256 [GiB] |
| P+ H      | CRi | Server952 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-47  | 10.213.208.103 | 2S 16C 32T   | 256 [GiB] |
| P+ I(1)   | Cri | Server353 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-16  | 10.180.187.80  | 2S 28C 56T   | 256 [GiB] |
| P+ W(2)   | Cri | Server412 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-59  | 10.46.159.33   | 2S 28C 56T   | 256 [GiB] |
| P+ C(1)   | Cri | Server333 | Moid-value | --  | (R) UCSC-C220-M4S  | SN-18  | 10.62.23.182   | 2S 28C 56T   | 256 [GiB] |
| P- H      | cri | Server391 | Moid-value | --  | (R) UCSC-C240-M4SX | SN-68  | 10.55.14.133   | 2S 16C 32T   | 128 [GiB] |
| P+ C(1)   | Cri | Server451 | Moid-value | --  | (R) UCSC-C240-M5SX | SN-47  | 10.24.120.201  | 2S 24C 48T   | 256 [GiB] |
+-----------+-----+-----------+------------+-----+--------------------+--------+----------------+--------------+-----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)